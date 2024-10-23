from pydantic import BaseModel, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import CoreSchema

g_locale = 'en-us'

def set_locale(locale):
    global g_locale
    g_locale = locale

def get_locale():
    return g_locale

# Common BaseModel for all zerocode fields
class ZeroCodeBaseModel(BaseModel, extra='forbid', frozen=True):
    _path = None

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        json_schema = handler(core_schema)
        json_schema = handler.resolve_ref_schema(json_schema)
        if cls._path.default == None:
            print("Path is not present in class {}".format(cls.__name__))
            return json_schema
        _description = cls._path.default.toDict()
        if 'title' not in _description.keys():
            print("Class definition title missing in class: {}".format(cls.__name__))
        elif 'title' in json_schema.keys():
            json_schema['title'] = _description['title']
        if 'description' not in _description.keys():
            print("Class definition description missing in class: {}".format(cls.__name__))
        else:
            json_schema['description'] = _description['description']
        if 'example' in _description.keys():
            json_schema['example'] = _description['example']
        if 'section' in _description.keys():
            json_schema['section'] = _description['section']
        if 'properties' not in json_schema.keys():
            return json_schema
        properties = json_schema['properties']
        for field in properties.keys():
            if field in _description.keys():
                if 'title' not in _description[field].keys():
                    print("Title missing in field: {}, for the class: {}".format(field, cls.__name__))
                else:
                    properties[field]['title'] = _description[field]['title']
                if 'description' not in _description[field].keys():
                    print("Title missing in field: {}, for the class: {}".format(field, cls.__name__))
                else:
                    properties[field]['description'] = _description[field]['description']
                if 'examples' in _description[field].keys():
                    properties[field]['examples'] = _description[field]['examples']
        return json_schema
