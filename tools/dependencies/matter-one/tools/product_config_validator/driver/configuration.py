from typing import Any, Optional, Literal, Union, List, Tuple
from pydantic import BaseModel, StrictInt, StrictBool, StrictStr, StrictFloat, ValidationError, model_validator, field_validator, Field, validator
from typing_extensions import Annotated, Self
from pydantic.functional_validators import AfterValidator
from functools import partial

from data_handler.var_handler import GPIOPin, validate_min_max, set_lightbulb_pin, check_lightbulb_output_config, check_lighting_config, check_color_map_str
from data_handler.base_model import ZeroCodeBaseModel, get_locale

import importlib
locale = get_locale()
module_name = f'driver.{locale}.description'
description_module = importlib.import_module(module_name)
description = description_module.description

class GPIOCfg(ZeroCodeBaseModel):
    gpio_num: GPIOPin
    active_level: Literal[(0,1)]

class GPIOCfgRelay(GPIOCfg):
    _path = description.relay_driver.relay_gpio.gpio_config
    # gpio_num: GPIOPin
    # active_level: Literal[(0,1)]

class HostedCfgRelay(ZeroCodeBaseModel):
    _path = description.relay_driver.relay_hosted.hosted_config
    uart_driver_id: StrictInt = Field(ge=0,le=255,default=30)

class led_GPIOCfg(GPIOCfg):
    _path = description.led_driver.led_gpio.gpio_config
    # gpio_num: GPIOPin
    # active_level: Literal[(0,1)]

class GPIOCfgButton(GPIOCfg):
    _path = description.button.gpio_driver.config
    long_press_time: StrictInt = Field(ge=0,le=65535,default=5)

class ADCCfgButton(ZeroCodeBaseModel):
    _path = description.button.adc_driver.config
    adc_channel: StrictInt = Field(ge=0,le=32,default=5)
    button_index: StrictInt = Field(ge=0,le=32,default=5)
    min: StrictInt = Field(ge=0,le=65535,default=5)
    max: StrictInt = Field(ge=0,le=65535,default=5)
    long_press_time: StrictInt = Field(ge=0,le=65535,default=5)

class HostedCfgButton(ZeroCodeBaseModel):
    _path = description.button_driver.button_hosted.config
    uart_driver_id: StrictInt = Field(ge=0,le=255,default=30)

class OnChipCfgTempSensor(ZeroCodeBaseModel):
    _path = description.tempsensor_driver.onchip_driver.onchip_config
    range_min: StrictInt = Field(ge=-40,le=500,default=-40)
    range_max: StrictInt = Field(ge=-40,le=500,default=125)

class NTCCfgTempSensor(ZeroCodeBaseModel):
    _path = description.tempsensor_driver.ntc_driver.ntc_config
    b_value: StrictInt = Field(ge=0,le=65535,default=3950)
    r25_ohm: StrictInt = Field(ge=0,le=65535,default=10000)
    fixed_ohm: StrictInt = Field(ge=0,le=65535,default=10000)
    vdd_mv: StrictInt = Field(ge=0,le=65535,default=3300)
    circuit_mode: StrictInt = Field(ge=1,le=2,default=1)
    atten: StrictInt = Field(ge=0,le=65535,default=3)
    unit: StrictInt = Field(ge=0,le=65535,default=0)
    channel: StrictInt = Field(ge=0,le=65535,default=3)

class HostedCfgRoller(ZeroCodeBaseModel):
    _path = description.roller_blind_driver.roller_blind_hosted.hosted_config
    uart_driver_id: StrictInt = Field(ge=0,le=255,default=30)

class RollerBlindCalibrationCfg_1(ZeroCodeBaseModel):
    _path = description.roller_blind_driver.roller_blind_gpio.roller_blind_auto_calib_driver.calibration_config
    calibration_type: Literal[1]
    detect_gpio: GPIOPin
    detection_frequency: StrictInt = Field(ge=0)
    detection_frequency_offset: StrictInt = Field(ge=0)

class RollerBlindCalibrationCfg_2(ZeroCodeBaseModel):
    _path = description.roller_blind_driver.roller_blind_gpio.roller_blind_manual_calib_driver.calibration_config
    calibration_type: Literal[2]

class RollerBlindGPIOCfg(ZeroCodeBaseModel):
    _path = description.roller_blind_driver.roller_blind_gpio.gpio_config
    up_relay_gpio: GPIOPin
    up_relay_active_level: Optional[Literal[1,2]] = None
    down_relay_gpio: GPIOPin
    down_relay_active_level: Optional[Literal[1,2]] = None

class RollerBlindCfg(ZeroCodeBaseModel):
    _path = description.roller_blind_driver.roller_blind_gpio.roller_blind_config
    allow_reverse_in_moving: StrictBool
    pause_between_moves: StrictBool
    delay_time_between_moves_ms: StrictInt = Field(ge=0,le=65535,default=0)
    relay_control_delay_time_ms: StrictInt = Field(ge=0,le=65535,default=0)
    default_max_move_time_ms: StrictInt = Field(ge=0,le=214748364)
    use_default_time_when_not_calibrated: Optional[StrictBool] = None
    move_time_compensation_percent: Optional[StrictInt] = None

# TODO: Add some checks based on beads_comb, color_mode, color_select, etc
class LightCfg(ZeroCodeBaseModel):
    _path = description.led_non_gpio.lighting_config
    enable_gradient: StrictBool
    enable_memory: StrictBool
    enable_lowpower: StrictBool
    sync_change_brightness: StrictBool
    disable_auto_on: StrictBool
    beads_comb: Annotated[Literal[1,2,3,4,5,6,7,8,9,10,11,12,13], AfterValidator(check_lighting_config)]
    fades_ms: StrictInt = Field(gt=0)
    enable_precise_cct_control: Optional[StrictBool] = None
    enable_precise_color_control: Optional[StrictBool] = None
    cct_kelvin_min: Optional[StrictInt] = None
    cct_kelvin_max: Optional[StrictInt] = None

class HardwareCfg(ZeroCodeBaseModel):
    _path = description.led_non_gpio.hardware_config
    white_min: StrictInt = Field(ge=0)
    white_max: StrictInt = Field(le=100)
    white_power_max: StrictInt = Field(ge=100,le=200)
    rgb_min: StrictInt = Field(ge=0)
    rgb_max: StrictInt = Field(le=100)
    rgb_power_max: StrictInt = Field(ge=100,le=300)

    _check_white_min_max = validate_min_max("white_min", "white_max")
    _check_rgb_min_max = validate_min_max("rgb_min", "rgb_max")

# TODO: verify if the min value of gamma_* is 60 or 80(as per docs)
class GammaCfg(ZeroCodeBaseModel):
    _path = description.led_non_gpio.gamma_config
    enable_gamma_adjust: StrictBool
    gamma_red: StrictInt = Field(ge=50,le=100)
    gamma_green: StrictInt = Field(ge=50,le=100)
    gamma_blue: StrictInt = Field(ge=50,le=100)
    gamma_cold: StrictInt = Field(ge=50,le=100)
    gamma_warm: StrictInt = Field(ge=50,le=100)
    curve_coe: StrictFloat = Field(default=None,ge=0.8,le=2.2)

class CCTMapEntry(BaseModel):
    cct: StrictInt = Field(ge=0,le=10000)
    cct_percentage: StrictInt = Field(ge=0,le=100)
    red: StrictFloat = Field(ge=0.0,le=1.0)
    green: StrictFloat = Field(ge=0.0,le=1.0)
    blue: StrictFloat = Field(ge=0.0,le=1.0)
    cold: StrictFloat = Field(ge=0.0,le=1.0)
    warm: StrictFloat = Field(ge=0.0,le=1.0)

class CctMapCfg(ZeroCodeBaseModel):
    _path = description.led_non_gpio.cctmap_cfg
    table: List[Tuple[StrictInt, StrictInt, StrictFloat, StrictFloat, StrictFloat, StrictFloat, StrictFloat]]

    def __hash__(self):
        # Hash the tuple representation of the table
        return hash(tuple(self.table))

class ColorMapCfg(ZeroCodeBaseModel):
    _path = description.led_non_gpio.colormap_cfg
    table: StrictStr

    @model_validator(mode='before')
    @classmethod
    def check_color_map_data(cls, data: Any) -> Any:
        for key, value in data.items():
            check_color_map_str(value)
        return data

class PWMCfg(ZeroCodeBaseModel):
    _path = description.led_driver.pwm_driver.pwm_config
    invert_level: Optional[StrictBool] = None
    pwm_hz: StrictInt = Field(ge=1000,le=20000)
    temperature_mode: Literal[(0,1)]
    phase_delay: Optional[Literal[(0, 1, 2, 4)]] = None
    gpio_red: StrictInt = Field(ge=-1)
    gpio_green: StrictInt = Field(ge=-1)
    gpio_blue: StrictInt = Field(ge=-1)
    gpio_cold_or_cct: StrictInt = Field(ge=-1)
    gpio_warm_or_brightness: StrictInt = Field(ge=-1)

    @model_validator(mode='before')
    @classmethod
    def check_light_bulb_pins(cls, data: Any) -> Any:
        for key, value in data.items():
            set_lightbulb_pin(value, key)
        check_lightbulb_output_config('PWM')
        return data

class WS2812Cfg(ZeroCodeBaseModel):
    _path = description.led_driver.ws2812_driver.ws2812_config
    led_num: StrictInt = Field(ge=1)
    ctrl_io: GPIOPin

class I2CBaseCfg(ZeroCodeBaseModel):
    gpio_clock: GPIOPin
    gpio_sda: GPIOPin
    iic_khz: StrictInt = Field(gt=0)
    out_red: Literal[-1, 0, 1, 2, 3, 4]
    out_green: Literal[-1, 0, 1, 2, 3, 4]
    out_blue: Literal[-1, 0, 1, 2, 3, 4]
    out_cold: Literal[-1, 0, 1, 2, 3, 4]
    out_warm: Literal[-1, 0, 1, 2, 3, 4]

    @model_validator(mode='before')
    @classmethod
    def check_light_bulb_pins(cls, data: Any) -> Any:
        for key, value in data.items():
            set_lightbulb_pin(value, key)
        check_lightbulb_output_config('I2C')
        return data

# TODO: verify if the steps value here is even valid, since some values do not match the documentation
class SM2135ECfg(I2CBaseCfg):
    _path = description.led_driver.sm2135e_driver.sm2135e_config
    white_current_max: StrictInt = Field(ge=10,le=60,multiple_of=5)
    rgb_current_max: StrictInt = Field(ge=10,le=50,multiple_of=5)

sm2135eh_white_current_max = list()
for i in range(0,56,5):
    sm2135eh_white_current_max.append(i)
for i in range(59,73,4):
    sm2135eh_white_current_max.append(i)

class SM2135EHCfg(I2CBaseCfg):
    _path = description.led_driver.sm2135eh_driver.sm2135eh_config
    white_current_max: Literal[tuple(sm2135eh_white_current_max)]
    rgb_current_max: StrictInt = Field(ge=4,le=64,multiple_of=4)

class SM2235EGHCfg(I2CBaseCfg):
    _path = description.led_driver.sm2235egh_driver.sm2235egh_config
    white_current_max: StrictInt = Field(ge=5,le=80,multiple_of=5)
    rgb_current_max: StrictInt = Field(ge=4,le=64,multiple_of=4)

class SM2335EGHCfg(I2CBaseCfg):
    _path = description.led_driver.sm2335egh_driver.sm2335egh_config
    white_current_max: StrictInt = Field(ge=5,le=80,multiple_of=5)
    rgb_current_max: StrictInt = Field(ge=10,le=160,multiple_of=10)

class BP5758DCfg(I2CBaseCfg):
    _path = description.led_driver.bp5758d_driver.bp5758d_config
    out1_current_max: StrictInt = Field(gt=0,le=90)
    out2_current_max: StrictInt = Field(gt=0,le=90)
    out3_current_max: StrictInt = Field(gt=0,le=90)
    out4_current_max: StrictInt = Field(gt=0,le=90)
    out5_current_max: StrictInt = Field(gt=0,le=90)

class BP1658CJCfg(I2CBaseCfg):
    _path = description.led_driver.bp1658cj_driver.bp1658cj_config
    white_current_max: StrictInt = Field(ge=0,le=75,multiple_of=5)
    rgb_current_max: StrictInt = Field(ge=0,le=150,multiple_of=10)
