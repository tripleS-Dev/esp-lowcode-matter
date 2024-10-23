# JSON validator

Pydantic based JSON validation tool to verify if the product config for products is valid or not. This tool also generates the JSON Schema and the JSON documentation.

## Features of JSON Schema

* Limit the field value to a min and max
* Make sure that a list/array in json contains atleast one number of items wherever required
* product_common should atleast containt ezc.product_common.factory_reset
* Field value should be a multiple of a number (like steps required in sm2135 drivers)
* No extra fields other than the defined ones are allowed, not even extra types are allowed, like if int field cannot have string value then it will raise error.
* Set default value for a field

Dyanmic and Hard logics are not supported in JsonSchema

## Features of Pydantic

* All the Json Schema features are supported by the pydantic
* checks if the input/output id is actually defined in driver
* check if Driver ID is repeated
* No two driver ID has same GPIO

## Setup

```sh
pip install -r requirements.txt
```

## Usage

* `python3 json_validator.py`: This will generate the schema and the documentation in all the supported languages.
* `python3 json_validator.py --output_path output`: This will generate the files at the given path instead of the default output path.
* `python3 json_validator.py --product_config_path product_config.json`: This will also validated the product config.

## How to add a features

Example:

If you want to add a new `xyz` driver support which has `a`, `b` and `c` as the json fields field then create a class for it in the `driver.py`:
```py
class xyz_driver(ZeroCodeBaseModel):
    _path = description.xyz
    x: StrictInt
    y: StrictInt
    z: StrictInt
```

Also add it to the common driver union: `Driver` variable defined in `driver.py`:
```py
Driver = Annotated[Union[ButtonDriver, RollerBlindDriver, LedDriver, xyz_driver], Field(discriminator='type')]
```

Then need to add the corresponding descriptions in all the language files: `description_en.py` and `description_cn.py`

Similarly anything can be added in their respective files and folders.
