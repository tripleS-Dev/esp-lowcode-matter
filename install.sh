#!/bin/bash

set -e

# Function to handle errors
handle_error() {
    echo "Error: $1"
    exit 1
}

OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

case $OS in
    darwin)
        case $ARCH in
            arm64) URL="https://github.com/project-chip/zap/releases/latest/download/zap-mac-arm64.zip" ;;
            x86_64) URL="https://github.com/project-chip/zap/releases/latest/download/zap-mac-x64.zip" ;;
            *) handle_error "Unsupported architecture for macOS" ;;
        esac
        ;;
    linux)
        case $ARCH in
            x86_64) URL="https://github.com/project-chip/zap/releases/latest/download/zap-linux-x64.zip" ;;
            aarch64) URL="https://github.com/project-chip/zap/releases/latest/download/zap-linux-arm64.zip" ;;
            *) handle_error "Unsupported architecture for Linux" ;;
        esac
        ;;
    *) handle_error "Unsupported OS" ;;
esac

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

# Simplify directory names by creating a variable
INSTALL_DIR="${LOW_CODE_PATH}/tools/dependencies/esp-matter/connectedhomeip/connectedhomeip/.environment/cipd/packages"

mkdir -p "$INSTALL_DIR" || handle_error "Failed to create directory $INSTALL_DIR"
echo "Installing zap..."

curl -L -o "$INSTALL_DIR/zap.zip" $URL || handle_error "Failed to download zap.zip"

if unzip -q "$INSTALL_DIR/zap.zip" -d "$INSTALL_DIR/zap"; then
    echo "Unzip successful."
else
    handle_error "Unzip failed"
fi
if [ -f "$INSTALL_DIR/zap/zap-cli"* ]; then
    rm "$INSTALL_DIR/zap.zip"
    echo "Successfully Downloaded zap"
else
    handle_error "Issue in unzipping the file"
fi

python3 -m pip install -r "${LOW_CODE_PATH}/tools/mfg/requirements.txt"
python3 -m pip install -r "${LOW_CODE_PATH}/tools/mfg/requirements_fixes.txt"
