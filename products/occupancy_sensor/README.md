# Occupancy Sensor (UART Driver) | LD2420 Radar

## Description

A occupancy detector using the LD2420 radar sensor, featuring periodic occupancy state reporting and button-triggered factory reset.

* **Occupancy Detection**: Uses LD2420 radar to detect presence and movement.
* **User Interaction**:
  * Long press on the button initiates a factory reset.
* **Device Status Indication**: WS2812 RGB LED displays socket state and system events.
* **Matter Data Model Specification**:
  * **Device Type** : `Occupancy Sensor`
  * **Additional Features**: `Radar`

## Hardware Configuration

<img src="../../docs/images/product_occupancy_sensor.png" alt="Occupancy Sensor LD2420 (UART Driver)" width="500"/>

The following hardware components are used for this product:

* **Devkit**: ESP32-C6 development board
* **Occupancy Sensor**: LD2420 mmWave Radar
* **Button**: On-board or external push-button

### Pin Assignment

| Peripheral       | Signal  | ESP32-C6 GPIO |
|------------------|---------|---------------|
| **LD2420 Radar** | TX/OT1  | GPIO2         |
| **LD2420 Radar** | RX      | GPIO3         |
| **BUTTON**       | GPIO    | GPIO9         |
| **RGB LED**      | GPIO    | GPIO8         |

> **Note**: GPIO assignments can be modified by updating these macros in **app_driver.cpp**: `BUTTON_GPIO_NUM`, `INDICATOR_GPIO_NUM`, `LD2420_RX_GPIO_NUM`, `LD2420_TX_GPIO_NUM`

## Understanding Code

### Initialization Sequence

The `app_driver_init()` function, called from `setup()` in `app_main.cpp`, performs the following:

* Configuring the button with debouncing and set the factory reset callback after long press detection.
* Initializing the WS2812 RGB LED for status indication.
* Initializing and sets up the LD2420 radar in normal mode.
* Creating a system timer that triggers every 2 seconds and calls `app_driver_read_and_report_feature()`

### Core Functions

Every 2 seconds, the timer callback:

* Reads occupancy data from the LD2420 radar sensor
* Reports it to the system via `app_driver_report_occupancy_sensor_state()`

### Extending with Other UART Sensors

To add any other UART sensor, you can follow these steps:

* Initialize it in `app_driver_init()`
* Add reading logic in `app_driver_read_and_report_feature()`
* Implement a function to report its data

## Related Documents

* [Temperature Sensor (I2C Driver) | SHT30](../temperature_sensor/README.md)
* [Programmer's Model](../../docs/programmer_model.md)
* [Components](../../components/README.md)
* [Drivers](../../drivers/README.md)
* [Products](../README.md)
