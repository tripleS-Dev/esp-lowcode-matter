import os
from typing import Any, Optional, Literal, Union
from pydantic import BaseModel, StrictInt, StrictStr, StrictBool, ValidationError, model_validator, field_validator, Field, conlist, conset
from pydantic_core import ValidationError
from typing_extensions import Annotated

from data_handler.var_handler import validate_min_max
from data_handler.base_model import ZeroCodeBaseModel, get_locale

import importlib
locale = get_locale()
module_name = f'pre_driver.{locale}.description'
description_module = importlib.import_module(module_name)
description = description_module.description

supported_pre_drivers = ("ezc.pre_driver.log_output", "ezc.pre_driver.power_management", "ezc.pre_driver.hosted_uart")


class PreDriverBaseModel(ZeroCodeBaseModel):
    type: Literal[supported_pre_drivers]

# TODO: Make sure that one of level or tx_gpio is present if logoutput exists
class LogOutput(PreDriverBaseModel):
    _path = description.log_output

    type: Literal['ezc.pre_driver.log_output'] = Field(title=description.log_output.type["title"])
    level: Optional[Literal[0,1,2,3,4,5]] = None
    tx_gpio: Optional[StrictInt] = None

class PowerManagement(PreDriverBaseModel):
    _path = description.power_management

    type: Literal['ezc.pre_driver.power_management']
    enable_light_sleep: StrictBool = Field(default=False)
    max_freq_mhz: StrictInt = Field(gt=40,le=240)
    min_freq_mhz: StrictInt = Field(ge=10,le=240)

    _check_freq = validate_min_max("min_freq_mhz", "max_freq_mhz")

class HostedUart(PreDriverBaseModel):
    _path = description.hosted_uart

    type: Literal['ezc.pre_driver.hosted_uart']
    uart_rx: StrictInt = Field(default=6)
    uart_tx: StrictInt = Field(default=7)
    uart_baudrate: StrictInt = Field(default=115200)
    ack_enable: StrictBool = Field(default=True)
    host_wakeup_pin: StrictInt = Field(default=-1)
    esp_wakeup_pin: StrictInt = Field(default=-1)

PreDriver = Annotated[Union[LogOutput, PowerManagement, HostedUart], Field(title='Pre Driver',discriminator='type')]
