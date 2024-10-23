from dotmap import DotMap

description = DotMap()

# Test Mode -> Common Items
test_mode = description.test_mode
test_mode.trigger.title = "Trigger Mechanism"
test_mode.trigger.description = "Test case trigger mechanism:\n• 0: Default: Automatically select Wi-Fi (1) or Thread (2) depending on the hardware.\n• 1: Wi-Fi: Using Wi-Fi network nearby with the specified SSID.\n• 2: Thread: Using a thread network nearby with the specified PANID and MAC.\n• 3: Sniffer: Using the sniffer method where another device is broadcasting the signal nearby with the given ID."

test_mode.ssid.title = "SSID"
test_mode.ssid.description = "Wi-Fi SSID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Wi-Fi based devices only."

test_mode.panid.title = "PANID"
test_mode.panid.description = "Thread PANID that the device will search for. If this is found along with the MAC, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Thread based devices only."

test_mode.mac.title = "MAC"
test_mode.mac.description = "Thread MAC that the device will search for. If this is found along with the PANID, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Thread based devices only."

test_mode.mac.title = "ID"
test_mode.mac.description = "Sniffer ID that the device will search for. If this is found, the test mode is triggered. If not specified, the default for the test mode will be used. This is applicable for Sniffer based trigger only."

# Test Mode -> Common
test_mode_common = description.test_mode_common
test_mode_common.update(test_mode)
test_mode_common.title = "Test Mode: Common"
test_mode_common.section = "Test Mode"
test_mode_common.description = "Common test modes"
test_mode_common.example = ['{"type": "ezc.test_mode.common", "subtype": 1}']

test_mode_common.type.title = "Type"
test_mode_common.type.description = "Test Mode type: ezc.test_mode.common"
test_mode_common.subtype.title = "Subtype"
test_mode_common.subtype.description = "Test type:\n• 1: Set test mode as complete. Do this once all the tests are done. This should be done before the device leaves the factory. Once the test mode is marked as complete, the device will not be able to enter the test mode again.\n• Default ssid: test_complete\n• Default panid: 0x198F\n• Default mac: 1212121212121212\n• Default id: 00_00\n\n• 2: Boot into the ota_1 partition to perform custom tests. The device should be booted back into the ota_0 partition before the device leaves the factory.\n• Default ssid: test_ota_1\n• Default panid: 0x198F\n• Default mac: 2323232323232323\n• Default id: 00_03\n\n"

# Test Mode -> BLE
test_mode_ble = description.test_mode_ble
test_mode_ble.update(test_mode)
test_mode_ble.title = "Test Mode: BLE"
test_mode_ble.section = "Test Mode"
test_mode_ble.description = "BLE related test modes"
test_mode_ble.example = ['{"type": "ezc.test_mode.ble", "subtype": 1}']

test_mode_ble.type.title = "Type"
test_mode_ble.type.description = "Test Mode type: ezc.test_mode.ble"
test_mode_ble.subtype.title = "Subtype"
test_mode_ble.subtype.description = "Test type:\n• 1: Broadcast the MAC address over BLE. This can be helpful to fetch the QR code for the device on the manufacturing line.\n• Default ssid: test_ble_mac\n• Default panid: 0x198F\n• Default mac: 3434343434343434\n• Default id: 00_01\n\n"

# Test Mode -> Sniffer
test_mode_sniffer = description.test_mode_sniffer
test_mode_sniffer.update(test_mode)
test_mode_sniffer.title = "Test Mode: Sniffer"
test_mode_sniffer.section = "Test Mode"
test_mode_sniffer.description = "Sniffer related test modes"
test_mode_sniffer.example = ['{"type": "ezc.test_mode.sniffer", "subtype": 1}']

test_mode_sniffer.type.title = "Type"
test_mode_sniffer.type.description = "Test Mode type: ezc.test_mode.sniffer"
test_mode_sniffer.subtype.title = "Subtype"
test_mode_sniffer.subtype.description = "Test type:\n• 1: Broadcast the MAC address using sniffer. This can be helpful to fetch the QR code for the device on the manufacturing line.\n• Default ssid: test_sniffer_mac\n• Default panid: 0x198F\n• Default mac: 4545454545454545\n• Default id: 00_02\n\n"

# Test Mode -> Light
test_mode_light = description.test_mode_light
test_mode_light.update(test_mode)
test_mode_light.title = "Test Mode: Light"
test_mode_light.section = "Test Mode"
test_mode_light.description = "Light related test modes"
test_mode_light.example = ['{"type": "ezc.test_mode.light", "subtype": 1, "interval_time_ms": 2000, "loop_count": 2, "r_time_s": 1, "g_time_s": 2, "b_time_s": 3, "w_time_s": 4, "c_time_s": 5}']

test_mode_light.type.title = "Type"
test_mode_light.type.description = "Test Mode type: ezc.test_mode.light"
test_mode_light.subtype.title = "Subtype"
test_mode_light.subtype.description = "Test type:\n• 1: Light test case 1. The light cycles through different colors.\n• Default ssid: test_light_1\n• Default panid: 0x198F\n• Default mac: 5656565656565656\n• Default id: 01_01\n\n• 2: Light test case 2. The light cycles through different colors.\n• Default ssid: test_light_2\n• Default panid: 0x198F\n• Default mac: 7878787878787878\n• Default id: 01_02\n\n• 3: Light test case 3. The light cycles through different colors.\n• Default ssid: test_light_3\n• Default panid: 0x198F\n• Default mac: 9090909090909090\n• Default id: 01_03\n\n• 4: Light test case 4. The light automatically finish color cycle test and aging test.\n• Default ssid: test_light_4\n• Default panid: 0x198F\n• Default mac: 0A0A0A0A0A0A0A0A\n• Default id: 01_04\n\n"
test_mode_light.interval_time_s.title = "Interval time (in seconds)"
test_mode_light.interval_time_s.description = "Interval time (in seconds) between displaying various colors, defualt is 1000ms"
test_mode_light.loop_count.title = "loop count"
test_mode_light.loop_count.description = "The number of cycles, default is 10"
test_mode_light.r_time_s.title = "Red time (in seconds)"
test_mode_light.r_time_s.description = "The duration for red color to stay displayed (in seconds), default is 10 minutes"
test_mode_light.g_time_.title = "green time (in seconds)"
test_mode_light.g_time_s.description = "The duration for green color to stay displayed (in seconds), default is 10 minutes"
test_mode_light.b_time_s.title = "blue time (in seconds)"
test_mode_light.b_time_s.description = "The duration for blue color to stay displayed (in seconds), default is 10 minutes"
test_mode_light.w_time_s.title = "warm time (in seconds)"
test_mode_light.w_time_s.description = "The duration for warm color to stay displayed (in seconds), default is 10 minutes"
test_mode_light.c_time_s.title = "cold time (in seconds)"
test_mode_light.c_time_s.description = "The duration for cold color to stay displayed (in seconds), default is 10 minutes"

# Test Mode -> Socket
test_mode_socket = description.test_mode_socket
test_mode_socket.update(test_mode)
test_mode_socket.title = "Test Mode: Socket"
test_mode_socket.section = "Test Mode"
test_mode_socket.description = "Socket related test modes"
test_mode_socket.example = ['{"type": "ezc.test_mode.socket", "subtype": 1}']

test_mode_socket.type.title = "Type"
test_mode_socket.type.description = "Test Mode type: ezc.test_mode.socket"
test_mode_socket.subtype.title = "Subtype"
test_mode_socket.subtype.description = "Test type:\n• 1: All sockets turn on and off, 3 times\n• Default ssid: test_socket_1\n• Default panid: 0x198F\n• Default mac: ABABABABABABABAB\n• Default id: 02_01\n\n• 2: All sockets change the level from 0 to 100 and back to 0\n• Default ssid: test_socket_2\n• Default panid: 0x198F\n• Default mac: CDCDCDCDCDCDCDCD\n• Default id: 02_02\n\n"

# Test Mode -> Window Covering
test_mode_window_covering = description.test_mode_window_covering
test_mode_window_covering.update(test_mode)
test_mode_window_covering.title = "Test Mode: Window Covering"
test_mode_window_covering.section = "Test Mode"
test_mode_window_covering.description = "Window covering related test modes"
test_mode_window_covering.example = ['{"type": "ezc.test_mode.window_covering", "subtype": 1}']

test_mode_window_covering.type.title = "Type"
test_mode_window_covering.type.description = "Test Mode type: ezc.test_mode.window_covering"
test_mode_window_covering.subtype.title = "Subtype"
test_mode_window_covering.subtype.description = "Test type:\n• 1: The window covering moves up and down alternatively, 3 times.\n• Default ssid: test_window_covering_1\n• Default panid: 0x198F\n• Default mac: EFEFEFEFEFEFEFEF\n• Default id: 03_01\n\n"
