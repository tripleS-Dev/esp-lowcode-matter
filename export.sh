#!/bin/bash

# Function to handle errors
handle_error() {
    echo "Error: $1"
    exit 1
}

if [ -z "${LOW_CODE_PATH}" ]
then
    # LOW_CODE_PATH not set in the environment.
    # If using bash or zsh, try to guess LOW_CODE_PATH from script location.
    self_path=""

    # shellcheck disable=SC2128  # ignore array expansion warning
    if [ -n "${BASH_SOURCE-}" ]
    then
        self_path="${BASH_SOURCE}"
    elif [ -n "${ZSH_VERSION-}" ]
    then
        self_path="${(%):-%x}"
    else
        echo "Could not detect LOW_CODE_PATH. Please set it before sourcing this script:"
        echo "  export LOW_CODE_PATH=(add path here)"
        return 1
    fi

    # shellcheck disable=SC2169,SC2169,SC2039  # unreachable with 'dash'
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # convert possibly relative path to absolute
        script_dir="$(realpath_int "${self_path}")"
        # resolve any ../ references to make the path shorter
        script_dir="$(cd "${script_dir}" || exit 1; pwd)"
    else
        # convert to full path and get the directory name of that
        script_name="$(readlink -f "${self_path}")"
        script_dir="$(dirname "${script_name}")"
    fi
    export LOW_CODE_PATH="${script_dir}"
    echo "Setting LOW_CODE_PATH to '${LOW_CODE_PATH}'"
fi

# Simplify directory names by creating variables
ESP_MATTER_DIR="${LOW_CODE_PATH}/tools/dependencies/esp-matter"
ZAP_DIR="$ESP_MATTER_DIR/connectedhomeip/connectedhomeip/.environment/cipd/packages/zap"

if [ -f "$ZAP_DIR/zap-cli"* ]; then
    echo "zap is already installed."
    export ZAP_INSTALL_PATH="$ZAP_DIR"
else
    handle_error "zap is not installed. run install.sh first."
fi

if [ ! -d "$ESP_MATTER_DIR" ]; then
    handle_error "$ESP_MATTER_DIR folder does not exist."
fi
export ESP_MATTER_PATH="$ESP_MATTER_DIR"

echo "Successfully exported variables"
