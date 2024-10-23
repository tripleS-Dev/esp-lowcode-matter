from pydantic import StrictInt, StrictStr, ValidationError, model_validator, Field
from typing import Any
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated
from enum import Enum
import json

# common dictionary with key:id and value:gpio
dict_id_gpio = dict()
out_gpio = list()
temp_id = int()
factory_reset_count, forced_rollback_count = None, None 
light_combination, peripheral_type, light_product_subtype = None, None, None

light_gpio = {
    'r' : None,
    'g' : None,
    'b' : None,
    'c' : None,
    'w' : None
}

# This is taken from https://github.com/espressif/esp-iot-solution/blob/master/components/led/lightbulb_driver/include/lightbulb.h file. 
# If that file is updated, this should be updated accordingly.
class beads_comb(Enum):
    C = 1
    W = 2
    CW = 3
    RGB = 4
    RGBC_4CH = 5
    RGBCC_4CH = 6
    RGBW_4CH = 7
    RGBWW_4CH = 8
    RGBCW_5CH = 9
    RGBCC_5CH = 10
    RGBWW_5CH = 11
    RGBC_5CH = 12
    RGBW_5CH = 13

def reset_data_handler_var():
    dict_id_gpio.clear()
    temp_id = int()

# checks if the id is already in use, if not then add it to the valid_id
def add_id(id: StrictInt) -> StrictInt:
    if id in dict_id_gpio.keys():
        raise ValueError("The following id: {} is already in use".format(id))
    global temp_id
    temp_id = id
    if temp_id not in dict_id_gpio.keys():
        dict_id_gpio[temp_id] = []
    return id

# checks if id is valid from dict_id_gpio
def check_id(id: StrictInt) -> StrictInt:
    if id is None:
        return id
    if id not in dict_id_gpio.keys():
        raise ValueError("The following id: {} have no drivers associated with it".format(id))
    return id

# common ID model to validate and constraint the value
ID = Annotated[StrictInt, Field(ge=1000,le=1999), AfterValidator(check_id)]

# checks if the gpio is already in use with some other drivers or not
def add_gpio(gpio_pin: StrictInt) -> StrictInt:
    for key,value in dict_id_gpio.items():
        if gpio_pin in value:
            raise ValueError("The following gpio_pin: {} is already in use by the id: {}".format(gpio_pin, key))
    if temp_id in dict_id_gpio.keys():
        dict_id_gpio[temp_id].append(gpio_pin)
    else:
        dict_id_gpio[temp_id] = [gpio_pin]
    return gpio_pin

# common GPIO Pin model, to validate if the gpio is not already used
GPIOPin = Annotated[StrictInt, Field(ge=0), AfterValidator(add_gpio)]

# model validator to check if minimum field is less than the maximum field
def check_min_max(data: Any, min: str, max: str) -> Any:
    if data[min] >= data[max]:
        return ValueError("The {} should be less than {}".format(min, max))
    return data

# returns the model validator which calls the check_min_max
def validate_min_max(min: str, max: str):
    return model_validator(mode='before')(lambda v: check_min_max(v, min, max))

# check validity of the specified number of counts
def check_power_cycle_count_validity():
    if factory_reset_count != None and forced_rollback_count != None:
        if forced_rollback_count <= factory_reset_count:
            raise ValueError("'count' in Forced Rollback must be greater than 'count' in Factory Reset")

# set the global factory_reset_count variable to the specified counts
def check_factory_reset_count(count : StrictInt) -> StrictInt:
    global factory_reset_count
    factory_reset_count = count
    check_power_cycle_count_validity()
    return count

# set the global forced_rollback_count variable to the specified counts
def check_forced_rollback_count(count : StrictInt) -> StrictInt:
    global forced_rollback_count
    forced_rollback_count = count
    check_power_cycle_count_validity()
    return count

def validate_lightbulb_pins(rgb_used : bool, c_used : bool, w_used : bool):
    if light_gpio['r'] == None or light_gpio['g'] == None or light_gpio['b'] == None or light_gpio['c'] == None or light_gpio['w'] == None or light_combination == None:
        return
    
    if rgb_used:
        if light_gpio['r'] == -1 or light_gpio['g'] == -1 or light_gpio['b'] == -1 :
            raise ValueError("Red, Green and Blue pin fields should have a valid pin specified as the selected light configuration is of type {}".format(beads_comb(light_combination).name))
        else:
            out_gpio.append(light_gpio['r'])
            out_gpio.append(light_gpio['g'])
            out_gpio.append(light_gpio['b'])
    else :
        if light_gpio['r'] != -1 or light_gpio['g'] != -1 or light_gpio['b'] != -1:
            raise ValueError("Red, Green and Blue pin fields should be set to '-1', these are not present in the light as the selected light configuration is of type {}.".format(beads_comb(light_combination).name))
    
    if c_used:
        if light_gpio['c'] == -1:
            raise ValueError("Cold/CCT pin field should have a valid pin specified as the selected light configuration is of type {}".format(beads_comb(light_combination).name))
        else:
            out_gpio.append(light_gpio['c'])
    else:
        if light_gpio['c'] != -1:
            raise ValueError("Cold/CCT pin field should be set to `-1`, it is not present in the light as the selected light configuration is of type {}".format(beads_comb(light_combination).name))
    
    if w_used:
        if light_gpio['w'] == -1:
            raise ValueError("Warm/Brightness pin field should have a valid pin specified as the selected light configuration is of type {}".format(beads_comb(light_combination).name))
        else:
            out_gpio.append(light_gpio['w'])
    else:
        if light_gpio['w'] != -1:
            raise ValueError("Warm/Brightness pin field should be set to `-1`, it is not present in the light as the selected light configuration is of type {}".format(beads_comb(light_combination).name))

def get_used_colors_in_lightbulb():
    if light_combination == None:
        return

    if light_combination <= 3:
        rgb_used = False
    else:
        rgb_used = True
    
    if light_combination == beads_comb.W.value or light_combination == beads_comb.RGB.value or light_combination == beads_comb.RGBW_4CH.value or light_combination == beads_comb.RGBWW_4CH.value or light_combination == beads_comb.RGBW_5CH.value:
        c_used = False
    else:
        c_used = True
    
    if light_combination == beads_comb.C.value or light_combination == beads_comb.RGB.value or light_combination == beads_comb.RGBC_4CH.value or light_combination == beads_comb.RGBCC_4CH.value or light_combination == beads_comb.RGBC_5CH.value:
        w_used = False
    else :
        w_used = True

    return rgb_used, c_used, w_used

def check_gpio_with_light_combination():
    if peripheral_type == None:
        return
    
    rgb_used, c_used, w_used = get_used_colors_in_lightbulb()
    validate_lightbulb_pins(rgb_used, c_used, w_used)
    
    if peripheral_type == 'PWM':
        for items in out_gpio:
            add_gpio(items)
    elif peripheral_type == 'I2C' and len(out_gpio) != len(set(out_gpio)):
        raise ValueError("The same pin is assigned to multiple outputs for different colors. Please assign a unique pin for each color output.")
        

def set_lightbulb_pin(value : StrictInt, key : str) -> StrictInt:
    color = None
    if key == 'gpio_red' or key == 'out_red':
        color = key.split('_')[1][0]
    elif key == 'gpio_green' or key == 'out_green':
        color = key.split('_')[1][0]
    elif key == 'gpio_blue' or key == 'out_blue':
        color = key.split('_')[1][0]
    elif key == 'gpio_cold_or_cct' or key == 'out_cold':
        color = key.split('_')[1][0]
    elif key == 'gpio_warm_or_brightness' or key == 'out_warm':
        color = key.split('_')[1][0]
    if color != None:
        light_gpio[color] = value

def check_lightbulb_output_config(type : str):
    global peripheral_type
    peripheral_type = type
    check_gpio_with_light_combination()

def check_light_product():
    if light_combination == None or light_product_subtype == None:
        return   
    err = False
    if light_combination == beads_comb.C.value or light_combination == beads_comb.W.value:
        if  light_product_subtype >= 3:
            err = True
    elif light_combination == beads_comb.CW.value:
        if  light_product_subtype >= 4:
            err = True
    elif light_combination == beads_comb.RGB.value:
        if light_product_subtype == 3:
            err = True  
    if err:
        raise ValueError("Product subtype should be compatible with the selected light configuration which is of type {}.".format(beads_comb(light_combination).name))   
    return

def check_lightbulb_product_with_lighting_config(data : StrictInt):
    global light_product_subtype
    light_product_subtype = data.subtype
    check_light_product()
    return data

def check_lighting_config(_light_combination : StrictInt) -> StrictInt:
    global light_combination
    light_combination = _light_combination
    check_gpio_with_light_combination()
    return _light_combination

def check_color_select(color_selected : int):
    if light_combination == None:
        return
    if color_selected == 1 and light_combination <= beads_comb.CW.value:
        raise ValueError("Color selected should be 2 as the configured light hardware does not contain RGB lights")
    elif color_selected == 2 and light_combination == beads_comb.RGB.value:
        raise ValueError("Color selected should be 1 as the configured light hardware does not contain C or W lights")

def check_color_map_str(color_map: StrictStr):
    try:
        color_map_array = json.loads(color_map)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON format") from e

    for row in color_map_array:
        if len(row) != 16:
            raise ValueError("Each row must contain 16 elements")
        
        hue_value = row[0]
        if not (0 <= hue_value <= 359 and isinstance(hue_value, int)):
            raise ValueError(f"Hue value error: {hue_value} is not an integer between 0 and 359")

        for i, value in enumerate(row[1:], start=1):
            if not (0 <= value <= 1):
                raise ValueError(f"Color tuning value at index {i}: {value} out of range which should be a float value between 0 to 1")
            if 0 < value < 1:
                if not (isinstance(value, float) and round(value, 4) == value):
                    raise ValueError(f"Color tuning value at index {i}: {value} error")              