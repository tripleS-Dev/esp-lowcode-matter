# Light (PWM Driver) | CW

## Description

A tunable white light featuring dual-channel LED control with the following capabilities:

* **Dual-Channel Control**: Independently manages cold and warm white LED channels
* **Light Management**:
  * On/Off state control
  * Brightness control
  * Adjustable color temperature.
* **Device Status Indicator**: Provides system status indication through light effects
* **Matter Data Model Specification**:
  * **Device Type** : `Color Temperature Light`

## Hardware Configuration

<img src="../../docs/images/product_light_cw_pwm.png" alt="Light Color Temperature" width="500"/>

The following hardware components were used for this product:

* **Devkit**: [M5Stack Nano C6 Dev Kit](https://shop.m5stack.com/products/m5stack-nanoc6-dev-kit?srsltid=AfmBOooXsbm_fgpDyK1yWqgPOwtjrL3WksxGlhmRKDZFmVj2omLLbWDX)
* **PWM LED**: Dual-channel constant current PWM LED
* **Optional**: Push-button for manual control (not implemented in current version)

### Pin Assignment

| Peripheral       | GPIO Pin | Function                   |
|------------------|----------|----------------------------|
| Cold White LED   | GPIO4    | Cool white channel control |
| Warm White LED   | GPIO6    | Warm white channel control |

> **Note**: GPIO assignments can be customized by modifying the following macros in **app_driver.cpp**:
> `COLD_CHANNEL_IO`, `WARM_CHANNEL_IO`

## Understanding Code

### Initialization Sequence

The `app_driver_init()` function performs the following:

* Configures both LED channels as outputs
* Initializes the light driver with:
  * Device type: `LIGHT_DEVICE_TYPE_LED`
  * Channel combination: `LIGHT_CHANNEL_COMB_2CH_CW`
  * Brightness range: 0-100%
* Sets default values:
  * Color temperature: 4000K
  * Brightness: 100%
  * Power state: ON

### Core Functions

* **Light Control**:
  * `app_driver_set_light_state`: Controls power state (true=ON, false=OFF)
  * `app_driver_set_light_brightness`: Sets brightness level (0-255 mapped to 0-100%)
  * `app_driver_set_light_temperature`: Adjusts color temperature (mireds value). The light driver uses Kelvin for temperature control, but the system reports the value in Mireds. Table for Kelvin to Mireds conversion:
    * **154 Mireds** → (1000000 / 154) Kelvin → **6500 K**
    * **250 Mireds** → (1000000 / 250) Kelvin → **4000 K**
    * **370 Mireds** → (1000000 / 370) Kelvin → **2700 K**

* **Visual Indicators**:
  * `LOW_CODE_EVENT_SETUP_MODE_START`: starts blinking effect, to indicate setup mode activation (2000ms interval)
  * `LOW_CODE_EVENT_SETUP_MODE_END`: stops blinking effect, to indicate setup mode has ended.
  * `LOW_CODE_EVENT_READY`: displays full brightness white light to indicate device is ready

### Extending Functionality

To add physical button functionality:

* Initialize GPIO button(s) in `app_driver_init()`
* Implement callbacks for:
  * Single press: Toggle power state
  * Long press: Factory reset the device
* Register callbacks using `button_driver_register_cb`

To set different light effects for different events:

* Extend `light_effect_config_t` in event handler
* Implement new effect types in `light_driver_effect_start`

## Related Documentation

* [Light (RMT Based) | RGBCW | WS2812](../light_rgbcw_ws2812/README.md)
* [Programmer's Model](../../docs/programmer_model.md)
* [Components](../../components/README.md)
* [Drivers](../../drivers/README.md)
* [Products](../README.md)
