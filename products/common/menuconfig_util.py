import argparse
import json
import os

parser = argparse.ArgumentParser(description="Low code menuconfig parser script")
parser.add_argument("--build_path", default="", type=str, help="Provide path for the build directory")
parser.add_argument("--idf_path", default="", type=str, help="Provide the IDF path")
args = vars(parser.parse_args())

build_path = args['build_path']
idf_path = args['idf_path']
config_env_path = "{}/config.env".format(build_path)

# These components are present in IDF_PATH but are required for low_code
exception_config = ['ulp', 'log', 'soc', 'esp_hw_support']

# edit the config.env file
with open(config_env_path, 'r') as config_env_file:
    config_env = json.load(config_env_file)
    component_kconfigs_list = config_env['COMPONENT_KCONFIGS'].split(";")

    # Remove all the kconfigs which are present in idf_path, since the program is baremetal
    for kconfig in component_kconfigs_list[:]:
        if kconfig.startswith(idf_path) and not any(substring in kconfig for substring in exception_config):
            component_kconfigs_list.remove(kconfig)
    config_env['COMPONENT_KCONFIGS'] = ';'.join(component_kconfigs_list)

    component_kconfigs_projbuild = config_env['COMPONENT_KCONFIGS_PROJBUILD'].split(";")
    for kconfig in component_kconfigs_projbuild[:]:
            if kconfig.startswith(idf_path) and not any(substring in kconfig for substring in exception_config):
                component_kconfigs_projbuild.remove(kconfig)
    config_env['COMPONENT_KCONFIGS_PROJBUILD'] = ';'.join(component_kconfigs_projbuild)

os.remove(config_env_path)
with open(config_env_path, 'w') as config_env_file:
    json.dump(config_env, config_env_file, indent=4)
