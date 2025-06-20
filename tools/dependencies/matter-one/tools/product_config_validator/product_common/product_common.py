from typing import Any, Optional, Union, Literal, Set
from typing_extensions import Annotated
from pydantic import BaseModel,StrictInt, StrictFloat, StrictStr, StrictBool, ValidationError, model_validator, field_validator, Field, validator, Extra, confrozenset
from pydantic.functional_validators import AfterValidator

from product_common.indicator_event import Event
from data_handler.var_handler import ID, check_factory_reset_count, check_forced_rollback_count
from data_handler.base_model import ZeroCodeBaseModel, get_locale
from data_handler.mandatory_field import MandatoryField

import importlib
locale = get_locale()
module_name = f'product_common.{locale}.description'
description_module = importlib.import_module(module_name)
description = description_module.description

supported_product_common = ("ezc.product_common.indicator", "ezc.product_common.back_light", "ezc.product_common.light_config", "ezc.product_common.factory_reset", "ezc.product_common.forced_rollback",
                  "ezc.product_common.socket_input_mode", "ezc.product_common.socket_power", "ezc.product_common.socket_config", "ezc.product_common.window_covering_calibration",
                  "ezc.product_common.window_covering_config", "ezc.product_common.advertise_mac", "ezc.product_common.zero_detect", "ezc.product_common.temp_protect")

class ProductCommonBaseModel(ZeroCodeBaseModel):
    type: Literal[supported_product_common]

# Indicator Model
class Indicatorbasemodel(ProductCommonBaseModel):
    _path = description.indicator
    type: Literal["ezc.product_common.indicator"]
    subtype: Literal[0, 1]
    class Config(ZeroCodeBaseModel):
        _path = description.indicator.config
        indicator_setup_timeout_en: Optional[StrictBool] = None
    config: Optional[Config] = None

class IndicatorNonHosted(Indicatorbasemodel):
    _path = description.indicator
    subtype: Literal[0]
    class Driver(ZeroCodeBaseModel):
        _path = description.indicator.driver
        output: ID
    driver: Driver = Field(strict=True)
    events: confrozenset(Event, min_length=1)

class IndicatorHosted(Indicatorbasemodel):
    _path = description.hosted_indicator
    subtype: Literal[1]

Indicator = Annotated[Union[IndicatorNonHosted, IndicatorHosted], Field(discriminator='subtype')]

# background light model
class BackLight(ProductCommonBaseModel):
    _path = description.backlight
    class Driver(ZeroCodeBaseModel):
        _path = description.backlight.driver
        input: Optional[ID] = None
        indicator: ID
        input_trigger_type: Optional[Literal[0,1,2,3,4,5,6,7,8,9]] = None
        exclude_button: Optional[frozenset[ID]] = None

    type: Literal["ezc.product_common.back_light"]
    power_bootup: StrictInt = Field(default=1,ge=-1,le=1)
    driver: Driver = Field(strict=True)

# light config
class LightConfig(ProductCommonBaseModel):
    _path = description.lightconfig

    class Driver(ZeroCodeBaseModel):
        _path = description.lightconfig.light_config
        switch_fade: StrictBool
        color_fade: StrictBool

    type: Literal["ezc.product_common.light_config"]
    light_config: Driver = Field(strict=True)

# Factory Reset BaseModel
class FactoryResetBaseModel(ProductCommonBaseModel):
    type: Literal["ezc.product_common.factory_reset"]
    subtype: Literal[1,2,3]
    immediately_trigger: Optional[StrictBool] = None
    auto_trigger: StrictBool = Field(default=False)

class FactoryResetOnOff(FactoryResetBaseModel):
    _path = description.factory_reset_1
    subtype: Literal[1]
    count: Annotated[StrictInt, Field(ge=3), AfterValidator(check_factory_reset_count)]

class FactoryResetLongPress(FactoryResetBaseModel):
    _path = description.factory_reset_2
    class DriverInput(ZeroCodeBaseModel):
        _path = description.factory_reset_2.driver
        input: ID
        alternative_input: Optional[ID] = None
        exclude_button: Optional[frozenset[ID]] = None
        press_time: Optional[StrictInt] = None

    subtype: Literal[2]
    driver: DriverInput

class FactoryResetHosted(FactoryResetBaseModel):
    _path = description.factory_reset_3
    subtype: Literal[3]

class FactoryResetMultipress(FactoryResetBaseModel):   
    _path = description.factory_reset_4
    class DriverInput(ZeroCodeBaseModel):
        _path = description.factory_reset_4.driver
        input: ID
        alternative_input: Optional[ID] = None
        multi_press_count: Optional[Annotated[StrictInt, Field(ge=2)]] = None

    subtype: Literal[4]
    driver: DriverInput

FactoryReset = Annotated[Union[FactoryResetOnOff, FactoryResetLongPress, FactoryResetHosted, FactoryResetMultipress], Field(title="Factory Reset",discriminator='subtype')]

class ForcedRollback(ProductCommonBaseModel):
    _path = description.forcedrollback
    type: Literal['ezc.product_common.forced_rollback']
    subtype: Literal[1]
    count: Annotated[StrictInt, Field(gt=3), AfterValidator(check_forced_rollback_count)]

class SocketInputMode(ProductCommonBaseModel):
    _path = description.socketinput
    class Driver(ZeroCodeBaseModel):
        _path = description.socketinput.driver
        input: ID

    type: Literal['ezc.product_common.socket_input_mode']
    driver: Driver = Field(strict=True)

class SocketPower(ProductCommonBaseModel):
    _path = description.socketpower
    class Driver(ZeroCodeBaseModel):
        _path = description.socketpower.driver
        input: ID
        input_mode: Optional[Literal[(0,1)]] = None
        input_trigger_type: Optional[Literal[0,1,2,3,4,5,6,7,8,9]] = None
        indicator: Optional[ID] = None

        @model_validator(mode='after')
        def validate_input_mode_trigger(self) -> 'Driver':
            if self.input_mode is None:
                return self
            if self.input_trigger_type is None:
                if self.input_mode == 1:
                    raise ValueError("input_trigger_type must be present when input_mode is a Rocker Switch.")
                else:
                    return self
            if self.input_mode == 0:
                if self.input_trigger_type in [8, 9]:
                    raise ValueError("input_trigger_type must not be 8 or 9 when input_mode is a Push Button")
            elif self.input_mode == 1:
                if self.input_trigger_type not in [8, 9]:
                    raise ValueError("input_trigger_type must be 8 or 9 when input_mode is a Rocker Switch")
            return self

    type: Literal['ezc.product_common.socket_power']
    driver: Driver = Field(strict=True)

class SocketConfig(ProductCommonBaseModel):
    _path = description.socketconfig
    type: Literal['ezc.product_common.socket_config']
    update_driver: StrictBool = Field(default=True)

class WindowCoveringCalibration(ProductCommonBaseModel):
    _path = description.window_covering_calib
    class Driver(ZeroCodeBaseModel):
        _path = description.window_covering_calib.driver
        enter_cali_input_trigger_type: Literal[0, 6]
        enter_calibration: frozenset[ID]
        enter_cali_exclude_button: Optional[frozenset[ID]] = None
        restore_default_input_trigger_type: Optional[Literal[0, 6]] = None
        restore_default: Optional[frozenset[ID]] = None
        restore_default_exclude_button: Optional[frozenset[ID]] = None

    type: Literal['ezc.product_common.window_covering_calibration']
    driver: Driver

class WindowCoveringConfig(ProductCommonBaseModel):
    _path = description.window_covering_config
    class Config(ZeroCodeBaseModel):
        _path = description.window_covering_config.window_covering_config
        update_driver: StrictBool = Field(default=True)
        set_defaults_when_poweron: Optional[StrictBool] = None
        indicator_off_end: Optional[StrictBool] = None
        stop_indicator_off_delay_time_ms: Optional[StrictInt] = None

    type: Literal['ezc.product_common.window_covering_config']
    window_covering_config: Config = Field(Strict=True)

class TempProtect(ProductCommonBaseModel):
    _path = description.tempprotect
    type: Literal['ezc.product_common.temp_protect']
    input: ID
    normal_temp: Optional[StrictFloat] = None
    warn_temp: Optional[StrictFloat] = None
    protect_temp: Optional[StrictFloat] = None
    normal_behaviors: Optional[Literal[0,1,2,3]] = None
    warn_behaviors: Optional[Literal[0,1,2,3]] = None
    protect_behaviors: Optional[Literal[0,1,2,3]] = None
    normal_sample_interval: Optional[StrictInt] = None
    fast_sample_interval: Optional[StrictInt] = None
    normal_sample_count: Optional[StrictInt] = None
    fast_sample_count: Optional[StrictInt] = None

class AdvertiseMac(ProductCommonBaseModel):
    _path = description.advertise_mac
    type: Literal['ezc.product_common.advertise_mac']
    subtype: Literal[1]
    count: StrictInt = Field(gt=0)

class ZeroDetect(ProductCommonBaseModel):
    _path = description.zerodetect
    class Driver(ZeroCodeBaseModel):
        _path = description.zerodetect.driver
        zero_detect: ID
        invalid_behaviors: StrictInt = Field(ge=0,le=3)
        lost_signal: StrictInt = Field(ge=0,le=3)
        delay_us: Optional[StrictInt] = Field(ge=0,le=10000,default=0)

    type: Literal['ezc.product_common.zero_detect']
    driver: Driver

ProductCommon = Annotated[Union[Indicator, BackLight, LightConfig, FactoryReset, ForcedRollback, SocketInputMode, SocketPower, SocketConfig, WindowCoveringCalibration, WindowCoveringConfig, AdvertiseMac, ZeroDetect, TempProtect], Field(discriminator='type')]
