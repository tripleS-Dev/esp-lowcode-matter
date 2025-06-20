from typing import Any, List, ClassVar, Union, Literal, Optional
from typing_extensions import Annotated
from pydantic import BaseModel,StrictInt, StrictBool, StrictStr, ValidationError, field_validator, Field, validator, Extra
from pydantic.functional_validators import AfterValidator

from data_handler.var_handler import ID, validate_min_max, check_lightbulb_product_with_lighting_config
from data_handler.base_model import ZeroCodeBaseModel, get_locale

import importlib
locale = get_locale()
module_name = f'product.{locale}.description'
description_module = importlib.import_module(module_name)
description = description_module.description

supported_product = ("ezc.product.light", "ezc.product.socket", "ezc.product.switch", "ezc.product.window_covering", "ezc.product.contact_sensor")

class ProductBaseModel(ZeroCodeBaseModel):
    type: Literal[supported_product]
    #TODO: Check JIRA-EZCH-84 for more details
    id: Optional[StrictInt] = Field(ge=1,le=100,default=1)

# Light Model
class LightBaseModel(ProductBaseModel):
    class Driver(ZeroCodeBaseModel):
        _path = description.light_base_model.driver
        input: Optional[ID] = None
        input_mode: Optional[Literal[(0,1)]] = None
        input_trigger_type: Optional[Literal[0,1,2,3,4,5,6,7,8,9]] = None
        output: ID

    type: Literal["ezc.product.light"]
    driver: Driver = Field(strict=True)

class LightDataModel_1(ZeroCodeBaseModel):
    _path = description.light_on_off.data_model

    power_default: Literal[(0,1)] = Field(default=0)
    power_bootup: StrictInt = Field(ge=-1,le=2,default=0)

class LightDataModel_2(LightDataModel_1):
    _path = description.light_dimmable.data_model

    level_default: StrictInt = Field(ge=0,le=100,default=50)
    level_bootup: StrictInt = Field(ge=-1,le=100,default=-1)

class LightDataModel_3(LightDataModel_2):
    _path = description.light_temperature.data_model

    color_mode_default: StrictInt = Field(ge=1,le=4,default=1)
    color_mode_bootup: Literal[-1,1,2,3,4]
    temperature_default: StrictInt = Field(ge=1500,le=7000,default=4000)
    # TODO: temperature_bootup has -1 as default value, but it cannot be -1 with the specification given
    temperature_bootup: StrictInt = Field(ge=-1,le=7000)
    temperature_minimum_default: StrictInt = Field(ge=1500,default=2200)
    temperature_maximum_default: StrictInt = Field(le=7000,default=7000)

    _check_temperature_min_max = validate_min_max("temperature_minimum_default", "temperature_maximum_default")

class LightDataModel_4(LightDataModel_3):
    _path = description.light_temperature_color.data_model
    _title = "Light Data Model for hue"
    hue_default: StrictInt = Field(ge=0,le=360,default=180)
    hue_bootup: StrictInt = Field(ge=-1,le=360,default=-1)
    saturation_default: StrictInt = Field(ge=0,le=100,default=100)
    saturation_bootup: StrictInt = Field(ge=-1,le=100,default=-1)

class LightDataModel_5(LightDataModel_4):
    _path = description.light_temp_extend_color.data_model

    color_x_default: StrictInt = Field(ge=0,le=100,default=100)
    color_y_default: StrictInt = Field(ge=0,le=100,default=100)

class LightOnOff(LightBaseModel):
    _path = description.light_on_off

    subtype: Literal[1]
    data_model: Optional[LightDataModel_1]

class LightDimmable(LightBaseModel):
    _path = description.light_dimmable
 
    subtype: Literal[2]
    data_model: Optional[LightDataModel_2]

class LightTemperature(LightBaseModel):
    _path = description.light_temperature
 
    subtype: Literal[3]
    data_model: Optional[LightDataModel_3]

class LightTemperatureColor(LightBaseModel):
    _path = description.light_temperature_color
 
    subtype: Literal[4]
    data_model: Optional[LightDataModel_4]

class LightTempExtendColor(LightBaseModel):
    _path = description.light_temp_extend_color
 
    subtype: Literal[5]
    data_model: Optional[LightDataModel_5]

Light = Annotated[Union[LightOnOff, LightDimmable, LightTemperature, LightTemperatureColor, LightTempExtendColor], Field(discriminator='subtype'), AfterValidator(check_lightbulb_product_with_lighting_config)]

# Socket Model
class SocketBaseModel(ProductBaseModel):
    class Driver(ZeroCodeBaseModel):
        _path = description.socketbase.driver
        input: ID
        input_mode: Optional[Literal[(0,1)]] = None
        input_trigger_type: Optional[Literal[0,1,2,3,4,5,6,7,8,9]] = None
        alternative_input: Optional[ID] = None
        alternative_input_mode: Optional[Literal[(0,1)]] = None
        alternative_input_trigger_type: Optional[Literal[0,1,2,3,4,5,6,7,8,9]] = None
        output: ID
        indicator: Optional[ID] = None
        feedback_signal_input: Optional[ID] = None
        trigger_edge: Optional[Literal[0,1,2,3]] = None
        #TODO: Check JIRA-EZCH-84 for more details
        hosted: Optional[StrictBool] = Field(default=False)

    type: Literal['ezc.product.socket']
    driver: Driver = Field(strict=True)

class SocketDataModel_1(ZeroCodeBaseModel):
    _path = description.socket_datamodel_1
    power_default: Literal[(0,1)] = Field(default=0)
    power_bootup: StrictInt = Field(ge=-1,le=2,default=0)

class SocketDataModel_2(SocketDataModel_1):
    _path = description.socket_datamodel_2
    level_default: StrictInt = Field(ge=0,le=100,default=50)
    level_bootup: StrictInt = Field(ge=-1,le=100,default=-1)

class SocketOnOff(SocketBaseModel):
    _path = description.socket_on_off
    subtype: Literal[1]
    data_model: Optional[SocketDataModel_1] = None

class SocketDimmable(SocketBaseModel):
    _path = description.socket_dimmable
    subtype: Literal[2]
    data_model: Optional[SocketDataModel_2] = None

def validate_input_mode_trigger(socket: SocketBaseModel) -> SocketBaseModel:
    if socket.driver.input_mode is None:
        return socket
    if socket.driver.input_trigger_type is None:
        if socket.driver.input_mode == 1:
            raise ValueError("input_trigger_type must be present when input_mode is a Rocker Switch.")
        else:
            return socket
    if socket.driver.input_mode == 1:
        if socket.driver.input_trigger_type is None:
            raise ValueError("input_trigger_type must be present when input_mode is a Rocker Switch")
        if socket.driver.input_trigger_type not in [8, 9]:
            raise ValueError("input_trigger_type must be 8 or 9 when input_mode is a Rocker Switch")
    elif socket.driver.input_mode == 0:
        if socket.driver.input_trigger_type in [8, 9]:
            raise ValueError("input_trigger_type must not be 8 or 9 when input_mode is a Push Button")
    return socket

Socket = Annotated[Union[SocketOnOff, SocketDimmable], Field(discriminator='subtype'), AfterValidator(validate_input_mode_trigger)]

# Switch model
class Switch(ProductBaseModel):
    _path = description.switch
    class Driver(ZeroCodeBaseModel):
        _path = description.switch.driver
        input: ID
        indicator: Optional[ID] = None
        #TODO: Check JIRA-EZCH-84 for more details
        hosted: Optional[StrictBool] = Field(default=False)
    type: Literal['ezc.product.switch']
    subtype: Literal[(1,2,3)]
    driver: Driver

# Window Covering Model
class WindowCovering(ProductBaseModel):
    _path = description.window_covering
    class Driver(ZeroCodeBaseModel):
        _path = description.window_covering.driver
        output: ID
        input_up: Optional[ID] = None
        input_down: Optional[ID] = None
        input_stop: Optional[ID] = None
        indicator_up: Optional[ID] = None
        indicator_down: Optional[ID] = None
        indicator_stop: Optional[ID] = None
        #TODO: Check JIRA-EZCH-84 for more details
        hosted: Optional[StrictBool] = Field(default=False)

    class DataModel(ZeroCodeBaseModel):
        _path = description.window_covering.data_model
        window_covering_type: Literal[-1,0,1,2,3,4,5,6,7,8,9]

    type: Literal["ezc.product.window_covering"]
    subtype: StrictInt = Field(ge=1, le=1)
    driver: Driver = Field(strict=True)
    data_model: Optional[DataModel] = None

class ContactSensor(ProductBaseModel):
    _path = description.contact_sensor
    subtype: Literal[1]
    class Driver(ZeroCodeBaseModel):
        _path = description.contact_sensor.driver
        input: ID

    type: Literal["ezc.product.contact_sensor"]
    driver: Driver = Field(strict=True)

Product = Annotated[Union[Light, Socket, Switch, WindowCovering, ContactSensor], Field(discriminator='type')]
