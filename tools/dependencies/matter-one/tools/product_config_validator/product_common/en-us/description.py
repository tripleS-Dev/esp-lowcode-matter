from dotmap import DotMap

description = DotMap()

# Product Common -> Indicator
indicator = description.indicator
indicator.title = "Indicator"
indicator.section = "Product Common"
indicator.description = "Indicator for various events to be shown on the product."
indicator.example = ['{"type": "ezc.product_common.indicator", "subtype": 0, "driver": {"output": 1000}, "events":[{"name": "setup_mode_start", "mode": "breathe", "speed": 2000, "color_select": 1, "r": 0, "g": 255, "b": 0, "min_brightness": 20, "max_brightness": 100, "total_ms": 0, "interrupt_forbidden": true}, {"name": "setup_successful", "mode": "restore"}]}']

indicator.type.title = "Type"
indicator.type.description = "Product Common type: ezc.product_common.indicator"

indicator.config.title = "Indicator Configurations"
indicator.config.description = "Indicator configuration settings"
indicator.config.example = ['{"config": {"indicator_setup_timeout_en": false}}']

indicator.config.indicator_setup_timeout_en.title = "Indicator setup timeout enable"
indicator.config.indicator_setup_timeout_en.description = "If user does not set up the device on it's first bootup a timeout will occur, and on the subsequent bootups the light will display the config of 'setup_mode_end' (Even if the indicator will not show, setup mode will stay ON until timeout occurs). This will enable user to use the bulb as a normal bulb and will not show config for 'setup_mode_start' until the user opens the setup mode from another device or performs factory reset on the device"

indicator.driver.title = "Indicator: Driver Configurations"
indicator.driver.description = "Driver details for indicator."
indicator.driver.example = ['{"driver": {"output": 1000}}']

indicator.driver.output.title = "Output"
indicator.driver.output.description = "Output Driver ID for indicator."

indicator.events.title = "Indicator: Events"
indicator.events.description = "Various events and how should the output be shown. Example, for LED indicators, these can be in the form of some LED patterns."

# Product Common -> Hosted Indicator
hosted_indicator = description.hosted_indicator
hosted_indicator.title = "Indicator for Hosted Solution"
hosted_indicator.section = "Product Common"
hosted_indicator.description = "Indicator for various events to be sent to host"
hosted_indicator.example = ['{"type": "ezc.product_common.indicator", "subtype": 1}']

hosted_indicator.type.title = "Type"
hosted_indicator.type.description = "Product Common type: ezc.product_common.indicator"

hosted_indicator.subtype.title = "Subtype"
hosted_indicator.subtype.description = "Set subtype to 1 for hosted configuration wherein all events are enabled"

# Product Common -> Indicator -> Events


# Product Common -> Back Light
backlight = description.backlight
backlight.title = "Back Light"
backlight.section = "Product Common"
backlight.description = "Background light which can be turned on and off for devices with a small screen."
backlight.example = ['{"type": "ezc.product_common.back_light", "power_bootup": 0, "driver": {"input": 1011, "input_trigger_type": 1, "indicator": 1008}}']

backlight.type.title = "Type"
backlight.type.description = "Product Common type: ezc.product_common.back_light"

backlight.power_bootup.title = "Power Bootup"
backlight.power_bootup.description = "Power state of the back light when the device boots up:\n• `0`: Always Off\n• `1`: Always On\n• `-1`: Previous value\n"

backlight.driver.title = "Back Light: Driver Configurations"
backlight.driver.description = "Driver details for back light."
backlight.driver.example = ['{"driver": {"input": 1011, "input_trigger_type": 1, "indicator": 1008}}']

# Product Common -> Back Light -> Driver
driver = backlight.driver
driver.input.title = "Input"
driver.input.description = "Input Driver ID for back light."

driver.input_trigger_type.title = "Input Trigger Type"
driver.input_trigger_type.description = "When to trigger the input:\n• 0: Press Down\n• 1: Press Up\n• 2: Repeat Press\n• 3: Repeat Press Release\n• 4: Single Click\n• 5: Double Click\n• 6: Long Press Start\n• 7: Long Press Hold\n\n"

driver.exclude_button.title = "Exclude Button"
driver.exclude_button.description = "List of driver IDs with which the input driver ID should not work together. Example: When an exclude button is pressed and the trigger input button is also pressed, the action should not be performed."

driver.indicator.title = "Indicator"
driver.indicator.description = "Indicator Driver ID for back light."

# Product Common -> Light Config
lightconfig = description.lightconfig
lightconfig.title = "Light Common Configurations"
lightconfig.section = "Product Common"
lightconfig.description = "Light related common configurations"
lightconfig.example = ['{"type": "ezc.product_common.light_config", "light_config": {"switch_fade": false, "color_fade": true}}']

lightconfig.type.title = "Type"
lightconfig.type.description = "Product Common type: ezc.product_common.light_config"

lightconfig.light_config.title = "Light Common Configurations: Details"
lightconfig.light_config.description = "Light related common configurations"
lightconfig.light_config.example = ['{"light_config": {"switch_fade": false, "color_fade": true}}']

# Product Common -> Light Config -> Light Config
light_config = lightconfig.light_config

light_config.switch_fade.title = "Switch Fade"
light_config.switch_fade.description = "Whether to enable the fade when the power state of the device changes."

light_config.color_fade.title = "Color Fade"
light_config.color_fade.description = "Whether to enable the fade when the color/brightness state of the device changes."

# Product Common -> Factory Reset
factory_reset = description.factory_reset
factory_reset.title = "Factory Reset"
factory_reset.section = "Product Common"
factory_reset.description = "Factory reset configuration. This is a mandatory configuration."
factory_reset.example = ['{"type": "ezc.product_common.factory_reset", "subtype": 1, "count": 3, "auto_trigger": true}', '{"type": "ezc.product_common.factory_reset", "subtype": 2, "driver": {"input": 1000}, "auto_trigger": true, "immediately_trigger": true}']

factory_reset.type.title = "Type"
factory_reset.type.description = "Product Common type: ezc.product_common.factory_reset. Factory reset is mantory in the configuration."

factory_reset.auto_trigger.title = "Auto Trigger"
factory_reset.auto_trigger.description = "Automatically trigger factory reset if the devices has been removed from the last Ecosystem (Matter fabric)."

factory_reset.immediately_trigger.title = "Immediately Trigger"
factory_reset.immediately_trigger.description = "Immediately trigger factory reset as soon as it is detected rather than waiting for a few seconds."

# Product Common -> Factory Reset: Power Cycle
factory_reset_1 = description.factory_reset_1
factory_reset_1.update(factory_reset)
factory_reset_1.title = "Factory Reset: Power Cycle"
factory_reset_1.section = "Product Common"
factory_reset_1.description = "Factory reset the device by power cycling (on-off-on-off)."
factory_reset_1.example = ['{"type": "ezc.product_common.factory_reset", "subtype": 1, "count": 3, "auto_trigger": true}']

factory_reset_1.subtype.title = "Subtype"
factory_reset_1.subtype.description = "Factory Reset type: 1"

factory_reset_1.count.title = "Count"
factory_reset_1.count.description = "Number of times the device needs to be power cycled"

# Product Common -> Factory Reset: Button Press
factory_reset_2 = description.factory_reset_2
factory_reset_2.update(factory_reset)
factory_reset_2.title = "Factory Reset: Button Press"
factory_reset_2.section = "Product Common"
factory_reset_2.description = "Factory reset the device by long pressing a button."
factory_reset_2.example = ['{"type": "ezc.product_common.factory_reset", "subtype": 2, "driver": {"input": 1000, "press_time": 7000}, "auto_trigger": true, "immediately_trigger": true}']

factory_reset_2.subtype.title = "Subtype"
factory_reset_2.subtype.description = "Factory Reset type: 2"

factory_reset_2.driver.title = "Factory Reset: Button Press: Driver Configurations"
factory_reset_2.driver.description = "Driver details for factory reset"
factory_reset_2.driver.example = ['{"driver": {"input": 1000, "press_time": 7000}}']

# Product Common -> Factory Reset: Button Press -> Driver
driver = factory_reset_2.driver
driver.input.title = "Input"
driver.input.description = "Input Driver ID for factory reset."

driver.alternative_input.title = "Alternate Input"
driver.alternative_input.description = "Alternate Input Driver ID for factory reset."

driver.exclude_button.title = "Exclude Button"
driver.exclude_button.description = "List of driver IDs with which the input driver ID should not work together. Example: When an exclude button is pressed and the trigger input button is also pressed, the action should not be performed."

driver.press_time.title = "Long Press Time (ms)"
driver.press_time.description = "Number of milliseconds for which the buttons should be pressed to trigger factory reset."

# Product Common -> Factory Reset: Hosted
factory_reset_3 = description.factory_reset_3
factory_reset_3.update(factory_reset)
factory_reset_3.title = "Factory Reset: Hosted over UART"
factory_reset_3.section = "Product Common"
factory_reset_3.description = "Factory reset the device by host over UART"
factory_reset_3.example = ['{"type": "ezc.product_common.factory_reset", "subtype": 3}']

factory_reset_3.subtype.title = "Subtype"
factory_reset_3.subtype.description = "Factory Reset type: 3"

# Product Common -> Forced Rollback: Power Cycle
forcedrollback = description.forcedrollback
forcedrollback.title = "Forced Rollback"
forcedrollback.section = "Product Common"
forcedrollback.description = "Forcefully rollback the device into the previous firmware after an OTA update. This is helpful in certification and also for testing OTA multiple times."
forcedrollback.example = ['{"type": "ezc.product_common.factory_reset", "subtype": 1, "count": 5}']

forcedrollback.type.title = "Type"
forcedrollback.type.description = "Product Common type: ezc.product_common.forced_rollback"

forcedrollback.subtype.title = "Subtype"
forcedrollback.subtype.description = "Forced Rollback type: 1"

forcedrollback.count.title = "Count"
forcedrollback.count.description = "Number of times the device needs to be power cycled"

# Product Common -> Socket Input Mode
socketinput = description.socketinput
socketinput.title = "Socket Input Mode"
socketinput.section = "Product Common"
socketinput.description = "Dynamically configure the socket's input mode to push button or rocker switch"
socketinput.example = ['{"type": "ezc.product_common.socket_input_mode", "driver": {"input": 1000}}']

socketinput.type.title = "Type"
socketinput.type.description = "Product Common type: ezc.product_common.socket_input_mode"

socketinput.driver.title = "Socket Input Mode: Driver Configurations"
socketinput.driver.description = "Driver details for socket input mode"
socketinput.driver.example = ['{"driver": {"input": 1000}}']

# Product Common -> Socket Input Mode -> Driver
driver = socketinput.driver

driver.input.title = "Input"
driver.input.description = "Input Driver ID for changing the socket input."

#  Product Common -> Socket Power
socketpower = description.socketpower
socketpower.title = "Socket Power"
socketpower.section = "Product Common"
socketpower.description = "Common button to change the power of all the sockets on the device. This is useful for multi-channel sockets like an extension board. If even one of the sockets is powered on, all of them will be powered off. If al the sockets are powered off, all of them will be powered on."
socketpower.example = ['{"type": "ezc.product_common.socket_power", "driver": {"input": 1002, "indicator": 1003}}']

socketpower.type.title = "Type"
socketpower.type.description = "Product Common type: ezc.product_common.socket_power"

socketpower.driver.title = "Socket Power: Driver Configurations"
socketpower.driver.description = "Driver details for socket power"
socketpower.driver.example = ['{"driver": {"input": 1002, "indicator": 1003}}']

# Product Common -> Socket Power -> Driver
driver = socketpower.driver

driver.input.title = "Input"
driver.input.description = "Input Driver ID for socket power."

driver.input_mode.title = "Input driver mode"
driver.input_mode.description = "What is the type of input:\n• 0: Push Button\n• 1: Rocker Switch\n"

driver.input_trigger_type.title = "Input Trigger Type"
driver.input_trigger_type.description = "When to trigger the input:\n• 0: Press Down\n• 1: Press Up\n• 2: Repeat Press\n• 3: Repeat Press Release\n• 4: Single Click\n• 5: Double Click\n• 6: Long Press Start\n• 7: Long Press Hold\n\n"

driver.indicator.title = "Indicator"
driver.indicator.description = "Indicator Driver ID for socket power."

# Product Common -> Socket Config
socketconfig = description.socketconfig
socketconfig.title = "Socket Common Configurations"
socketconfig.section = "Product Common"
socketconfig.description = "Socket related common configurations"
socketconfig.example = ['{"type": "ezc.product_common.socket_config", "update_driver": true}']

socketconfig.type.title = "Type"
socketconfig.type.description = "Product Common type: ezc.product_common.socket_config"

socketconfig.update_driver.title = "Update Driver"
socketconfig.update_driver.description = "Set to false if the driver is already updated and does not need to be updated again. This is useful in 2 chip solutions, where the socket output is changed as soon as the button is pressed on the Host MCU before sending the command to the Espressif module."

# Product-Commoon -> Window Covering Calibration
window_covering_calib = description.window_covering_calib
window_covering_calib.title = "Window Covering Calibration"
window_covering_calib.section = "Product Common"
window_covering_calib.description = "Calibration for window covering can be triggered with this"
window_covering_calib.example = ['{"type": "ezc.product_common.window_covering_calibration", "driver": {"enter_calibration": [1000],"enter_cali_input_trigger_type": 0}}']

window_covering_calib.type.title = "Type"
window_covering_calib.type.description = "Product Common type: ezc.product_common.window_covering_calibration"

window_covering_calib.driver.title = "Window Covering Calibration: Driver Configurations"
window_covering_calib.driver.description = "Driver details for window covering calibration"
window_covering_calib.driver.example = ['{"driver": {"enter_calibration": [1000],"enter_cali_input_trigger_type": 0}}']

# Product Common -> Window Covering Calibration -> window_covering_config
driver = window_covering_calib.driver
driver.enter_calibration.title = "Enter Calibration Mode Input"
driver.enter_calibration.description = "List of Input Driver IDs to enter calibration mode. If multiple are give, all of them need to be pressed together."

driver.enter_cali_input_trigger_type.title = "Enter Calibration Input Trigger Type"
driver.enter_cali_input_trigger_type.description = "When to trigger the input:\n• 0: Press Down\n• 6: Long Press Start\n\n"

driver.enter_cali_exclude_button.title = "Enter Calibration Exclude Button"
driver.enter_cali_exclude_button.description = "List of driver IDs with which the input driver ID should not work together. Example: When an exclude button is pressed and the trigger input button is also pressed, the action should not be performed."

driver.restore_default.title = "Restore Default Input"
driver.restore_default.description = "List of Input Driver IDs to restore the default calibration. If multiple are give, all of them need to be pressed together."

driver.restore_default_input_trigger_type.title = "Restore Default Input Trigger Type"
driver.restore_default_input_trigger_type.description = "When to trigger the input:\n• 0: Press Down\n• 6: Long Press Start\n\n"

driver.restore_default_exclude_button.title = "Restore Default Exclude Button"
driver.restore_default_exclude_button.description = "List of driver IDs with which the input driver ID should not work together. Example: When an exclude button is pressed and the trigger input button is also pressed, the action should not be performed."

# Product Common -> Window covering Config
window_covering_config = description.window_covering_config
window_covering_config.title = "Window Covering Common Configurations"
window_covering_config.section = "Product Common"
window_covering_config.description = "Window covering related common configurations"
window_covering_config.example = ['{"type": "ezc.product_common.window_covering_config", "window_covering_config": {"set_defaults_when_poweron": true, "indicator_off_end": true, "stop_indicator_off_delay_time_ms": 1000, "update_driver": true}}']

window_covering_config.type.title = "Type"
window_covering_config.type.description = "Product Common type: ezc.product_common.window_covering_config"

window_covering_config.window_covering_config.title = "Window Covering Common Configurations: Details"
window_covering_config.window_covering_config.description = "Window covering related common configurations"
window_covering_config.window_covering_config.example = ['{"window_covering_config": {"set_defaults_when_poweron": true, "indicator_off_end": true, "stop_indicator_off_delay_time_ms": 1000, "update_driver": true}}']

# Product Common -> Window covering Config -> Config
config = window_covering_config.window_covering_config
config.stop_indicator_off_delay_time_ms.title = "Stop Indicator time (in ms)"
config.stop_indicator_off_delay_time_ms.description = "The time for which the stop indicator light stays on after the movement has stopped."

config.indicator_off_end.title = "Indicator off at end"
config.indicator_off_end.description = "Whether the indicator light should turn off when the window covering is at the end."

config.update_driver.title = "Update Driver"
config.update_driver.description = "Set to false if the driver is already updated and does not need to be updated again. This is useful in 2 chip solutions, where the window covering level is changed as soon as the button is pressed on the Host MCU before sending the command to the Espressif module."

config.set_defaults_when_poweron.title = "Whether to set defaults value at power on"
config.set_defaults_when_poweron.description = "Set to True if the device should go to default position when powered on."

# Product Common -> Advertise Mac: Power Cycle
advertise_mac = description.advertise_mac
advertise_mac.title = "Advertise MAC"
advertise_mac.section = "Product Common"
advertise_mac.description = "The device advertises its MAC address over BLE. This can be triggered by some user action like power cycling the device x number of times. This can be useful in cases where the QR code of the device needs to be shared with an end user, in case they are unable to find it again."
advertise_mac.example = ['{"type": "ezc.product_common.advertise_mac", "subtype": 1, "count": 3}']

advertise_mac.type.title = "Type"
advertise_mac.type.description = "Product Common type: ezc.product_common.advertise_mac"

advertise_mac.subtype.title = "Subtype"
advertise_mac.subtype.description = "Advertise MAC type: 1"

advertise_mac.count.title = "Count"
advertise_mac.count.description = "Number of times the device needs to be power cycled"

# Product Common -> Indicator -> Event: Base Model
event_base = description.event_base

event_base.name.title = "Event Name"
event_base.name.description = "\n• setup_mode_start: Device in setup mode\n• setup_started: Device setup started\n• setup_successful: Device setup completed successfully\n• setup_failed: Device setup completed failed\n• identification_start: Identification start\n• identification_stop: Identification stop\n• identification_blink: Identification blink effect\n• identification_breathe: Identification breathe effect\n• identification_okay: Identification okay effect\n• identification_channel_change: Identification channel change effect\n• identification_finish_effect: Identification finish the current effect and stop\n• identification_stop_effect: Identification stop immediately\n• factory_reset_triggered: Factory reset has been triggered and will be performed now\n• forced_rollback_triggered: Forced rollback has been triggered and will be performed now\n• driver_mode: Used to indicate the mode in which the driver currently is\n• test_mode_start: Test mode has been started\n• test_mode_complete: Test mode has been completed\n• test_mode_ble: Test mode BLE for advertising mac has been started\n"

# Product Common -> Indicator -> Event: Restore
restore = description.event_restore
restore.update(event_base)
restore.title = "Indicator: Event: Restore"
restore.description = "Stop the effect and go back to previous state"
restore.example = ['{"name":"setup_mode_start","mode":"restore"}']

restore.mode.title = "Mode"
restore.mode.description = "Indicator Event: `restore`"

# Product Common -> Indicator -> Event: RGB
rgb = description.rgb
rgb.color_select.title = "Color Select"
rgb.color_select.description = "Color mode to be used for the effect. Should be `1` for rgb color mode"
rgb.r.title = "Red Value"
rgb.r.description = "Red value for the effect"
rgb.g.title = "Green Value"
rgb.g.description = "Green value for the effect"
rgb.b.title = "Blue Value"
rgb.b.description = "Blue value for the effect"

# Product Common -> Indicator -> Event: CCT
cct = description.cct
cct.color_select.title = "Color Select"
cct.color_select.description = "Color mode selection to be used for the effect. Should be `2` for white color mode"
cct.cct.title = "CCT"
cct.cct.description = "CCT value used for the effect, percentage or kelvin"

# Product Common -> Indicator -> Event: Solid: RGB
solid = description.solid_rgb
solid.update(rgb)
solid.title = "Indicator: Event: Solid: RGB"
solid.description = "Event solid for color select: `Color`"
solid.example = ['{"name":"setup_mode_start","mode":"solid","speed":2000,"color_select":1,"r":0,"g":0,"b":0,"max_brightness":100}']

solid.mode.title = "Mode"
solid.mode.description = "`solid` for mode Solid"
solid.mode.max_brightness.title = "Maximum Brightness"
solid.mode.max_brightness.description = "Maximum brightness upto which the effect should go"

# Product Common -> Indicator -> Event: Solid: CCT
solid = description.solid_cct
solid.update(cct)
solid.title = "Indicator: Event: Solid: CCT"
solid.description = "Event solid for color select: `White`"
solid.example = ['{"name":"setup_mode_start","mode":"solid","speed":2000,"color_select":2,"cct":0,"max_brightness":100}']

solid.mode.title = "Mode"
solid.mode.description = "`solid` for mode Solid"
solid.mode.max_brightness.title = "Maximum Brightness"
solid.mode.max_brightness.description = "Maximum brightness upto which the effect should go"

# Product Common -> Indicator -> Event: Blink/Breathe: RGB
bb = description.blink_breathe_rgb
bb.update(rgb)
bb.title = "Indicator: Event: Blink/Breathe: RGB"
bb.description = "Event Blink or Breathe for color select: `Color`"
bb.example = ['{"name":"setup_mode_start","mode":"breathe","speed":2000,"color_select":1,"r":0,"g":255,"b":0,"min_brightness":20,"max_brightness":100,"total_ms":0,"interrupt_forbidden":true}']

bb.mode.title = "Mode"
bb.mode.description = "Effect type\n• breathe: Maximum brightness to minimum brightness and back to maximum brightness, gradually\n• blink: Maximum brightness to minimum brightness and back to maximum brightness, instantly\n"
bb.speed.title = "Speed"
bb.speed.description = "Time for a cycle to compelete, in case of breathe or blink, in m.\n• default: 500\n"
bb.min_brightness.title = "Minimum Brightness"
bb.min_brightness.description = "Minimum brightness upto which the effect should go"
bb.max_brightness.title = "Maximum Brightness"
bb.max_brightness.description = "Maximum brightness upto which the effect should go, also used in solid mode"

# Product Common -> Indicator -> Event: Blink/Breathe: CCT
bb = description.blink_breathe_cct
bb.update(cct)
bb.title = "Indicator: Event: Blink/Breathe: CCT"
bb.description = "Event Blink or Breathe for color select: `White`"
bb.example = ['{"name":"setup_mode_start","mode":"breathe","speed":2000,"color_select":2,"cct":0,"min_brightness":20,"max_brightness":100,"total_ms":0,"interrupt_forbidden":true}']

bb.mode.title = "Mode"
bb.mode.description = "Effect type\n• breathe: Maximum brightness to minimum brightness and back to maximum brightness, gradually\n• blink: Maximum brightness to minimum brightness and back to maximum brightness, instantly\n"
bb.speed.title = "Speed"
bb.speed.description = "Time for a cycle to compelete, in case of breathe or blink, in m.\n• default: 500\n"
bb.min_brightness.title = "Minimum Brightness"
bb.min_brightness.description = "Minimum brightness upto which the effect should go"
bb.max_brightness.title = "Maximum Brightness"
bb.max_brightness.description = "Maximum brightness upto which the effect should go, also used in solid mode"

# Product Common -> temp protect
tempprotect = description.tempprotect
tempprotect.title = "Temperature protect"
tempprotect.section = "Product Common"
tempprotect.description = "Temperature protect configuration. This is an optional configuration."
tempprotect.example = ['{"type": "ezc.product_common.temp_protect", "input": 1005, "normal_temp": 25, "warn_temp": 105}']

tempprotect.type.title = "Type"
tempprotect.type.description = "Product Common type: ezc.product_common.temp_protect. Devices with temperature protect."
tempprotect.input.title = "Temperature sensor driver input id"
tempprotect.input.description = "Temperature sensor driver input id"
tempprotect.normal_temp.title = "Device normal operating temperature"
tempprotect.normal_temp.description = "Device normal operating temperature"
tempprotect.warn_temp.title = "Device warning operating temperature"
tempprotect.warn_temp.description = "Device warning operating temperature"
tempprotect.protect_temp.title = "Device protect temperature"
tempprotect.protect_temp.description = "Device protect temperature"
tempprotect.normal_behaviors.title = "Normal behaviors"
tempprotect.normal_behaviors.description = "Behavior when temperature reaches normal temperature"
tempprotect.warn_behaviors.title = "Warn behaviors"
tempprotect.warn_behaviors.description = "Behavior when temperature exceeded warning temperature"
tempprotect.protect_behaviors.title = "Protect behaviors"
tempprotect.protect_behaviors.description = "Behavior when temperature exceeded protect temperature"
tempprotect.normal_sample_interval.title = "normal sample interval"
tempprotect.normal_sample_interval.description = "normal sample interval"
tempprotect.fast_sample_interval.title = "fast sample interval"
tempprotect.fast_sample_interval.description = "fast sample interval when temperature is higher than warn temperature"
tempprotect.normal_sample_count.title = "normal sample count"
tempprotect.normal_sample_count.description = "normal sample count to calculate average temperature"
tempprotect.fast_sample_count.title = "fast sample count"
tempprotect.fast_sample_count.description = "fast sample count to calculate average temperature"

# Product Common -> Zero Detect
zerodetect = description.zerodetect
zerodetect.title = "Zero Detect"
zerodetect.section = "Product Common"
zerodetect.description = "Zero Detect configuration. This is an optional configuration."
zerodetect.example = ['{"type": "ezc.product_common.zero_detect", "driver": { "zero_detect": 1005, "invalid_behaviors": 0, "lost_signal": 0, "delay_us": 0 }}']

zerodetect.type.title = "Type"
zerodetect.type.description = "Product Common type: ezc.product_common.zero_detect. Devices with zero-crossing detection functionality should have corresponding configurations."

zerodetect.driver.title = "Zero Detect: Driver Configurations"
zerodetect.driver.description = "Driver details for Zero Detect"
zerodetect.driver.example = ['{"driver": { "zero_detect": 1005, "invalid_behaviors": 0, "lost_signal": 0, "delay_us": 0 }}']

# Product Common -> Zero Detect -> Driver
driver = zerodetect.driver
driver.zerodetect.title = "Zero Detect Driver ID"
driver.zerodetect.description = "Zero Detect Driver ID."

driver.invalid_behaviors.title = "Invalid Behaviors"
driver.invalid_behaviors.description = "Behavior when the signal is invalid."

driver.lost_signal.title = "Lost Signal Behaviors"
driver.lost_signal.description = "Behavior when the signal is lost."

driver.delay_us.title = "Delay after zero crossing"
driver.delay_us.description = "Delay after zero crossing, unit: us."
