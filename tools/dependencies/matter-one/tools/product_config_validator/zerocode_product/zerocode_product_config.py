from typing import Any, Optional, Literal
from pydantic import BaseModel, StrictInt, StrictStr, StrictBool, ValidationError, model_validator, field_validator, Field, conlist, conset

from pre_driver.pre_driver import PreDriver
from driver.driver import Driver
from product_common.product_common import ProductCommon
from product.product import Product
from test_mode.test_mode import TestMode

from data_handler.var_handler import reset_data_handler_var
from data_handler.base_model import ZeroCodeBaseModel, get_locale
from data_handler.mandatory_field import MandatoryField

from typing_extensions import Annotated

import importlib
locale = get_locale()
module_name = f'zerocode_product.{locale}.description'
description_module = importlib.import_module(module_name)
description = description_module.description

# TODO: Add a `title`, `description`, and `example` value for all the field
class ZerocodeProductConfig(ZeroCodeBaseModel):
    _path = description.zerocode_product
    config_version: Literal[3]
    pre_driver: Optional[conset(PreDriver)] = None
    driver: conset(Driver, min_length=1)
    # product_common: MandatoryField(conset(ProductCommon, min_length=1), [{"type": "ezc.product_common.factory_reset"}], field_type="allOf")
    product_common: conset(ProductCommon, min_length=1)
    product: conset(Product, min_length=1)
    test_mode: Optional[conset(TestMode, min_length=1)] = None
    device_management: Optional[StrictBool] = None

    @model_validator(mode='before')
    @classmethod
    def reset_variables(cls, data: Any) -> Any:
        reset_data_handler_var()
        return data
