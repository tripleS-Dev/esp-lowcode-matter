from dotmap import DotMap

description = DotMap()

driver = description.light_base_model.driver
driver.title = "Light: Driver Configurations"
driver.description = "Driver details for light"
driver.example = ['{"driver":{"output":1000}}']

driver.output.title = "Output ID"
driver.output.description = "Output ID for light driver"
driver.input.title = "Input ID"
driver.input.description = "Input ID for light driver"
driver.input_mode.title = "Input Mode"
driver.input_mode.description = "Input driver mode\n• 0: Push Button\n• 1: Rocker Switch\n"
driver.input_trigger_type.title = "Input Trigger Type"
driver.input_trigger_type.description = "When to trigger the input:\n• 0: Press Down\n• 1: Press Up\n• 2: Repeat Press\n• 3: Repeat Press Release\n• 4: Single Click\n• 5: Double Click\n• 6: Long Press Start\n• 7: Long Press Hold\n\n"

light_data_model = description.light_data_model
light_data_model.power_default.title = "Power Default"
light_data_model.power_default.description = "Default power state of the device \n• `0`: Off\n• `1`: On\n"
light_data_model.power_bootup.title = "Power Boot Up"
light_data_model.power_bootup.description = "Power state of the device when it boots up:\n• `0`: Always Off\n• `1`: Always On\n• `2`: Toggle the previous value\n• `-1`: Previous value\n"
light_data_model.level_default.title = "Level Default"
light_data_model.level_default.description = "Default level/brightness of the device"
light_data_model.level_bootup.title = "Level Bootup"
light_data_model.level_bootup.description = "Level/brightness of the device when it boots up (if -1 then previous value is taken)"
light_data_model.color_mode_default.title = "Color Mode Default"
light_data_model.color_mode_default.description = "Default Color Mode of the device\n• `1`: Temperature\n• `2`: Color: Hue Saturation\n• `3`: Color: XY\n• `4`: Color: Enhanced Hue Saturation\n"
light_data_model.color_mode_bootup.title = "Color Mode Bootup"
light_data_model.color_mode_bootup.description = "Color mode of the device when it boots up\n• 1: Temperature\n• 2: Color: Hue Saturation\n• 3: Color: XY\n• 4: Color: Enhanced Hue Saturation\n• -1: Previous value\n"
light_data_model.temperature_default.title = "Temperature default"
light_data_model.temperature_default.description = "Default temperature of the device\n"

light_data_model.temperature_bootup.title = "Temperature Bootup"
light_data_model.temperature_bootup.description = "Temperature of the device when it boots up\n• 2000 to 9000\n• -1: Previous value\n"

light_data_model.temperature_minimum.title = "Temperature Minimum"
light_data_model.temperature_minimum.description = "Minimum temperature of the device\n• max: temperature_maximum_default\n"

light_data_model.temperature_maximum.title = "Temperature Maximum"
light_data_model.temperature_maximum.description = "Maximum temperature of the device"

light_data_model.hue_default.title = "Hue Default"
light_data_model.hue_default.description = "Default hue of the device\n"

light_data_model.hue_bootup.title = "Hue Bootup"
light_data_model.hue_bootup.description = "Hue of the device when it boots up\n• 0 to 360\n• -1: Previous value\n"

light_data_model.saturation_default.title = "Saturation Default"
light_data_model.saturation_default.description = "Default saturation of the device\n"

light_data_model.saturation_bootup.title = "Satuation Bootup"
light_data_model.saturation_bootup.description = "Saturation of the device when it boots up\n• 0 to 100\n• -1: Previous value\n"

light_data_model.color_x_default.title = "Color X Default"
light_data_model.color_x_default.description = "Default color X of the device"

light_data_model.color_y_default.title = "Color Y Default"
light_data_model.color_y_default.description = "Default color Y of the device"

light_on_off = description.light_on_off
light_on_off.update(description.light_base_model)
light_on_off.title = "Light: On Off"
light_on_off.description = "Light: On/Off: Product with on/off capabilities"
light_on_off.example = ['{"type":"ezc.product.light","subtype":1,"driver":{"output":1000},"data_model":{"power_default":1,"power_bootup":-1}}']
light_on_off.subytype.title = "Subtype"
light_on_off.subytype.description = "`1` Represents Light On/Off"

light_on_off.data_model.update(light_data_model)
light_on_off.data_model.title = "Light: On/Off: Data model"
light_on_off.data_model.description = "Data Model for Light On/Off"
light_on_off.data_model.example = ['{"data_model":{"power_default":1,"power_bootup":-1}}']

light_dimmable = description.light_dimmable
light_dimmable.title = "Light: Dimmable"
light_dimmable.description = "Light: Dimmable: Product with brightness capabilities"
light_dimmable.example = ['{"type":"ezc.product.light","subtype":2,"driver":{"output":1000},"data_model":{"power_default":1,"power_bootup":-1,"level_default":50,"level_bootup":-1}}']
light_dimmable.subytype.title = "Subtype"
light_dimmable.subytype.description = "`2`: Represents Light Dimmable"
light_dimmable.data_model.update(light_data_model)
light_dimmable.data_model.title = "Light: Dimmable: Data Model"
light_dimmable.data_model.description = "Data Model for Light Dimmable"
light_dimmable.data_mode.example = ['"data_model":{"power_default":1,"power_bootup":-1,"level_default":50,"level_bootup":-1}}']

light_temperature = description.light_temperature
light_temperature.title = "Light: Temperature"
light_temperature.description = "Light: Temperature: Product with temperature capabilities"
light_temperature.example = ['{"type":"ezc.product.light","subtype":3,"driver":{"output":1000},"data_model":{"power_default":1,"power_bootup":-1,"level_default":50,"level_bootup":-1,"color_mode_default":1,"color_mode_bootup":-1,"temperature_default":4000,"temperature_bootup":-1,"temperature_minimum_default":2000,"temperature_maximum_default":9000,"hue_default":180,"hue_bootup":-1,"saturation_default":100,"saturation_bootup":-1}}']
light_temperature.subytype.title = "Subtype"
light_temperature.subytype.description = "`3`: Represents Light Temperature"
light_temperature.data_model.update(light_data_model)
light_temperature.data_model.title = "Light: Temperature: Data Model"
light_temperature.data_model.description = "Data Model for Light Temperature"
light_temperature.data_model.example = ['{"data_model":{"power_default":1,"power_bootup":-1,"level_default":50,"level_bootup":-1,"color_mode_default":1,"color_mode_bootup":-1,"temperature_default":4000,"temperature_bootup":-1,"temperature_minimum_default":2000,"temperature_maximum_default":9000,"hue_default":180,"hue_bootup":-1,"saturation_default":100,"saturation_bootup":-1}}']

light_temperature_color = description.light_temperature_color
light_temperature_color.title = "Light: Temperature and Color"
light_temperature_color.description = "Light: Temperature and Color: Product with temperature and color capabilities"
light_temperature_color.example = ['{"type":"ezc.product.light","subtype":4,"driver":{"output":1000},"data_model":{"power_default":1,"power_bootup":-1,"level_default":50,"level_bootup":-1,"color_mode_default":1,"color_mode_bootup":-1,"temperature_default":4000,"temperature_bootup":-1,"temperature_minimum_default":2000,"temperature_maximum_default":9000,"hue_default":180,"hue_bootup":-1,"saturation_default":100,"saturation_bootup":-1}}']
light_temperature_color.subytype.title = "Subtype"
light_temperature_color.subytype.description = "`4`: Represents Light Temperature color"
light_temperature_color.data_model.update(light_data_model)
light_temperature_color.data_model.title = "Light: Temperature and Color: Data Model"
light_temperature_color.data_model.description = "Data Model for Light Temperature Color"
light_temperature_color.data_model.example = ['{"data_model":{"power_default":1,"power_bootup":-1,"level_default":50,"level_bootup":-1,"color_mode_default":1,"color_mode_bootup":-1,"temperature_default":4000,"temperature_bootup":-1,"temperature_minimum_default":2000,"temperature_maximum_default":9000,"hue_default":180,"hue_bootup":-1,"saturation_default":100,"saturation_bootup":-1}}']

light_temperature_color.subytype.title = "Subtype"
light_temp_extend_color = description.light_temp_extend_color
light_temp_extend_color.title = "Light: Temperature and Extended Color"
light_temp_extend_color.description = "Light: Temperature and Extended Color: Product with temperature and extended color capabilities"
light_temp_extend_color.example = ['{"type":"ezc.product.light","subtype":5,"driver":{"output":1000},"data_model":{"power_default":1,"power_bootup":-1,"level_default":50,"level_bootup":-1,"color_mode_default":1,"color_mode_bootup":-1,"temperature_default":4000,"temperature_bootup":-1,"temperature_minimum_default":2000,"temperature_maximum_default":9000,"hue_default":180,"hue_bootup":-1,"saturation_default":100,"saturation_bootup":-1,"color_x_default":1,"color_y_default":1}}']
light_temp_extend_color.subytype.title = "Subtype"
light_temp_extend_color.subytype.description = "`5`: Represents Temperature Extended color"
light_temp_extend_color.data_model.update(light_data_model)
light_temp_extend_color.data_model.title = "Light: Temperature and Extended Color: Data Model"
light_temp_extend_color.data_model.description = "Data Model for Light Temperature Extended Color"
light_temp_extend_color.data_model.example = ['{"data_model":{"power_default":1,"power_bootup":-1,"level_default":50,"level_bootup":-1,"color_mode_default":1,"color_mode_bootup":-1,"temperature_default":4000,"temperature_bootup":-1,"temperature_minimum_default":2000,"temperature_maximum_default":9000,"hue_default":180,"hue_bootup":-1,"saturation_default":100,"saturation_bootup":-1,"color_x_default":1,"color_y_default":1}}']
light_temp_extend_color.subytype.title = "Subtype"

productbase = description.productbase
productbase.id.title = "Product ID"
productbase.id.description = "Product ID to distinguish between different products. Should be unique for each product"

# Product -> Socket
socketbase = description.socketbase
socketbase.update(productbase)
socketbase.type.title = "Type"
socketbase.type.description = "Product: `ezc.product.socket`"

driver = socketbase.driver
driver.title = "Socket: Driver Configurations"
driver.description = "Socket driver input and output configurations"
driver.example = ['{"driver":{"input":1000,"input_mode":1,"input_trigger_type":1,"output":1001,"indicator":1002}}']

driver.input.title = "Input"
driver.input.description = "Input driver ID"
driver.input_mode.title = "Input Mode"
driver.input_mode.description = "Input driver mode\n• 0: Push Button\n• 1: Rocker Switch\n"
driver.input_trigger_type.title = "Input Trigger Type"
driver.input_trigger_type.description = "Input trigger type\n• 0: trigger when input/button Press Down\n• 1: trigger when input/button Press Up\n• 2: trigger when input/button Repeat Press\n• 3: trigger when input/button Repeat Press release\n• 4: trigger when input/button single click\n• 5: trigger when input/button double click\n• 6: trigger when input/button long press start\n• 7: trigger when input/button long press hold\n• 8: trigger on/off when rocker switch is pressed\n• 9: trigger toggle when rocker switch is pressed\n"
driver.alternative_input.title = "Alternative Input"
driver.alternative_input.description = "Alternative Input driver ID"
driver.alternative_input_mode.title = "Alternative Input Mode"
driver.alternative_input_mode.description = "Alternative Input driver mode\n• 0: Push Button\n• 1: Rocker Switch\n"
driver.alternative_input_trigger_type.title = "Alternative Input Trigger Type"
driver.alternative_input_trigger_type.description = "Alternative Input trigger type\n• 0: trigger when input/button Press Down\n• 1: trigger when input/button Press Up\n• 2: trigger when input/button Repeat Press\n• 3: trigger when input/button Repeat Press release\n• 4: trigger when input/button single click\n• 5: trigger when input/button double click\n• 6: trigger when input/button long press start\n• 7: trigger when input/button long press hold\n• 8: trigger on/off when rocker switch is pressed\n• 9: trigger toggle when rocker switch is pressed\n"
driver.output.title = "Output"
driver.output.description = "Output driver ID"
driver.indicator.title = "Indicator"
driver.indicator.description = "Indicator driver ID"
driver.hosted.title = "Hosted"
driver.hosted.description = "Whether the product is hosted or not\n• true: hosted product\n• false: non-hosted product"

# Product -> socket datamodel 1
datamodel1 = description.socket_datamodel_1
datamodel1.title = "Socket: On/Off: Data Model"
datamodel1.description = "Datamodel for simple On/Off sockets"
datamodel1.example = ['{"data_model":{"power_default":1,"power_bootup":-1}}']
datamodel1.power_default.title = "Default Power State"
datamodel1.power_default.description = "Default power state of the device\n• 0: Off\n• 1: On\n"

datamodel1.power_bootup.title = "Power State on Boot Up"
datamodel1.power_bootup.description = "Power state of the device when it boots up\n• 0: Always Off\n• 1: Always On\n• 2: Toggle the previous value\n• -1: Previous value\n"

# Product -> socket datamodel 2
datamodel2 = description.socket_datamodel_2
datamodel2.update(datamodel1)
datamodel2.title = "Socket: Dimmable: Data Model"
datamodel2.description = "Datamodel of Dimmable Socket"
datamodel2.example = ['{"data_model":{"power_default":1,"power_bootup":-1,"level_default":50,"level_bootup":50}}']
datamodel2.level_default.title = "Default Level"
datamodel2.level_default.description = "Default level/brightness of the device"
datamodel2.level_bootup.title = "Level/Brightnesss on Bootup"
datamodel2.level_bootup.description = "Level/Brightness of the device when it boots up"

# product -> Socket on off
socket_onoff = description.socket_on_off
socket_onoff.title = "Socket: On/Off"
socket_onoff.description = "Product Description for On/Off Socket"
socket_onoff.example = ['{"type":"ezc.product.socket","subtype":1,"driver":{"input":1000,"input_mode":1,"input_trigger_type":1,"output":1001,"indicator":1002},"data_model":{"power_default":1,"power_bootup":-1}}']
socket_onoff.subytype.title = "Subtype"
socket_onoff.subytype.description = "should be `1` for socket on/off"
socket_onoff.data_model.update(datamodel1)

# product -> Socket Dimmable
socket_dim = description.socket_dimmable
socket_dim.title = "Socket: Dimmable"
socket_dim.description = "Product Description for Dimmable Socket"
socket_dim.example = ['{"type":"ezc.product.socket","subtype":2,"driver":{"input":1000,"input_mode":1,"input_trigger_type":1,"output":1001,"indicator":1002},"data_model":{"power_default":1,"power_bootup":-1,"level_default":50,"level_bootup":50}}']
socket_dim.subytype.title = "Subtype"
socket_dim.subytype.description = "should be `2` for socket dimmable"
socket_dim.data_model.update(datamodel2)

# product -> Switch
switch = description.switch
switch.title = "Switch"
switch.description = "Product Switch description and options"
switch.update(productbase)
switch.example = ['{"type":"ezc.product.switch","subtype":1,"driver":{"input":1000}}']
switch.type.title = "Type"
switch.type.description = "Product: ezc.product.switch"
switch.subytype.title = "Subtype"
switch.subytype.description = "Type of device\n• 1: On Off\n• 2: Dimmer\n• 3: Color Dimmer\n"

driver = switch.driver
driver.title = "Switch: Driver Configurations"
driver.description = "Driver configurations for switch"
driver.example = ['{"driver":{"input":1000}}']
driver.input.title = "Input"
driver.input.description = "Input driver ID"
driver.indicator.title = "Indicator"
driver.indicator.description = "Indicator output ID"
driver.hosted.title = "Hosted"
driver.hosted.description = "Whether the product is hosted or not\n• true: hosted product\n• false: non-hosted product"

# product -> Window Covering
window = description.window_covering
window.title = "Window Covering"
window.description = "Window covering description and configurations"
window.update(productbase)
window.example = ['{"type":"ezc.product.window_covering","subtype":1,"driver":{"output":1002,"input_up":1000,"input_down":1001},"data_model":{"window_covering_type":1}}']
window.type.title = "Type"
window.type.description = "Product window covering: `ezc.product.window_covering`"
window.subtype.title = "Subtype"
window.subtype.description = "1: Position aware lift"

driver = window.driver
driver.title = "Window Covering: Driver Configurations"
driver.description = "Window covering driver configurations"
driver.example = ['{"driver":{"output":1002,"input_up":1000,"input_down":1001}}']
driver.output.title = "Output ID"
driver.output.description = "Output Driver ID"
driver.input_up.title = "Input Up ID"
driver.input_up.description = "Input driver ID for up motion"
driver.input_down.title = "Input Down ID"
driver.input_down.description = "Input driver ID for down motion"
driver.input_stop.title = "Input Stop ID"
driver.input_stop.description = "Input driver ID to stop the motion"
driver.indicator_up.title = "Up Indicator ID"
driver.indicator_up.description = "Output driver ID for indicating up motion"
driver.indicator_down.title = "Down Indicator ID"
driver.indicator_down.description = "Output driver ID for indicating down motion"
driver.indicator_stop.title = "Stop Indicator ID"
driver.indicator_stop.description = "Output driver ID for indicating stop motion"
driver.hosted.title = "Hosted"
driver.hosted.description = "Whether the product is hosted or not\n• true: hosted product\n• false: non-hosted product"

datamodel = window.data_model
datamodel.title = "Window Covering: Data Model"
datamodel.description = "Window covering datamodel configuration for product"
datamodel.example = ['{"data_model":{"window_covering_type":1}}']
datamodel.window_covering_type.title = "Window Covering Type"
datamodel.window_covering_type.description = "Type of window covering\n• 0: Rollershade\n• 1: Rollershade - 2 Motor\n• 2: Rollershade - Exterior\n• 3: Rollershade - Exterior - 2 Motor\n• 4: Curtain/Drapery\n• 5: Awning\n• 6: Shutter\n• 7: Tilt Blind - Tilt only\n• 8: Tilt Blind - Lift and Tilt\n• 9: Projector Screen\n• -1: Other\n"
