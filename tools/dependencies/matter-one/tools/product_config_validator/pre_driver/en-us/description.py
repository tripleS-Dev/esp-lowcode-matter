from dotmap import DotMap

description = DotMap()

# Pre Driver -> Log Output
log_output = description.log_output
log_output.title = "Log Output"
log_output.section = "Pre Driver"
log_output.description = "Configure the console logs. This can be used to change the log level or even change the default IO pin."
log_output.example = ['{"type": "ezc.pre_driver.log_output", "level": 0}', '{"type": "ezc.pre_driver.log_output", "tx_gpio": 19}']

log_output.type.title = "type"
log_output.type.description = "Pre Driver type: ezc.pre_driver.log_output"

log_output.level.title = "Log Level"
log_output.level.description = "Set the log level:\n• 0: No logs\n• 1: Error\n• 2: Warning\n• 3: Info\n• 4: Debug\n• 5: Verbose\n"

log_output.tx_gpio.title = "TX GPIO"
log_output.tx_gpio.description = "Change the tx gpio for console logs. Possible GPIO values depend on the selected module."

# Pre Driver -> Power Management
power_management = description.power_management
power_management.title = "Power Management"
power_management.section = "Pre Driver"
power_management.description = "Configure the power usage of the device. This can be useful for devices which have power limitations."
power_management.example = ['{"type": "ezc.pre_driver.power_management", "enable_light_sleep": true, "max_freq_mhz": 160, "min_freq_mhz": 10}']

power_management.type.title = "type"
power_management.type.description = "Pre Driver type: ezc.pre_driver.power_management"

power_management.enable_light_sleep.title = "Enable Light Sleep"
power_management.enable_light_sleep.description = "It enables light sleep, It helps in reducing power usage."

power_management.max_freq_mhz.title = "Max Frequency (in Mhz)"
power_management.max_freq_mhz.description = "Maximum frequency that device will go to."

power_management.min_freq_mhz.title = "Min Frequency (in Mhz)"
power_management.min_freq_mhz.description = "Minimum frequency that device will go to."

# Pre Driver -> Hosted UART
hosted_uart = description.hosted_uart
hosted_uart.title = "Hosted Configuration"
hosted_uart.section = "Pre Driver"
hosted_uart.description = "Configure UART settings for Hosted solutions"
hosted_uart.example = ['{"type": "ezc.pre_driver.hosted_uart", "uart_rx": 6, "uart_tx": 7, "uart_baudrate": 115200, "ack_enable": false, "host_wakeup_pin": -1, "esp_wakeup_pin": -1}']

hosted_uart.type.title = "type"
hosted_uart.type.description = "Pre Driver type: ezc.pre_driver.hosted_uart"

hosted_uart.uart_rx.title = "UART RX pin"
hosted_uart.uart_rx.description = "Valid GPIO for RX pin for ESP ZeroCode module"

hosted_uart.uart_tx.title = "UART TX pin"
hosted_uart.uart_tx.description = "Valid GPIO for TX pin for ESP ZeroCode module"

hosted_uart.uart_baudrate.title = "UART Baudrate"
hosted_uart.uart_baudrate.description = "Communication baudrate for UART"

hosted_uart.ack_enable.title = "ACK Enabled"
hosted_uart.ack_enable.description = "Enable to send/receive acknowledgement after every command"

hosted_uart.host_wakeup_pin.title = "Host Wakeup Pin"
hosted_uart.host_wakeup_pin.description = "GPIO Pin used for waking host before sending any command. -1 to disable host wakeup"

hosted_uart.esp_wakeup_pin.title = "ESP Wakeup Pin"
hosted_uart.esp_wakeup_pin.description = "GPIO Pin used for waking ESP before receiving any command. -1 to disable ESP wakeup"
