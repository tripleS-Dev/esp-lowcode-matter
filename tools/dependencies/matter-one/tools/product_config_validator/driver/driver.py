from typing import Any, List, ClassVar, Union, Literal
from typing_extensions import Annotated
from pydantic import BaseModel,StrictInt, StrictStr, ValidationError, model_validator, field_validator, Field, validator, Extra
from driver.configuration import *
from data_handler.var_handler import add_id
from data_handler.base_model import ZeroCodeBaseModel, get_locale

import importlib
locale = get_locale()
module_name = f'driver.{locale}.description'
description_module = importlib.import_module(module_name)
description = description_module.description

supported_drivers = ("ezc.driver.button", "ezc.driver.relay", "ezc.driver.roller_blind", "ezc.driver.led", "ezc.driver.zero_detect", "ezc.driver.temp_sensor", "ezc.driver.contact_sensor")
supported_led_drivers = ("ws2812", "pwm", "bp5758d", "sm2135e", "sm2135eh", "sm2235egh", "sm2335egh", "bp1658cj", "gpio", "kp18058")
supported_temp_sensor_drivers = ("onchip", "ntc")

# Contains common items of all the Drivers
class DriverBaseModel(ZeroCodeBaseModel):
    id: StrictInt = Field(ge=1000, le=1999)
    type: Literal[supported_drivers]
    name: StrictStr

    # Add id to the list of valid_id
    _add_id = validator('id', allow_reuse=True)(add_id)

# Button Driver Model
class ButtonBaseDriver(DriverBaseModel):
    type: Literal['ezc.driver.button']
    name: Literal['gpio', 'adc', 'hosted']

class ButtonGPIODriver(ButtonBaseDriver):
    _path = description.button.gpio_driver
    name: Literal['gpio']
    gpio_config: GPIOCfgButton = Field(strict=True)

class ButtonADCDriver(ButtonBaseDriver):
    _path = description.button.adc_driver
    name: Literal['adc']
    adc_config: ADCCfgButton = Field(strict=True)

# Button Driver based on hosted
class ButtonHostedDriver(ButtonBaseDriver):
    _path = description.button_driver.button_hosted
    name: Literal['hosted']
    hosted_config: HostedCfgButton = Field(strict=True)

ButtonDriver = Annotated[Union[ButtonGPIODriver, ButtonADCDriver, ButtonHostedDriver], Field(title='ButtonDriver',discriminator='name')]

# Relay Driver Model
class RelayBaseDriver(DriverBaseModel):
    type: Literal['ezc.driver.relay']
    name: Literal['gpio', 'hosted']

# Relay Driver based on gpio
class RelayGPIODriver(RelayBaseDriver):
    _path = description.relay_driver.relay_gpio
    name: Literal['gpio']
    gpio_config: GPIOCfgRelay = Field(strict=True)

# Relay Driver based on hosted
class RelayHostedDriver(RelayBaseDriver):
    _path = description.relay_driver.relay_hosted
    name: Literal['hosted']
    hosted_config: HostedCfgRelay = Field(strict=True)

RelayDriver = Annotated[Union[RelayGPIODriver, RelayHostedDriver], Field(title='RelayDriver',discriminator='name')]

# Zero Detect Driver Model
class ZeroDetectDriver(DriverBaseModel):
    _path = description.zerodetect_driver
    type: Literal['ezc.driver.zero_detect']
    name: Literal['gpio', 'mcpwm']
    capture_gpio_num: GPIOPin
    zero_signal_type: Literal[(0,1)]
    max_freq_hz: StrictInt = Field(ge=10,le=200)
    min_freq_hz: StrictInt = Field(ge=10,le=200)
    valid_times: StrictInt = Field(ge=0,le=200)
    invalid_times: StrictInt = Field(ge=0,le=200)
    signal_lost_time_us: StrictInt = Field(ge=1,le=18446744073709551615)

# Temp Sensor Driver Model
class TempSensorBaseDriver(DriverBaseModel):
    type: Literal['ezc.driver.temp_sensor']
    name: Literal[supported_temp_sensor_drivers]

class TempSensorOnChipDriver(TempSensorBaseDriver):
    _path = description.tempsensor_driver.onchip_driver
    name: Literal['onchip']
    onchip_config: OnChipCfgTempSensor = Field(strict=True)

class TempSensorNTCDriver(TempSensorBaseDriver):
    _path = description.tempsensor_driver.ntc_driver
    name: Literal['ntc']
    ntc_config: NTCCfgTempSensor = Field(strict=True)

TempSensorDriver = Annotated[Union[TempSensorOnChipDriver, TempSensorNTCDriver], Field(title='TempSensorDriver',discriminator='name')]

# Roller Blind Driver Model
class RollerBlindDriverBaseModel(DriverBaseModel):
    type: Literal['ezc.driver.roller_blind']
    name: Literal['gpio', 'hosted']

RollerBlindCalibrationCfg = Annotated[Union[RollerBlindCalibrationCfg_1, RollerBlindCalibrationCfg_2], Field(...,discriminator='calibration_type')]

class RollerBlindGPIODriver(RollerBlindDriverBaseModel):
    _path = description.roller_blind_driver.roller_blind_gpio
    name: Literal['gpio']
    gpio_config: RollerBlindGPIOCfg
    roller_blind_config: RollerBlindCfg
    calibration_config: RollerBlindCalibrationCfg

class RollerBlindHostedDriver(RollerBlindDriverBaseModel):
    _path = description.roller_blind_driver.roller_blind_hosted
    name: Literal['hosted']
    # ToDo: Add hosted config to generic across multiple hosted drivers
    hosted_config: HostedCfgRoller = Field(strict=True)

RollerBlindDriver = Annotated[Union[RollerBlindGPIODriver, RollerBlindHostedDriver], Field(title='RollerBlindDriver',discriminator='name')]

# LedDriver Model
class LedDriverBaseModel(DriverBaseModel):
    type: Literal['ezc.driver.led']
    name: Literal[supported_led_drivers]

# Led Driver based on non-gpio
class LedDriverNonGPIO(LedDriverBaseModel):
    lighting_config: LightCfg = Field(strict=True)
    hardware_config: HardwareCfg = Field(strict=True)
    gamma_config: GammaCfg = Field(strict=True)
    cct_map: Optional[CctMapCfg] = None
    color_map: Optional[ColorMapCfg] =  None

class LedDriverWS2812(LedDriverNonGPIO):
    _path = description.led_driver.ws2812_driver
    name: Literal['ws2812']
    ws2812_config: WS2812Cfg = Field(strict=True)

class LedDriverPWM(LedDriverNonGPIO):
    _path = description.led_driver.pwm_driver
    name: Literal['pwm']
    pwm_config: PWMCfg = Field(strict=True)

class LedDriverBP5758D(LedDriverNonGPIO):
    _path = description.led_driver.bp5758d_driver
    name: Literal['bp5758d']
    bp5758d_config: BP5758DCfg = Field(strict=True)

class LedDriverBP1658CJ(LedDriverNonGPIO):
    _path = description.led_driver.bp1658cj_driver
    name: Literal['bp1658cj']
    bp1658cj_config: BP1658CJCfg = Field(strict=True)

class LedDriverSM2135E(LedDriverNonGPIO):
    _path = description.led_driver.sm2135e_driver
    name: Literal['sm2135e']
    sm2135e_config: SM2135ECfg = Field(strict=True)

class LedDriverSM2135EH(LedDriverNonGPIO):
    _path = description.led_driver.sm2135eh_driver
    name: Literal['sm2135eh']
    sm2135eh_config: SM2135EHCfg = Field(strict=True)

class LedDriverSM2235EGH(LedDriverNonGPIO):
    _path = description.led_driver.sm2235egh_driver
    name: Literal['sm2235egh']
    sm2235egh_config: SM2235EGHCfg = Field(strict=True)

class LedDriverSM2335EGH(LedDriverNonGPIO):
    _path = description.led_driver.sm2335egh_driver
    name: Literal['sm2335egh']
    sm2335egh_config: SM2335EGHCfg = Field(strict=True)

LedDriverSM = Annotated[Union[LedDriverSM2135E, LedDriverSM2135EH, LedDriverSM2235EGH, LedDriverSM2335EGH], Field(title='SM Driver', discriminator='name')]

# LedDriver based on GPIO
class LedDriverGPIO(LedDriverBaseModel):
    _path = description.led_driver.led_gpio
    name: Literal['gpio']
    gpio_config: led_GPIOCfg = Field(strict=True)

class LedDriverKP18058(LedDriverNonGPIO):
    _path = description.led_driver.kp18058_driver
    name: Literal['kp18058']
    kp18058_config: KP18058Cfg = Field(strict=True)

# common annotated LedDriver
LedDriver = Annotated[Union[LedDriverWS2812, LedDriverPWM, LedDriverBP5758D, LedDriverBP1658CJ, LedDriverSM, LedDriverGPIO, LedDriverKP18058], Field(title='LedDriver',discriminator='name')]

# Contact Sensor Driver Model
class ContactSensorDriverBaseModel(DriverBaseModel):
    type: Literal['ezc.driver.contact_sensor']
    name: Literal['gpio']

class ContactSensorGPIODriver(ContactSensorDriverBaseModel):
    _path = description.contact_sensor_driver.contact_sensor_gpio
    name: Literal['gpio']
    gpio_config: ContactSensorGPIOCfg = Field(strict=True)

# Common Driver Annotation
Driver = Annotated[Union[ButtonDriver, RelayDriver, RollerBlindDriver, LedDriver, ZeroDetectDriver, TempSensorDriver, ContactSensorGPIODriver], Field(discriminator='type')]
