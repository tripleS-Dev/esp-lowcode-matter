from dotmap import DotMap

description = DotMap()

driver_base = description.driver_base
driver_base.id.title = "ID"
driver_base.id.description = "This must be unique for each driver object created. Make sure to use the correct Driver ID in the other sections."

# Driver -> Button
buttonbase = description.button_driver_base
buttonbase.update(driver_base)
buttonbase.title = "Button Driver"
buttonbase.section = "Driver"
buttonbase.description = "Button input driver to give input to the device"
buttonbase.type.title = "Type"
buttonbase.type.description = "Driver: ezc.driver.button"

# Driver -> Button -> gpio_driver
gpiobutton = description.button.gpio_driver
gpiobutton.update(buttonbase)
gpiobutton.title = "Button Driver: GPIO Driver"
gpiobutton.description = "Applicable if GPIO is selected as Button Driver"
gpiobutton.example = ['{"id": 1000,"type": "ezc.driver.button","name": "gpio", "gpio_config": {"gpio_num": 9,"active_level": 0,"long_press_time": 5}}']
gpiobutton.name.title = "Button name"
gpiobutton.name.description = "Button subtype: GPIO"

# Driver -> Button -> gpio_driver -> gpio_config
config = gpiobutton.config
config.title = "Button Driver: GPIO Configurations"
config.description = "Configuration for GPIO button, applicable if `ezc.driver.gpio` is selected"
config.example = ['{"gpio_config": {"gpio_num": 9,"active_level": 0,"long_press_time": 5}}']
config.gpio_num.title = "GPIO pin number"
config.gpio_num.description = "Input GPIO for the driver. Range of values depend on the chip"
config.active_level.title = "Button Active Level"
config.active_level.description = "When is the input detected, is it active_high or active_low\n• 0: Active low. The input is detected when the input pin is connected to GND\n• 1: Active high. The input is detected when the input pin is connected to VCC\n"
config.long_press_time.title = "Long Press Time"
config.long_press_time.description = "Time in seconds for long press event to be detected."

# Driver -> Button -> adc_driver
adcbutton = description.button.adc_driver
adcbutton.update(buttonbase)
adcbutton.title = "Button Driver: ADC Driver"
adcbutton.description = "Applicable if ADC is selected as Button Driver"
adcbutton.example = ['{"id": 1000,"type": "ezc.driver.button","name": "adc", "adc_config": {"gpio_num": 9,"active_level": 0,"long_press_time": 5}}']
adcbutton.name.title = "Button name"
adcbutton.name.description = "Button subtype: ADC"

# Driver -> Button -> adc_driver -> adc_config
config = adcbutton.config
config.title = "Button Driver: ADC Configurations"
config.description = "Configuration for ADC button, applicable if `ezc.driver.gpio` is selected"
config.example = ['{"adc_config": {"adc_channel": 0,"button_index": 1,"min": 100,"max": 500,"long_press_time": 5}}']
config.adc_channel.title = "ADC Channel"
config.adc_channel.description = "Input ADC for the driver. Range of values depend on the chip"
config.button_index.title = "Button Index"
config.button_index.description = "button index on the channel"
config.min.title = "Min Voltage"
config.min.description = "min voltage in mv corresponding to the button"
config.max.title = "Max Voltage"
config.max.description = "max voltage in mv corresponding to the button"
config.long_press_time.title = "Long Press Time"
config.long_press_time.description = "Time in seconds for long press event to be detected."

# Driver -> Button -> hosted_driver
hostedbutton = description.button_driver.button_hosted
hostedbutton.update(buttonbase)
hostedbutton.title = "Button Driver: Hosted Driver"
hostedbutton.description = "UART based button driver"
hostedbutton.example = ['{"id": 1000,"type": "ezc.driver.button","name": "hosted", "hosted_config": {"uart_driver_id": 1}}']
hostedbutton.name.title = "Name"
hostedbutton.name.description = "`hosted` applicable only if hosted driver is selected"

# Driver -> Button -> hosted_driver -> hosted_config
config = hostedbutton.config
config.title = "Button Driver: Hosted Configuration"
config.description = "Applicable if hosted is selected"
config.example = ['{"hosted_config": {"uart_driver_id": 1}}']
config.uart_driver_id.title= "Unique Driver ID"
config.uart_driver_id.description = "Unique driver id used to distinguish different buttons connected to host"

# Driver -> Relay
relaybase = description.relaybase
relaybase.title = "Relay Driver"
relaybase.section = "Driver"
relaybase.description = "Relay Driver"
relaybase.example = ['{"id": 1000,"type": "ezc.driver.relay","name": "gpio", "gpio_config": {"gpio_num": 10,"active_level": 0}}']
relaybase.update(driver_base)
relaybase.type.title = "Type"
relaybase.type.description = "Driver: ezc.driver.relay"
relaybase.name.title = "Relay name"
relaybase.name.description = "Subtype of relay"

# Driver -> Relay -> gpio_driver
gpiorelay = description.relay_driver.relay_gpio
gpiorelay.update(relaybase)
gpiorelay.title = "Relay Driver: GPIO"
gpiorelay.description = "GPIO based relay driver"
gpiorelay.example = ['{"id": 1000,"type": "ezc.driver.relay","name": "gpio", "gpio_config": {"gpio_num": 10,"active_level": 0}}']
gpiorelay.name.title = "Name"
gpiorelay.name.description = "`gpio` applicable only if gpio driver is selected"

# Driver -> Relay -> gpio_driver -> gpio_config
config = gpiorelay.gpio_config
config.title = "Relay Driver: GPIO Configuration"
config.description = "Applicable if gpio is selected"
config.example = ['{"gpio_config": {"gpio_num": 10,"active_level": 0}}']

config.gpio_num.title= "Relay Output GPIO"
config.gpio_num.description = "Output GPIO for the driver. Range of values depend on the chip"
config.active_level.title = "Relay Active Level"
config.active_level.description = "When is the output turned on\n• 0: The output is on when it connected to GND\n• 1: The output is on when it connected to VCC\n"

# Driver -> Relay -> hosted_driver
hostedrelay = description.relay_driver.relay_hosted
hostedrelay.update(relaybase)
hostedrelay.title = "Relay Driver: Hosted"
hostedrelay.description = "UART based relay driver"
hostedrelay.example = ['{"id": 1000,"type": "ezc.driver.relay","name": "hosted", "hosted_config": {"uart_driver_id": 1}}']
hostedrelay.name.title = "Name"
hostedrelay.name.description = "`hosted` applicable only if hosted driver is selected"

# Driver -> Relay -> hosted_driver -> hosted_config
config = hostedrelay.hosted_config
config.title = "Relay Driver: Hosted Configuration"
config.description = "Applicable if hosted is selected"
config.example = ['{"hosted_config": {"uart_driver_id": 1}}']
config.uart_driver_id.title= "Unique Driver ID"
config.uart_driver_id.description = "Unique driver id used to distinguish different relays connected to host"

# Driver -> TempSensor
tempsensorbase = description.tempsensor_driver_base
tempsensorbase.update(driver_base)
tempsensorbase.title = "Temperature Sensor Driver"
tempsensorbase.section = "Driver"
tempsensorbase.description = "Temperature sensor driver to capture temperature data"
tempsensorbase.type.title = "Type"
tempsensorbase.type.description = "Driver: ezc.driver.temp_sensor"

# Driver -> TempSensor -> onchip_driver
onchip_driver = description.tempsensor_driver.onchip_driver
onchip_driver.update(tempsensorbase)
onchip_driver.title = "Temperature Sensor Driver: OnChip Driver"
onchip_driver.description = "Applicable if OnChip is selected as Temperature Sensor Driver"
onchip_driver.example = ['{"id": 1000, "type": "ezc.driver.temp_sensor", "name": "onchip", "onchip_config": {"range_min": 50, "range_max": 125 }}']
onchip_driver.name.title = "Name"
onchip_driver.name.description = "Driver name: OnChip"

config = onchip_driver.onchip_config
config.title = "Temperature Sensor Driver: OnChip Configuration"
config.description = "Applicable if OnChip Sensor is selected"
config.example = ['{"onchip_config": {"range_min": 50, "range_max": 125 }}']
config.range_min.title= "Minimum temperature"
config.range_min.description = "The minimum value of the temperature want to test (in degree Celcius)"
config.range_max.title = "Maximum temperature"
config.range_max.description = "The maximum value of the temperature want to test (in degree Celcius)"

# Driver -> TempSensor -> ntc_driver
ntc_driver = description.tempsensor_driver.ntc_driver
ntc_driver.update(tempsensorbase)
ntc_driver.title = "Temperature Sensor Driver: NTC Driver"
ntc_driver.description = "Applicable if NTC is selected as Temperature Sensor Driver"
ntc_driver.example = ['{"id": 1000, "type": "ezc.driver.temp_sensor", "name": "ntc", "ntc_config" : {"b_value": 3950,"r25_ohm": 10000,"fixed_ohm": 10000,"vdd_mv": 3300,"circuit_mode": 1,"atten": 3,"unit": 0,"channel": 3}}']
ntc_driver.name.title = "Name"
ntc_driver.name.description = "Driver name: NTC"

config = ntc_driver.ntc_config
config.title = "Temperature Sensor Driver: NTC Configuration"
config.description = "Applicable if NTC is selected"
config.example = ['{"ntc_config" : {"b_value": 3950,"r25_ohm": 10000,"fixed_ohm": 10000,"vdd_mv": 3300,"circuit_mode": 1,"atten": 3,"unit": 0,"channel": 3}}']
config.b_value.title= "beta value of NTC (K)"
config.b_value.description = "beta value of NTC (K)"
config.r25_ohm.title = "25℃ resistor value of NTC (K)"
config.r25_ohm.description = "25℃ resistor value of NTC (K)"
config.fixed_ohm.title= "fixed resistor value (Ω)"
config.fixed_ohm.description = "fixed resistor value (Ω)"
config.vdd_mv.title = "vdd voltage (mv)"
config.vdd_mv.description = "vdd voltage (mv)"
config.circuit_mode.title= "ntc circuit mode"
config.circuit_mode.description = "ntc circuit mode"
config.atten.title= "adc atten"
config.atten.description = "adc atten"
config.unit.title = "adc channel"
config.unit.description = "adc channel"
config.channel.title = "adc unit"
config.channel.description = "adc unit"

# Driver -> ZeroDetect
zerodetect = description.zerodetect_driver
zerodetect.title = "ZeroDetect Driver"
zerodetect.section = "Driver"
zerodetect.description = "ZeroDetect driver to capture Zero-Cross signal"
zerodetect.example = ['{"id": 1000, "type": "ezc.driver.zero_detect", "name": "gpio", "capture_gpio_num": 6, "zero_signal_type": 1, "max_freq_hz": 65, "min_freq_hz": 45, "valid_times": 6, "invalid_times": 20, "signal_lost_time_us": 100000}']

zerodetect.update(driver_base)
zerodetect.type.title = "Type"
zerodetect.type.description = "Driver: ezc.driver.zero_detect"
zerodetect.name.title = "ZeroDetect name"
zerodetect.name.description = "ZeroDetect subtype"

zerodetect.capture_gpio_num.title = "GPIO pin number"
zerodetect.capture_gpio_num.description = "Input GPIO for the driver. Range of values depend on the chip"
zerodetect.zero_signal_type.title = "Zero Signal Type"
zerodetect.zero_signal_type.description = "Zero-crossing signal types include pulse and square wave."
zerodetect.max_freq_hz.title = "Support max frequency"
zerodetect.max_freq_hz.description = "Support Maximum Frequency of Zero-Cross Detection Signal."
zerodetect.min_freq_hz.title = "Support min frequency"
zerodetect.min_freq_hz.description = "Support Minimum Frequency of Zero-Cross Detection Signal."
zerodetect.valid_times.title = "Threshold for determining the validity of zero-crossing signals."
zerodetect.valid_times.description = "When the zero-cross detection signal is within the frequency range, it will be considered as a valid signal if it occurs more than X times."
zerodetect.invalid_times.title = "Threshold for determining the in-validity of zero-crossing signals."
zerodetect.invalid_times.description = "When the zero-cross detection signal is without the frequency range, it will be considered as a in-valid signal if it occurs more than X times."
zerodetect.signal_lost_time_us.title = "Timeout duration for determining signal loss"
zerodetect.signal_lost_time_us.description = "Timeout duration for determining signal loss."

# Driver -> Led base Model
ledbase = description.ledbase
ledbase.title = "Light Driver"
ledbase.section = "Driver"
ledbase.description = "LED and Light Bulb Driver"
ledbase.update(driver_base)
ledbase.type.description = "Driver: ezc.driver.led"
ledbase.type.title = "Type"

# Driver -> led driver gpio
led_gpio = description.led_driver.led_gpio
led_gpio.update(ledbase)
led_gpio.title = "Light Driver: GPIO LED Driver"
led_gpio.description = "GPIO powered led driver"
led_gpio.example = ['{"id": 1002, "type": "ezc.driver.led", "name": "gpio", "gpio_config": {"gpio_num": 12, "active_level": 0}}']

led_gpio.name.title = "Name"
led_gpio.name.description = "`gpio` applicable only if gpio led driver is selected"

# Driver -> led_driver_gpio -> gpio_config
config = led_gpio.gpio_config
config.title = "Light Driver: GPIO LED Driver: Configurations"
config.description = "Applicable if gpio is selected"
config.example = ['{"gpio_config": {"gpio_num": 10,"active_level": 0}}']

config.gpio_num.title= "Light Output GPIO"
config.gpio_num.description = "Output GPIO for the driver. Range of values depend on the chip"
config.active_level.title = "Light Active Level"
config.active_level.description = "When is the output turned on\n• 0: The output is on when it connected to GND\n• 1: The output is on when it connected to VCC\n"

# Driver -> led non-gpio
led_non_gpio = description.led_non_gpio
led_non_gpio.update(ledbase)

# Driver -> led non-gpio -> lighting_config
lighting_config = led_non_gpio.lighting_config
lighting_config.title = "Light Driver: Lighting Configurations"
lighting_config.description = "More light configurations"
lighting_config.example = ['{"lighting_config": {"enable_gradient": true, "enable_memory": false, "enable_lowpower": false, "sync_change_brightness": true, "disable_auto_on": true, "beads_comb": 3, "fades_ms": 300, "cct_kelvin_min": 2200, "cct_kelvin_max": 7000}}']

lighting_config.enable_gradient.title = "Enable Gradient"
lighting_config.enable_gradient.description = "Switch gradient\n• true: enable\n• false: disable\n"
lighting_config.enable_memory.title = "Enable Memory"
lighting_config.enable_memory.description = "Retain the power state on reboot"
lighting_config.enable_lowpower.title = "Enable Lowpower"
lighting_config.enable_lowpower.description = "Low power consumption mode"
lighting_config.sync_change_brightness.title = "Sync Brightness Change"
lighting_config.sync_change_brightness.description = "Change the brightness synchronously"
lighting_config.disable_auto_on.title = "Disable Auto On"
lighting_config.disable_auto_on.description = "Disable turning on of the light"
lighting_config.fades_ms.title = "Fade (in ms)"
lighting_config.fades_ms.description = "Default ramp time in ms"
lighting_config.cct_kelvin_min.title = "Minimum Color Temperature"
lighting_config.cct_kelvin_min.description = "Min color temperature support by hardware in kelvin\nRange: 1500K~7000K\nDefault: 2000K"
lighting_config.cct_kelvin_max.title = "Maximum Color Temperature"
lighting_config.cct_kelvin_max.description = "Max color temperature support by hardware in kelvin\nRange: 1500K~7000K\nDefault: 7000K"
lighting_config.beads_comb.title = "LED Beads Combination"
lighting_config.beads_comb.description = "LED Beads Combination support by hardware\n• 1: C\n• 2: W\n• 3: CW\n• 4: RGB\n• 5: 4CH_RGBC\n• 6: 4CH_RGBCC\n• 7: 4CH_RGBW\n• 8: 4CH_RGBWW\n• 9: 5CH_RGBCW\n• 10: 5CH_RGBCC\n• 11: 5CH_RGBWW\n• 12: 5CH_RGBC\n• 13: 5CH_RGBW\n"
lighting_config.enable_precise_cct_control.title = "Precise CCT Control"
lighting_config.enable_precise_cct_control.description = "Precise CCT Control\n• true: enable\n• false: disable\n"
lighting_config.enable_precise_color_control.title = "Precise Color Control"
lighting_config.enable_precise_color_control.description = "Precise Color Control\n• true: enable\n• false: disable\n"

# Driver -> led non-gpio -> hardware_config
config = led_non_gpio.hardware_config
config.title = "Light Driver: Hardware Configurations"
config.description = "Hardware configuration of led"
config.example = ['{"hardware_config": {"white_min": 1, "white_max": 100, "white_power_max": 100, "rgb_min": 1, "rgb_max": 100, "rgb_power_max": 100}}']
config.white_min.title = "White Minimum"
config.white_min.description = "Minimum brightness of white light\n"
config.white_max.title = "White Maximum"
config.white_max.description = "Maximum brightness of white light\n"
config.white_power_max.title = "White Power Maximum"
config.white_power_max.description = "Maximum white light power, 100-200.\n• If it is set to 100, the total output power is 100% of the single channel.\n"
config.rgb_min.title = "Minimum RGB Brightness"
config.rgb_min.description = "Minimum brightness of color light\n"
config.rgb_max.title = "Maximum RGB Brightness"
config.rgb_max.description = "Maximum brightness of color light\n"
config.rgb_power_max.title = "Maximum Brightness Color Light"
config.rgb_power_max.description = "Maximum power of color light\n• If it is set to 100, the total output power is 300% of the single channel, that is, 3-channel full power output.\n"

# Driver -> led non-gpio -> gamma_config
config = led_non_gpio.gamma_config
config.title = "Light Driver: Gamma Configurations"
config.description = "Gamma configurations for light bulb. Applicable for all except when gpio is selected"
config.example = ['{"gamma_config": {"enable_gamma_adjust": true, "gamma_red": 100, "gamma_green": 100, "gamma_blue": 100, "gamma_cold": 100, "gamma_warm": 100, "curve_coe": 1}}']
config.enable_gamma_adjust.title = "Enable color light calibration"
config.enable_gamma_adjust.description = "Enable color light calibration\n• true: enable\n• false: disable\n"
config.gamma_red.title = "Red Gamma Calibration"
config.gamma_red.description = "Red gamma calibration\n"
config.gamma_green.title = "Green gamma calibration"
config.gamma_green.description = "Green gamma calibration\n"
config.gamma_blue.title = "Blue gamma calibration"
config.gamma_blue.description = "Blue gamma calibration\n"
config.gamma_cold.title = "Cold gamma calibration"
config.gamma_cold.description = "Cold gamma calibration\n"
config.gamma_warm.title = "Warm gamma calibration"
config.gamma_warm.description = "Warm gamma calibration\n"
config.curve_coe.title = "White balance"
config.curve_coe.description = "White balance\n"

# Driver -> led non-gpio -> cctmap_cfg
config = led_non_gpio.cctmap_cfg
config.title = "Light Driver: CCT Map Configurations"
config.description = "CCT Map configurations for light bulb. Applicable for light with precise cct control enable\nMap data format is as follows:\n\t[[cct_kelvin, cct_percentage, coef_red, coef_green, coef_blue, coef_cold, coef_warm], ...]"
config.example = ['{"cct_map": { "table": "[[2200, 0, 0.033, 0.033, 0.034, 0.45, 0.45],[7000, 100, 0.033, 0.033, 0.034, 0.45, 0.45]]"}}']
config.table.title = "CCT Map Table"
config.table.description = "CCT Map Table\n• cct: Color temperature in kelvin\n• cct_percentage: Percentage of color temperature\n• red: Red light output\n• green: Green light output\n• blue: Blue light output\n• cold: Cold white light output\n• warm: Warm white light output\n"

# Driver -> led non-gpio -> colormap_cfg
config = led_non_gpio.colormap_cfg
config.title = "Light Driver: Color Map Configurations"
config.description = "Color Map configurations for light bulb. Applicable for light with precise color control enable\nMap data format is as follows:\n\t[[hue, saturation_100_red, saturation_100_green, saturation_100_blue, saturation_100_cold, saturation_100_warm, saturation_50_red, saturation_50_green, saturation_50_blue, saturation_50_cold, saturation_50_warm, saturation_0_red, saturation_0_green, saturation_0_blue, saturation_0_cold, saturation_0_warm], ...]"
config.example = ['{"color_map":{"table":"[[0,1,0,0,0,0,0.9120,0.0440,0.0440,0,0,0.4854,0.2573,0.2573,0,0],[15,0.9218,0.0782,0,0,0,0.8549,0.0907,0.0544,0,0,0.5112,0.2639,0.2248,0,0]]"}}']
config.table.title = "Color Map Table"
config.table.description = "Color Map Table. Add at least 12 sets of color data"

# Driver -> WS2812
ws2812_driver = description.led_driver.ws2812_driver
ws2812_driver.update(led_non_gpio)
ws2812_driver.title = "Light Driver: WS2812 LED Driver"
ws2812_driver.description = "Applicable if ws2812 is selected as led driver"
ws2812_driver.example = ['{"id": 1000, "type": "ezc.driver.led", "name": "ws2812", "ws2812_config": {"led_num": 1, "ctrl_io": 8}, "lighting_config": {"enable_gradient": true, "enable_memory": false, "enable_lowpower": false, "sync_change_brightness": true, "disable_auto_on": true, "beads_comb": 3, "fades_ms": 300, "cct_kelvin_min": 2200, "cct_kelvin_max": 7000}, "hardware_config": {"white_min": 1, "white_max": 100, "white_power_max": 100, "rgb_min": 1, "rgb_max": 100, "rgb_power_max": 100}, "gamma_config": {"enable_gamma_adjust": true, "gamma_red": 100, "gamma_green": 100, "gamma_blue": 100, "gamma_cold": 100, "gamma_warm": 100, "curve_coe": 1}}']

ws2812_driver.name.title = "Name"
ws2812_driver.name.description = "Driver name: WS2812"

# Driver -> WS2812 -> ws2812_config
config = ws2812_driver.ws2812_config
config.title = "Light Driver: WS2812 LED Driver: Configurations"
config.description = "WS2812 LED driver extra configurations"
config.example = ['{"ws2812_config": {"led_num": 1, "ctrl_io": 8}}']

config.led_num.title = "Number of LEDs"
config.led_num.description = "Number of LEDs"
config.ctrl_io.title = "Control IO"
config.ctrl_io.description = 'Data signal pin. Range of values depends on the chip'

# Driver -> PWM driver
pwm_driver = description.led_driver.pwm_driver
pwm_driver.update(led_non_gpio)
pwm_driver.title = "Light Driver: PWM Light Driver"
pwm_driver.description = "PWM light driver configuration"
pwm_driver.example = ['{"id": 1000, "type": "ezc.driver.led", "name": "pwm", "pwm_config": {"pwm_hz": 4000, "invert_level": false, "temperature_mode": 1, "gpio_red": 4, "gpio_green": 5, "gpio_blue": 6, "gpio_cold_or_cct": 3, "gpio_warm_or_brightness": 7}, "lighting_config": {"enable_gradient": true, "enable_memory": false, "enable_lowpower": false, "sync_change_brightness": true, "disable_auto_on": true, "beads_comb": 3, "fades_ms": 300, "cct_kelvin_min": 2200, "cct_kelvin_max": 7000}, "hardware_config": {"white_min": 1, "white_max": 100, "white_power_max": 100, "rgb_min": 1, "rgb_max": 100, "rgb_power_max": 100}, "gamma_config": {"enable_gamma_adjust": true, "gamma_red": 100, "gamma_green": 100, "gamma_blue": 100, "gamma_cold": 100, "gamma_warm": 100, "curve_coe": 1}}']

pwm_driver.name.title = "Name"
pwm_driver.name.description = "Applicable if `pwm` is selected as the light driver"
pwm_driver.pwm_config.title = "Light Driver: PWM Light Driver: Configurations"
pwm_driver.pwm_config.description = "Contains extra PWM configurations"
pwm_driver.pwm_config.example = ['{"pwm_config": {"pwm_hz": 4000, "invert_level": false, "temperature_mode": 1, "gpio_red": 4, "gpio_green": 5, "gpio_blue": 6, "gpio_cold_or_cct": 3, "gpio_warm_or_brightness": 7}}']

# Driver -> Pwm Driver -> pwm_config
config = pwm_driver.pwm_config
config.pwm_hz.title = "PWM frequency (in hz)"
config.pwm_hz.description = "PWM frequency (in hz)"
config.invert_level.title = "PWM invert level"
config.invert_level.description = "PWM invert level\n• true: invert\n• false: not invert\n"
config.temperature_mode.title = "Temperature Mode"
config.temperature_mode.description = "riving mode of color temperature adjustment\n• 0: CCT mode: CCT + brightness\n• 1: CW mode: cold white light + warm white light\n"
config.phase_delay.title = "Phase Delay"
config.phase_delay.description = "Phase delay in pwm:\n• 0: No phase delay\n• 1: RGB channel phase delay\n• 2: CW channel phase delay\n• 4: RGBCW channel phase delay\n"
config.gpio_red.title = "GPIO red"
config.gpio_red.description = "Red light output pin. Range of values depend on the chip"
config.gpio_green.title = "GPIO green"
config.gpio_green.description = "Green light output pin. Range of values depend on the chip"
config.gpio_blue.title = "GPIO blue"
config.gpio_blue.description = "Blue light output pin. Range of values depend on the chip"
config.gpio_cold_or_cct.title = "Cold white light/CCT output pin"
config.gpio_cold_or_cct.description = "Cold white light/CCT output pin. Range of values depend on the chip"
config.gpio_warm_or_brightness.title = "gpio_warm_or_brightness: Warm"
config.gpio_warm_or_brightness.description = "Warm white light/brightness output pin. Range of values depend on the chip"

# Driver -> i2cbase
config = description.i2c_base_cfg
config.gpio_clock.title = "IIC clock signal pin"
config.gpio_clock.description = "IIC clock signal pin. Range of values depend on the chip"
config.gpio_sda.title = "IIC data signal pin"
config.gpio_sda.description = "IIC data signal pin. Range of values depend on the chip"

config.iic_khz.title = "IIC Frequency"
config.iic_khz.description = "IIC signal frequency in KHz"
config.out_red.title = "Red light output pin"
config.out_red.description = "Red light output pin. Range of values depend on the chip"
config.out_green.title = "Green light output pin"
config.out_green.description = "Green light output pin. Range of values depend on the chip"
config.out_blue.title = "Blue light output pin"
config.out_blue.description = "Blue light output pin. Range of values depend on the chip"
config.out_cold.title = "Cold white light output pin"
config.out_cold.description = "Cold white light output pin. Range of values depend on the chip"
config.out_warm.title = "Warm white light output pin"
config.out_warm.description = "Warm white light output pin. Range of values depend on the chip"


# Driver -> BP5758D
bp5758d_driver = description.led_driver.bp5758d_driver
bp5758d_driver.update(led_non_gpio)
bp5758d_driver.title = "Light Driver: BP5758D Light Driver"
bp5758d_driver.description = "BP5758D driver support"
bp5758d_driver.example = ['{"id": 1000, "type": "ezc.driver.led", "name": "bp5758d", "bp5758d_config": {"gpio_clock": 10, "gpio_sda": 4, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_warm": 3, "out_cold": 4, "out1_current_max": 6, "out2_current_max": 6, "out3_current_max": 6, "out4_current_max": 13, "out5_current_max": 13}, "lighting_config": {"enable_gradient": true, "enable_memory": false, "enable_lowpower": false, "sync_change_brightness": true, "disable_auto_on": true, "beads_comb": 3, "fades_ms": 300, "cct_kelvin_min": 2200, "cct_kelvin_max": 7000}, "hardware_config": {"white_min": 1, "white_max": 100, "white_power_max": 100, "rgb_min": 1, "rgb_max": 100, "rgb_power_max": 100}, "gamma_config": {"enable_gamma_adjust": true, "gamma_red": 100, "gamma_green": 100, "gamma_blue": 100, "gamma_cold": 100, "gamma_warm": 100, "curve_coe": 1}}']

bp5758d_driver.name.title = "Name"
bp5758d_driver.name.description = "Applicable only if `bp5758d` is selected as light driver"

# Driver -> BP5758D -> bp5758d_config
config = bp5758d_driver.bp5758d_config
config.update(description.i2c_base_cfg)
config.title = "Light Driver: BP5758D Light Driver: Configurations"
config.description = "Applicable if bp5758d is selected"
config.example = ['{"bp5758d_config": {"gpio_clock": 10, "gpio_sda": 4, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_warm": 3, "out_cold": 4, "out1_current_max": 6, "out2_current_max": 6, "out3_current_max": 6, "out4_current_max": 13, "out5_current_max": 13}}']

config.out1_current_max.title = "Channel 1 Current Max"
config.out1_current_max.description = "Maximum #1 channel current in mA"
config.out2_current_max.title = "Channel 2 Current Max"
config.out2_current_max.description = "Maximum #2 channel current in mA"
config.out3_current_max.title = "Channel 3 Current Max"
config.out3_current_max.description = "Maximum #3 channel current in mA"
config.out4_current_max.title = "Channel 4 Current Max"
config.out4_current_max.description = "Maximum #4 channel current in mA"

# Driver -> BP1658CJ
bp1658cj_driver = description.led_driver.bp1658cj_driver
bp1658cj_driver.update(led_non_gpio)
bp1658cj_driver.title = "Light Driver: BP1658CJ Light Driver"
bp1658cj_driver.description = "BP1658CJ driver support"
bp1658cj_driver.example = ['{"id": 1000, "type": "ezc.driver.led", "name": "bp1658cj", "bp1658cj_config": {"gpio_clock": 7, "gpio_sda": 3, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_cold": 4, "out_warm": 3, "white_current_max": 50, "rgb_current_max": 50},"lighting_config": {"enable_gradient": true, "enable_memory": false, "enable_lowpower": false, "sync_change_brightness": true, "disable_auto_on": true, "beads_comb": 3, "fades_ms": 300, "cct_kelvin_min": 2200, "cct_kelvin_max": 7000}, "hardware_config": {"white_min": 1, "white_max": 100, "white_power_max": 100, "rgb_min": 1, "rgb_max": 100, "rgb_power_max": 100}, "gamma_config": {"enable_gamma_adjust": true, "gamma_red": 100, "gamma_green": 100, "gamma_blue": 100, "gamma_cold": 100, "gamma_warm": 100, "curve_coe": 1}}']

bp1658cj_driver.name.title = "Name"
bp1658cj_driver.name.description = "Applicable only if `bp1658cj` is selected as light driver"

# Driver -> BP1658CJ -> bp1658cj_config
config = bp1658cj_driver.bp1658cj_config
config.update(description.i2c_base_cfg)
config.title = "Light Driver: BP1658CJ Light Driver: Configurations"
config.description = "Applicable if `bp1658cj is selected"
config.example = ['{"bp1658cj_config": {"gpio_clock": 7, "gpio_sda": 3, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_cold": 4, "out_warm": 3, "white_current_max": 50, "rgb_current_max": 50}}']

config.white_current_max.title = "White Current Max"
config.white_current_max.description = "Maximum white light current in mA"
config.rgb_current_max.title= "RGB Current Max"
config.rgb_current_max.description = "Maximum current of color light in mA"

# Driver -> SM2135E
sm2135e_driver = description.led_driver.sm2135e_driver
sm2135e_driver.update(led_non_gpio)
sm2135e_driver.title = "Light Driver: SM2135E Light Driver"
sm2135e_driver.description = "SM2135E driver support"
sm2135e_driver.example = ['{"id": 1000, "type": "ezc.driver.led", "name": "sm2135e", "sm2135e_config": {"gpio_clock": 7, "gpio_sda": 3, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_cold": 4, "out_warm": 3, "white_current_max": 50, "rgb_current_max": 30},"lighting_config": {"enable_gradient": true, "enable_memory": false, "enable_lowpower": false, "sync_change_brightness": true, "disable_auto_on": true, "beads_comb": 3, "fades_ms": 300, "cct_kelvin_min": 2200, "cct_kelvin_max": 7000}, "hardware_config": {"white_min": 1, "white_max": 100, "white_power_max": 100, "rgb_min": 1, "rgb_max": 100, "rgb_power_max": 100}, "gamma_config": {"enable_gamma_adjust": true, "gamma_red": 100, "gamma_green": 100, "gamma_blue": 100, "gamma_cold": 100, "gamma_warm": 100, "curve_coe": 1}}']

sm2135e_driver.name.title = "Name"
sm2135e_driver.name.description = "Applicable only if `sm2135e` is selected as light driver"

# Driver -> sm2135e -> sm2135e_config
config = sm2135e_driver.sm2135e_config
config.update(description.i2c_base_cfg)
config.title = "Light Driver: SM2135E Light Driver: Configurations"
config.description = "Applicable if `sm2135e is selected"
config.example = ['{"sm2135e_config": {"gpio_clock": 7, "gpio_sda": 3, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_cold": 4, "out_warm": 3, "white_current_max": 50, "rgb_current_max": 30}}']

config.white_current_max.title = "White Current Max"
config.white_current_max.description = "Maximum white light current in mA"
config.rgb_current_max.title= "RGB Current Max"
config.rgb_current_max.description = "Maximum current of color light in mA"

# Driver -> sm2135eh
sm2135eh_driver = description.led_driver.sm2135eh_driver
sm2135eh_driver.update(led_non_gpio)
sm2135eh_driver.title = "Light Driver: SM2135EH Light Driver"
sm2135eh_driver.description = "SM2135EH driver support"
sm2135eh_driver.example = ['{"id": 1000, "type": "ezc.driver.led", "name": "sm2135eh", "sm2135eh_config": {"gpio_clock": 7, "gpio_sda": 3, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_cold": 4, "out_warm": 3, "white_current_max": 50, "rgb_current_max": 28},"lighting_config": {"enable_gradient": true, "enable_memory": false, "enable_lowpower": false, "sync_change_brightness": true, "disable_auto_on": true, "beads_comb": 3, "fades_ms": 300, "cct_kelvin_min": 2200, "cct_kelvin_max": 7000}, "hardware_config": {"white_min": 1, "white_max": 100, "white_power_max": 100, "rgb_min": 1, "rgb_max": 100, "rgb_power_max": 100}, "gamma_config": {"enable_gamma_adjust": true, "gamma_red": 100, "gamma_green": 100, "gamma_blue": 100, "gamma_cold": 100, "gamma_warm": 100, "curve_coe": 1}}']
sm2135eh_driver.name.title = "Name"
sm2135eh_driver.name.description = "Applicable only if `sm2135eh` is selected as light driver"

# Driver -> sm2135eh -> sm2135e_config
config = sm2135eh_driver.sm2135eh_config
config.update(description.i2c_base_cfg)
config.title = "Light Driver: SM2135EH Light Driver: Configurations"
config.description = "Applicable if `sm2135eh is selected"
config.example = ['{"sm2135eh_config": {"gpio_clock": 7, "gpio_sda": 3, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_cold": 4, "out_warm": 3, "white_current_max": 50, "rgb_current_max": 28}}']

config.white_current_max.title = "White Current Max"
config.white_current_max.description = "Maximum white light current in mA"
config.rgb_current_max.title= "RGB Current Max"
config.rgb_current_max.description = "Maximum current of color light in mA"

# Driver -> sm2235egh
sm2235egh_driver = description.led_driver.sm2235egh_driver
sm2235egh_driver.update(led_non_gpio)
sm2235egh_driver.title = "Light Driver: SM2135EGH Light Driver"
sm2235egh_driver.description = "SM2135EGH driver support"
sm2235egh_driver.example = ['{"id": 1000, "type": "ezc.driver.led", "name": "sm2235egh", "sm2235egh_config": {"gpio_clock": 7, "gpio_sda": 3, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_cold": 4, "out_warm": 3, "white_current_max": 50, "rgb_current_max": 28},"lighting_config": {"enable_gradient": true, "enable_memory": false, "enable_lowpower": false, "sync_change_brightness": true, "disable_auto_on": true, "beads_comb": 3, "fades_ms": 300, "cct_kelvin_min": 2200, "cct_kelvin_max": 7000}, "hardware_config": {"white_min": 1, "white_max": 100, "white_power_max": 100, "rgb_min": 1, "rgb_max": 100, "rgb_power_max": 100}, "gamma_config": {"enable_gamma_adjust": true, "gamma_red": 100, "gamma_green": 100, "gamma_blue": 100, "gamma_cold": 100, "gamma_warm": 100, "curve_coe": 1}}']
sm2235egh_driver.name.title = "Name"
sm2235egh_driver.name.description = "Applicable only if `sm2135egh` is selected as light driver"

# Driver -> sm2235egh -> sm2235_config
config = sm2235egh_driver.sm2235egh_config
config.update(description.i2c_base_cfg)
config.title = "Light Driver: SM2135EGH Light Driver: Configurations"
config.description = "Applicable if `sm2235egh is selected"
config.example = ['{"sm2235egh_config": {"gpio_clock": 7, "gpio_sda": 3, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_cold": 4, "out_warm": 3, "white_current_max": 50, "rgb_current_max": 28}}']

config.white_current_max.title = "White Current Max"
config.white_current_max.description = "Maximum white light current in mA"
config.rgb_current_max.title= "RGB Current Max"
config.rgb_current_max.description = "Maximum current of color light in mA"

# Driver -> sm2335egh
sm2335egh_driver = description.led_driver.sm2335egh_driver
sm2335egh_driver.update(led_non_gpio)
sm2335egh_driver.title = "Light Driver: SM2335EGH Light Driver"
sm2335egh_driver.description = "SM2335EGH driver support"
sm2335egh_driver.example = ['{"id": 1000, "type": "ezc.driver.led", "name": "sm2335egh", "sm2335egh_config": {"gpio_clock": 7, "gpio_sda": 3, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_cold": 4, "out_warm": 3, "white_current_max": 50, "rgb_current_max": 30},"lighting_config": {"enable_gradient": true, "enable_memory": false, "enable_lowpower": false, "sync_change_brightness": true, "disable_auto_on": true, "beads_comb": 3, "fades_ms": 300, "cct_kelvin_min": 2200, "cct_kelvin_max": 7000}, "hardware_config": {"white_min": 1, "white_max": 100, "white_power_max": 100, "rgb_min": 1, "rgb_max": 100, "rgb_power_max": 100}, "gamma_config": {"enable_gamma_adjust": true, "gamma_red": 100, "gamma_green": 100, "gamma_blue": 100, "gamma_cold": 100, "gamma_warm": 100, "curve_coe": 1}}']
sm2335egh_driver.name.title = "Name"
sm2335egh_driver.name.description = "Applicable only if `sm2335egh` is selected as light driver"

# Driver -> sm2335egh -> sm2335egh_config
config = sm2335egh_driver.sm2335egh_config
config.update(description.i2c_base_cfg)
config.title = "Light Driver: SM2335EGH Light Driver: Configurations"
config.description = "Applicable if `sm2335egh` is selected"
config.example = ['{"sm2335egh_config": {"gpio_clock": 7, "gpio_sda": 3, "iic_khz": 300, "out_red": 2, "out_green": 1, "out_blue": 0, "out_cold": 4, "out_warm": 3, "white_current_max": 50, "rgb_current_max": 30}}']

config.white_current_max.title = "White Current Max"
config.white_current_max.description = "Maximum white light current in mA"
config.rgb_current_max.title= "RGB Current Max"
config.rgb_current_max.description = "Maximum current of color light in mA"

# Driver -> KP18058
kp18058_driver = description.led_driver.kp18058_driver
kp18058_driver.update(led_non_gpio)
kp18058_driver.title = "Light Driver: KP18058 Light Driver"
kp18058_driver.description = "KP18058 driver support"
kp18058_driver.example = ['{"id":1000,"type":"ezc.driver.led","name":"kp18058","lighting_config":{"enable_gradient":true,"enable_memory":false,"enable_lowpower":false,"sync_change_brightness":true,"disable_auto_on":true,"beads_comb":9,"fades_ms":800,"enable_precise_cct_control":false},"kp18058_config":{"gpio_clock":7,"gpio_sda":3,"iic_khz":300,"out_red":2,"out_green":1,"out_blue":0,"out_cold":4,"out_warm":3,"rgb_current_max":7.5,"white_current_max":27.5,"advanced_cfg":{"disable_voltage_compensation":0,"compensation":310,"slope":7.5,"disable_chopping_dimming":0,"chopping_freq":250,"enable_rc_filter":1}},"hardware_config":{"white_min":10,"white_max":100,"white_power_max":100,"rgb_min":10,"rgb_max":100,"rgb_power_max":300},"gamma_config":{"enable_gamma_adjust":true,"gamma_red":100,"gamma_green":100,"gamma_blue":100,"gamma_cold":100,"gamma_warm":100,"curve_coe":1}}']
kp18058_driver.name.title = "Name"
kp18058_driver.name.description = "Applicable only if `kp18058` is selected as light driver"

# Driver -> kp18058 -> kp18058_config
config = kp18058_driver.kp18058_config
config.update(description.i2c_base_cfg)
config.title = "Light Driver: KP18058 Light Driver: Configurations"
config.description = "Applicable if `kp18058` is selected"
config.example = ['{"kp18058_config":{"gpio_clock":7,"gpio_sda":3,"iic_khz":300,"out_red":2,"out_green":1,"out_blue":0,"out_cold":4,"out_warm":3,"rgb_current_max":7.5,"white_current_max":27.5,"advanced_cfg":{"disable_voltage_compensation":0,"compensation":310,"slope":7.5,"disable_chopping_dimming":0,"chopping_freq":250,"enable_rc_filter":1}}}']

config.white_current_max.title = "White Current Max"
config.white_current_max.description = "Maximum white light current in mA"
config.rgb_current_max.title= "RGB Current Max"
config.rgb_current_max.description = "Maximum current of color light in mA"
config.advanced_cfg.title= "Advanced Config"
config.advanced_cfg.description = "KP18058 optional driver config"

# Driver -> kp18058 -> kp18058_config -> advanced_cfg
advanced_cfg = kp18058_driver.kp18058_config.advanced_cfg
advanced_cfg.update(kp18058_driver)
advanced_cfg.title = "KP18058 advanced params"
advanced_cfg.description = "Custom advanced params"
advanced_cfg.example = ['{"advanced_cfg":{"disable_voltage_compensation":0,"compensation":310,"slope":7.5,"disable_chopping_dimming":0,"chopping_freq":250,"enable_rc_filter":1}}']

# Driver -> Roller blind base
roller_blind_base = description.roller_blind_base
roller_blind_base.section = "Driver"
roller_blind_base.type.title = "Type"
roller_blind_base.type.description = "Driver: ezc.driver.roller_blind"
roller_blind_base.name.title = "Name"
roller_blind_base.name.description = "`gpio` applicable if gpio roller blind driver is used."

# Driver -> Roller blind gpio
gpio_roller_blind = description.roller_blind_driver.roller_blind_gpio
gpio_roller_blind.update(roller_blind_base)
# Driver -> Roller blind -> roller_blind_gpio
gpio_roller_blind.title = "Roller blind Driver: GPIO"
gpio_roller_blind.description = "GPIO based Roller blind driver"
gpio_roller_blind.example = ['{"id":1001,"type":"ezc.driver.roller_blind","name":"gpio","roller_blind_config":{"allow_reverse_in_moving":false,"pause_between_moves":true,"delay_time_between_moves_ms":500,"relay_control_delay_time_ms":0,"default_max_move_time_ms":60000},"gpio_config":{"up_relay_gpio":10,"down_relay_gpio":11},"calibration_config":{"calibration_type":1,"detect_gpio":12,"detection_frequency":50,"detection_frequency_offset":20}}']
gpio_roller_blind.name.title = "Name"
gpio_roller_blind.name.description = "`gpio` applicable only if gpio driver is selected"

# Driver -> Roller blind gpio -> Roller blind config
config = gpio_roller_blind.roller_blind_config
config.title = "Roller Blind Driver: Configurations: Movement Settings"
config.description = "More Roller Blind Configuration"
config.example = ['{"roller_blind_config": {"allow_reverse_in_moving": false, "pause_between_moves": true, "delay_time_between_moves_ms": 500, "relay_control_delay_time_ms": 0, "default_max_move_time_ms": 60000, "use_default_time_when_not_calibrated": false}}']

config.allow_reverse_in_moving.title = "Allow Reverse In Moving"
config.allow_reverse_in_moving.description = "Behaviour when pressing the opposite direction button, when in motion.\n• true: Reverse the motion\n• false: Stop the motion\n"
config.pause_between_moves.title = "Pause Between Moves"
config.pause_between_moves.description = "Whether to pause between movements.\n• true: pause between movements.\n• false: don't have pause between movements.\n"
config.delay_time_between_moves_ms.title = "Delay Time Between Moves (in ms)"
config.delay_time_between_moves_ms.description = "Delay in between changing the direction, in milliseconds.\n"
config.relay_control_delay_time_ms.title = "Relay Control Delay Time (in ms)"
config.relay_control_delay_time_ms.description = "Relay control delay time"
config.default_max_move_time_ms.title = "Default Max Move Time (in ms)"
config.default_max_move_time_ms.description = "The default moving time for the up and down during calibration or before calibration."
config.use_default_time_when_not_calibrated.title = "Use Default Time When Not Calibrated"
config.use_default_time_when_not_calibrated.description = "Always moving default time when un-calibrate.\n• true: use default time.\n• false: don't use default time.\n"
config.move_time_compensation_percent.title = "Move Time Compensation Percent"
config.move_time_compensation_percent.description = "Compensation moving time when the target position of window covering is the end of window cover(fully open/close)..\n• min: 0\n• max: 100\n• step: 1\n• default: 0\n"

# Driver -> Roller blind gpio -> GPIO config
config = gpio_roller_blind.gpio_config
config.title = "Roller Blind Driver: Configurations: GPIO Settings"
config.description = "More GPIO Configuration"
config.example = ['{"gpio_config": {"up_relay_gpio": 25, "up_relay_active_level": 1, "down_relay_gpio": 12, "down_relay_active_level": 1}}']

config.up_relay_active_level.title = "Up Relay Active Level"
config.up_relay_active_level.description = "When is the output turned on\n• 0: The output is on when it connected to GND\n• 1: The output is on when it connected to VCC\n• default: 1\n"
config.up_relay_gpio.title = "Up Relay GPIO"
config.up_relay_gpio.description = "Output GPIO for the up relay driver. Range of values depend on the chip"
config.down_relay_gpio.title = "Down Relay GPIO"
config.down_relay_gpio.description = "Output GPIO for the down relay driver. Range of values depend on the chip"
config.down_relay_active_level.title = "Down Relay Active Level"
config.down_relay_active_level.description = "When is the output turned on\n• 0: The output is on when it connected to GND\n• 1: The output is on when it connected to VCC\n• default: 1\n"

# Driver -> roller blind auto calibration
driver = gpio_roller_blind.roller_blind_auto_calib_driver
driver.title = "Roller Blind Driver: Automatic Calibration"
driver.description = "Roller Blind driver for Auto-calibration"
driver.example = ['{"id": 1002, "type": "ezc.driver.roller_blind", "name": "gpio", "roller_blind_config": {"allow_reverse_in_moving": false, "pause_between_moves": true, "delay_time_between_moves_ms": 500, "relay_control_delay_time_ms": 0, "default_max_move_time_ms": 60000, "use_default_time_when_not_calibrated": false}, "gpio_config": {"up_relay_gpio": 6, "up_relay_active_level": 1, "down_relay_gpio": 7, "down_relay_active_level": 1}, "calibration_config": {"calibration_type": 1, "detect_gpio": 26, "detection_frequency": 50, "detection_frequency_offset": 20}}']

# Driver -> roller blind driver(auto calibration) -> calibration_config
config = driver.calibration_config
config.title = "Roller Blind Driver: Automatic calibration configurations"
config.description = "Automatic Roller Blind calibration configurations and options"
config.example = ['{"calibration_config": {"calibration_type": 1, "detect_gpio": 26, "detection_frequency": 50, "detection_frequency_offset": 20}}']

config.calibration_type.title = "Calibration type"
config.calibration_type.description = "`1` for Auto Calibration, `2` for Manual Calibration"
config.detect_gpio.title = "Input Detect GPIO"
config.detect_gpio.description = "Input GPIO to detect frequency for auto calibration if auto calibration type. Range of values depend on the chip"
config.detection_frequency.title = "Frequency"
config.detection_frequency.description = "The frequency to be detected for auto calibration if auto calibration type"
config.detection_frequency_offset.title = "Detection Frequency Offset"
config.detection_frequency_offset.description = "The offset in the frequency to be detected for auto calibration if auto calibration type"

# Driver -> roller blind manual calibration
driver = gpio_roller_blind.roller_blind_manual_calib_driver
driver.title = "Roller Blind Driver: Manual Calibration"
driver.description = "Roller blind driver for manual calibration"
driver.example = ['{"id": 1002, "type": "ezc.driver.roller_blind", "name": "gpio", "roller_blind_config": {"allow_reverse_in_moving": false, "pause_between_moves": true, "delay_time_between_moves_ms": 500, "relay_control_delay_time_ms": 0, "default_max_move_time_ms": 60000, "use_default_time_when_not_calibrated": false}, "gpio_config": {"up_relay_gpio": 6, "up_relay_active_level": 1, "down_relay_gpio": 7, "down_relay_active_level": 1}, "calibration_config": {"calibration_type": 2}}']

# Driver -> roller blind driver(manual calibration) -> calibration_config
config = driver.calibration_config
config.title = "Roller Blind Driver: Manual calibration configurations"
config.description = "Manual Roller Blind calibration configurations and options"
config.example = ['{"calibration_config": {"calibration_type": 2}}']

config.calibration_type.title = "Calibration type"
config.calibration_type.description = "`1` for Auto Calibration, `2` for Manual Calibration"

# Driver -> Roller blind hosted
hosted_roller_blind = description.roller_blind_driver.roller_blind_hosted
hosted_roller_blind.update(roller_blind_base)
# Driver -> Roller blind -> hosted_driver
hosted_roller_blind.title = "Roller blind Driver: Hosted"
hosted_roller_blind.description = "UART based Roller blind driver"
hosted_roller_blind.example = ['{"id": 1000,"type": "ezc.driver.roller_blind","name": "hosted", "hosted_config": {"uart_driver_id": 1}}']
hosted_roller_blind.name.title = "Name"
hosted_roller_blind.name.description = "`hosted` applicable only if hosted driver is selected"

# Driver -> Roller blind -> hosted_driver -> hosted_config
config = hosted_roller_blind.hosted_config
config.title = "Roller blind Driver: Hosted Configuration"
config.description = "Applicable if hosted is selected"
config.example = ['{"hosted_config": {"uart_driver_id": 1}}']
config.uart_driver_id.title= "Unique Driver ID"
config.uart_driver_id.description = "Unique driver id used to distinguish different Roller blind connected to host"

# Driver -> Contact sensor
config = description.contact_sensor_driver.contact_sensor_gpio
config.title = "Contact Sensor Driver"
config.description = "Contact Sensor driver"
config.example = ['{"id": 1000, "type": "ezc.driver.contact_sensor", "name": "gpio", "gpio_config": {"gpio_num": 7, "active_level": 0}}']

config = description.contact_sensor_driver.contact_sensor_gpio.gpio_config
config.title = "Contact Sensor Driver: Configurations"
config.description = "Contact Sensor driver configurations"
config.example = ['{"gpio_config": {"gpio_num": 7, "active_level": 0}}']
