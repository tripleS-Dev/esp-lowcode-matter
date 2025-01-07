import sys
import os
from attribute_bounds_lookup import BoundsLookup
import json

try:
    import idl_lint
    from matter_idl.matter_idl_parser import CreateParser
    from matter_idl.matter_idl_types import *
except ModuleNotFoundError:
    # Check if ESP_MATTER_PATH is defined
    ESP_MATTER_PATH = os.getenv('ESP_MATTER_PATH')
    if ESP_MATTER_PATH is None:
        print("Error: The environment variable 'ESP_MATTER_PATH' is not set.")
        sys.exit(1)

    SCRIPT_PATH = os.path.join(os.getenv('ESP_MATTER_PATH'), "connectedhomeip", "connectedhomeip", "scripts")
    sys.path.append(SCRIPT_PATH)
    sys.path.append(os.path.join(SCRIPT_PATH, 'py_matter_idl'))

    import idl_lint
    from matter_idl.matter_idl_parser import CreateParser
    from matter_idl.matter_idl_types import *

__all__ = ['BoundsLookup', 'CreateParser', 'idl_lint', 'FieldQuality', 'AttributeQuality', 'CommandQuality']