## TODO: To be removed later
## setting required for build system
add_compile_definitions(CONFIG_ESP_CONSOLE_UART_NUM=0)
add_compile_definitions(CONFIG_BOOTLOADER_LOG_LEVEL=0)
set(CONFIG_ESPTOOLPY_FLASHMODE dio CACHE PATH "" FORCE)
set(CONFIG_ESPTOOLPY_FLASHFREQ "80m" CACHE PATH "" FORCE)
set(CONFIG_ESPTOOLPY_FLASHSIZE "4MB" CACHE PATH "" FORCE)
set(CONFIG_PARTITION_TABLE_OFFSET 0xC000 CACHE PATH "" FORCE)
set(CONFIG_BOOTLOADER_OFFSET_IN_FLASH 0x0 CACHE PATH "" FORCE)
set(CONFIG_ESP_REV_MIN_FULL 0 CACHE PATH "" FORCE)
set(CONFIG_ESP_REV_MAX_FULL 99 CACHE PATH "" FORCE)

# override the cmake configure_file function
# This has been done to check when config.env file is generated and edit it
# refer: https://gitlab.kitware.com/cmake/cmake/-/issues/23482
function(configure_file)
    # This calls the original configure_file func
    _configure_file(${ARGN})

    list(GET ARGN 0 configure_file_input)
    list(GET ARGN 1 configure_file_output)
    set(config_env_path "${CMAKE_BINARY_DIR}/config.env")
    if (config_env_path STREQUAL configure_file_output)
        message(STATUS "The input is: ${configure_file_input}")
        message(STATUS "The output is: ${configure_file_output}")
        execute_process(
            COMMAND ${python} ${CMAKE_SOURCE_DIR}/../common/menuconfig_util.py --build_path ${CMAKE_BINARY_DIR} --idf_path $ENV{IDF_PATH}
            RESULT_VARIABLE menuconfig_utils_result
            COMMAND_ECHO STDOUT
        )
        if (menuconfig_utils_result)
            message(FATAL_ERROR "Failed to run the menuconfig_util script")
        endif()
    endif()
endfunction()
