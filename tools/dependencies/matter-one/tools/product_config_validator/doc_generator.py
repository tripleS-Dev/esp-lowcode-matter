import contextlib
import importlib.metadata
import json
import sys
import urllib.parse
from datetime import datetime

from loguru import logger

from mdutils.mdutils import MdUtils
import re

from jsonschema_markdown.utils import (
    create_const_markdown,
    create_enum_markdown,
    sort_properties,
)

def get_markdown_link_text(text):
  """
  Extracts the text within the square brackets of a markdown link.

  Args:
    text: The string containing the markdown link.

  Returns:
    The text within the square brackets, or None if the string is not a markdown link.
  """
  pattern = r"\[(.*?)\]\(#.*?\)"
  match = re.match(pattern, text)
  if match:
    return match.group(1)
  else:
    return None

def get_defs(title, defs):
    for key, item in defs.items():
        if 'title' in item.keys():
            if item['title'] == title:
                return key
    return None

def create_md_file_objects(mdfile, parent, defs, level):
    if 'title' in parent.keys():
        mdfile.new_header(level=level, title = parent['title'])
    if 'section' in parent.keys():
        mdfile.new_line("Section: " + parent['section'], bold_italics_code='b')

    if 'description' in parent.keys():
        description = parent['description'].replace("\n","<br>").replace("\t", "&nbsp;&nbsp;")
        mdfile.new_paragraph(description)

    if 'example' in parent.keys():
        mdfile.new_line()
        mdfile.new_header(level=level+1, title="Examples", add_table_of_contents='n')
        for json_string in parent['example']:
            json_obj = json.loads(json_string)
            example = json.dumps(json_obj, indent=4)
            mdfile.new_line("<details open>")
            mdfile.new_line("<summary>Example</summary>")
            mdfile.insert_code(example, language='json')
            mdfile.new_line("</details>")
    mdfile.new_line()
    mdfile.new_header(level=level+1, title="Properties",add_table_of_contents='n')
    return _create_definition_table(mdfile,parent,defs)

def heirarchy_traverse(parent,defs, mdfile, level=1):
    all_possible_values = create_md_file_objects(mdfile,parent,defs,level)
    for key,item in all_possible_values.items():
        list = item.split(', ')
        title_printed = False
        for i in list:
            title = get_markdown_link_text(i)
            if title is not None:
                if not title_printed and level == 1:
                    mdfile.new_header(level, title=parent['properties'][key]['title'])
                    title_printed = True
                name = get_defs(title,defs)
                heirarchy_traverse(defs[name], defs, mdfile, level+1)
            
def generate_documentation(schema: dict, output_file_path) -> str:
    """
    Generate a markdown string from a given JSON schema.

    Args:
        schema (dict): The JSON schema to generate markdown from.
        footer (bool, optional): Whether to include a footer section in the markdown with the current date and time. Defaults to True.
        replace_refs (bool, optional): This feature is experimental. Whether to replace JSON references with their resolved values. Defaults to False.
        debug (bool, optional): Whether to print debug messages. Defaults to False.

    Returns:
        str: The generated markdown string.
    """
    logger.remove()
    logger.add(sys.stderr, level="INFO")

    mdfile = MdUtils(file_name=output_file_path)

    defs = schema.get("definitions", schema.get("$defs", {}))
    heirarchy_traverse(schema,defs,mdfile)
    mdfile.new_table_of_contents(table_title='', depth=3)
    mdfile.create_md_file()

    # Add content at the top
    with open(output_file_path, 'r', encoding='utf-8') as file:
        existing_content = file.read().lstrip('\n')
    top_note_text = "<b>Note:</b> The Advanced text mode for JSON configuration offers a lot of felixibility which might result in the device not working as expected because of some mismatch in configurations. Do evaluate and ensure that things work correctly on your end. You can always reach out to us at `zerocode@espressif.com` for any questions or help.\n<br><br>\n"
    modified_content = top_note_text + existing_content
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

def _create_definition_table(mdfile, schema: dict, defs: dict) -> str:
    """
    Create a table of the properties in the schema.
    Outputs a markdown table with the following columns:
    - Property name
    - Type
    - Required
    - Possible Values / Definition Subschema
    - Deprecated
    - Default value
    - Description

    Search for deprecated string in the description or a deprecated key set to true in the property
    """

    if schema.get("enum"):
        return create_enum_markdown(schema)

    if schema.get("const"):
        return create_const_markdown(schema)

    list_of_strings = ["Name", "Description", "Possible Values", "Default", "Type", "Required"]
    column = len(list_of_strings)
    rows = len(schema["properties"].keys())
    all_possible_values = dict()
    for property_name, property_details in schema["properties"].items():
        property_type = property_details.get("type")

        logger.debug(f"Processing {property_name} of type {property_type}")
        logger.debug(f"Property details: {property_details}")

        property_type, possible_values = _get_property_details(
            property_type, property_details, defs
        )
        if possible_values == "boolean":
            possible_values = "`true`, `false`"
        if possible_values == "integer":
            possible_values = ""
        if property_type == "const":
            property_type = "fixed value"
        logger.debug(
            f"Finished processing {property_name} of type {property_type}: {possible_values}"
        )

        default = property_details.get("default")
        description = property_details.get("description", "").strip(" \n")
        description = description.replace("\n", "<br>").replace("\t", "&nbsp;&nbsp;")
        list_of_strings.extend([property_name, description,possible_values,'`'+json.dumps(default)+'`' if default else '',property_type, '✓' if property_name in schema.get('required', []) else ''])
        all_possible_values[property_name] = possible_values
    mdfile.new_table(columns=column, rows=rows+1, text=list_of_strings, text_align='left')
    return all_possible_values

def _get_property_ref(ref, defs):
    ref = ref.split("/")[-1]
    if ref in defs:
        return (defs[ref].get("type", "object(?)"),'[{}](#{})'.format(defs[ref]['title'],defs[ref]['title'].replace(' ', '-').replace(':', '').replace('/', '').lower()))
    else:
        return "Missing type", "Missing definition", "Missing Reference Name"


def get_property_if_ref(property_details: dict, defs) -> tuple:
    """
    Check if the property is a reference.
    """

    # Check if the property is a reference
    ref_from_property = property_details.get("$ref")
    if ref_from_property:
        return _get_property_ref(ref_from_property, defs)

    # Check if the property is a reference in additionalProperties
    ref_from_additional_properties = (
        property_details["additionalProperties"].get("$ref")
        if isinstance(property_details.get("additionalProperties"), dict)
        else None
    )
    if ref_from_additional_properties:
        return _get_property_ref(ref_from_additional_properties, defs)

    return None, None


def _get_property_details(property_type: str, property_details: dict, defs: dict):
    """
    Get the possible values for a property.
    """

    # Check if the property is a reference
    ref_type, ref_details = get_property_if_ref(property_details, defs)
    if ref_type or ref_details:
        return ref_type, ref_details

    if "enum" in property_details:
        return (
            property_type,
            ", ".join([f"`{str(value)}`" for value in property_details["enum"]]),
        )

    array_like = (
        "oneOf"
        if "oneOf" in property_details
        else "anyOf"
        if "anyOf" in property_details
        else "allOf"
        if "allOf" in property_details
        else None
    )

    array_separator = {"oneOf": ", ", "anyOf": " or ", "allOf": " and "}

    # TODO: Check why are we removing null from array_like
    if array_like:
        with contextlib.suppress(Exception):
            property_details[array_like].remove({"type": "null"})
            if len(property_details[array_like]) == 1:
                return _get_property_details(
                    property_details[array_like][0].get("type"),
                    property_details[array_like][0],
                    defs,
                )

    if array_like:
        types = []
        details = []
        for value in property_details[array_like]:
            ref_type, ref_details = get_property_if_ref(value, defs)
            if ref_type or ref_details:
                types.append(ref_type)
                details.append(ref_details)
            else:
                ref_type, ref_details = _get_property_details(
                    value.get("type"), value, defs
                )
                types.append(ref_type)
                details.append(ref_details)
        types_set = set(types)
        if len(types_set) > 1:
            logger.warning(f"Multiple types in {array_like} property: {types_set}")

        return (
            types[0],
            array_separator[array_like].join(details),
        )

    elif "items" in property_details:
        array_like = (
            "oneOf"
            if "oneOf" in property_details["items"]
            else "anyOf"
            if "anyOf" in property_details["items"]
            else "allOf"
            if "allOf" in property_details["items"]
            else None
        )

        if array_like:
            types = []
            details = []
            for value in property_details["items"][array_like]:
                ref_type, ref_details = get_property_if_ref(value, defs)
                if ref_type or ref_details:
                    types.append(ref_type)
                    details.append(ref_details)
                else:
                    ref_type, ref_details = _get_property_details(
                        value.get("type"), value, defs
                    )
                    types.append(ref_type)
                    details.append(ref_details)
            types_set = set(types)
            if len(types_set) > 1:
                logger.warning(
                    f"Multiple types in items,{array_like} property: {types_set}"
                )

            return (
                types[0],
                array_separator[array_like].join(details),
            )

        ref_type, ref_details = get_property_if_ref(property_details["items"], defs)
        if ref_type or ref_details:
            return property_type, ref_details
        else:
            ref_type, ref_details = _get_property_details(
                property_details["items"].get("type"), property_details["items"], defs
            )
            return property_type, ref_details

    elif "pattern" in property_details:
        pattern = property_details["pattern"]
        res_details = f"[`{pattern}`](https://regex101.com/?regex={urllib.parse.quote_plus(pattern)})"
        return property_type, res_details
    elif "additionalProperties" in property_details and not isinstance(
        property_details["additionalProperties"], bool
    ):
        new_type = property_details["additionalProperties"].get("type")
        return new_type, new_type
    elif "const" in property_details:
        res_details = f"`{property_details.get('const')}`"
        return "const", res_details
    elif property_type in ["integer", "number"]:
        # write the range of the integer in the format a <= x <= b
        minimum = property_details.get("minimum")
        maximum = property_details.get("maximum")
        exclusive_minimum = property_details.get("exclusiveMinimum")
        exclusive_maximum = property_details.get("exclusiveMaximum")
        if minimum is not None and maximum is not None:
            if exclusive_minimum is not None and exclusive_maximum is not None:
                res_details = f"`{minimum} < x < {maximum}`"
            elif exclusive_minimum is not None:
                res_details = f"`{minimum} < x <= {maximum}`"
            elif exclusive_maximum is not None:
                res_details = f"`{minimum} <= x < {maximum}`"
            else:
                res_details = f"`{minimum} <= x <= {maximum}`"
        elif minimum is not None:
            if exclusive_minimum is not None:
                res_details = f"`{minimum} < x`"
            else:
                res_details = f"`{minimum} <= x`"
        elif maximum is not None:
            if exclusive_maximum is not None:
                res_details = f"`x < {maximum}`"
            else:
                res_details = f"`x <= {maximum}`"
        else:
            # fallback to integer when no range is specified
            res_details = property_type

        return property_type, res_details

    else:
        return property_type, f"{property_type}"
