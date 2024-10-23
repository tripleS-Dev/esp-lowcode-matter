import json, re
from typing import Dict, List

def parse_location(loc, json_file):
    final_loc = list()
    json_dict = json_file
    for i in loc:
        if type(i) == str:
            if i in json_dict.keys():
                final_loc.append(i)
                json_dict = json_dict[i]
        if type(i) == int:
            if type(json_dict) == list:
                final_loc.append(i)
                json_dict = json_dict[i]
    return final_loc

def parse_missing(e):
    # Add the extra "missing_field" title
    e["key"] = e["loc"][-1]
    e["value"] = None
    return e

def parse_extra_forbidden(e):
    e["type"] = "Invalid Field"
    e["key"] = e["loc"][-1]
    e["value"] = e["input"]
    return e

def parse_union_tag_invalid(e):
    e["type"] = "Invalid Input"
    key_value = re.search("Input tag '(.+?)' found using '(.+?)' does not match any of the expected tags",e["msg"])
    e["key"] = key_value.group(2)
    e["value"] = key_value.group(1)
    e["loc"] = [i for i in e["loc"]]
    e["loc"].append(e["key"])
    return e

def parse_value_error(e):
    e["msg"] = e["msg"].replace("Value error, ", "")
    if len(e["loc"]) > 0:
        e["key"] = e["loc"][-1]
    e["value"] = e["input"]
    del e["input"]
    return e

def parse_union_tag_not_found(e):
    e["type"] = "missing"
    e["loc"] = [i for i in e["loc"]]
    e["loc"].append(re.search("Unable to extract tag using discriminator '(.+?)'" ,e["msg"]).group(1))
    e["key"] = e["loc"][-1]
    e["msg"] = "Field required"
    del e["input"]
    return parse_missing(e)

def parse_missing_mandatory_field(e):
    del e["input"]
    e["key"] = e["loc"][-1]
    e["value"] = e["ctx"]
    return e

var_type_error = ["int_type", "bool_type", "float_type"]
def parse_var_type(e):
    e["key"] = e["loc"][-1]
    e["value"] = e["input"]
    del e["input"]
    return e

def error_handling(error, json_file):
    final_error = dict()
    final_error["error"] = list()
    for e in error.errors():
        if e["type"] == "missing":
            e = parse_missing(e)
        elif e["type"] == "extra_forbidden":
            e = parse_extra_forbidden(e)
        elif e["type"] == "union_tag_invalid":
            e = parse_union_tag_invalid(e)
        elif e["type"] == "value_error":
            e = parse_value_error(e)
        elif e["type"] == "union_tag_not_found":
            e = parse_union_tag_not_found(e)
        elif e["type"] ==  "missing_mandatory_field" or e["type"] == "field_not_allowed":
            e = parse_missing_mandatory_field(e)
        elif e["type"] in var_type_error:
            e = parse_var_type(e)

        if "loc" in e.keys():
            e["loc"] = parse_location(e["loc"], json_file)
        if "url" in e.keys():
            del e["url"]
        if "ctx" in e.keys():
            del e["ctx"]
        final_error["error"].append(e)
    return final_error
