## set IDF_PATH & ESP_AMP_PATH
if(NOT DEFINED ENV{IDF_PATH})
    message(FATAL_ERROR "Please set IDF_PATH to the path of esp-idf repo")
endif(NOT DEFINED ENV{IDF_PATH})
set(IDF_PATH $ENV{IDF_PATH} CACHE PATH "" FORCE)

if(NOT IDF_TARGET STREQUAL "esp32c6")
    message(FATAL_ERROR "Please set idf target to esp32c6 by running: idf.py set-target esp32c6")
endif()

if(NOT DEFINED ENV{ESP_AMP_PATH})
    message(FATAL_ERROR "Please set ESP_AMP_PATH to the path of esp_amp repo")
endif(NOT DEFINED ENV{ESP_AMP_PATH})
set(ESP_AMP_PATH $ENV{ESP_AMP_PATH} CACHE PATH "" FORCE)

## esp_amp settings
include($ENV{ESP_AMP_PATH}/components/esp_amp/cmake/subcore_project.cmake)

## set sdkconfig.defaults
list(APPEND SDKCONFIG_DEFAULTS "../common/sdkconfig.defaults")

## additional flags for LP core
idf_build_set_property(COMPILE_OPTIONS "-Wno-error=uninitialized;-Wno-error=maybe-uninitialized;-Wno-missing-field-initializers" APPEND)

if(NOT DEFINED ENV{LOW_CODE_PATH})
    message(FATAL_ERROR "Please set LOW_CODE_PATH to the path of low_code repo")
endif(NOT DEFINED ENV{LOW_CODE_PATH})
include($ENV{LOW_CODE_PATH}/tools/cmake/low_code_menuconfig.cmake)
