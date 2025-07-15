# Socket | 1 Channel

## Description

A smart socket featuring relay control, status indication via a WS2812 RGB LED, and button-based user interactions:

* **Relay Control**: Controls power via a GPIO-connected relay.
* **User Input**:
  * Single button press toggles the socket state.
  * Long press triggers a factory reset.
* **Device Status Indication**: WS2812 RGB LED displays socket state and system events.
* **Matter Data Model Specification**:
  * **Device Type** : `On/Off Plug`

## Hardware Configuration

<img src="../../docs/images/product_socket.png" alt="Socket Single Channel" width="500"/>

The following hardware components are used for this product:

* **Devkit**: ESP32-C6 development board
* **Power Relay**: Single-channel relay
* **Indicator**: On-board WS2812 RGB LED
* **Button**: On-board or external push-button

### Pin Assignment

| Peripheral      | GPIO Pin | Function                |
|-----------------|----------|-------------------------|
| Relay Control   | GPIO2    | Main power switching    |
| Button          | GPIO9    | User input              |
| RGB LED         | GPIO8    | Status indication       |

> **Note**: GPIO assignments can be customized by modifying the following macros in **app_driver.cpp**:
> `RELAY_GPIO_NUM`, `BUTTON_GPIO_NUM`, `INDICATOR_GPIO_NUM`

## Understanding Code

### Initialization Sequence

The `app_driver_init()` function, called from `setup()` in `app_main.cpp`, performs the following:

* Configures the relay GPIO as output.
* Initializes the button with debounce handling and registers the following callbacks:
  * **Single-click**: Toggles the socket state.
  * **Long-press**: Initiates factory reset.
* Initializes the WS2812 RGB LED for status indication.

### Core Functions

* **Power Control**:
  * `app_driver_toggle_socket_state_button_callback` is invoked on a single-click event.
  * It toggles the socket state using `app_driver_set_socket_state`, updates the LED accordingly, and reports the new state to the system.

* **Visual Indicators**:
  * `LOW_CODE_EVENT_SETUP_MODE_START`: starts blinking effect, to indicate setup mode activation (2000ms interval)
  * `LOW_CODE_EVENT_SETUP_MODE_END`: stops blinking effect, to indicate setup mode has ended.
  * `LOW_CODE_EVENT_READY`: displays full brightness white light to indicate device is ready

### Extending Functionality

To add a second relay channel to the system, implement the following changes:

* **Matter Data Model Extension**:
  * Add a second On/Off Plug Device Type endpoint to the Matter cluster configuration.
  * Run `Upload Configuration` command to upload the updated data model on the device.

* **Configure an Additional Button Input**:
  * Initialize an additional GPIO button.
  * Register a **single-click event callback** using `button_driver_register_cb`.
  * Inside the callback:
    * Toggle the state of the second relay.
    * Report the new relay state to the system using `low_code_feature_update_to_system`.

## Related Documentation

* [Socket | 2 Channel](../socket_2_channel/README.md)
* [Programmer's Model](../../docs/programmer_model.md)
* [Components](../../components/README.md)
* [Drivers](../../drivers/README.md)
* [Products](../README.md)
