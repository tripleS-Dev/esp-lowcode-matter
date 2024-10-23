from typing import Any, Optional, ClassVar, Union, Literal
from typing_extensions import Annotated
from pydantic import BaseModel,StrictInt, StrictStr, StrictBool, ValidationError, model_validator, field_validator, Field, validator, Extra

from data_handler.var_handler import validate_min_max, check_color_select
from data_handler.base_model import ZeroCodeBaseModel, get_locale

import importlib
locale = get_locale()
module_name = f'product_common.{locale}.description'
description_module = importlib.import_module(module_name)
description = description_module.description

# TODO: get clarity on what is optional and what is not and make sure that different events are supported in different Event
supported_events_name = ("setup_mode_start", "setup_mode_end", "setup_started", "setup_successful", "setup_failed", "identification_start", "identification_stop", "identification_blink", "identification_breathe", "identification_okay", "identification_channel_change", "identification_finish_effect", "identification_stop_effect",
                         "factory_reset_triggered", "forced_rollback_triggered", "driver_mode", "test_mode_start", "test_mode_complete", "test_mode_ble", "advertise_self_mac_trigged", "ready", "network_connected", "network_disconnected","normal_temp", "warn_temp", "protect_temp")

class EventBaseModel(ZeroCodeBaseModel):
    name: Literal[supported_events_name]
    mode: StrictStr

# handles `restore` event model
class EventRestore(EventBaseModel):
    _path = description.event_restore
    mode: Literal["restore"]

class EventColorRGB(ZeroCodeBaseModel):
    color_select: Literal[1]
    r: StrictInt = Field(ge=0,le=255)
    g: StrictInt = Field(ge=0,le=255)
    b: StrictInt = Field(ge=0,le=255)

    @model_validator(mode='before')
    @classmethod
    def check_color_selection(cls, data: Any) -> Any:
        check_color_select(1)
        return data

class EventColorCCT(ZeroCodeBaseModel):
    color_select: Literal[2]
    cct: StrictInt = Field(ge=0,default=50,le=10000)

    @model_validator(mode='before')
    @classmethod
    def check_color_selection(cls, data: Any) -> Any:
        check_color_select(2)
        return data

# handles `solid` event model
class EventSolidBaseModel(EventBaseModel):
    mode: Literal["solid"]
    max_brightness: Optional[StrictInt] = Field(ge=0, le=100)

class EventSolidRGB(EventSolidBaseModel,EventColorRGB):
    _path = description.solid_rgb
    pass
class EventSolidCCT(EventSolidBaseModel,EventColorCCT):
    _path = description.solid_cct
    pass

EventSolid = Annotated[Union[EventSolidRGB, EventSolidCCT], Field(discriminator="color_select")]

# handles `blink` and `breathe` event model
class EventBlinkBreatheBaseModel(EventBaseModel):
    mode: Literal["blink", "breathe"] 
    speed: Optional[StrictInt] = Field(ge=0)
    min_brightness: StrictInt = Field(ge=0, le=100)
    max_brightness: StrictInt = Field(ge=0, le=100)
    total_ms: Optional[StrictInt] = Field(ge=0)
    interrupt_forbidden: Optional[StrictBool] = None

    _check_brightness = validate_min_max("min_brightness", "max_brightness")

class EventBlinkBreatheRGB(EventBlinkBreatheBaseModel,EventColorRGB):
    _path = description.blink_breathe_rgb
    pass
class EventBlinkBreatheCCT(EventBlinkBreatheBaseModel,EventColorCCT):
    _path = description.blink_breathe_cct
    pass

EventBlinkBreathe = Annotated[Union[EventBlinkBreatheRGB, EventBlinkBreatheCCT], Field(discriminator="color_select")]

# Global Event annotated class
Event = Annotated[Union[EventRestore, EventSolid, EventBlinkBreathe], Field(discriminator='mode')]
