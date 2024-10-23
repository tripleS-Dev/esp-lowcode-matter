from typing_extensions import Annotated
from typing import Any
from pydantic import Field, ValidationError
from pydantic.functional_validators import BeforeValidator
from pydantic_core import PydanticCustomError
from enum import Enum

class MandatoryFieldType(Enum):
    AllOf = "allOf"     # (AND) Must be valid against all of the subschemas
    AnyOf = "anyOf"     # (OR) Must be valid against any of the subschemas
    OneOf = "oneOf"     # (XOR) Must be valid against exactly one of the subschemas
    Not = "not"         # (NOT) Must not be valid against the given schema

def _contains_field(field_value_pair: list, type: MandatoryFieldType = MandatoryFieldType.AllOf):
    if type not in MandatoryFieldType._value2member_map_ :
        print("Error: The field type is not valid")
        return Field()
    json_schema = dict()
    json_schema[type] = list()
    for item in field_value_pair:
        contains_json_schema = dict()
        contains_json_schema["contains"] = dict()
        contains_json_schema["contains"]["properties"] = dict()
        contains_json_schema["contains"]["required"] = list()
        for key,value in item.items():
            contains_json_schema["contains"]["required"].append(key)
            contains_json_schema["contains"]["properties"].update({
                key : {"const": value}
            })
        json_schema[type].append(contains_json_schema)
    return Field(json_schema_extra=json_schema)

def _lambda_mandatory_field_validator(data: Any, field_value_pair: list, field_type: str):
    if field_type not in MandatoryFieldType._value2member_map_ :
        print("Error: The Field type is not valid")
        return data
    count = 0
    for item in field_value_pair:
        found = False
        for data_item in data:
            match_key_count = 0
            for key,value in item.items():
                if key in data_item.keys():
                    if value == data_item[key]:
                        match_key_count = match_key_count + 1
            if match_key_count == len(item.keys()):
                found = True
                count = count + 1
        if not found:
            if field_type == "allOf":
                raise PydanticCustomError('missing_mandatory_field', "The following field is mandatory: {}".format(item), item)
        else:
            if field_type == "not":
                raise PydanticCustomError('field_not_allowed', "The following field is invalid: {}".format(item), item)
    if count == 0:
        if field_type == "anyOf":
            raise PydanticCustomError("missing_mandatory_field","Minimum one of the following field is mandatory: {}".format(field_value_pair), field_value_pair)
        elif field_type == "oneOf":
            raise PydanticCustomError("missing_mandatory_field","Any one of the following field is mandatory: {}".format(field_value_pair), field_value_pair)
    else:
        if field_type == "oneOf":
            raise PydanticCustomError('field_not_allowed', "Only one of the following field is allowed: {}".format(field_value_pair), field_value_pair)
    return data

def mandatory_field_validator(field_value_pair: list, field_type: MandatoryFieldType):
    return lambda v: _lambda_mandatory_field_validator(v, field_value_pair, field_type)

def MandatoryField(type: Any, field_value_pair: list, field_type: str):
    return Annotated[type, _contains_field(field_value_pair, field_type), BeforeValidator(mandatory_field_validator(field_value_pair, field_type))]


