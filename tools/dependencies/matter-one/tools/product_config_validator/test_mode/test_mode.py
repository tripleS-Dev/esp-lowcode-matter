from typing import Any, Literal, Optional, Union
from typing_extensions import Annotated
from pydantic import BaseModel,StrictInt, StrictStr, ValidationError, model_validator, field_validator, Field, validator, Extra
from data_handler.base_model import ZeroCodeBaseModel, get_locale

import importlib
locale = get_locale()
module_name = f'test_mode.{locale}.description'
description_module = importlib.import_module(module_name)
description = description_module.description

# TODO: check if there are additioanl constraints like ssid can only be present if it is non-thread device
supported_test_mode = ('ezc.test_mode.common', 'ezc.test_mode.ble', 'ezc.test_mode.sniffer', 'ezc.test_mode.light', 'ezc.test_mode.socket', 'ezc.test_mode.window_covering', 'ezc.test_mode.low_code')
# TODO: Make sure that products can have test_mode for specific products only,
#       like light can have test_mode for lights only
class TestModeBaseModel(ZeroCodeBaseModel):
    type: Literal[supported_test_mode]
    subtype: StrictInt
    trigger: Optional[Literal[0,1,2,3]] = None
    ssid: Optional[StrictStr] = None
    panid: Optional[int] = None
    mac: Optional[StrictStr] = None
    id: Optional[StrictStr] = None

class TestModeCommon(TestModeBaseModel):
    _path = description.test_mode_common

    type: Literal['ezc.test_mode.common']
    subtype: Literal[1, 2]

class TestModeBLE(TestModeBaseModel):
    _path = description.test_mode_ble

    type: Literal['ezc.test_mode.ble']
    subtype: Literal[1]

class TestModeSniffer(TestModeBaseModel):
    _path = description.test_mode_sniffer

    type: Literal['ezc.test_mode.sniffer']
    subtype: Literal[1]

class TestModeLight(TestModeBaseModel):
    _path = description.test_mode_light

    type: Literal['ezc.test_mode.light']
    subtype: Literal[1,2,3,4]
    interval_time_s: Optional[StrictInt] = None
    loop_count: Optional[StrictInt] = None
    r_time_s: Optional[StrictInt] = None
    g_time_s: Optional[StrictInt] = None
    b_time_s: Optional[StrictInt] = None
    w_time_s: Optional[StrictInt] = None
    c_time_s: Optional[StrictInt] = None

class TestModeSocket(TestModeBaseModel):
    _path = description.test_mode_socket

    type: Literal['ezc.test_mode.socket']
    subtype: Literal[1,2]

class TestModeWindowCovering(TestModeBaseModel):
    _path = description.test_mode_window_covering

    type: Literal['ezc.test_mode.window_covering']
    subtype: Literal[1]

class TestModeLowCode(TestModeBaseModel):
    _path = description.test_mode_low_code
    type: Literal['ezc.test_mode.low_code']

TestMode = Annotated[Union[TestModeCommon, TestModeBLE, TestModeSniffer, TestModeLight, TestModeSocket, TestModeWindowCovering, TestModeLowCode], Field(discriminator='type')]
