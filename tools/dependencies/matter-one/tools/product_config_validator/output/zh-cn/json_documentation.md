<b>Note:</b> The Advanced text mode for JSON configuration offers a lot of felixibility which might result in the device not working as expected because of some mismatch in configurations. Do evaluate and ensure that things work correctly on your end. You can always reach out to us at `zerocode@espressif.com` for any questions or help.
<br><br>
* [ZeroCode Product Configuration](#zerocode-product-configuration)
* [Pre Driver](#pre-driver)
	* [Log Output](#log-output)
	* [Power Management](#power-management)
	* [Hosted Configuration](#hosted-configuration)
* [Driver](#driver)
	* [Button Driver: GPIO Driver](#button-driver-gpio-driver)
		* [Button Driver: GPIO Configurations](#button-driver-gpio-configurations)
	* [Button Driver: ADC Driver](#button-driver-adc-driver)
		* [Button Driver: ADC Configurations](#button-driver-adc-configurations)
	* [Button Driver: Hosted Driver](#button-driver-hosted-driver)
		* [Button Driver: Hosted Configuration](#button-driver-hosted-configuration)
	* [Relay Driver: GPIO](#relay-driver-gpio)
		* [Relay Driver: GPIO Configuration](#relay-driver-gpio-configuration)
	* [Relay Driver: Hosted](#relay-driver-hosted)
		* [Relay Driver: Hosted Configuration](#relay-driver-hosted-configuration)
	* [Roller blind Driver: GPIO](#roller-blind-driver-gpio)
		* [Roller Blind Driver: Configurations: GPIO Settings](#roller-blind-driver-configurations-gpio-settings)
		* [Roller Blind Driver: Configurations: Movement Settings](#roller-blind-driver-configurations-movement-settings)
		* [Roller Blind Driver: Automatic calibration configurations](#roller-blind-driver-automatic-calibration-configurations)
		* [Roller Blind Driver: Manual calibration configurations](#roller-blind-driver-manual-calibration-configurations)
	* [Roller blind Driver: Hosted](#roller-blind-driver-hosted)
		* [Roller blind Driver: Hosted Configuration](#roller-blind-driver-hosted-configuration)
	* [Light Driver: WS2812 LED Driver](#light-driver-ws2812-led-driver)
		* [Light Driver: Lighting Configurations](#light-driver-lighting-configurations)
		* [Light Driver: Hardware Configurations](#light-driver-hardware-configurations)
		* [Light Driver: Gamma Configurations](#light-driver-gamma-configurations)
		* [Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)
		* [Light Driver: Color Map Configurations](#light-driver-color-map-configurations)
		* [Light Driver: WS2812 LED Driver: Configurations](#light-driver-ws2812-led-driver-configurations)
	* [Light Driver: PWM Light Driver](#light-driver-pwm-light-driver)
		* [Light Driver: Lighting Configurations](#light-driver-lighting-configurations)
		* [Light Driver: Hardware Configurations](#light-driver-hardware-configurations)
		* [Light Driver: Gamma Configurations](#light-driver-gamma-configurations)
		* [Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)
		* [Light Driver: Color Map Configurations](#light-driver-color-map-configurations)
		* [Light Driver: PWM Light Driver: Configurations](#light-driver-pwm-light-driver-configurations)
	* [Light Driver: BP5758D Light Driver](#light-driver-bp5758d-light-driver)
		* [Light Driver: Lighting Configurations](#light-driver-lighting-configurations)
		* [Light Driver: Hardware Configurations](#light-driver-hardware-configurations)
		* [Light Driver: Gamma Configurations](#light-driver-gamma-configurations)
		* [Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)
		* [Light Driver: Color Map Configurations](#light-driver-color-map-configurations)
		* [Light Driver: BP5758D Light Driver: Configurations](#light-driver-bp5758d-light-driver-configurations)
	* [Light Driver: BP1658CJ Light Driver](#light-driver-bp1658cj-light-driver)
		* [Light Driver: Lighting Configurations](#light-driver-lighting-configurations)
		* [Light Driver: Hardware Configurations](#light-driver-hardware-configurations)
		* [Light Driver: Gamma Configurations](#light-driver-gamma-configurations)
		* [Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)
		* [Light Driver: Color Map Configurations](#light-driver-color-map-configurations)
		* [Light Driver: BP1658CJ Light Driver: Configurations](#light-driver-bp1658cj-light-driver-configurations)
	* [Light Driver: SM2135E Light Driver](#light-driver-sm2135e-light-driver)
		* [Light Driver: Lighting Configurations](#light-driver-lighting-configurations)
		* [Light Driver: Hardware Configurations](#light-driver-hardware-configurations)
		* [Light Driver: Gamma Configurations](#light-driver-gamma-configurations)
		* [Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)
		* [Light Driver: Color Map Configurations](#light-driver-color-map-configurations)
		* [Light Driver: SM2135E Light Driver: Configurations](#light-driver-sm2135e-light-driver-configurations)
	* [Light Driver: SM2135EH Light Driver](#light-driver-sm2135eh-light-driver)
		* [Light Driver: Lighting Configurations](#light-driver-lighting-configurations)
		* [Light Driver: Hardware Configurations](#light-driver-hardware-configurations)
		* [Light Driver: Gamma Configurations](#light-driver-gamma-configurations)
		* [Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)
		* [Light Driver: Color Map Configurations](#light-driver-color-map-configurations)
		* [Light Driver: SM2135EH Light Driver: Configurations](#light-driver-sm2135eh-light-driver-configurations)
	* [Light Driver: SM2135EGH Light Driver](#light-driver-sm2135egh-light-driver)
		* [Light Driver: Lighting Configurations](#light-driver-lighting-configurations)
		* [Light Driver: Hardware Configurations](#light-driver-hardware-configurations)
		* [Light Driver: Gamma Configurations](#light-driver-gamma-configurations)
		* [Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)
		* [Light Driver: Color Map Configurations](#light-driver-color-map-configurations)
		* [Light Driver: SM2135EGH Light Driver: Configurations](#light-driver-sm2135egh-light-driver-configurations)
	* [Light Driver: SM2335EGH Light Driver](#light-driver-sm2335egh-light-driver)
		* [Light Driver: Lighting Configurations](#light-driver-lighting-configurations)
		* [Light Driver: Hardware Configurations](#light-driver-hardware-configurations)
		* [Light Driver: Gamma Configurations](#light-driver-gamma-configurations)
		* [Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)
		* [Light Driver: Color Map Configurations](#light-driver-color-map-configurations)
		* [Light Driver: SM2335EGH Light Driver: Configurations](#light-driver-sm2335egh-light-driver-configurations)
	* [Light Driver: GPIO LED Driver](#light-driver-gpio-led-driver)
		* [Light Driver: GPIO LED Driver: Configurations](#light-driver-gpio-led-driver-configurations)
	* [ZeroDetect Driver](#zerodetect-driver)
	* [Temperature Sensor Driver: OnChip Driver](#temperature-sensor-driver-onchip-driver)
		* [Temperature Sensor Driver: OnChip Configuration](#temperature-sensor-driver-onchip-configuration)
	* [Temperature Sensor Driver: NTC Driver](#temperature-sensor-driver-ntc-driver)
		* [Temperature Sensor Driver: NTC Configuration](#temperature-sensor-driver-ntc-configuration)
* [Product Common](#product-common)
	* [Indicator](#indicator)
		* [Indicator: Driver Configurations](#indicator-driver-configurations)
		* [Indicator: Event: Restore](#indicator-event-restore)
		* [Indicator: Event: Solid: RGB](#indicator-event-solid-rgb)
		* [Indicator: Event: Solid: CCT](#indicator-event-solid-cct)
		* [Indicator: Event: Blink/Breathe: RGB](#indicator-event-blinkbreathe-rgb)
		* [Indicator: Event: Blink/Breathe: CCT](#indicator-event-blinkbreathe-cct)
	* [Indicator for Hosted Solution](#indicator-for-hosted-solution)
	* [Back Light](#back-light)
		* [Back Light: Driver Configurations](#back-light-driver-configurations)
	* [Light Common Configurations](#light-common-configurations)
		* [Light Common Configurations: Details](#light-common-configurations-details)
	* [Factory Reset: Power Cycle](#factory-reset-power-cycle)
	* [Factory Reset: Button Press](#factory-reset-button-press)
		* [Factory Reset: Button Press: Driver Configurations](#factory-reset-button-press-driver-configurations)
	* [Factory Reset: Hosted over UART](#factory-reset-hosted-over-uart)
	* [Forced Rollback](#forced-rollback)
	* [Socket Input Mode](#socket-input-mode)
		* [Socket Input Mode: Driver Configurations](#socket-input-mode-driver-configurations)
	* [Socket Power](#socket-power)
		* [Socket Power: Driver Configurations](#socket-power-driver-configurations)
	* [Socket Common Configurations](#socket-common-configurations)
	* [Window Covering Calibration](#window-covering-calibration)
		* [Window Covering Calibration: Driver Configurations](#window-covering-calibration-driver-configurations)
	* [Window Covering Common Configurations](#window-covering-common-configurations)
		* [Window Covering Common Configurations: Details](#window-covering-common-configurations-details)
	* [Advertise MAC](#advertise-mac)
	* [Zero Detect](#zero-detect)
		* [Zero Detect: Driver Configurations](#zero-detect-driver-configurations)
	* [Temperature protect](#temperature-protect)
* [Product](#product)
	* [Light: On Off](#light-on-off)
		* [Light: Driver Configurations](#light-driver-configurations)
		* [Light: On/Off: Data model](#light-onoff-data-model)
	* [Light: Dimmable](#light-dimmable)
		* [Light: Driver Configurations](#light-driver-configurations)
		* [Light: Dimmable: Data Model](#light-dimmable-data-model)
	* [Light: Temperature](#light-temperature)
		* [Light: Driver Configurations](#light-driver-configurations)
		* [Light: Temperature: Data Model](#light-temperature-data-model)
	* [Light: Temperature and Color](#light-temperature-and-color)
		* [Light: Driver Configurations](#light-driver-configurations)
		* [Light: Temperature and Color: Data Model](#light-temperature-and-color-data-model)
	* [Light: Temperature and Extended Color](#light-temperature-and-extended-color)
		* [Light: Driver Configurations](#light-driver-configurations)
		* [Light: Temperature and Extended Color: Data Model](#light-temperature-and-extended-color-data-model)
	* [Socket: On/Off](#socket-onoff)
		* [Socket: Driver Configurations](#socket-driver-configurations)
		* [Socket: On/Off: Data Model](#socket-onoff-data-model)
	* [Socket: Dimmable](#socket-dimmable)
		* [Socket: Driver Configurations](#socket-driver-configurations)
		* [Socket: Dimmable: Data Model](#socket-dimmable-data-model)
	* [Switch](#switch)
		* [Switch: Driver Configurations](#switch-driver-configurations)
	* [Window Covering](#window-covering)
		* [Window Covering: Driver Configurations](#window-covering-driver-configurations)
		* [Window Covering: Data Model](#window-covering-data-model)
* [Test Mode](#test-mode)
	* [Test Mode: Common](#test-mode-common)
	* [Test Mode: BLE](#test-mode-ble)
	* [Test Mode: Sniffer](#test-mode-sniffer)
	* [Test Mode: Light](#test-mode-light)
	* [Test Mode: Socket](#test-mode-socket)
	* [Test Mode: Window Covering](#test-mode-window-covering)

# ZeroCode Product Configuration


The ZeroCode Product Configurations is divided into the following sections:<br>• **Pre Driver:** These are things which are initialised even before the device drivers are initialised. This is done at the very start of the bootup. This includes power related and communication related initialisations.<br>• **Driver:** The drivers are initialised at this stage. This include the lower level drivers like, button, LED, etc. They are then used/linked later in the configuration based on their Driver IDs.<br>• **Product Common:** This includes things which are common to the product as a whole. The drivers which are initialised before are used here.<br>• **Product:** This represents the actual product and how it is shown in the Ecosystems. Example, to create a 2 channel socket, the socket must be present 2 times here. The drivers which are initialised before are used here.<br>• **Test Mode:** These initialise the test modes that can be performed in the factory during manufacturing. If enabled, they need to be marked as completed before the device leaves the factory. Until then, the device checks for the trigger for the test modes on bootup.<br>  

## Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "config_version": 3,
    "driver": [
        {
            "id": 1000,
            "type": "ezc.driver.button",
            "name": "gpio",
            "gpio_config": {
                "gpio_num": 9,
                "active_level": 0,
                "long_press_time": 5
            }
        },
        {
            "id": 1001,
            "type": "ezc.driver.relay",
            "name": "gpio",
            "gpio_config": {
                "gpio_num": 10,
                "active_level": 0
            }
        },
        {
            "id": 1002,
            "type": "ezc.driver.led",
            "name": "gpio",
            "gpio_config": {
                "gpio_num": 8,
                "active_level": 0
            }
        }
    ],
    "product_common": [
        {
            "type": "ezc.product_common.indicator",
            "driver": {
                "output": 1002
            },
            "events": [
                {
                    "name": "setup_mode_start",
                    "mode": "blink",
                    "speed": 4000,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 0
                },
                {
                    "name": "setup_started",
                    "mode": "blink",
                    "speed": 1000,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 0
                },
                {
                    "name": "setup_successful",
                    "mode": "restore"
                },
                {
                    "name": "setup_failed",
                    "mode": "restore"
                },
                {
                    "name": "setup_mode_end",
                    "mode": "restore"
                },
                {
                    "name": "ready",
                    "mode": "restore"
                },
                {
                    "name": "identification_start",
                    "mode": "blink",
                    "speed": 1000,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 0
                },
                {
                    "name": "identification_stop",
                    "mode": "restore"
                },
                {
                    "name": "identification_blink",
                    "mode": "blink",
                    "speed": 1000,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 1000
                },
                {
                    "name": "identification_breathe",
                    "mode": "blink",
                    "speed": 1000,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 15000
                },
                {
                    "name": "identification_okay",
                    "mode": "blink",
                    "speed": 700,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 1400
                },
                {
                    "name": "identification_channel_change",
                    "mode": "blink",
                    "speed": 8000,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 8000
                },
                {
                    "name": "identification_finish_effect",
                    "mode": "restore"
                },
                {
                    "name": "identification_stop_effect",
                    "mode": "restore"
                },
                {
                    "name": "factory_reset_triggered",
                    "mode": "blink",
                    "speed": 400,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 0
                },
                {
                    "name": "forced_rollback_triggered",
                    "mode": "blink",
                    "speed": 400,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 0
                },
                {
                    "name": "driver_mode",
                    "mode": "blink",
                    "speed": 1000,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 0
                },
                {
                    "name": "test_mode_start",
                    "mode": "blink",
                    "speed": 500,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 1500
                },
                {
                    "name": "test_mode_complete",
                    "mode": "blink",
                    "speed": 500,
                    "color_select": 2,
                    "cct": 50,
                    "min_brightness": 20,
                    "max_brightness": 100,
                    "total_ms": 3000
                }
            ]
        },
        {
            "type": "ezc.product_common.factory_reset",
            "subtype": 2,
            "driver": {
                "input": 1000
            },
            "auto_trigger": true
        }
    ],
    "product": [
        {
            "type": "ezc.product.socket",
            "subtype": 1,
            "driver": {
                "input": 1000,
                "output": 1001,
                "indicator": 1002
            },
            "data_model": {
                "power_default": 1,
                "power_bootup": -1
            }
        }
    ],
    "test_mode": [
        {
            "type": "ezc.test_mode.common",
            "subtype": 1
        },
        {
            "type": "ezc.test_mode.ble",
            "subtype": 1
        },
        {
            "type": "ezc.test_mode.socket",
            "subtype": 1
        }
    ]
}
```  
</details>  

## Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|config_version|Product configuration version|`3`||integer|✓|
|pre_driver|Peripheral settings required before initialising the drivers|[Log Output](#log-output), [Power Management](#power-management), [Hosted Configuration](#hosted-configuration)||object||
|driver|Contains the Driver specifications|[Button Driver: GPIO Driver](#button-driver-gpio-driver), [Button Driver: ADC Driver](#button-driver-adc-driver), [Button Driver: Hosted Driver](#button-driver-hosted-driver), [Relay Driver: GPIO](#relay-driver-gpio), [Relay Driver: Hosted](#relay-driver-hosted), [Roller blind Driver: GPIO](#roller-blind-driver-gpio), [Roller blind Driver: Hosted](#roller-blind-driver-hosted), [Light Driver: WS2812 LED Driver](#light-driver-ws2812-led-driver), [Light Driver: PWM Light Driver](#light-driver-pwm-light-driver), [Light Driver: BP5758D Light Driver](#light-driver-bp5758d-light-driver), [Light Driver: BP1658CJ Light Driver](#light-driver-bp1658cj-light-driver), [Light Driver: SM2135E Light Driver](#light-driver-sm2135e-light-driver), [Light Driver: SM2135EH Light Driver](#light-driver-sm2135eh-light-driver), [Light Driver: SM2135EGH Light Driver](#light-driver-sm2135egh-light-driver), [Light Driver: SM2335EGH Light Driver](#light-driver-sm2335egh-light-driver), [Light Driver: GPIO LED Driver](#light-driver-gpio-led-driver), [ZeroDetect Driver](#zerodetect-driver), [Temperature Sensor Driver: OnChip Driver](#temperature-sensor-driver-onchip-driver), [Temperature Sensor Driver: NTC Driver](#temperature-sensor-driver-ntc-driver)||object|✓|
|product_common|Common product configurations|[Indicator](#indicator), [Indicator for Hosted Solution](#indicator-for-hosted-solution), [Back Light](#back-light), [Light Common Configurations](#light-common-configurations), [Factory Reset: Power Cycle](#factory-reset-power-cycle), [Factory Reset: Button Press](#factory-reset-button-press), [Factory Reset: Hosted over UART](#factory-reset-hosted-over-uart), [Forced Rollback](#forced-rollback), [Socket Input Mode](#socket-input-mode), [Socket Power](#socket-power), [Socket Common Configurations](#socket-common-configurations), [Window Covering Calibration](#window-covering-calibration), [Window Covering Common Configurations](#window-covering-common-configurations), [Advertise MAC](#advertise-mac), [Zero Detect](#zero-detect), [Temperature protect](#temperature-protect)||object|✓|
|product|Product specifications and configurations|[Light: On Off](#light-on-off), [Light: Dimmable](#light-dimmable), [Light: Temperature](#light-temperature), [Light: Temperature and Color](#light-temperature-and-color), [Light: Temperature and Extended Color](#light-temperature-and-extended-color), [Socket: On/Off](#socket-onoff), [Socket: Dimmable](#socket-dimmable), [Switch](#switch), [Window Covering](#window-covering)||object|✓|
|test_mode|Testing configurations|[Test Mode: Common](#test-mode-common), [Test Mode: BLE](#test-mode-ble), [Test Mode: Sniffer](#test-mode-sniffer), [Test Mode: Light](#test-mode-light), [Test Mode: Socket](#test-mode-socket), [Test Mode: Window Covering](#test-mode-window-covering)||object||
|device_management|Device Managmenet description|`true`, `false`||boolean||

# Pre Driver

## Log Output
  
**Section: Pre Driver**

Configure the console logs. This can be used to change the log level or even change the default IO pin.  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.pre_driver.log_output",
    "level": 0
}
```  
</details>  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.pre_driver.log_output",
    "tx_gpio": 19
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Pre Driver type: ezc.pre_driver.log_output|`ezc.pre_driver.log_output`||string|✓|
|level|Set the log level:<br>• 0: No logs<br>• 1: Error<br>• 2: Warning<br>• 3: Info<br>• 4: Debug<br>• 5: Verbose|`0`, `1`, `2`, `3`, `4`, `5`||integer||
|tx_gpio|Change the tx gpio for console logs. Possible GPIO values depend on the selected module.|||integer||

## Power Management
  
**Section: Pre Driver**

Configure the power usage of the device. This can be useful for devices which have power limitations.  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.pre_driver.power_management",
    "enable_light_sleep": true,
    "max_freq_mhz": 160,
    "min_freq_mhz": 10
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Pre Driver type: ezc.pre_driver.power_management|`ezc.pre_driver.power_management`||string|✓|
|enable_light_sleep|It enables light sleep, It helps in reducing power usage.|`true`, `false`||boolean||
|max_freq_mhz|Maximum frequency that device will go to.|`x <= 240`||integer|✓|
|min_freq_mhz|Minimum frequency that device will go to.|`10 <= x <= 240`||integer|✓|

## Hosted Configuration
  
**Section: Pre Driver**

Configure UART settings for Hosted solutions  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.pre_driver.hosted_uart",
    "uart_rx": 6,
    "uart_tx": 7,
    "uart_baudrate": 115200,
    "ack_enable": false,
    "host_wakeup_pin": -1,
    "esp_wakeup_pin": -1
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Pre Driver type: ezc.pre_driver.hosted_uart|`ezc.pre_driver.hosted_uart`||string|✓|
|uart_rx|Valid GPIO for RX pin for ESP ZeroCode module||`6`|integer||
|uart_tx|Valid GPIO for TX pin for ESP ZeroCode module||`7`|integer||
|uart_baudrate|Communication baudrate for UART||`115200`|integer||
|ack_enable|Enable to send/receive acknowledgement after every command|`true`, `false`|`true`|boolean||
|host_wakeup_pin|GPIO Pin used for waking host before sending any command. -1 to disable host wakeup||`-1`|integer||
|esp_wakeup_pin|GPIO Pin used for waking ESP before receiving any command. -1 to disable ESP wakeup||`-1`|integer||

# Driver

## Button Driver: GPIO Driver
  
**Section: Driver**

Applicable if GPIO is selected as Button Driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.button",
    "name": "gpio",
    "gpio_config": {
        "gpio_num": 9,
        "active_level": 0,
        "long_press_time": 5
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.button|`ezc.driver.button`||string|✓|
|name|Button subtype: GPIO|`gpio`||string|✓|
|gpio_config||[Button Driver: GPIO Configurations](#button-driver-gpio-configurations)||object|✓|

### Button Driver: GPIO Configurations


Configuration for GPIO button, applicable if `ezc.driver.gpio` is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gpio_config": {
        "gpio_num": 9,
        "active_level": 0,
        "long_press_time": 5
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|gpio_num|Input GPIO for the driver. Range of values depend on the chip|`0 <= x`||integer|✓|
|active_level|When is the input detected, is it active_high or active_low<br>• 0: Active low. The input is detected when the input pin is connected to GND<br>• 1: Active high. The input is detected when the input pin is connected to VCC|`0`, `1`||integer|✓|
|long_press_time|Time in seconds for long press event to be detected.|`0 <= x <= 65535`|`5`|integer||

## Button Driver: ADC Driver
  
**Section: Driver**

Applicable if ADC is selected as Button Driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.button",
    "name": "adc",
    "adc_config": {
        "gpio_num": 9,
        "active_level": 0,
        "long_press_time": 5
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.button|`ezc.driver.button`||string|✓|
|name|Button subtype: ADC|`adc`||string|✓|
|adc_config||[Button Driver: ADC Configurations](#button-driver-adc-configurations)||object|✓|

### Button Driver: ADC Configurations


Configuration for ADC button, applicable if `ezc.driver.gpio` is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "adc_config": {
        "adc_channel": 0,
        "button_index": 1,
        "min": 100,
        "max": 500,
        "long_press_time": 5
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|adc_channel|Input ADC for the driver. Range of values depend on the chip|`0 <= x <= 32`|`5`|integer||
|button_index|button index on the channel|`0 <= x <= 32`|`5`|integer||
|min|min voltage in mv corresponding to the button|`0 <= x <= 65535`|`5`|integer||
|max|max voltage in mv corresponding to the button|`0 <= x <= 65535`|`5`|integer||
|long_press_time|Time in seconds for long press event to be detected.|`0 <= x <= 65535`|`5`|integer||

## Button Driver: Hosted Driver
  
**Section: Driver**

UART based button driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.button",
    "name": "hosted",
    "hosted_config": {
        "uart_driver_id": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.button|`ezc.driver.button`||string|✓|
|name|`hosted` applicable only if hosted driver is selected|`hosted`||string|✓|
|hosted_config||[Button Driver: Hosted Configuration](#button-driver-hosted-configuration)||object|✓|

### Button Driver: Hosted Configuration


Applicable if hosted is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hosted_config": {
        "uart_driver_id": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|uart_driver_id|Unique driver id used to distinguish different buttons connected to host|`0 <= x <= 255`|`30`|integer||

## Relay Driver: GPIO
  
**Section: Driver**

GPIO based relay driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.relay",
    "name": "gpio",
    "gpio_config": {
        "gpio_num": 10,
        "active_level": 0
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.relay|`ezc.driver.relay`||string|✓|
|name|`hosted` applicable only if hosted driver is selected|`gpio`||string|✓|
|gpio_config|Applicable if gpio is selected|[Relay Driver: GPIO Configuration](#relay-driver-gpio-configuration)||object|✓|

### Relay Driver: GPIO Configuration


Applicable if gpio is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gpio_config": {
        "gpio_num": 10,
        "active_level": 0
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|gpio_num|Output GPIO for the driver. Range of values depend on the chip|`0 <= x`||integer|✓|
|active_level|When is the output turned on<br>• 0: The output is on when it connected to GND<br>• 1: The output is on when it connected to VCC|`0`, `1`||integer|✓|

## Relay Driver: Hosted
  
**Section: Driver**

UART based relay driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.relay",
    "name": "hosted",
    "hosted_config": {
        "uart_driver_id": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.relay|`ezc.driver.relay`||string|✓|
|name|`hosted` applicable only if hosted driver is selected|`hosted`||string|✓|
|hosted_config|Applicable if hosted is selected|[Relay Driver: Hosted Configuration](#relay-driver-hosted-configuration)||object|✓|

### Relay Driver: Hosted Configuration


Applicable if hosted is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hosted_config": {
        "uart_driver_id": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|uart_driver_id|Unique driver id used to distinguish different relays connected to host|`0 <= x <= 255`|`30`|integer||

## Roller blind Driver: GPIO
  
**Section: Driver**

GPIO based Roller blind driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1001,
    "type": "ezc.driver.roller_blind",
    "name": "gpio",
    "roller_blind_config": {
        "allow_reverse_in_moving": false,
        "pause_between_moves": true,
        "delay_time_between_moves_ms": 500,
        "relay_control_delay_time_ms": 0,
        "default_max_move_time_ms": 60000
    },
    "gpio_config": {
        "up_relay_gpio": 10,
        "down_relay_gpio": 11
    },
    "calibration_config": {
        "calibration_type": 1,
        "detect_gpio": 12,
        "detection_frequency": 50,
        "detection_frequency_offset": 20
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id||`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.roller_blind|`ezc.driver.roller_blind`||string|✓|
|name|`hosted` applicable only if hosted driver is selected|`gpio`||string|✓|
|gpio_config|More GPIO Configuration|[Roller Blind Driver: Configurations: GPIO Settings](#roller-blind-driver-configurations-gpio-settings)||object|✓|
|roller_blind_config|More Roller Blind Configuration|[Roller Blind Driver: Configurations: Movement Settings](#roller-blind-driver-configurations-movement-settings)||object|✓|
|calibration_config||[Roller Blind Driver: Automatic calibration configurations](#roller-blind-driver-automatic-calibration-configurations), [Roller Blind Driver: Manual calibration configurations](#roller-blind-driver-manual-calibration-configurations)||object|✓|

### Roller Blind Driver: Configurations: GPIO Settings


More GPIO Configuration  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gpio_config": {
        "up_relay_gpio": 25,
        "up_relay_active_level": 1,
        "down_relay_gpio": 12,
        "down_relay_active_level": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|up_relay_gpio|Output GPIO for the up relay driver. Range of values depend on the chip|`0 <= x`||integer|✓|
|up_relay_active_level|When is the output turned on<br>• 0: The output is on when it connected to GND<br>• 1: The output is on when it connected to VCC<br>• default: 1|`1`, `2`||integer||
|down_relay_gpio|Output GPIO for the down relay driver. Range of values depend on the chip|`0 <= x`||integer|✓|
|down_relay_active_level|When is the output turned on<br>• 0: The output is on when it connected to GND<br>• 1: The output is on when it connected to VCC<br>• default: 1|`1`, `2`||integer||

### Roller Blind Driver: Configurations: Movement Settings


More Roller Blind Configuration  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "roller_blind_config": {
        "allow_reverse_in_moving": false,
        "pause_between_moves": true,
        "delay_time_between_moves_ms": 500,
        "relay_control_delay_time_ms": 0,
        "default_max_move_time_ms": 60000,
        "use_default_time_when_not_calibrated": false
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|allow_reverse_in_moving|Behaviour when pressing the opposite direction button, when in motion.<br>• true: Reverse the motion<br>• false: Stop the motion|`true`, `false`||boolean|✓|
|pause_between_moves|Whether to pause between movements.<br>• true: pause between movements.<br>• false: don't have pause between movements.|`true`, `false`||boolean|✓|
|delay_time_between_moves_ms|Delay in between changing the direction, in milliseconds.|`0 <= x <= 65535`||integer||
|relay_control_delay_time_ms|Relay control delay time|`0 <= x <= 65535`||integer||
|default_max_move_time_ms|The default moving time for the up and down during calibration or before calibration.|`0 <= x <= 214748364`||integer|✓|
|use_default_time_when_not_calibrated|Always moving default time when un-calibrate.<br>• true: use default time.<br>• false: don't use default time.|`true`, `false`||boolean||
|move_time_compensation_percent|Compensation moving time when the target position of window covering is the end of window cover(fully open/close)..<br>• min: 0<br>• max: 100<br>• step: 1<br>• default: 0|||integer||

### Roller Blind Driver: Automatic calibration configurations


Automatic Roller Blind calibration configurations and options  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "calibration_config": {
        "calibration_type": 1,
        "detect_gpio": 26,
        "detection_frequency": 50,
        "detection_frequency_offset": 20
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|calibration_type|`1` for Auto Calibration, `2` for Manual Calibration|`1`||integer|✓|
|detect_gpio|Input GPIO to detect frequency for auto calibration if auto calibration type. Range of values depend on the chip|`0 <= x`||integer|✓|
|detection_frequency|The frequency to be detected for auto calibration if auto calibration type|`0 <= x`||integer|✓|
|detection_frequency_offset|The offset in the frequency to be detected for auto calibration if auto calibration type|`0 <= x`||integer|✓|

### Roller Blind Driver: Manual calibration configurations


Manual Roller Blind calibration configurations and options  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "calibration_config": {
        "calibration_type": 2
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|calibration_type|`1` for Auto Calibration, `2` for Manual Calibration|`2`||integer|✓|

## Roller blind Driver: Hosted
  
**Section: Driver**

UART based Roller blind driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.roller_blind",
    "name": "hosted",
    "hosted_config": {
        "uart_driver_id": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id||`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.roller_blind|`ezc.driver.roller_blind`||string|✓|
|name|`hosted` applicable only if hosted driver is selected|`hosted`||string|✓|
|hosted_config|Applicable if hosted is selected|[Roller blind Driver: Hosted Configuration](#roller-blind-driver-hosted-configuration)||object|✓|

### Roller blind Driver: Hosted Configuration


Applicable if hosted is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hosted_config": {
        "uart_driver_id": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|uart_driver_id|Unique driver id used to distinguish different Roller blind connected to host|`0 <= x <= 255`|`30`|integer||

## Light Driver: WS2812 LED Driver
  
**Section: Driver**

Applicable if ws2812 is selected as led driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.led",
    "name": "ws2812",
    "ws2812_config": {
        "led_num": 1,
        "ctrl_io": 8
    },
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    },
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    },
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.led|`ezc.driver.led`||string|✓|
|name|Driver name: WS2812|`ws2812`||string|✓|
|lighting_config|More light configurations|[Light Driver: Lighting Configurations](#light-driver-lighting-configurations)||object|✓|
|hardware_config|Hardware configuration of led|[Light Driver: Hardware Configurations](#light-driver-hardware-configurations)||object|✓|
|gamma_config|Gamma configurations for light bulb. Applicable for all except when gpio is selected|[Light Driver: Gamma Configurations](#light-driver-gamma-configurations)||object|✓|
|cct_map||[Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)||object||
|color_map||[Light Driver: Color Map Configurations](#light-driver-color-map-configurations)||object||
|ws2812_config|WS2812 LED driver extra configurations|[Light Driver: WS2812 LED Driver: Configurations](#light-driver-ws2812-led-driver-configurations)||object|✓|

### Light Driver: Lighting Configurations


More light configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gradient|Switch gradient<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|enable_memory|Retain the power state on reboot|`true`, `false`||boolean|✓|
|enable_lowpower|Low power consumption mode|`true`, `false`||boolean|✓|
|sync_change_brightness|Change the brightness synchronously|`true`, `false`||boolean|✓|
|disable_auto_on|Disable turning on of the light|`true`, `false`||boolean|✓|
|beads_comb|LED Beads Combination support by hardware<br>• 1: C<br>• 2: W<br>• 3: CW<br>• 4: RGB<br>• 5: 4CH_RGBC<br>• 6: 4CH_RGBCC<br>• 7: 4CH_RGBW<br>• 8: 4CH_RGBWW<br>• 9: 5CH_RGBCW<br>• 10: 5CH_RGBCC<br>• 11: 5CH_RGBWW<br>• 12: 5CH_RGBC<br>• 13: 5CH_RGBW|`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`||integer|✓|
|fades_ms|Default ramp time in ms|||integer|✓|
|enable_precise_cct_control|Precise CCT Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|enable_precise_color_control|Precise Color Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|cct_kelvin_min|Min color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 2000K|`1500 <= x <= 7000`|`2200`|integer||
|cct_kelvin_max|Max color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 7000K|`1500 <= x <= 7000`|`7000`|integer||

### Light Driver: Hardware Configurations


Hardware configuration of led  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|white_min|Minimum brightness of white light|`0 <= x`||integer|✓|
|white_max|Maximum brightness of white light|`x <= 100`||integer|✓|
|white_power_max|Maximum white light power, 100-200.<br>• If it is set to 100, the total output power is 100% of the single channel.|`100 <= x <= 200`||integer|✓|
|rgb_min|Minimum brightness of color light|`0 <= x`||integer|✓|
|rgb_max|Maximum brightness of color light|`x <= 100`||integer|✓|
|rgb_power_max|Maximum power of color light<br>• If it is set to 100, the total output power is 300% of the single channel, that is, 3-channel full power output.|`100 <= x <= 300`||integer|✓|

### Light Driver: Gamma Configurations


Gamma configurations for light bulb. Applicable for all except when gpio is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gamma_adjust|Enable color light calibration<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|gamma_red|Red gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_green|Green gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_blue|Blue gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_cold|Cold gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_warm|Warm gamma calibration|`50 <= x <= 100`||integer|✓|
|curve_coe|White balance|`0.8 <= x <= 2.2`||number||

### Light Driver: CCT Map Configurations


CCT Map configurations for light bulb. Applicable for light with precise cct control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[cct_kelvin, cct_percentage, coef_red, coef_green, coef_blue, coef_cold, coef_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "cct_map": {
        "table": "[[2200, 0, 0.033, 0.033, 0.034, 0.45, 0.45],[7000, 100, 0.033, 0.033, 0.034, 0.45, 0.45]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|CCT Map Table<br>• cct: Color temperature in kelvin<br>• cct_percentage: Percentage of color temperature<br>• red: Red light output<br>• green: Green light output<br>• blue: Blue light output<br>• cold: Cold white light output<br>• warm: Warm white light output|string||string|✓|

### Light Driver: Color Map Configurations


Color Map configurations for light bulb. Applicable for light with precise color control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[hue, saturation_100_red, saturation_100_green, saturation_100_blue, saturation_100_cold, saturation_100_warm, saturation_50_red, saturation_50_green, saturation_50_blue, saturation_50_cold, saturation_50_warm, saturation_0_red, saturation_0_green, saturation_0_blue, saturation_0_cold, saturation_0_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "color_map": {
        "table": "[[0,1,0,0,0,0,0.9120,0.0440,0.0440,0,0,0.4854,0.2573,0.2573,0,0],[15,0.9218,0.0782,0,0,0,0.8549,0.0907,0.0544,0,0,0.5112,0.2639,0.2248,0,0]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|Color Map Table. Add at least 12 sets of color data|string||string|✓|

### Light Driver: WS2812 LED Driver: Configurations


WS2812 LED driver extra configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "ws2812_config": {
        "led_num": 1,
        "ctrl_io": 8
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|led_num|Number of LEDs|`1 <= x`||integer|✓|
|ctrl_io|Data signal pin. Range of values depends on the chip|`0 <= x`||integer|✓|

## Light Driver: PWM Light Driver
  
**Section: Driver**

PWM light driver configuration  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.led",
    "name": "pwm",
    "pwm_config": {
        "pwm_hz": 4000,
        "invert_level": false,
        "temperature_mode": 1,
        "gpio_red": 4,
        "gpio_green": 5,
        "gpio_blue": 6,
        "gpio_cold_or_cct": 3,
        "gpio_warm_or_brightness": 7
    },
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    },
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    },
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.led|`ezc.driver.led`||string|✓|
|name|Applicable if `pwm` is selected as the light driver|`pwm`||string|✓|
|lighting_config|More light configurations|[Light Driver: Lighting Configurations](#light-driver-lighting-configurations)||object|✓|
|hardware_config|Hardware configuration of led|[Light Driver: Hardware Configurations](#light-driver-hardware-configurations)||object|✓|
|gamma_config|Gamma configurations for light bulb. Applicable for all except when gpio is selected|[Light Driver: Gamma Configurations](#light-driver-gamma-configurations)||object|✓|
|cct_map||[Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)||object||
|color_map||[Light Driver: Color Map Configurations](#light-driver-color-map-configurations)||object||
|pwm_config|Contains extra PWM configurations|[Light Driver: PWM Light Driver: Configurations](#light-driver-pwm-light-driver-configurations)||object|✓|

### Light Driver: Lighting Configurations


More light configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gradient|Switch gradient<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|enable_memory|Retain the power state on reboot|`true`, `false`||boolean|✓|
|enable_lowpower|Low power consumption mode|`true`, `false`||boolean|✓|
|sync_change_brightness|Change the brightness synchronously|`true`, `false`||boolean|✓|
|disable_auto_on|Disable turning on of the light|`true`, `false`||boolean|✓|
|beads_comb|LED Beads Combination support by hardware<br>• 1: C<br>• 2: W<br>• 3: CW<br>• 4: RGB<br>• 5: 4CH_RGBC<br>• 6: 4CH_RGBCC<br>• 7: 4CH_RGBW<br>• 8: 4CH_RGBWW<br>• 9: 5CH_RGBCW<br>• 10: 5CH_RGBCC<br>• 11: 5CH_RGBWW<br>• 12: 5CH_RGBC<br>• 13: 5CH_RGBW|`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`||integer|✓|
|fades_ms|Default ramp time in ms|||integer|✓|
|enable_precise_cct_control|Precise CCT Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|enable_precise_color_control|Precise Color Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|cct_kelvin_min|Min color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 2000K|`1500 <= x <= 7000`|`2200`|integer||
|cct_kelvin_max|Max color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 7000K|`1500 <= x <= 7000`|`7000`|integer||

### Light Driver: Hardware Configurations


Hardware configuration of led  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|white_min|Minimum brightness of white light|`0 <= x`||integer|✓|
|white_max|Maximum brightness of white light|`x <= 100`||integer|✓|
|white_power_max|Maximum white light power, 100-200.<br>• If it is set to 100, the total output power is 100% of the single channel.|`100 <= x <= 200`||integer|✓|
|rgb_min|Minimum brightness of color light|`0 <= x`||integer|✓|
|rgb_max|Maximum brightness of color light|`x <= 100`||integer|✓|
|rgb_power_max|Maximum power of color light<br>• If it is set to 100, the total output power is 300% of the single channel, that is, 3-channel full power output.|`100 <= x <= 300`||integer|✓|

### Light Driver: Gamma Configurations


Gamma configurations for light bulb. Applicable for all except when gpio is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gamma_adjust|Enable color light calibration<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|gamma_red|Red gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_green|Green gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_blue|Blue gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_cold|Cold gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_warm|Warm gamma calibration|`50 <= x <= 100`||integer|✓|
|curve_coe|White balance|`0.8 <= x <= 2.2`||number||

### Light Driver: CCT Map Configurations


CCT Map configurations for light bulb. Applicable for light with precise cct control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[cct_kelvin, cct_percentage, coef_red, coef_green, coef_blue, coef_cold, coef_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "cct_map": {
        "table": "[[2200, 0, 0.033, 0.033, 0.034, 0.45, 0.45],[7000, 100, 0.033, 0.033, 0.034, 0.45, 0.45]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|CCT Map Table<br>• cct: Color temperature in kelvin<br>• cct_percentage: Percentage of color temperature<br>• red: Red light output<br>• green: Green light output<br>• blue: Blue light output<br>• cold: Cold white light output<br>• warm: Warm white light output|string||string|✓|

### Light Driver: Color Map Configurations


Color Map configurations for light bulb. Applicable for light with precise color control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[hue, saturation_100_red, saturation_100_green, saturation_100_blue, saturation_100_cold, saturation_100_warm, saturation_50_red, saturation_50_green, saturation_50_blue, saturation_50_cold, saturation_50_warm, saturation_0_red, saturation_0_green, saturation_0_blue, saturation_0_cold, saturation_0_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "color_map": {
        "table": "[[0,1,0,0,0,0,0.9120,0.0440,0.0440,0,0,0.4854,0.2573,0.2573,0,0],[15,0.9218,0.0782,0,0,0,0.8549,0.0907,0.0544,0,0,0.5112,0.2639,0.2248,0,0]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|Color Map Table. Add at least 12 sets of color data|string||string|✓|

### Light Driver: PWM Light Driver: Configurations


Contains extra PWM configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "pwm_config": {
        "pwm_hz": 4000,
        "invert_level": false,
        "temperature_mode": 1,
        "gpio_red": 4,
        "gpio_green": 5,
        "gpio_blue": 6,
        "gpio_cold_or_cct": 3,
        "gpio_warm_or_brightness": 7
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|invert_level|PWM invert level<br>• true: invert<br>• false: not invert|`true`, `false`||boolean||
|pwm_hz|PWM frequency (in hz)|`1000 <= x <= 20000`||integer|✓|
|temperature_mode|riving mode of color temperature adjustment<br>• 0: CCT mode: CCT + brightness<br>• 1: CW mode: cold white light + warm white light|`0`, `1`||integer|✓|
|phase_delay|Phase delay in pwm:<br>• 0: No phase delay<br>• 1: RGB channel phase delay<br>• 2: CW channel phase delay<br>• 4: RGBCW channel phase delay|`0`, `1`, `2`, `4`||integer||
|gpio_red|Red light output pin. Range of values depend on the chip|`-1 <= x`||integer|✓|
|gpio_green|Green light output pin. Range of values depend on the chip|`-1 <= x`||integer|✓|
|gpio_blue|Blue light output pin. Range of values depend on the chip|`-1 <= x`||integer|✓|
|gpio_cold_or_cct|Cold white light/CCT output pin. Range of values depend on the chip|`-1 <= x`||integer|✓|
|gpio_warm_or_brightness|Warm white light/brightness output pin. Range of values depend on the chip|`-1 <= x`||integer|✓|

## Light Driver: BP5758D Light Driver
  
**Section: Driver**

BP5758D driver support  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.led",
    "name": "bp5758d",
    "bp5758d_config": {
        "gpio_clock": 10,
        "gpio_sda": 4,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_warm": 3,
        "out_cold": 4,
        "out1_current_max": 6,
        "out2_current_max": 6,
        "out3_current_max": 6,
        "out4_current_max": 13,
        "out5_current_max": 13
    },
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    },
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    },
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.led|`ezc.driver.led`||string|✓|
|name|Applicable only if `bp5758d` is selected as light driver|`bp5758d`||string|✓|
|lighting_config|More light configurations|[Light Driver: Lighting Configurations](#light-driver-lighting-configurations)||object|✓|
|hardware_config|Hardware configuration of led|[Light Driver: Hardware Configurations](#light-driver-hardware-configurations)||object|✓|
|gamma_config|Gamma configurations for light bulb. Applicable for all except when gpio is selected|[Light Driver: Gamma Configurations](#light-driver-gamma-configurations)||object|✓|
|cct_map||[Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)||object||
|color_map||[Light Driver: Color Map Configurations](#light-driver-color-map-configurations)||object||
|bp5758d_config|Applicable if bp5758d is selected|[Light Driver: BP5758D Light Driver: Configurations](#light-driver-bp5758d-light-driver-configurations)||object|✓|

### Light Driver: Lighting Configurations


More light configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gradient|Switch gradient<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|enable_memory|Retain the power state on reboot|`true`, `false`||boolean|✓|
|enable_lowpower|Low power consumption mode|`true`, `false`||boolean|✓|
|sync_change_brightness|Change the brightness synchronously|`true`, `false`||boolean|✓|
|disable_auto_on|Disable turning on of the light|`true`, `false`||boolean|✓|
|beads_comb|LED Beads Combination support by hardware<br>• 1: C<br>• 2: W<br>• 3: CW<br>• 4: RGB<br>• 5: 4CH_RGBC<br>• 6: 4CH_RGBCC<br>• 7: 4CH_RGBW<br>• 8: 4CH_RGBWW<br>• 9: 5CH_RGBCW<br>• 10: 5CH_RGBCC<br>• 11: 5CH_RGBWW<br>• 12: 5CH_RGBC<br>• 13: 5CH_RGBW|`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`||integer|✓|
|fades_ms|Default ramp time in ms|||integer|✓|
|enable_precise_cct_control|Precise CCT Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|enable_precise_color_control|Precise Color Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|cct_kelvin_min|Min color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 2000K|`1500 <= x <= 7000`|`2200`|integer||
|cct_kelvin_max|Max color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 7000K|`1500 <= x <= 7000`|`7000`|integer||

### Light Driver: Hardware Configurations


Hardware configuration of led  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|white_min|Minimum brightness of white light|`0 <= x`||integer|✓|
|white_max|Maximum brightness of white light|`x <= 100`||integer|✓|
|white_power_max|Maximum white light power, 100-200.<br>• If it is set to 100, the total output power is 100% of the single channel.|`100 <= x <= 200`||integer|✓|
|rgb_min|Minimum brightness of color light|`0 <= x`||integer|✓|
|rgb_max|Maximum brightness of color light|`x <= 100`||integer|✓|
|rgb_power_max|Maximum power of color light<br>• If it is set to 100, the total output power is 300% of the single channel, that is, 3-channel full power output.|`100 <= x <= 300`||integer|✓|

### Light Driver: Gamma Configurations


Gamma configurations for light bulb. Applicable for all except when gpio is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gamma_adjust|Enable color light calibration<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|gamma_red|Red gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_green|Green gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_blue|Blue gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_cold|Cold gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_warm|Warm gamma calibration|`50 <= x <= 100`||integer|✓|
|curve_coe|White balance|`0.8 <= x <= 2.2`||number||

### Light Driver: CCT Map Configurations


CCT Map configurations for light bulb. Applicable for light with precise cct control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[cct_kelvin, cct_percentage, coef_red, coef_green, coef_blue, coef_cold, coef_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "cct_map": {
        "table": "[[2200, 0, 0.033, 0.033, 0.034, 0.45, 0.45],[7000, 100, 0.033, 0.033, 0.034, 0.45, 0.45]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|CCT Map Table<br>• cct: Color temperature in kelvin<br>• cct_percentage: Percentage of color temperature<br>• red: Red light output<br>• green: Green light output<br>• blue: Blue light output<br>• cold: Cold white light output<br>• warm: Warm white light output|string||string|✓|

### Light Driver: Color Map Configurations


Color Map configurations for light bulb. Applicable for light with precise color control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[hue, saturation_100_red, saturation_100_green, saturation_100_blue, saturation_100_cold, saturation_100_warm, saturation_50_red, saturation_50_green, saturation_50_blue, saturation_50_cold, saturation_50_warm, saturation_0_red, saturation_0_green, saturation_0_blue, saturation_0_cold, saturation_0_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "color_map": {
        "table": "[[0,1,0,0,0,0,0.9120,0.0440,0.0440,0,0,0.4854,0.2573,0.2573,0,0],[15,0.9218,0.0782,0,0,0,0.8549,0.0907,0.0544,0,0,0.5112,0.2639,0.2248,0,0]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|Color Map Table. Add at least 12 sets of color data|string||string|✓|

### Light Driver: BP5758D Light Driver: Configurations


Applicable if bp5758d is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "bp5758d_config": {
        "gpio_clock": 10,
        "gpio_sda": 4,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_warm": 3,
        "out_cold": 4,
        "out1_current_max": 6,
        "out2_current_max": 6,
        "out3_current_max": 6,
        "out4_current_max": 13,
        "out5_current_max": 13
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|gpio_clock|IIC clock signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|gpio_sda|IIC data signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|iic_khz|IIC signal frequency in KHz|||integer|✓|
|out_red|Red light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_green|Green light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_blue|Blue light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_cold|Cold white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_warm|Warm white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out1_current_max|Maximum #1 channel current in mA|`x <= 90`||integer|✓|
|out2_current_max|Maximum #2 channel current in mA|`x <= 90`||integer|✓|
|out3_current_max|Maximum #3 channel current in mA|`x <= 90`||integer|✓|
|out4_current_max|Maximum #4 channel current in mA|`x <= 90`||integer|✓|
|out5_current_max||`x <= 90`||integer|✓|

## Light Driver: BP1658CJ Light Driver
  
**Section: Driver**

BP1658CJ driver support  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.led",
    "name": "bp1658cj",
    "bp1658cj_config": {
        "gpio_clock": 7,
        "gpio_sda": 3,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_cold": 4,
        "out_warm": 3,
        "white_current_max": 50,
        "rgb_current_max": 50
    },
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    },
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    },
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.led|`ezc.driver.led`||string|✓|
|name|Applicable only if `bp1658cj` is selected as light driver|`bp1658cj`||string|✓|
|lighting_config|More light configurations|[Light Driver: Lighting Configurations](#light-driver-lighting-configurations)||object|✓|
|hardware_config|Hardware configuration of led|[Light Driver: Hardware Configurations](#light-driver-hardware-configurations)||object|✓|
|gamma_config|Gamma configurations for light bulb. Applicable for all except when gpio is selected|[Light Driver: Gamma Configurations](#light-driver-gamma-configurations)||object|✓|
|cct_map||[Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)||object||
|color_map||[Light Driver: Color Map Configurations](#light-driver-color-map-configurations)||object||
|bp1658cj_config|Applicable if `bp1658cj is selected|[Light Driver: BP1658CJ Light Driver: Configurations](#light-driver-bp1658cj-light-driver-configurations)||object|✓|

### Light Driver: Lighting Configurations


More light configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gradient|Switch gradient<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|enable_memory|Retain the power state on reboot|`true`, `false`||boolean|✓|
|enable_lowpower|Low power consumption mode|`true`, `false`||boolean|✓|
|sync_change_brightness|Change the brightness synchronously|`true`, `false`||boolean|✓|
|disable_auto_on|Disable turning on of the light|`true`, `false`||boolean|✓|
|beads_comb|LED Beads Combination support by hardware<br>• 1: C<br>• 2: W<br>• 3: CW<br>• 4: RGB<br>• 5: 4CH_RGBC<br>• 6: 4CH_RGBCC<br>• 7: 4CH_RGBW<br>• 8: 4CH_RGBWW<br>• 9: 5CH_RGBCW<br>• 10: 5CH_RGBCC<br>• 11: 5CH_RGBWW<br>• 12: 5CH_RGBC<br>• 13: 5CH_RGBW|`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`||integer|✓|
|fades_ms|Default ramp time in ms|||integer|✓|
|enable_precise_cct_control|Precise CCT Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|enable_precise_color_control|Precise Color Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|cct_kelvin_min|Min color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 2000K|`1500 <= x <= 7000`|`2200`|integer||
|cct_kelvin_max|Max color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 7000K|`1500 <= x <= 7000`|`7000`|integer||

### Light Driver: Hardware Configurations


Hardware configuration of led  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|white_min|Minimum brightness of white light|`0 <= x`||integer|✓|
|white_max|Maximum brightness of white light|`x <= 100`||integer|✓|
|white_power_max|Maximum white light power, 100-200.<br>• If it is set to 100, the total output power is 100% of the single channel.|`100 <= x <= 200`||integer|✓|
|rgb_min|Minimum brightness of color light|`0 <= x`||integer|✓|
|rgb_max|Maximum brightness of color light|`x <= 100`||integer|✓|
|rgb_power_max|Maximum power of color light<br>• If it is set to 100, the total output power is 300% of the single channel, that is, 3-channel full power output.|`100 <= x <= 300`||integer|✓|

### Light Driver: Gamma Configurations


Gamma configurations for light bulb. Applicable for all except when gpio is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gamma_adjust|Enable color light calibration<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|gamma_red|Red gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_green|Green gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_blue|Blue gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_cold|Cold gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_warm|Warm gamma calibration|`50 <= x <= 100`||integer|✓|
|curve_coe|White balance|`0.8 <= x <= 2.2`||number||

### Light Driver: CCT Map Configurations


CCT Map configurations for light bulb. Applicable for light with precise cct control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[cct_kelvin, cct_percentage, coef_red, coef_green, coef_blue, coef_cold, coef_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "cct_map": {
        "table": "[[2200, 0, 0.033, 0.033, 0.034, 0.45, 0.45],[7000, 100, 0.033, 0.033, 0.034, 0.45, 0.45]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|CCT Map Table<br>• cct: Color temperature in kelvin<br>• cct_percentage: Percentage of color temperature<br>• red: Red light output<br>• green: Green light output<br>• blue: Blue light output<br>• cold: Cold white light output<br>• warm: Warm white light output|string||string|✓|

### Light Driver: Color Map Configurations


Color Map configurations for light bulb. Applicable for light with precise color control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[hue, saturation_100_red, saturation_100_green, saturation_100_blue, saturation_100_cold, saturation_100_warm, saturation_50_red, saturation_50_green, saturation_50_blue, saturation_50_cold, saturation_50_warm, saturation_0_red, saturation_0_green, saturation_0_blue, saturation_0_cold, saturation_0_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "color_map": {
        "table": "[[0,1,0,0,0,0,0.9120,0.0440,0.0440,0,0,0.4854,0.2573,0.2573,0,0],[15,0.9218,0.0782,0,0,0,0.8549,0.0907,0.0544,0,0,0.5112,0.2639,0.2248,0,0]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|Color Map Table. Add at least 12 sets of color data|string||string|✓|

### Light Driver: BP1658CJ Light Driver: Configurations


Applicable if `bp1658cj is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "bp1658cj_config": {
        "gpio_clock": 7,
        "gpio_sda": 3,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_cold": 4,
        "out_warm": 3,
        "white_current_max": 50,
        "rgb_current_max": 50
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|gpio_clock|IIC clock signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|gpio_sda|IIC data signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|iic_khz|IIC signal frequency in KHz|||integer|✓|
|out_red|Red light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_green|Green light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_blue|Blue light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_cold|Cold white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_warm|Warm white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|white_current_max|Maximum white light current in mA|`0 <= x <= 75`||integer|✓|
|rgb_current_max|Maximum current of color light in mA|`0 <= x <= 150`||integer|✓|

## Light Driver: SM2135E Light Driver
  
**Section: Driver**

SM2135E driver support  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.led",
    "name": "sm2135e",
    "sm2135e_config": {
        "gpio_clock": 7,
        "gpio_sda": 3,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_cold": 4,
        "out_warm": 3,
        "white_current_max": 50,
        "rgb_current_max": 30
    },
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    },
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    },
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.led|`ezc.driver.led`||string|✓|
|name|Applicable only if `sm2135e` is selected as light driver|`sm2135e`||string|✓|
|lighting_config|More light configurations|[Light Driver: Lighting Configurations](#light-driver-lighting-configurations)||object|✓|
|hardware_config|Hardware configuration of led|[Light Driver: Hardware Configurations](#light-driver-hardware-configurations)||object|✓|
|gamma_config|Gamma configurations for light bulb. Applicable for all except when gpio is selected|[Light Driver: Gamma Configurations](#light-driver-gamma-configurations)||object|✓|
|cct_map||[Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)||object||
|color_map||[Light Driver: Color Map Configurations](#light-driver-color-map-configurations)||object||
|sm2135e_config|Applicable if `sm2135e is selected|[Light Driver: SM2135E Light Driver: Configurations](#light-driver-sm2135e-light-driver-configurations)||object|✓|

### Light Driver: Lighting Configurations


More light configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gradient|Switch gradient<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|enable_memory|Retain the power state on reboot|`true`, `false`||boolean|✓|
|enable_lowpower|Low power consumption mode|`true`, `false`||boolean|✓|
|sync_change_brightness|Change the brightness synchronously|`true`, `false`||boolean|✓|
|disable_auto_on|Disable turning on of the light|`true`, `false`||boolean|✓|
|beads_comb|LED Beads Combination support by hardware<br>• 1: C<br>• 2: W<br>• 3: CW<br>• 4: RGB<br>• 5: 4CH_RGBC<br>• 6: 4CH_RGBCC<br>• 7: 4CH_RGBW<br>• 8: 4CH_RGBWW<br>• 9: 5CH_RGBCW<br>• 10: 5CH_RGBCC<br>• 11: 5CH_RGBWW<br>• 12: 5CH_RGBC<br>• 13: 5CH_RGBW|`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`||integer|✓|
|fades_ms|Default ramp time in ms|||integer|✓|
|enable_precise_cct_control|Precise CCT Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|enable_precise_color_control|Precise Color Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|cct_kelvin_min|Min color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 2000K|`1500 <= x <= 7000`|`2200`|integer||
|cct_kelvin_max|Max color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 7000K|`1500 <= x <= 7000`|`7000`|integer||

### Light Driver: Hardware Configurations


Hardware configuration of led  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|white_min|Minimum brightness of white light|`0 <= x`||integer|✓|
|white_max|Maximum brightness of white light|`x <= 100`||integer|✓|
|white_power_max|Maximum white light power, 100-200.<br>• If it is set to 100, the total output power is 100% of the single channel.|`100 <= x <= 200`||integer|✓|
|rgb_min|Minimum brightness of color light|`0 <= x`||integer|✓|
|rgb_max|Maximum brightness of color light|`x <= 100`||integer|✓|
|rgb_power_max|Maximum power of color light<br>• If it is set to 100, the total output power is 300% of the single channel, that is, 3-channel full power output.|`100 <= x <= 300`||integer|✓|

### Light Driver: Gamma Configurations


Gamma configurations for light bulb. Applicable for all except when gpio is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gamma_adjust|Enable color light calibration<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|gamma_red|Red gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_green|Green gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_blue|Blue gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_cold|Cold gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_warm|Warm gamma calibration|`50 <= x <= 100`||integer|✓|
|curve_coe|White balance|`0.8 <= x <= 2.2`||number||

### Light Driver: CCT Map Configurations


CCT Map configurations for light bulb. Applicable for light with precise cct control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[cct_kelvin, cct_percentage, coef_red, coef_green, coef_blue, coef_cold, coef_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "cct_map": {
        "table": "[[2200, 0, 0.033, 0.033, 0.034, 0.45, 0.45],[7000, 100, 0.033, 0.033, 0.034, 0.45, 0.45]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|CCT Map Table<br>• cct: Color temperature in kelvin<br>• cct_percentage: Percentage of color temperature<br>• red: Red light output<br>• green: Green light output<br>• blue: Blue light output<br>• cold: Cold white light output<br>• warm: Warm white light output|string||string|✓|

### Light Driver: Color Map Configurations


Color Map configurations for light bulb. Applicable for light with precise color control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[hue, saturation_100_red, saturation_100_green, saturation_100_blue, saturation_100_cold, saturation_100_warm, saturation_50_red, saturation_50_green, saturation_50_blue, saturation_50_cold, saturation_50_warm, saturation_0_red, saturation_0_green, saturation_0_blue, saturation_0_cold, saturation_0_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "color_map": {
        "table": "[[0,1,0,0,0,0,0.9120,0.0440,0.0440,0,0,0.4854,0.2573,0.2573,0,0],[15,0.9218,0.0782,0,0,0,0.8549,0.0907,0.0544,0,0,0.5112,0.2639,0.2248,0,0]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|Color Map Table. Add at least 12 sets of color data|string||string|✓|

### Light Driver: SM2135E Light Driver: Configurations


Applicable if `sm2135e is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "sm2135e_config": {
        "gpio_clock": 7,
        "gpio_sda": 3,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_cold": 4,
        "out_warm": 3,
        "white_current_max": 50,
        "rgb_current_max": 30
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|gpio_clock|IIC clock signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|gpio_sda|IIC data signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|iic_khz|IIC signal frequency in KHz|||integer|✓|
|out_red|Red light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_green|Green light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_blue|Blue light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_cold|Cold white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_warm|Warm white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|white_current_max|Maximum white light current in mA|`10 <= x <= 60`||integer|✓|
|rgb_current_max|Maximum current of color light in mA|`10 <= x <= 50`||integer|✓|

## Light Driver: SM2135EH Light Driver
  
**Section: Driver**

SM2135EH driver support  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.led",
    "name": "sm2135eh",
    "sm2135eh_config": {
        "gpio_clock": 7,
        "gpio_sda": 3,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_cold": 4,
        "out_warm": 3,
        "white_current_max": 50,
        "rgb_current_max": 28
    },
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    },
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    },
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.led|`ezc.driver.led`||string|✓|
|name|Applicable only if `sm2135eh` is selected as light driver|`sm2135eh`||string|✓|
|lighting_config|More light configurations|[Light Driver: Lighting Configurations](#light-driver-lighting-configurations)||object|✓|
|hardware_config|Hardware configuration of led|[Light Driver: Hardware Configurations](#light-driver-hardware-configurations)||object|✓|
|gamma_config|Gamma configurations for light bulb. Applicable for all except when gpio is selected|[Light Driver: Gamma Configurations](#light-driver-gamma-configurations)||object|✓|
|cct_map||[Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)||object||
|color_map||[Light Driver: Color Map Configurations](#light-driver-color-map-configurations)||object||
|sm2135eh_config|Applicable if `sm2135eh is selected|[Light Driver: SM2135EH Light Driver: Configurations](#light-driver-sm2135eh-light-driver-configurations)||object|✓|

### Light Driver: Lighting Configurations


More light configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gradient|Switch gradient<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|enable_memory|Retain the power state on reboot|`true`, `false`||boolean|✓|
|enable_lowpower|Low power consumption mode|`true`, `false`||boolean|✓|
|sync_change_brightness|Change the brightness synchronously|`true`, `false`||boolean|✓|
|disable_auto_on|Disable turning on of the light|`true`, `false`||boolean|✓|
|beads_comb|LED Beads Combination support by hardware<br>• 1: C<br>• 2: W<br>• 3: CW<br>• 4: RGB<br>• 5: 4CH_RGBC<br>• 6: 4CH_RGBCC<br>• 7: 4CH_RGBW<br>• 8: 4CH_RGBWW<br>• 9: 5CH_RGBCW<br>• 10: 5CH_RGBCC<br>• 11: 5CH_RGBWW<br>• 12: 5CH_RGBC<br>• 13: 5CH_RGBW|`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`||integer|✓|
|fades_ms|Default ramp time in ms|||integer|✓|
|enable_precise_cct_control|Precise CCT Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|enable_precise_color_control|Precise Color Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|cct_kelvin_min|Min color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 2000K|`1500 <= x <= 7000`|`2200`|integer||
|cct_kelvin_max|Max color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 7000K|`1500 <= x <= 7000`|`7000`|integer||

### Light Driver: Hardware Configurations


Hardware configuration of led  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|white_min|Minimum brightness of white light|`0 <= x`||integer|✓|
|white_max|Maximum brightness of white light|`x <= 100`||integer|✓|
|white_power_max|Maximum white light power, 100-200.<br>• If it is set to 100, the total output power is 100% of the single channel.|`100 <= x <= 200`||integer|✓|
|rgb_min|Minimum brightness of color light|`0 <= x`||integer|✓|
|rgb_max|Maximum brightness of color light|`x <= 100`||integer|✓|
|rgb_power_max|Maximum power of color light<br>• If it is set to 100, the total output power is 300% of the single channel, that is, 3-channel full power output.|`100 <= x <= 300`||integer|✓|

### Light Driver: Gamma Configurations


Gamma configurations for light bulb. Applicable for all except when gpio is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gamma_adjust|Enable color light calibration<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|gamma_red|Red gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_green|Green gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_blue|Blue gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_cold|Cold gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_warm|Warm gamma calibration|`50 <= x <= 100`||integer|✓|
|curve_coe|White balance|`0.8 <= x <= 2.2`||number||

### Light Driver: CCT Map Configurations


CCT Map configurations for light bulb. Applicable for light with precise cct control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[cct_kelvin, cct_percentage, coef_red, coef_green, coef_blue, coef_cold, coef_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "cct_map": {
        "table": "[[2200, 0, 0.033, 0.033, 0.034, 0.45, 0.45],[7000, 100, 0.033, 0.033, 0.034, 0.45, 0.45]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|CCT Map Table<br>• cct: Color temperature in kelvin<br>• cct_percentage: Percentage of color temperature<br>• red: Red light output<br>• green: Green light output<br>• blue: Blue light output<br>• cold: Cold white light output<br>• warm: Warm white light output|string||string|✓|

### Light Driver: Color Map Configurations


Color Map configurations for light bulb. Applicable for light with precise color control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[hue, saturation_100_red, saturation_100_green, saturation_100_blue, saturation_100_cold, saturation_100_warm, saturation_50_red, saturation_50_green, saturation_50_blue, saturation_50_cold, saturation_50_warm, saturation_0_red, saturation_0_green, saturation_0_blue, saturation_0_cold, saturation_0_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "color_map": {
        "table": "[[0,1,0,0,0,0,0.9120,0.0440,0.0440,0,0,0.4854,0.2573,0.2573,0,0],[15,0.9218,0.0782,0,0,0,0.8549,0.0907,0.0544,0,0,0.5112,0.2639,0.2248,0,0]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|Color Map Table. Add at least 12 sets of color data|string||string|✓|

### Light Driver: SM2135EH Light Driver: Configurations


Applicable if `sm2135eh is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "sm2135eh_config": {
        "gpio_clock": 7,
        "gpio_sda": 3,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_cold": 4,
        "out_warm": 3,
        "white_current_max": 50,
        "rgb_current_max": 28
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|gpio_clock|IIC clock signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|gpio_sda|IIC data signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|iic_khz|IIC signal frequency in KHz|||integer|✓|
|out_red|Red light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_green|Green light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_blue|Blue light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_cold|Cold white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_warm|Warm white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|white_current_max|Maximum white light current in mA|`0`, `5`, `10`, `15`, `20`, `25`, `30`, `35`, `40`, `45`, `50`, `55`, `59`, `63`, `67`, `71`||integer|✓|
|rgb_current_max|Maximum current of color light in mA|`4 <= x <= 64`||integer|✓|

## Light Driver: SM2135EGH Light Driver
  
**Section: Driver**

SM2135EGH driver support  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.led",
    "name": "sm2235egh",
    "sm2235egh_config": {
        "gpio_clock": 7,
        "gpio_sda": 3,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_cold": 4,
        "out_warm": 3,
        "white_current_max": 50,
        "rgb_current_max": 28
    },
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    },
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    },
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.led|`ezc.driver.led`||string|✓|
|name|Applicable only if `sm2135egh` is selected as light driver|`sm2235egh`||string|✓|
|lighting_config|More light configurations|[Light Driver: Lighting Configurations](#light-driver-lighting-configurations)||object|✓|
|hardware_config|Hardware configuration of led|[Light Driver: Hardware Configurations](#light-driver-hardware-configurations)||object|✓|
|gamma_config|Gamma configurations for light bulb. Applicable for all except when gpio is selected|[Light Driver: Gamma Configurations](#light-driver-gamma-configurations)||object|✓|
|cct_map||[Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)||object||
|color_map||[Light Driver: Color Map Configurations](#light-driver-color-map-configurations)||object||
|sm2235egh_config|Applicable if `sm2235egh is selected|[Light Driver: SM2135EGH Light Driver: Configurations](#light-driver-sm2135egh-light-driver-configurations)||object|✓|

### Light Driver: Lighting Configurations


More light configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gradient|Switch gradient<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|enable_memory|Retain the power state on reboot|`true`, `false`||boolean|✓|
|enable_lowpower|Low power consumption mode|`true`, `false`||boolean|✓|
|sync_change_brightness|Change the brightness synchronously|`true`, `false`||boolean|✓|
|disable_auto_on|Disable turning on of the light|`true`, `false`||boolean|✓|
|beads_comb|LED Beads Combination support by hardware<br>• 1: C<br>• 2: W<br>• 3: CW<br>• 4: RGB<br>• 5: 4CH_RGBC<br>• 6: 4CH_RGBCC<br>• 7: 4CH_RGBW<br>• 8: 4CH_RGBWW<br>• 9: 5CH_RGBCW<br>• 10: 5CH_RGBCC<br>• 11: 5CH_RGBWW<br>• 12: 5CH_RGBC<br>• 13: 5CH_RGBW|`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`||integer|✓|
|fades_ms|Default ramp time in ms|||integer|✓|
|enable_precise_cct_control|Precise CCT Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|enable_precise_color_control|Precise Color Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|cct_kelvin_min|Min color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 2000K|`1500 <= x <= 7000`|`2200`|integer||
|cct_kelvin_max|Max color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 7000K|`1500 <= x <= 7000`|`7000`|integer||

### Light Driver: Hardware Configurations


Hardware configuration of led  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|white_min|Minimum brightness of white light|`0 <= x`||integer|✓|
|white_max|Maximum brightness of white light|`x <= 100`||integer|✓|
|white_power_max|Maximum white light power, 100-200.<br>• If it is set to 100, the total output power is 100% of the single channel.|`100 <= x <= 200`||integer|✓|
|rgb_min|Minimum brightness of color light|`0 <= x`||integer|✓|
|rgb_max|Maximum brightness of color light|`x <= 100`||integer|✓|
|rgb_power_max|Maximum power of color light<br>• If it is set to 100, the total output power is 300% of the single channel, that is, 3-channel full power output.|`100 <= x <= 300`||integer|✓|

### Light Driver: Gamma Configurations


Gamma configurations for light bulb. Applicable for all except when gpio is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gamma_adjust|Enable color light calibration<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|gamma_red|Red gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_green|Green gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_blue|Blue gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_cold|Cold gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_warm|Warm gamma calibration|`50 <= x <= 100`||integer|✓|
|curve_coe|White balance|`0.8 <= x <= 2.2`||number||

### Light Driver: CCT Map Configurations


CCT Map configurations for light bulb. Applicable for light with precise cct control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[cct_kelvin, cct_percentage, coef_red, coef_green, coef_blue, coef_cold, coef_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "cct_map": {
        "table": "[[2200, 0, 0.033, 0.033, 0.034, 0.45, 0.45],[7000, 100, 0.033, 0.033, 0.034, 0.45, 0.45]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|CCT Map Table<br>• cct: Color temperature in kelvin<br>• cct_percentage: Percentage of color temperature<br>• red: Red light output<br>• green: Green light output<br>• blue: Blue light output<br>• cold: Cold white light output<br>• warm: Warm white light output|string||string|✓|

### Light Driver: Color Map Configurations


Color Map configurations for light bulb. Applicable for light with precise color control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[hue, saturation_100_red, saturation_100_green, saturation_100_blue, saturation_100_cold, saturation_100_warm, saturation_50_red, saturation_50_green, saturation_50_blue, saturation_50_cold, saturation_50_warm, saturation_0_red, saturation_0_green, saturation_0_blue, saturation_0_cold, saturation_0_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "color_map": {
        "table": "[[0,1,0,0,0,0,0.9120,0.0440,0.0440,0,0,0.4854,0.2573,0.2573,0,0],[15,0.9218,0.0782,0,0,0,0.8549,0.0907,0.0544,0,0,0.5112,0.2639,0.2248,0,0]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|Color Map Table. Add at least 12 sets of color data|string||string|✓|

### Light Driver: SM2135EGH Light Driver: Configurations


Applicable if `sm2235egh is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "sm2235egh_config": {
        "gpio_clock": 7,
        "gpio_sda": 3,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_cold": 4,
        "out_warm": 3,
        "white_current_max": 50,
        "rgb_current_max": 28
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|gpio_clock|IIC clock signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|gpio_sda|IIC data signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|iic_khz|IIC signal frequency in KHz|||integer|✓|
|out_red|Red light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_green|Green light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_blue|Blue light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_cold|Cold white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_warm|Warm white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|white_current_max|Maximum white light current in mA|`5 <= x <= 80`||integer|✓|
|rgb_current_max|Maximum current of color light in mA|`4 <= x <= 64`||integer|✓|

## Light Driver: SM2335EGH Light Driver
  
**Section: Driver**

SM2335EGH driver support  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.led",
    "name": "sm2335egh",
    "sm2335egh_config": {
        "gpio_clock": 7,
        "gpio_sda": 3,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_cold": 4,
        "out_warm": 3,
        "white_current_max": 50,
        "rgb_current_max": 30
    },
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    },
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    },
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.led|`ezc.driver.led`||string|✓|
|name|Applicable only if `sm2335egh` is selected as light driver|`sm2335egh`||string|✓|
|lighting_config|More light configurations|[Light Driver: Lighting Configurations](#light-driver-lighting-configurations)||object|✓|
|hardware_config|Hardware configuration of led|[Light Driver: Hardware Configurations](#light-driver-hardware-configurations)||object|✓|
|gamma_config|Gamma configurations for light bulb. Applicable for all except when gpio is selected|[Light Driver: Gamma Configurations](#light-driver-gamma-configurations)||object|✓|
|cct_map||[Light Driver: CCT Map Configurations](#light-driver-cct-map-configurations)||object||
|color_map||[Light Driver: Color Map Configurations](#light-driver-color-map-configurations)||object||
|sm2335egh_config|Applicable if `sm2335egh` is selected|[Light Driver: SM2335EGH Light Driver: Configurations](#light-driver-sm2335egh-light-driver-configurations)||object|✓|

### Light Driver: Lighting Configurations


More light configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "lighting_config": {
        "enable_gradient": true,
        "enable_memory": false,
        "enable_lowpower": false,
        "sync_change_brightness": true,
        "disable_auto_on": true,
        "beads_comb": 3,
        "fades_ms": 300,
        "cct_kelvin_min": 2200,
        "cct_kelvin_max": 7000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gradient|Switch gradient<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|enable_memory|Retain the power state on reboot|`true`, `false`||boolean|✓|
|enable_lowpower|Low power consumption mode|`true`, `false`||boolean|✓|
|sync_change_brightness|Change the brightness synchronously|`true`, `false`||boolean|✓|
|disable_auto_on|Disable turning on of the light|`true`, `false`||boolean|✓|
|beads_comb|LED Beads Combination support by hardware<br>• 1: C<br>• 2: W<br>• 3: CW<br>• 4: RGB<br>• 5: 4CH_RGBC<br>• 6: 4CH_RGBCC<br>• 7: 4CH_RGBW<br>• 8: 4CH_RGBWW<br>• 9: 5CH_RGBCW<br>• 10: 5CH_RGBCC<br>• 11: 5CH_RGBWW<br>• 12: 5CH_RGBC<br>• 13: 5CH_RGBW|`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`||integer|✓|
|fades_ms|Default ramp time in ms|||integer|✓|
|enable_precise_cct_control|Precise CCT Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|enable_precise_color_control|Precise Color Control<br>• true: enable<br>• false: disable|`true`, `false`||boolean||
|cct_kelvin_min|Min color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 2000K|`1500 <= x <= 7000`|`2200`|integer||
|cct_kelvin_max|Max color temperature support by hardware in kelvin<br>Range: 1500K~7000K<br>Default: 7000K|`1500 <= x <= 7000`|`7000`|integer||

### Light Driver: Hardware Configurations


Hardware configuration of led  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "hardware_config": {
        "white_min": 1,
        "white_max": 100,
        "white_power_max": 100,
        "rgb_min": 1,
        "rgb_max": 100,
        "rgb_power_max": 100
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|white_min|Minimum brightness of white light|`0 <= x`||integer|✓|
|white_max|Maximum brightness of white light|`x <= 100`||integer|✓|
|white_power_max|Maximum white light power, 100-200.<br>• If it is set to 100, the total output power is 100% of the single channel.|`100 <= x <= 200`||integer|✓|
|rgb_min|Minimum brightness of color light|`0 <= x`||integer|✓|
|rgb_max|Maximum brightness of color light|`x <= 100`||integer|✓|
|rgb_power_max|Maximum power of color light<br>• If it is set to 100, the total output power is 300% of the single channel, that is, 3-channel full power output.|`100 <= x <= 300`||integer|✓|

### Light Driver: Gamma Configurations


Gamma configurations for light bulb. Applicable for all except when gpio is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gamma_config": {
        "enable_gamma_adjust": true,
        "gamma_red": 100,
        "gamma_green": 100,
        "gamma_blue": 100,
        "gamma_cold": 100,
        "gamma_warm": 100,
        "curve_coe": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enable_gamma_adjust|Enable color light calibration<br>• true: enable<br>• false: disable|`true`, `false`||boolean|✓|
|gamma_red|Red gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_green|Green gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_blue|Blue gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_cold|Cold gamma calibration|`50 <= x <= 100`||integer|✓|
|gamma_warm|Warm gamma calibration|`50 <= x <= 100`||integer|✓|
|curve_coe|White balance|`0.8 <= x <= 2.2`||number||

### Light Driver: CCT Map Configurations


CCT Map configurations for light bulb. Applicable for light with precise cct control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[cct_kelvin, cct_percentage, coef_red, coef_green, coef_blue, coef_cold, coef_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "cct_map": {
        "table": "[[2200, 0, 0.033, 0.033, 0.034, 0.45, 0.45],[7000, 100, 0.033, 0.033, 0.034, 0.45, 0.45]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|CCT Map Table<br>• cct: Color temperature in kelvin<br>• cct_percentage: Percentage of color temperature<br>• red: Red light output<br>• green: Green light output<br>• blue: Blue light output<br>• cold: Cold white light output<br>• warm: Warm white light output|string||string|✓|

### Light Driver: Color Map Configurations


Color Map configurations for light bulb. Applicable for light with precise color control enable<br>Map data format is as follows:<br>&nbsp;&nbsp;[[hue, saturation_100_red, saturation_100_green, saturation_100_blue, saturation_100_cold, saturation_100_warm, saturation_50_red, saturation_50_green, saturation_50_blue, saturation_50_cold, saturation_50_warm, saturation_0_red, saturation_0_green, saturation_0_blue, saturation_0_cold, saturation_0_warm], ...]  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "color_map": {
        "table": "[[0,1,0,0,0,0,0.9120,0.0440,0.0440,0,0,0.4854,0.2573,0.2573,0,0],[15,0.9218,0.0782,0,0,0,0.8549,0.0907,0.0544,0,0,0.5112,0.2639,0.2248,0,0]]"
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|table|Color Map Table. Add at least 12 sets of color data|string||string|✓|

### Light Driver: SM2335EGH Light Driver: Configurations


Applicable if `sm2335egh` is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "sm2335egh_config": {
        "gpio_clock": 7,
        "gpio_sda": 3,
        "iic_khz": 300,
        "out_red": 2,
        "out_green": 1,
        "out_blue": 0,
        "out_cold": 4,
        "out_warm": 3,
        "white_current_max": 50,
        "rgb_current_max": 30
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|gpio_clock|IIC clock signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|gpio_sda|IIC data signal pin. Range of values depend on the chip|`0 <= x`||integer|✓|
|iic_khz|IIC signal frequency in KHz|||integer|✓|
|out_red|Red light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_green|Green light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_blue|Blue light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_cold|Cold white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|out_warm|Warm white light output pin. Range of values depend on the chip|`-1`, `0`, `1`, `2`, `3`, `4`||integer|✓|
|white_current_max|Maximum white light current in mA|`5 <= x <= 80`||integer|✓|
|rgb_current_max|Maximum current of color light in mA|`10 <= x <= 160`||integer|✓|

## Light Driver: GPIO LED Driver
  
**Section: Driver**

GPIO powered led driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1002,
    "type": "ezc.driver.led",
    "name": "gpio",
    "gpio_config": {
        "gpio_num": 12,
        "active_level": 0
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.led|`ezc.driver.led`||string|✓|
|name|`gpio` applicable only if gpio led driver is selected|`gpio`||string|✓|
|gpio_config|Applicable if gpio is selected|[Light Driver: GPIO LED Driver: Configurations](#light-driver-gpio-led-driver-configurations)||object|✓|

### Light Driver: GPIO LED Driver: Configurations


Applicable if gpio is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "gpio_config": {
        "gpio_num": 10,
        "active_level": 0
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|gpio_num|Output GPIO for the driver. Range of values depend on the chip|`0 <= x`||integer|✓|
|active_level|When is the output turned on<br>• 0: The output is on when it connected to GND<br>• 1: The output is on when it connected to VCC|`0`, `1`||integer|✓|

## ZeroDetect Driver
  
**Section: Driver**

ZeroDetect driver to capture Zero-Cross signal  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.zero_detect",
    "name": "gpio",
    "capture_gpio_num": 6,
    "zero_signal_type": 1,
    "max_freq_hz": 65,
    "min_freq_hz": 45,
    "valid_times": 6,
    "invalid_times": 20,
    "signal_lost_time_us": 100000
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.zero_detect|`ezc.driver.zero_detect`||string|✓|
|name|ZeroDetect subtype|`gpio`, `mcpwm`||string|✓|
|capture_gpio_num|Input GPIO for the driver. Range of values depend on the chip|`0 <= x`||integer|✓|
|zero_signal_type|Zero-crossing signal types include pulse and square wave.|`0`, `1`||integer|✓|
|max_freq_hz|Support Maximum Frequency of Zero-Cross Detection Signal.|`10 <= x <= 200`||integer|✓|
|min_freq_hz|Support Minimum Frequency of Zero-Cross Detection Signal.|`10 <= x <= 200`||integer|✓|
|valid_times|When the zero-cross detection signal is within the frequency range, it will be considered as a valid signal if it occurs more than X times.|`0 <= x <= 200`||integer|✓|
|invalid_times|When the zero-cross detection signal is without the frequency range, it will be considered as a in-valid signal if it occurs more than X times.|`0 <= x <= 200`||integer|✓|
|signal_lost_time_us|Timeout duration for determining signal loss.|`1 <= x <= 18446744073709551615`||integer|✓|

## Temperature Sensor Driver: OnChip Driver
  
**Section: Driver**

Applicable if OnChip is selected as Temperature Sensor Driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.temp_sensor",
    "name": "onchip",
    "onchip_config": {
        "range_min": 50,
        "range_max": 125
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.temp_sensor|`ezc.driver.temp_sensor`||string|✓|
|name|Driver name: OnChip|`onchip`||string|✓|
|onchip_config|Applicable if OnChip Sensor is selected|[Temperature Sensor Driver: OnChip Configuration](#temperature-sensor-driver-onchip-configuration)||object|✓|

### Temperature Sensor Driver: OnChip Configuration


Applicable if OnChip Sensor is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "onchip_config": {
        "range_min": 50,
        "range_max": 125
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|range_min|The minimum value of the temperature want to test (in degree Celcius)|`-40 <= x <= 500`|`-40`|integer||
|range_max|The maximum value of the temperature want to test (in degree Celcius)|`-40 <= x <= 500`|`125`|integer||

## Temperature Sensor Driver: NTC Driver
  
**Section: Driver**

Applicable if NTC is selected as Temperature Sensor Driver  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "id": 1000,
    "type": "ezc.driver.temp_sensor",
    "name": "ntc",
    "ntc_config": {
        "b_value": 3950,
        "r25_ohm": 10000,
        "fixed_ohm": 10000,
        "vdd_mv": 3300,
        "circuit_mode": 1,
        "atten": 3,
        "unit": 0,
        "channel": 3
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections.|`1000 <= x <= 1999`||integer|✓|
|type|Driver: ezc.driver.temp_sensor|`ezc.driver.temp_sensor`||string|✓|
|name|Driver name: NTC|`ntc`||string|✓|
|ntc_config|Applicable if NTC is selected|[Temperature Sensor Driver: NTC Configuration](#temperature-sensor-driver-ntc-configuration)||object|✓|

### Temperature Sensor Driver: NTC Configuration


Applicable if NTC is selected  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "ntc_config": {
        "b_value": 3950,
        "r25_ohm": 10000,
        "fixed_ohm": 10000,
        "vdd_mv": 3300,
        "circuit_mode": 1,
        "atten": 3,
        "unit": 0,
        "channel": 3
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|b_value|beta value of NTC (K)|`0 <= x <= 65535`|`3950`|integer||
|r25_ohm|25℃ resistor value of NTC (K)|`0 <= x <= 65535`|`10000`|integer||
|fixed_ohm|fixed resistor value (Ω)|`0 <= x <= 65535`|`10000`|integer||
|vdd_mv|vdd voltage (mv)|`0 <= x <= 65535`|`3300`|integer||
|circuit_mode|ntc circuit mode|`1 <= x <= 2`|`1`|integer||
|atten|adc atten|`0 <= x <= 65535`|`3`|integer||
|unit|adc channel|`0 <= x <= 65535`||integer||
|channel|adc unit|`0 <= x <= 65535`|`3`|integer||

# Product Common

## Indicator
  
**Section: Product Common**

Indicator for various events to be shown on the product.  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.indicator",
    "subtype": 0,
    "driver": {
        "output": 1000
    },
    "events": [
        {
            "name": "setup_mode_start",
            "mode": "breathe",
            "speed": 2000,
            "color_select": 1,
            "r": 0,
            "g": 255,
            "b": 0,
            "min_brightness": 20,
            "max_brightness": 100,
            "total_ms": 0,
            "interrupt_forbidden": true
        },
        {
            "name": "setup_successful",
            "mode": "restore"
        }
    ]
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.indicator|`ezc.product_common.indicator`||string|✓|
|subtype||`0`||integer|✓|
|driver|Driver details for indicator.|[Indicator: Driver Configurations](#indicator-driver-configurations)||object|✓|
|events|Various events and how should the output be shown. Example, for LED indicators, these can be in the form of some LED patterns.|[Indicator: Event: Restore](#indicator-event-restore), [Indicator: Event: Solid: RGB](#indicator-event-solid-rgb), [Indicator: Event: Solid: CCT](#indicator-event-solid-cct), [Indicator: Event: Blink/Breathe: RGB](#indicator-event-blinkbreathe-rgb), [Indicator: Event: Blink/Breathe: CCT](#indicator-event-blinkbreathe-cct)||object|✓|

### Indicator: Driver Configurations


Driver details for indicator.  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "output": 1000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|output|Output Driver ID for indicator.|`1000 <= x <= 1999`||integer|✓|

### Indicator: Event: Restore


Stop the effect and go back to previous state  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "name": "setup_mode_start",
    "mode": "restore"
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|name|• setup_mode_start: Device in setup mode<br>• setup_started: Device setup started<br>• setup_successful: Device setup completed successfully<br>• setup_failed: Device setup completed failed<br>• identification_start: Identification start<br>• identification_stop: Identification stop<br>• identification_blink: Identification blink effect<br>• identification_breathe: Identification breathe effect<br>• identification_okay: Identification okay effect<br>• identification_channel_change: Identification channel change effect<br>• identification_finish_effect: Identification finish the current effect and stop<br>• identification_stop_effect: Identification stop immediately<br>• factory_reset_triggered: Factory reset has been triggered and will be performed now<br>• forced_rollback_triggered: Forced rollback has been triggered and will be performed now<br>• driver_mode: Used to indicate the mode in which the driver currently is<br>• test_mode_start: Test mode has been started<br>• test_mode_complete: Test mode has been completed<br>• test_mode_ble: Test mode BLE for advertising mac has been started|`setup_mode_start`, `setup_mode_end`, `setup_started`, `setup_successful`, `setup_failed`, `identification_start`, `identification_stop`, `identification_blink`, `identification_breathe`, `identification_okay`, `identification_channel_change`, `identification_finish_effect`, `identification_stop_effect`, `factory_reset_triggered`, `forced_rollback_triggered`, `driver_mode`, `test_mode_start`, `test_mode_complete`, `test_mode_ble`, `advertise_self_mac_trigged`, `ready`, `network_connected`, `network_disconnected`, `normal_temp`, `warn_temp`, `protect_temp`||string|✓|
|mode|Indicator Event: `restore`|`restore`||string|✓|

### Indicator: Event: Solid: RGB


Event solid for color select: `Color`  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "name": "setup_mode_start",
    "mode": "solid",
    "speed": 2000,
    "color_select": 1,
    "r": 0,
    "g": 0,
    "b": 0,
    "max_brightness": 100
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|color_select|Color mode to be used for the effect. Should be `1` for rgb color mode|`1`||integer|✓|
|r|Red value for the effect|`0 <= x <= 255`||integer|✓|
|g|Green value for the effect|`0 <= x <= 255`||integer|✓|
|b|Blue value for the effect|`0 <= x <= 255`||integer|✓|
|name||`setup_mode_start`, `setup_mode_end`, `setup_started`, `setup_successful`, `setup_failed`, `identification_start`, `identification_stop`, `identification_blink`, `identification_breathe`, `identification_okay`, `identification_channel_change`, `identification_finish_effect`, `identification_stop_effect`, `factory_reset_triggered`, `forced_rollback_triggered`, `driver_mode`, `test_mode_start`, `test_mode_complete`, `test_mode_ble`, `advertise_self_mac_trigged`, `ready`, `network_connected`, `network_disconnected`, `normal_temp`, `warn_temp`, `protect_temp`||string|✓|
|mode|`solid` for mode Solid|`solid`||string|✓|
|max_brightness||`0 <= x <= 100`||integer|✓|

### Indicator: Event: Solid: CCT


Event solid for color select: `White`  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "name": "setup_mode_start",
    "mode": "solid",
    "speed": 2000,
    "color_select": 2,
    "cct": 0,
    "max_brightness": 100
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|color_select|Color mode selection to be used for the effect. Should be `2` for white color mode|`2`||integer|✓|
|cct|CCT value used for the effect, percentage or kelvin|`0 <= x <= 10000`|`50`|integer||
|name||`setup_mode_start`, `setup_mode_end`, `setup_started`, `setup_successful`, `setup_failed`, `identification_start`, `identification_stop`, `identification_blink`, `identification_breathe`, `identification_okay`, `identification_channel_change`, `identification_finish_effect`, `identification_stop_effect`, `factory_reset_triggered`, `forced_rollback_triggered`, `driver_mode`, `test_mode_start`, `test_mode_complete`, `test_mode_ble`, `advertise_self_mac_trigged`, `ready`, `network_connected`, `network_disconnected`, `normal_temp`, `warn_temp`, `protect_temp`||string|✓|
|mode|`solid` for mode Solid|`solid`||string|✓|
|max_brightness||`0 <= x <= 100`||integer|✓|

### Indicator: Event: Blink/Breathe: RGB


Event Blink or Breathe for color select: `Color`  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "name": "setup_mode_start",
    "mode": "breathe",
    "speed": 2000,
    "color_select": 1,
    "r": 0,
    "g": 255,
    "b": 0,
    "min_brightness": 20,
    "max_brightness": 100,
    "total_ms": 0,
    "interrupt_forbidden": true
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|color_select|Color mode to be used for the effect. Should be `1` for rgb color mode|`1`||integer|✓|
|r|Red value for the effect|`0 <= x <= 255`||integer|✓|
|g|Green value for the effect|`0 <= x <= 255`||integer|✓|
|b|Blue value for the effect|`0 <= x <= 255`||integer|✓|
|name||`setup_mode_start`, `setup_mode_end`, `setup_started`, `setup_successful`, `setup_failed`, `identification_start`, `identification_stop`, `identification_blink`, `identification_breathe`, `identification_okay`, `identification_channel_change`, `identification_finish_effect`, `identification_stop_effect`, `factory_reset_triggered`, `forced_rollback_triggered`, `driver_mode`, `test_mode_start`, `test_mode_complete`, `test_mode_ble`, `advertise_self_mac_trigged`, `ready`, `network_connected`, `network_disconnected`, `normal_temp`, `warn_temp`, `protect_temp`||string|✓|
|mode|Effect type<br>• breathe: Maximum brightness to minimum brightness and back to maximum brightness, gradually<br>• blink: Maximum brightness to minimum brightness and back to maximum brightness, instantly|`blink`, `breathe`||string|✓|
|speed|Time for a cycle to compelete, in case of breathe or blink, in m.<br>• default: 500|`0 <= x`||integer|✓|
|min_brightness|Minimum brightness upto which the effect should go|`0 <= x <= 100`||integer|✓|
|max_brightness|Maximum brightness upto which the effect should go, also used in solid mode|`0 <= x <= 100`||integer|✓|
|total_ms||`0 <= x`||integer|✓|
|interrupt_forbidden||`true`, `false`||boolean||

### Indicator: Event: Blink/Breathe: CCT


Event Blink or Breathe for color select: `White`  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "name": "setup_mode_start",
    "mode": "breathe",
    "speed": 2000,
    "color_select": 2,
    "cct": 0,
    "min_brightness": 20,
    "max_brightness": 100,
    "total_ms": 0,
    "interrupt_forbidden": true
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|color_select|Color mode selection to be used for the effect. Should be `2` for white color mode|`2`||integer|✓|
|cct|CCT value used for the effect, percentage or kelvin|`0 <= x <= 10000`|`50`|integer||
|name||`setup_mode_start`, `setup_mode_end`, `setup_started`, `setup_successful`, `setup_failed`, `identification_start`, `identification_stop`, `identification_blink`, `identification_breathe`, `identification_okay`, `identification_channel_change`, `identification_finish_effect`, `identification_stop_effect`, `factory_reset_triggered`, `forced_rollback_triggered`, `driver_mode`, `test_mode_start`, `test_mode_complete`, `test_mode_ble`, `advertise_self_mac_trigged`, `ready`, `network_connected`, `network_disconnected`, `normal_temp`, `warn_temp`, `protect_temp`||string|✓|
|mode|Effect type<br>• breathe: Maximum brightness to minimum brightness and back to maximum brightness, gradually<br>• blink: Maximum brightness to minimum brightness and back to maximum brightness, instantly|`blink`, `breathe`||string|✓|
|speed|Time for a cycle to compelete, in case of breathe or blink, in m.<br>• default: 500|`0 <= x`||integer|✓|
|min_brightness|Minimum brightness upto which the effect should go|`0 <= x <= 100`||integer|✓|
|max_brightness|Maximum brightness upto which the effect should go, also used in solid mode|`0 <= x <= 100`||integer|✓|
|total_ms||`0 <= x`||integer|✓|
|interrupt_forbidden||`true`, `false`||boolean||

## Indicator for Hosted Solution
  
**Section: Product Common**

Indicator for various events to be sent to host  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.indicator",
    "subtype": 1
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.indicator|`ezc.product_common.indicator`||string|✓|
|subtype|Set subtype to 1 for hosted configuration wherein all events are enabled|`1`||integer|✓|

## Back Light
  
**Section: Product Common**

Background light which can be turned on and off for devices with a small screen.  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.back_light",
    "power_bootup": 0,
    "driver": {
        "input": 1011,
        "input_trigger_type": 1,
        "indicator": 1008
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.back_light|`ezc.product_common.back_light`||string|✓|
|power_bootup|Power state of the back light when the device boots up:<br>• `0`: Always Off<br>• `1`: Always On<br>• `-1`: Previous value|`-1 <= x <= 1`|`1`|integer||
|driver|Driver details for back light.|[Back Light: Driver Configurations](#back-light-driver-configurations)||object|✓|

### Back Light: Driver Configurations


Driver details for back light.  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "input": 1011,
        "input_trigger_type": 1,
        "indicator": 1008
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input Driver ID for back light.|`1000 <= x <= 1999`||integer|✓|
|indicator|Indicator Driver ID for back light.|`1000 <= x <= 1999`||integer|✓|
|input_trigger_type|When to trigger the input:<br>• 0: Press Down<br>• 1: Press Up<br>• 2: Repeat Press<br>• 3: Repeat Press Release<br>• 4: Single Click<br>• 5: Double Click<br>• 6: Long Press Start<br>• 7: Long Press Hold|`0 <= x <= 7`||integer|✓|
|exclude_button|List of driver IDs with which the input driver ID should not work together. Example: When an exclude button is pressed and the trigger input button is also pressed, the action should not be performed.|`1000 <= x <= 1999`||array||

## Light Common Configurations
  
**Section: Product Common**

Light related common configurations  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.light_config",
    "light_config": {
        "switch_fade": false,
        "color_fade": true
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.light_config|`ezc.product_common.light_config`||string|✓|
|light_config|Light related common configurations|[Light Common Configurations: Details](#light-common-configurations-details)||object|✓|

### Light Common Configurations: Details


Light related common configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "light_config": {
        "switch_fade": false,
        "color_fade": true
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|switch_fade|Whether to enable the fade when the power state of the device changes.|`true`, `false`||boolean|✓|
|color_fade|Whether to enable the fade when the color/brightness state of the device changes.|`true`, `false`||boolean|✓|

## Factory Reset: Power Cycle
  
**Section: Product Common**

Factory reset the device by power cycling (on-off-on-off).  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.factory_reset",
    "subtype": 1,
    "count": 3,
    "auto_trigger": true
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.factory_reset. Factory reset is mantory in the configuration.|`ezc.product_common.factory_reset`||string|✓|
|subtype|Factory Reset type: 1|`1`||integer|✓|
|immediately_trigger|Immediately trigger factory reset as soon as it is detected rather than waiting for a few seconds.|`true`, `false`||boolean||
|auto_trigger|Automatically trigger factory reset if the devices has been removed from the last Ecosystem (Matter fabric).|`true`, `false`||boolean||
|count|Number of times the device needs to be power cycled|`3 <= x`||integer|✓|

## Factory Reset: Button Press
  
**Section: Product Common**

Factory reset the device by long pressing a button.  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.factory_reset",
    "subtype": 2,
    "driver": {
        "input": 1000,
        "press_time": 7000
    },
    "auto_trigger": true,
    "immediately_trigger": true
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.factory_reset. Factory reset is mantory in the configuration.|`ezc.product_common.factory_reset`||string|✓|
|subtype|Factory Reset type: 2|`2`||integer|✓|
|immediately_trigger|Immediately trigger factory reset as soon as it is detected rather than waiting for a few seconds.|`true`, `false`||boolean||
|auto_trigger|Automatically trigger factory reset if the devices has been removed from the last Ecosystem (Matter fabric).|`true`, `false`||boolean||
|driver|Driver details for factory reset|[Factory Reset: Button Press: Driver Configurations](#factory-reset-button-press-driver-configurations)||object|✓|

### Factory Reset: Button Press: Driver Configurations


Driver details for factory reset  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "input": 1000,
        "press_time": 7000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input Driver ID for factory reset.|`1000 <= x <= 1999`||integer|✓|
|alternative_input|Alternate Input Driver ID for factory reset.|`1000 <= x <= 1999`||integer||
|exclude_button|List of driver IDs with which the input driver ID should not work together. Example: When an exclude button is pressed and the trigger input button is also pressed, the action should not be performed.|`1000 <= x <= 1999`||array||
|press_time|Number of milliseconds for which the buttons should be pressed to trigger factory reset.|||integer||

## Factory Reset: Hosted over UART
  
**Section: Product Common**

Factory reset the device by host over UART  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.factory_reset",
    "subtype": 3
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.factory_reset. Factory reset is mantory in the configuration.|`ezc.product_common.factory_reset`||string|✓|
|subtype|Factory Reset type: 3|`3`||integer|✓|
|immediately_trigger|Immediately trigger factory reset as soon as it is detected rather than waiting for a few seconds.|`true`, `false`||boolean||
|auto_trigger|Automatically trigger factory reset if the devices has been removed from the last Ecosystem (Matter fabric).|`true`, `false`||boolean||

## Forced Rollback
  
**Section: Product Common**

Forcefully rollback the device into the previous firmware after an OTA update. This is helpful in certification and also for testing OTA multiple times.  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.factory_reset",
    "subtype": 1,
    "count": 5
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.forced_rollback|`ezc.product_common.forced_rollback`||string|✓|
|subtype|Forced Rollback type: 1|`1`||integer|✓|
|count|Number of times the device needs to be power cycled|||integer|✓|

## Socket Input Mode
  
**Section: Product Common**

Dynamically configure the socket's input mode to push button or rocker switch  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.socket_input_mode",
    "driver": {
        "input": 1000
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.socket_input_mode|`ezc.product_common.socket_input_mode`||string|✓|
|driver|Driver details for socket input mode|[Socket Input Mode: Driver Configurations](#socket-input-mode-driver-configurations)||object|✓|

### Socket Input Mode: Driver Configurations


Driver details for socket input mode  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "input": 1000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input Driver ID for changing the socket input.|`1000 <= x <= 1999`||integer|✓|

## Socket Power
  
**Section: Product Common**

Common button to change the power of all the sockets on the device. This is useful for multi-channel sockets like an extension board. If even one of the sockets is powered on, all of them will be powered off. If al the sockets are powered off, all of them will be powered on.  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.socket_power",
    "driver": {
        "input": 1002,
        "indicator": 1003
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.socket_power|`ezc.product_common.socket_power`||string|✓|
|driver|Driver details for socket power|[Socket Power: Driver Configurations](#socket-power-driver-configurations)||object|✓|

### Socket Power: Driver Configurations


Driver details for socket power  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "input": 1002,
        "indicator": 1003
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input Driver ID for socket power.|`1000 <= x <= 1999`||integer|✓|
|input_mode|What is the type of input:<br>• 0: Push Button<br>• 1: Rocker Switch|`0`, `1`||integer||
|input_trigger_type|When to trigger the input:<br>• 0: Press Down<br>• 1: Press Up<br>• 2: Repeat Press<br>• 3: Repeat Press Release<br>• 4: Single Click<br>• 5: Double Click<br>• 6: Long Press Start<br>• 7: Long Press Hold|`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer||
|indicator|Indicator Driver ID for socket power.|`1000 <= x <= 1999`||integer||

## Socket Common Configurations
  
**Section: Product Common**

Socket related common configurations  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.socket_config",
    "update_driver": true
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.socket_config|`ezc.product_common.socket_config`||string|✓|
|update_driver|Set to false if the driver is already updated and does not need to be updated again. This is useful in 2 chip solutions, where the socket output is changed as soon as the button is pressed on the Host MCU before sending the command to the Espressif module.|`true`, `false`|`true`|boolean||

## Window Covering Calibration
  
**Section: Product Common**

Calibration for window covering can be triggered with this  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.window_covering_calibration",
    "driver": {
        "enter_calibration": [
            1000
        ],
        "enter_cali_input_trigger_type": 0
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.window_covering_calibration|`ezc.product_common.window_covering_calibration`||string|✓|
|driver|Driver details for window covering calibration|[Window Covering Calibration: Driver Configurations](#window-covering-calibration-driver-configurations)||object|✓|

### Window Covering Calibration: Driver Configurations


Driver details for window covering calibration  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "enter_calibration": [
            1000
        ],
        "enter_cali_input_trigger_type": 0
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enter_cali_input_trigger_type|When to trigger the input:<br>• 0: Press Down<br>• 6: Long Press Start|`0`, `6`||integer|✓|
|enter_calibration|List of Input Driver IDs to enter calibration mode. If multiple are give, all of them need to be pressed together.|`1000 <= x <= 1999`||array|✓|
|enter_cali_exclude_button|List of driver IDs with which the input driver ID should not work together. Example: When an exclude button is pressed and the trigger input button is also pressed, the action should not be performed.|`1000 <= x <= 1999`||array||
|restore_default_input_trigger_type|When to trigger the input:<br>• 0: Press Down<br>• 6: Long Press Start|`0`, `6`||integer||
|restore_default|List of Input Driver IDs to restore the default calibration. If multiple are give, all of them need to be pressed together.|`1000 <= x <= 1999`||array||
|restore_default_exclude_button|List of driver IDs with which the input driver ID should not work together. Example: When an exclude button is pressed and the trigger input button is also pressed, the action should not be performed.|`1000 <= x <= 1999`||array||

## Window Covering Common Configurations
  
**Section: Product Common**

Window covering related common configurations  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.window_covering_config",
    "window_covering_config": {
        "set_defaults_when_poweron": true,
        "indicator_off_end": true,
        "stop_indicator_off_delay_time_ms": 1000,
        "update_driver": true
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.window_covering_config|`ezc.product_common.window_covering_config`||string|✓|
|window_covering_config|Window covering related common configurations|[Window Covering Common Configurations: Details](#window-covering-common-configurations-details)||object|✓|

### Window Covering Common Configurations: Details


Window covering related common configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "window_covering_config": {
        "set_defaults_when_poweron": true,
        "indicator_off_end": true,
        "stop_indicator_off_delay_time_ms": 1000,
        "update_driver": true
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|update_driver|Set to false if the driver is already updated and does not need to be updated again. This is useful in 2 chip solutions, where the window covering level is changed as soon as the button is pressed on the Host MCU before sending the command to the Espressif module.|`true`, `false`|`true`|boolean||
|set_defaults_when_poweron|Set to True if the device should go to default position when powered on.|`true`, `false`||boolean||
|indicator_off_end|Whether the indicator light should turn off when the window covering is at the end.|`true`, `false`||boolean||
|stop_indicator_off_delay_time_ms|The time for which the stop indicator light stays on after the movement has stopped.|||integer||

## Advertise MAC
  
**Section: Product Common**

The device advertises its MAC address over BLE. This can be triggered by some user action like power cycling the device x number of times. This can be useful in cases where the QR code of the device needs to be shared with an end user, in case they are unable to find it again.  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.advertise_mac",
    "subtype": 1,
    "count": 3
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.advertise_mac|`ezc.product_common.advertise_mac`||string|✓|
|subtype|Advertise MAC type: 1|`1`||integer|✓|
|count|Number of times the device needs to be power cycled|||integer|✓|

## Zero Detect
  
**Section: Product Common**

Zero Detect configuration. This is an optional configuration.  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.zero_detect",
    "driver": {
        "zero_detect": 1005,
        "invalid_behaviors": 0,
        "lost_signal": 0
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.zero_detect. Devices with zero-crossing detection functionality should have corresponding configurations.|`ezc.product_common.zero_detect`||string|✓|
|driver|Driver details for Zero Detect|[Zero Detect: Driver Configurations](#zero-detect-driver-configurations)||object|✓|

### Zero Detect: Driver Configurations


Driver details for Zero Detect  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "zero_detect": 1005,
        "invalid_behaviors": 0,
        "lost_signal": 0
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|zero_detect||`1000 <= x <= 1999`||integer|✓|
|invalid_behaviors|Behavior when the signal is invalid.|`0 <= x <= 3`||integer|✓|
|lost_signal|Behavior when the signal is lost.|`0 <= x <= 3`||integer|✓|

## Temperature protect
  
**Section: Product Common**

Temperature protect configuration. This is an optional configuration.  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product_common.temp_protect",
    "input": 1005,
    "normal_temp": 25,
    "warn_temp": 105
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product Common type: ezc.product_common.temp_protect. Devices with temperature protect.|`ezc.product_common.temp_protect`||string|✓|
|input|Temperature sensor driver input id|`1000 <= x <= 1999`||integer|✓|
|normal_temp|Device normal operating temperature|number||number||
|warn_temp|Device warning operating temperature|number||number||
|protect_temp|Device protect temperature|number||number||
|normal_behaviors|Behavior when temperature reaches normal temperature|`0`, `1`, `2`, `3`||integer||
|warn_behaviors|Behavior when temperature exceeded warning temperature|`0`, `1`, `2`, `3`||integer||
|protect_behaviors|Behavior when temperature exceeded protect temperature|`0`, `1`, `2`, `3`||integer||
|normal_sample_interval|normal sample interval|||integer||
|fast_sample_interval|fast sample interval when temperature is higher than warn temperature|||integer||
|normal_sample_count|normal sample count to calculate average temperature|||integer||
|fast_sample_count|fast sample count to calculate average temperature|||integer||

# Product

## Light: On Off


Light: On/Off: Product with on/off capabilities  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product.light",
    "subtype": 1,
    "driver": {
        "output": 1000
    },
    "data_model": {
        "power_default": 1,
        "power_bootup": -1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type||`ezc.product.light`||string|✓|
|id||`1 <= x <= 100`|`1`|integer||
|driver|Driver details for light|[Light: Driver Configurations](#light-driver-configurations)||object|✓|
|subtype||`1`||integer|✓|
|data_model|Data Model for Light On/Off|[Light: On/Off: Data model](#light-onoff-data-model)||object|✓|

### Light: Driver Configurations


Driver details for light  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "output": 1000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input ID for light driver|`1000 <= x <= 1999`||integer||
|input_mode|Input driver mode<br>• 0: Push Button<br>• 1: Rocker Switch|`0`, `1`||integer||
|input_trigger_type|When to trigger the input:<br>• 0: Press Down<br>• 1: Press Up<br>• 2: Repeat Press<br>• 3: Repeat Press Release<br>• 4: Single Click<br>• 5: Double Click<br>• 6: Long Press Start<br>• 7: Long Press Hold|`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer||
|output|Output ID for light driver|`1000 <= x <= 1999`||integer|✓|

### Light: On/Off: Data model


Data Model for Light On/Off  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "data_model": {
        "power_default": 1,
        "power_bootup": -1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|power_default|Default power state of the device <br>• `0`: Off<br>• `1`: On|`0`, `1`||integer||
|power_bootup|Power state of the device when it boots up:<br>• `0`: Always Off<br>• `1`: Always On<br>• `2`: Toggle the previous value<br>• `-1`: Previous value|`-1 <= x <= 2`||integer||

## Light: Dimmable


Light: Dimmable: Product with brightness capabilities  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product.light",
    "subtype": 2,
    "driver": {
        "output": 1000
    },
    "data_model": {
        "power_default": 1,
        "power_bootup": -1,
        "level_default": 50,
        "level_bootup": -1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type||`ezc.product.light`||string|✓|
|id||`1 <= x <= 100`|`1`|integer||
|driver||[Light: Driver Configurations](#light-driver-configurations)||object|✓|
|subtype||`2`||integer|✓|
|data_model|Data Model for Light Dimmable|[Light: Dimmable: Data Model](#light-dimmable-data-model)||object|✓|

### Light: Driver Configurations


Driver details for light  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "output": 1000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input ID for light driver|`1000 <= x <= 1999`||integer||
|input_mode|Input driver mode<br>• 0: Push Button<br>• 1: Rocker Switch|`0`, `1`||integer||
|input_trigger_type|When to trigger the input:<br>• 0: Press Down<br>• 1: Press Up<br>• 2: Repeat Press<br>• 3: Repeat Press Release<br>• 4: Single Click<br>• 5: Double Click<br>• 6: Long Press Start<br>• 7: Long Press Hold|`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer||
|output|Output ID for light driver|`1000 <= x <= 1999`||integer|✓|

### Light: Dimmable: Data Model


Data Model for Light Dimmable  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|power_default|Default power state of the device <br>• `0`: Off<br>• `1`: On|`0`, `1`||integer||
|power_bootup|Power state of the device when it boots up:<br>• `0`: Always Off<br>• `1`: Always On<br>• `2`: Toggle the previous value<br>• `-1`: Previous value|`-1 <= x <= 2`||integer||
|level_default|Default level/brightness of the device|`0 <= x <= 100`|`50`|integer||
|level_bootup|Level/brightness of the device when it boots up (if -1 then previous value is taken)|`-1 <= x <= 100`|`-1`|integer||

## Light: Temperature


Light: Temperature: Product with temperature capabilities  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product.light",
    "subtype": 3,
    "driver": {
        "output": 1000
    },
    "data_model": {
        "power_default": 1,
        "power_bootup": -1,
        "level_default": 50,
        "level_bootup": -1,
        "color_mode_default": 1,
        "color_mode_bootup": -1,
        "temperature_default": 4000,
        "temperature_bootup": -1,
        "temperature_minimum_default": 1500,
        "temperature_maximum_default": 7000,
        "hue_default": 180,
        "hue_bootup": -1,
        "saturation_default": 100,
        "saturation_bootup": -1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type||`ezc.product.light`||string|✓|
|id||`1 <= x <= 100`|`1`|integer||
|driver||[Light: Driver Configurations](#light-driver-configurations)||object|✓|
|subtype||`3`||integer|✓|
|data_model|Data Model for Light Temperature|[Light: Temperature: Data Model](#light-temperature-data-model)||object|✓|

### Light: Driver Configurations


Driver details for light  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "output": 1000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input ID for light driver|`1000 <= x <= 1999`||integer||
|input_mode|Input driver mode<br>• 0: Push Button<br>• 1: Rocker Switch|`0`, `1`||integer||
|input_trigger_type|When to trigger the input:<br>• 0: Press Down<br>• 1: Press Up<br>• 2: Repeat Press<br>• 3: Repeat Press Release<br>• 4: Single Click<br>• 5: Double Click<br>• 6: Long Press Start<br>• 7: Long Press Hold|`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer||
|output|Output ID for light driver|`1000 <= x <= 1999`||integer|✓|

### Light: Temperature: Data Model


Data Model for Light Temperature  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "data_model": {
        "power_default": 1,
        "power_bootup": -1,
        "level_default": 50,
        "level_bootup": -1,
        "color_mode_default": 1,
        "color_mode_bootup": -1,
        "temperature_default": 4000,
        "temperature_bootup": -1,
        "temperature_minimum_default": 1500,
        "temperature_maximum_default": 7000,
        "hue_default": 180,
        "hue_bootup": -1,
        "saturation_default": 100,
        "saturation_bootup": -1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|power_default|Default power state of the device <br>• `0`: Off<br>• `1`: On|`0`, `1`||integer||
|power_bootup|Power state of the device when it boots up:<br>• `0`: Always Off<br>• `1`: Always On<br>• `2`: Toggle the previous value<br>• `-1`: Previous value|`-1 <= x <= 2`||integer||
|level_default|Default level/brightness of the device|`0 <= x <= 100`|`50`|integer||
|level_bootup|Level/brightness of the device when it boots up (if -1 then previous value is taken)|`-1 <= x <= 100`|`-1`|integer||
|color_mode_default|Default Color Mode of the device<br>• `1`: Temperature<br>• `2`: Color: Hue Saturation<br>• `3`: Color: XY<br>• `4`: Color: Enhanced Hue Saturation|`1 <= x <= 4`|`1`|integer||
|color_mode_bootup|Color mode of the device when it boots up<br>• 1: Temperature<br>• 2: Color: Hue Saturation<br>• 3: Color: XY<br>• 4: Color: Enhanced Hue Saturation<br>• -1: Previous value|`-1`, `1`, `2`, `3`, `4`||integer|✓|
|temperature_default|Default temperature of the device|`1500 <= x <= 7000`|`4000`|integer||
|temperature_bootup|Temperature of the device when it boots up<br>• 1500 to 7000<br>• -1: Previous value|`-1 <= x <= 7000`||integer|✓|
|temperature_minimum_default|Minimum temperature of the device<br>Range: 1500K~7000K<br>Default: 2000K<br>The config should same as 'cct_kelvin_min' in driver config|`1500 <= x`|`2200`|integer||
|temperature_maximum_default|Maximum temperature of the device<br>Range: 1500K~7000K<br>Default: 7000K<br>The config should same as 'cct_kelvin_max' in driver config|`x <= 7000`|`7000`|integer||

## Light: Temperature and Color


Light: Temperature and Color: Product with temperature and color capabilities  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product.light",
    "subtype": 4,
    "driver": {
        "output": 1000
    },
    "data_model": {
        "power_default": 1,
        "power_bootup": -1,
        "level_default": 50,
        "level_bootup": -1,
        "color_mode_default": 1,
        "color_mode_bootup": -1,
        "temperature_default": 4000,
        "temperature_bootup": -1,
        "temperature_minimum_default": 1500,
        "temperature_maximum_default": 7000,
        "hue_default": 180,
        "hue_bootup": -1,
        "saturation_default": 100,
        "saturation_bootup": -1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type||`ezc.product.light`||string|✓|
|id||`1 <= x <= 100`|`1`|integer||
|driver||[Light: Driver Configurations](#light-driver-configurations)||object|✓|
|subtype||`4`||integer|✓|
|data_model|Data Model for Light Temperature Color|[Light: Temperature and Color: Data Model](#light-temperature-and-color-data-model)||object|✓|

### Light: Driver Configurations


Driver details for light  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "output": 1000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input ID for light driver|`1000 <= x <= 1999`||integer||
|input_mode|Input driver mode<br>• 0: Push Button<br>• 1: Rocker Switch|`0`, `1`||integer||
|input_trigger_type|When to trigger the input:<br>• 0: Press Down<br>• 1: Press Up<br>• 2: Repeat Press<br>• 3: Repeat Press Release<br>• 4: Single Click<br>• 5: Double Click<br>• 6: Long Press Start<br>• 7: Long Press Hold|`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer||
|output|Output ID for light driver|`1000 <= x <= 1999`||integer|✓|

### Light: Temperature and Color: Data Model


Data Model for Light Temperature Color  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "data_model": {
        "power_default": 1,
        "power_bootup": -1,
        "level_default": 50,
        "level_bootup": -1,
        "color_mode_default": 1,
        "color_mode_bootup": -1,
        "temperature_default": 4000,
        "temperature_bootup": -1,
        "temperature_minimum_default": 1500,
        "temperature_maximum_default": 7000,
        "hue_default": 180,
        "hue_bootup": -1,
        "saturation_default": 100,
        "saturation_bootup": -1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|power_default|Default power state of the device <br>• `0`: Off<br>• `1`: On|`0`, `1`||integer||
|power_bootup|Power state of the device when it boots up:<br>• `0`: Always Off<br>• `1`: Always On<br>• `2`: Toggle the previous value<br>• `-1`: Previous value|`-1 <= x <= 2`||integer||
|level_default|Default level/brightness of the device|`0 <= x <= 100`|`50`|integer||
|level_bootup|Level/brightness of the device when it boots up (if -1 then previous value is taken)|`-1 <= x <= 100`|`-1`|integer||
|color_mode_default|Default Color Mode of the device<br>• `1`: Temperature<br>• `2`: Color: Hue Saturation<br>• `3`: Color: XY<br>• `4`: Color: Enhanced Hue Saturation|`1 <= x <= 4`|`1`|integer||
|color_mode_bootup|Color mode of the device when it boots up<br>• 1: Temperature<br>• 2: Color: Hue Saturation<br>• 3: Color: XY<br>• 4: Color: Enhanced Hue Saturation<br>• -1: Previous value|`-1`, `1`, `2`, `3`, `4`||integer|✓|
|temperature_default|Default temperature of the device|`1500 <= x <= 7000`|`4000`|integer||
|temperature_bootup|Temperature of the device when it boots up<br>• 1500 to 7000<br>• -1: Previous value|`-1 <= x <= 7000`||integer|✓|
|temperature_minimum_default|Minimum temperature of the device<br>Range: 1500K~7000K<br>Default: 2000K<br>The config should same as 'cct_kelvin_min' in driver config|`1500 <= x`|`2200`|integer||
|temperature_maximum_default|Maximum temperature of the device<br>Range: 1500K~7000K<br>Default: 7000K<br>The config should same as 'cct_kelvin_max' in driver config|`x <= 7000`|`7000`|integer||
|hue_default|Default hue of the device|`0 <= x <= 360`|`180`|integer||
|hue_bootup|Hue of the device when it boots up<br>• 0 to 360<br>• -1: Previous value|`-1 <= x <= 360`|`-1`|integer||
|saturation_default|Default saturation of the device|`0 <= x <= 100`|`100`|integer||
|saturation_bootup|Saturation of the device when it boots up<br>• 0 to 100<br>• -1: Previous value|`-1 <= x <= 100`|`-1`|integer||

## Light: Temperature and Extended Color


Light: Temperature and Extended Color: Product with temperature and extended color capabilities  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product.light",
    "subtype": 5,
    "driver": {
        "output": 1000
    },
    "data_model": {
        "power_default": 1,
        "power_bootup": -1,
        "level_default": 50,
        "level_bootup": -1,
        "color_mode_default": 1,
        "color_mode_bootup": -1,
        "temperature_default": 4000,
        "temperature_bootup": -1,
        "temperature_minimum_default": 1500,
        "temperature_maximum_default": 7000,
        "hue_default": 180,
        "hue_bootup": -1,
        "saturation_default": 100,
        "saturation_bootup": -1,
        "color_x_default": 1,
        "color_y_default": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type||`ezc.product.light`||string|✓|
|id||`1 <= x <= 100`|`1`|integer||
|driver||[Light: Driver Configurations](#light-driver-configurations)||object|✓|
|subtype||`5`||integer|✓|
|data_model|Data Model for Light Temperature Extended Color|[Light: Temperature and Extended Color: Data Model](#light-temperature-and-extended-color-data-model)||object|✓|

### Light: Driver Configurations


Driver details for light  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "output": 1000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input ID for light driver|`1000 <= x <= 1999`||integer||
|input_mode|Input driver mode<br>• 0: Push Button<br>• 1: Rocker Switch|`0`, `1`||integer||
|input_trigger_type|When to trigger the input:<br>• 0: Press Down<br>• 1: Press Up<br>• 2: Repeat Press<br>• 3: Repeat Press Release<br>• 4: Single Click<br>• 5: Double Click<br>• 6: Long Press Start<br>• 7: Long Press Hold|`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer||
|output|Output ID for light driver|`1000 <= x <= 1999`||integer|✓|

### Light: Temperature and Extended Color: Data Model


Data Model for Light Temperature Extended Color  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "data_model": {
        "power_default": 1,
        "power_bootup": -1,
        "level_default": 50,
        "level_bootup": -1,
        "color_mode_default": 1,
        "color_mode_bootup": -1,
        "temperature_default": 4000,
        "temperature_bootup": -1,
        "temperature_minimum_default": 1500,
        "temperature_maximum_default": 7000,
        "hue_default": 180,
        "hue_bootup": -1,
        "saturation_default": 100,
        "saturation_bootup": -1,
        "color_x_default": 1,
        "color_y_default": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|power_default|Default power state of the device <br>• `0`: Off<br>• `1`: On|`0`, `1`||integer||
|power_bootup|Power state of the device when it boots up:<br>• `0`: Always Off<br>• `1`: Always On<br>• `2`: Toggle the previous value<br>• `-1`: Previous value|`-1 <= x <= 2`||integer||
|level_default|Default level/brightness of the device|`0 <= x <= 100`|`50`|integer||
|level_bootup|Level/brightness of the device when it boots up (if -1 then previous value is taken)|`-1 <= x <= 100`|`-1`|integer||
|color_mode_default|Default Color Mode of the device<br>• `1`: Temperature<br>• `2`: Color: Hue Saturation<br>• `3`: Color: XY<br>• `4`: Color: Enhanced Hue Saturation|`1 <= x <= 4`|`1`|integer||
|color_mode_bootup|Color mode of the device when it boots up<br>• 1: Temperature<br>• 2: Color: Hue Saturation<br>• 3: Color: XY<br>• 4: Color: Enhanced Hue Saturation<br>• -1: Previous value|`-1`, `1`, `2`, `3`, `4`||integer|✓|
|temperature_default|Default temperature of the device|`1500 <= x <= 7000`|`4000`|integer||
|temperature_bootup|Temperature of the device when it boots up<br>• 1500 to 7000<br>• -1: Previous value|`-1 <= x <= 7000`||integer|✓|
|temperature_minimum_default|Minimum temperature of the device<br>Range: 1500K~7000K<br>Default: 2000K<br>The config should same as 'cct_kelvin_min' in driver config|`1500 <= x`|`2200`|integer||
|temperature_maximum_default|Maximum temperature of the device<br>Range: 1500K~7000K<br>Default: 7000K<br>The config should same as 'cct_kelvin_max' in driver config|`x <= 7000`|`7000`|integer||
|hue_default|Default hue of the device|`0 <= x <= 360`|`180`|integer||
|hue_bootup|Hue of the device when it boots up<br>• 0 to 360<br>• -1: Previous value|`-1 <= x <= 360`|`-1`|integer||
|saturation_default|Default saturation of the device|`0 <= x <= 100`|`100`|integer||
|saturation_bootup|Saturation of the device when it boots up<br>• 0 to 100<br>• -1: Previous value|`-1 <= x <= 100`|`-1`|integer||
|color_x_default|Default color X of the device|`0 <= x <= 100`|`100`|integer||
|color_y_default|Default color Y of the device|`0 <= x <= 100`|`100`|integer||

## Socket: On/Off


Product Description for On/Off Socket  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product.socket",
    "subtype": 1,
    "driver": {
        "input": 1000,
        "input_mode": 1,
        "input_trigger_type": 1,
        "output": 1001,
        "indicator": 1002
    },
    "data_model": {
        "power_default": 1,
        "power_bootup": -1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type||`ezc.product.socket`||string|✓|
|id||`1 <= x <= 100`|`1`|integer||
|driver||[Socket: Driver Configurations](#socket-driver-configurations)||object|✓|
|subtype||`1`||integer|✓|
|data_model|Datamodel for simple On/Off sockets|[Socket: On/Off: Data Model](#socket-onoff-data-model)||object||

### Socket: Driver Configurations


Socket driver input and output configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "input": 1000,
        "input_mode": 1,
        "input_trigger_type": 1,
        "output": 1001,
        "indicator": 1002
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input driver ID|`1000 <= x <= 1999`||integer|✓|
|input_mode|Input driver mode<br>• 0: Push Button<br>• 1: Rocker Switch|`0`, `1`||integer||
|input_trigger_type|Input trigger type<br>• 0: trigger when input/button Press Down<br>• 1: trigger when input/button Press Up<br>• 2: trigger when input/button Repeat Press<br>• 3: trigger when input/button Repeat Press release<br>• 4: trigger when input/button single click<br>• 5: trigger when input/button double click<br>• 6: trigger when input/button long press start<br>• 7: trigger when input/button long press hold<br>• 8: trigger on/off when rocker switch is pressed<br>• 9: trigger toggle when rocker switch is pressed|`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer||
|alternative_input|Alternative Input driver ID|`1000 <= x <= 1999`||integer||
|alternative_input_mode|Alternative Input driver mode<br>• 0: Push Button<br>• 1: Rocker Switch|`0`, `1`||integer||
|alternative_input_trigger_type|Alternative Input trigger type<br>• 0: trigger when input/button Press Down<br>• 1: trigger when input/button Press Up<br>• 2: trigger when input/button Repeat Press<br>• 3: trigger when input/button Repeat Press release<br>• 4: trigger when input/button single click<br>• 5: trigger when input/button double click<br>• 6: trigger when input/button long press start<br>• 7: trigger when input/button long press hold<br>• 8: trigger on/off when rocker switch is pressed<br>• 9: trigger toggle when rocker switch is pressed|`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer||
|output|Output driver ID|`1000 <= x <= 1999`||integer|✓|
|indicator|Indicator driver ID|`1000 <= x <= 1999`||integer||
|feedback_signal_input||`1000 <= x <= 1999`||integer||
|hosted|Whether the product is hosted or not<br>• true: hosted product<br>• false: non-hosted product|`true`, `false`||boolean||

### Socket: On/Off: Data Model


Datamodel for simple On/Off sockets  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "data_model": {
        "power_default": 1,
        "power_bootup": -1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|power_default|Default power state of the device<br>• 0: Off<br>• 1: On|`0`, `1`||integer||
|power_bootup|Power state of the device when it boots up<br>• 0: Always Off<br>• 1: Always On<br>• 2: Toggle the previous value<br>• -1: Previous value|`-1 <= x <= 2`||integer||

## Socket: Dimmable


Product Description for Dimmable Socket  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product.socket",
    "subtype": 2,
    "driver": {
        "input": 1000,
        "input_mode": 1,
        "input_trigger_type": 1,
        "output": 1001,
        "indicator": 1002
    },
    "data_model": {
        "power_default": 1,
        "power_bootup": -1,
        "level_default": 50,
        "level_bootup": 50
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type||`ezc.product.socket`||string|✓|
|id||`1 <= x <= 100`|`1`|integer||
|driver||[Socket: Driver Configurations](#socket-driver-configurations)||object|✓|
|subtype||`2`||integer|✓|
|data_model|Datamodel of Dimmable Socket|[Socket: Dimmable: Data Model](#socket-dimmable-data-model)||object||

### Socket: Driver Configurations


Socket driver input and output configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "input": 1000,
        "input_mode": 1,
        "input_trigger_type": 1,
        "output": 1001,
        "indicator": 1002
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input driver ID|`1000 <= x <= 1999`||integer|✓|
|input_mode|Input driver mode<br>• 0: Push Button<br>• 1: Rocker Switch|`0`, `1`||integer||
|input_trigger_type|Input trigger type<br>• 0: trigger when input/button Press Down<br>• 1: trigger when input/button Press Up<br>• 2: trigger when input/button Repeat Press<br>• 3: trigger when input/button Repeat Press release<br>• 4: trigger when input/button single click<br>• 5: trigger when input/button double click<br>• 6: trigger when input/button long press start<br>• 7: trigger when input/button long press hold<br>• 8: trigger on/off when rocker switch is pressed<br>• 9: trigger toggle when rocker switch is pressed|`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer||
|alternative_input|Alternative Input driver ID|`1000 <= x <= 1999`||integer||
|alternative_input_mode|Alternative Input driver mode<br>• 0: Push Button<br>• 1: Rocker Switch|`0`, `1`||integer||
|alternative_input_trigger_type|Alternative Input trigger type<br>• 0: trigger when input/button Press Down<br>• 1: trigger when input/button Press Up<br>• 2: trigger when input/button Repeat Press<br>• 3: trigger when input/button Repeat Press release<br>• 4: trigger when input/button single click<br>• 5: trigger when input/button double click<br>• 6: trigger when input/button long press start<br>• 7: trigger when input/button long press hold<br>• 8: trigger on/off when rocker switch is pressed<br>• 9: trigger toggle when rocker switch is pressed|`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer||
|output|Output driver ID|`1000 <= x <= 1999`||integer|✓|
|indicator|Indicator driver ID|`1000 <= x <= 1999`||integer||
|feedback_signal_input||`1000 <= x <= 1999`||integer||
|hosted|Whether the product is hosted or not<br>• true: hosted product<br>• false: non-hosted product|`true`, `false`||boolean||

### Socket: Dimmable: Data Model


Datamodel of Dimmable Socket  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "data_model": {
        "power_default": 1,
        "power_bootup": -1,
        "level_default": 50,
        "level_bootup": 50
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|power_default|Default power state of the device<br>• 0: Off<br>• 1: On|`0`, `1`||integer||
|power_bootup|Power state of the device when it boots up<br>• 0: Always Off<br>• 1: Always On<br>• 2: Toggle the previous value<br>• -1: Previous value|`-1 <= x <= 2`||integer||
|level_default|Default level/brightness of the device|`0 <= x <= 100`|`50`|integer||
|level_bootup|Level/Brightness of the device when it boots up|`-1 <= x <= 100`|`-1`|integer||

## Switch


Product Switch description and options  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product.switch",
    "subtype": 1,
    "driver": {
        "input": 1000
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product: ezc.product.switch|`ezc.product.switch`||string|✓|
|id|Product ID to distinguish between different products. Should be unique for each product|`1 <= x <= 100`|`1`|integer||
|subtype||`1`, `2`, `3`||integer|✓|
|driver|Driver configurations for switch|[Switch: Driver Configurations](#switch-driver-configurations)||object|✓|

### Switch: Driver Configurations


Driver configurations for switch  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "input": 1000
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|input|Input driver ID|`1000 <= x <= 1999`||integer|✓|
|indicator|Indicator output ID|`1000 <= x <= 1999`||integer||
|hosted|Whether the product is hosted or not<br>• true: hosted product<br>• false: non-hosted product|`true`, `false`||boolean||

## Window Covering


Window covering description and configurations  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.product.window_covering",
    "subtype": 1,
    "driver": {
        "output": 1002,
        "input_up": 1000,
        "input_down": 1001
    },
    "data_model": {
        "window_covering_type": 1
    }
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Product window covering: `ezc.product.window_covering`|`ezc.product.window_covering`||string|✓|
|id|Product ID to distinguish between different products. Should be unique for each product|`1 <= x <= 100`|`1`|integer||
|subtype|1: Position aware lift|`1 <= x <= 1`||integer|✓|
|driver|Window covering driver configurations|[Window Covering: Driver Configurations](#window-covering-driver-configurations)||object|✓|
|data_model|Window covering datamodel configuration for product|[Window Covering: Data Model](#window-covering-data-model)||object||

### Window Covering: Driver Configurations


Window covering driver configurations  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "driver": {
        "output": 1002,
        "input_up": 1000,
        "input_down": 1001
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|output|Output Driver ID|`1000 <= x <= 1999`||integer|✓|
|input_up|Input driver ID for up motion|`1000 <= x <= 1999`||integer||
|input_down|Input driver ID for down motion|`1000 <= x <= 1999`||integer||
|input_stop|Input driver ID to stop the motion|`1000 <= x <= 1999`||integer||
|indicator_up|Output driver ID for indicating up motion|`1000 <= x <= 1999`||integer||
|indicator_down|Output driver ID for indicating down motion|`1000 <= x <= 1999`||integer||
|indicator_stop|Output driver ID for indicating stop motion|`1000 <= x <= 1999`||integer||
|hosted|Whether the product is hosted or not<br>• true: hosted product<br>• false: non-hosted product|`true`, `false`||boolean||

### Window Covering: Data Model


Window covering datamodel configuration for product  

#### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "data_model": {
        "window_covering_type": 1
    }
}
```  
</details>  

#### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|window_covering_type|Type of window covering<br>• 0: Rollershade<br>• 1: Rollershade - 2 Motor<br>• 2: Rollershade - Exterior<br>• 3: Rollershade - Exterior - 2 Motor<br>• 4: Curtain/Drapery<br>• 5: Awning<br>• 6: Shutter<br>• 7: Tilt Blind - Tilt only<br>• 8: Tilt Blind - Lift and Tilt<br>• 9: Projector Screen<br>• -1: Other|`-1`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`||integer|✓|

# Test Mode

## Test Mode: Common
  
**Section: Test Mode**

Common test modes  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.test_mode.common",
    "subtype": 1
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Test Mode type: ezc.test_mode.common|`ezc.test_mode.common`||string|✓|
|subtype|Test type:<br>• 1: Set test mode as complete. Do this once all the tests are done. This should be done before the device leaves the factory. Once the test mode is marked as complete, the device will not be able to enter the test mode again.<br>• Default ssid: test_complete<br>• Default panid: 0x198F<br>• Default mac: 1212121212121212<br>• Default id: 00_00<br><br>• 2: Boot into the ota_1 partition to perform custom tests. The device should be booted back into the ota_0 partition before the device leaves the factory.<br>• Default ssid: test_ota_1<br>• Default panid: 0x198F<br>• Default mac: 2323232323232323<br>• Default id: 00_03|`1`, `2`||integer|✓|
|trigger|Test case trigger mechanism:<br>• 0: Default: Automatically select Wi-Fi (1) or Thread (2) depending on the hardware.<br>• 1: Wi-Fi: Using Wi-Fi network nearby with the specified SSID.<br>• 2: Thread: Using a thread network nearby with the specified PANID and MAC.<br>• 3: Sniffer: Using the sniffer method where another device is broadcasting the signal nearby with the given ID.|`0`, `1`, `2`, `3`||integer||
|ssid|Wi-Fi SSID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Wi-Fi based devices only.|string||string||
|panid|Thread PANID that the device will search for. If this is found along with the MAC, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Thread based devices only.|||integer||
|mac|Sniffer ID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Sniffer based trigger only.|string||string||
|id||string||string||

## Test Mode: BLE
  
**Section: Test Mode**

BLE related test modes  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.test_mode.ble",
    "subtype": 1
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Test Mode type: ezc.test_mode.ble|`ezc.test_mode.ble`||string|✓|
|subtype|Test type:<br>• 1: Broadcast the MAC address over BLE. This can be helpful to fetch the QR code for the device on the manufacturing line.<br>• Default ssid: test_ble_mac<br>• Default panid: 0x198F<br>• Default mac: 3434343434343434<br>• Default id: 00_01|`1`||integer|✓|
|trigger|Test case trigger mechanism:<br>• 0: Default: Automatically select Wi-Fi (1) or Thread (2) depending on the hardware.<br>• 1: Wi-Fi: Using Wi-Fi network nearby with the specified SSID.<br>• 2: Thread: Using a thread network nearby with the specified PANID and MAC.<br>• 3: Sniffer: Using the sniffer method where another device is broadcasting the signal nearby with the given ID.|`0`, `1`, `2`, `3`||integer||
|ssid|Wi-Fi SSID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Wi-Fi based devices only.|string||string||
|panid|Thread PANID that the device will search for. If this is found along with the MAC, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Thread based devices only.|||integer||
|mac|Sniffer ID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Sniffer based trigger only.|string||string||
|id||string||string||

## Test Mode: Sniffer
  
**Section: Test Mode**

Sniffer related test modes  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.test_mode.sniffer",
    "subtype": 1
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Test Mode type: ezc.test_mode.sniffer|`ezc.test_mode.sniffer`||string|✓|
|subtype|Test type:<br>• 1: Broadcast the MAC address using sniffer. This can be helpful to fetch the QR code for the device on the manufacturing line.<br>• Default ssid: test_sniffer_mac<br>• Default panid: 0x198F<br>• Default mac: 4545454545454545<br>• Default id: 00_02|`1`||integer|✓|
|trigger|Test case trigger mechanism:<br>• 0: Default: Automatically select Wi-Fi (1) or Thread (2) depending on the hardware.<br>• 1: Wi-Fi: Using Wi-Fi network nearby with the specified SSID.<br>• 2: Thread: Using a thread network nearby with the specified PANID and MAC.<br>• 3: Sniffer: Using the sniffer method where another device is broadcasting the signal nearby with the given ID.|`0`, `1`, `2`, `3`||integer||
|ssid|Wi-Fi SSID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Wi-Fi based devices only.|string||string||
|panid|Thread PANID that the device will search for. If this is found along with the MAC, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Thread based devices only.|||integer||
|mac|Sniffer ID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Sniffer based trigger only.|string||string||
|id||string||string||

## Test Mode: Light
  
**Section: Test Mode**

Light related test modes  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.test_mode.light",
    "subtype": 1,
    "interval_time_ms": 2000,
    "loop_count": 2,
    "r_time_s": 1,
    "g_time_s": 2,
    "b_time_s": 3,
    "w_time_s": 4,
    "c_time_s": 5
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Test Mode type: ezc.test_mode.light|`ezc.test_mode.light`||string|✓|
|subtype|Test type:<br>• 1: Light test case 1. The light cycles through different colors.<br>• Default ssid: test_light_1<br>• Default panid: 0x198F<br>• Default mac: 5656565656565656<br>• Default id: 01_01<br><br>• 2: Light test case 2. The light cycles through different colors.<br>• Default ssid: test_light_2<br>• Default panid: 0x198F<br>• Default mac: 7878787878787878<br>• Default id: 01_02<br><br>• 3: Light test case 3. The light cycles through different colors.<br>• Default ssid: test_light_3<br>• Default panid: 0x198F<br>• Default mac: 9090909090909090<br>• Default id: 01_03<br><br>• 4: Light test case 4. The light automatically finish color cycle test and aging test.<br>• Default ssid: test_light_4<br>• Default panid: 0x198F<br>• Default mac: 0A0A0A0A0A0A0A0A<br>• Default id: 01_04|`1`, `2`, `3`, `4`||integer|✓|
|trigger|Test case trigger mechanism:<br>• 0: Default: Automatically select Wi-Fi (1) or Thread (2) depending on the hardware.<br>• 1: Wi-Fi: Using Wi-Fi network nearby with the specified SSID.<br>• 2: Thread: Using a thread network nearby with the specified PANID and MAC.<br>• 3: Sniffer: Using the sniffer method where another device is broadcasting the signal nearby with the given ID.|`0`, `1`, `2`, `3`||integer||
|ssid|Wi-Fi SSID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Wi-Fi based devices only.|string||string||
|panid|Thread PANID that the device will search for. If this is found along with the MAC, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Thread based devices only.|||integer||
|mac|Sniffer ID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Sniffer based trigger only.|string||string||
|id||string||string||
|interval_time_s|Interval time (in seconds) between displaying various colors, defualt is 1000ms|||integer||
|loop_count|The number of cycles, default is 10|||integer||
|r_time_s|The duration for red color to stay displayed (in seconds), default is 10 minutes|||integer||
|g_time_s|The duration for green color to stay displayed (in seconds), default is 10 minutes|||integer||
|b_time_s|The duration for blue color to stay displayed (in seconds), default is 10 minutes|||integer||
|w_time_s|The duration for warm color to stay displayed (in seconds), default is 10 minutes|||integer||
|c_time_s|The duration for cold color to stay displayed (in seconds), default is 10 minutes|||integer||

## Test Mode: Socket
  
**Section: Test Mode**

Socket related test modes  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.test_mode.socket",
    "subtype": 1
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Test Mode type: ezc.test_mode.socket|`ezc.test_mode.socket`||string|✓|
|subtype|Test type:<br>• 1: All sockets turn on and off, 3 times<br>• Default ssid: test_socket_1<br>• Default panid: 0x198F<br>• Default mac: ABABABABABABABAB<br>• Default id: 02_01<br><br>• 2: All sockets change the level from 0 to 100 and back to 0<br>• Default ssid: test_socket_2<br>• Default panid: 0x198F<br>• Default mac: CDCDCDCDCDCDCDCD<br>• Default id: 02_02|`1`, `2`||integer|✓|
|trigger|Test case trigger mechanism:<br>• 0: Default: Automatically select Wi-Fi (1) or Thread (2) depending on the hardware.<br>• 1: Wi-Fi: Using Wi-Fi network nearby with the specified SSID.<br>• 2: Thread: Using a thread network nearby with the specified PANID and MAC.<br>• 3: Sniffer: Using the sniffer method where another device is broadcasting the signal nearby with the given ID.|`0`, `1`, `2`, `3`||integer||
|ssid|Wi-Fi SSID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Wi-Fi based devices only.|string||string||
|panid|Thread PANID that the device will search for. If this is found along with the MAC, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Thread based devices only.|||integer||
|mac|Sniffer ID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Sniffer based trigger only.|string||string||
|id||string||string||

## Test Mode: Window Covering
  
**Section: Test Mode**

Window covering related test modes  

### Examples
  
<details open>  
<summary>Example</summary>

```json
{
    "type": "ezc.test_mode.window_covering",
    "subtype": 1
}
```  
</details>  

### Properties

|Name|Description|Possible Values|Default|Type|Required|
| :--- | :--- | :--- | :--- | :--- | :--- |
|type|Test Mode type: ezc.test_mode.window_covering|`ezc.test_mode.window_covering`||string|✓|
|subtype|Test type:<br>• 1: The window covering moves up and down alternatively, 3 times.<br>• Default ssid: test_window_covering_1<br>• Default panid: 0x198F<br>• Default mac: EFEFEFEFEFEFEFEF<br>• Default id: 03_01|`1`||integer|✓|
|trigger|Test case trigger mechanism:<br>• 0: Default: Automatically select Wi-Fi (1) or Thread (2) depending on the hardware.<br>• 1: Wi-Fi: Using Wi-Fi network nearby with the specified SSID.<br>• 2: Thread: Using a thread network nearby with the specified PANID and MAC.<br>• 3: Sniffer: Using the sniffer method where another device is broadcasting the signal nearby with the given ID.|`0`, `1`, `2`, `3`||integer||
|ssid|Wi-Fi SSID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Wi-Fi based devices only.|string||string||
|panid|Thread PANID that the device will search for. If this is found along with the MAC, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Thread based devices only.|||integer||
|mac|Sniffer ID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Sniffer based trigger only.|string||string||
|id||string||string||
