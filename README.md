# Low Code: LP Core

## Setup

Clone the repositories.

```sh
cd esp-matter-lowcode
git submodule update --init --recursive
cd ..
```

```sh
git clone -b release/v5.3 https://github.com/espressif/esp-idf.git --recursive
cd esp-idf
export ESP_IDF_PATH=$(pwd)/esp-idf
./install.sh
. ./export.sh
cd ..
```

```sh
git clone --single-branch -b feature/matter-file-parsing --depth 1 https://github.com/espressif/esp-matter.git
cd esp-matter
export ESP_MATTER_PATH=$(pwd)/esp-matter
git submodule update --init --depth 1
cd connectedhomeip/connectedhomeip
./scripts/checkout_submodules.py --platform esp32 linux --shallow
cd ..
./install.sh
. ./export.sh
cd ..
```

```sh
git clone -b development https://github.com/espressif/esp-amp.git
cd esp-amp
export ESP_AMP_PATH=$(pwd)/esp-amp
git submodule update --init --recursive
cd ..
```

## Pre-built Binaries

Flash the pre-built binaries to the device.

```sh
cd pre_built_binaries
esptool.py erase_flash
esptool.py write_flash $(cat flash_args)
```

## Per device configuration

```sh
cd tools/mfg
./mfg_low_code.sh ../../products/light
```

## Build

```sh
cd products/light
idf.py set-target esp32c6
idf.py build
```

## Flash

```sh
esptool.py write_flash 0x20C000 build/subcore_light.subcore.bin
```

## Monitor

```sh
python3 -m esp_idf_monitor
```
