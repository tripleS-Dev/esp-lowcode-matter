from dotmap import DotMap

description = DotMap()
zerocode_product = description.zerocode_product

zerocode_product.title = "ZeroCode Product Configuration"
zerocode_product.description = "The ZeroCode Product Configurations is divided into the following sections:\n• **Pre Driver:** These are things which are initialised even before the device drivers are initialised. This is done at the very start of the bootup. This includes power related and communication related initialisations.\n• **Driver:** The drivers are initialised at this stage. This include the lower level drivers like, button, LED, etc. They are then used/linked later in the configuration based on their Driver IDs.\n• **Product Common:** This includes things which are common to the product as a whole. The drivers which are initialised before are used here.\n• **Product:** This represents the actual product and how it is shown in the Ecosystems. Example, to create a 2 channel socket, the socket must be present 2 times here. The drivers which are initialised before are used here.\n• **Test Mode:** These initialise the test modes that can be performed in the factory during manufacturing. If enabled, they need to be marked as completed before the device leaves the factory. Until then, the device checks for the trigger for the test modes on bootup.\n"

zerocode_product.example = ['{"config_version":3,"driver":[{"id":1000,"type":"ezc.driver.button","name":"gpio","gpio_config":{"gpio_num":9,"active_level":0,"long_press_time":5}},{"id":1001,"type":"ezc.driver.relay","name":"gpio","gpio_config":{"gpio_num":10,"active_level":0}},{"id":1002,"type":"ezc.driver.led","name":"gpio","gpio_config":{"gpio_num":8,"active_level":0}}],"product_common":[{"type":"ezc.product_common.indicator","driver":{"output":1002},"events":[{"name":"setup_mode_start","mode":"blink","speed":4000,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":0},{"name":"setup_started","mode":"blink","speed":1000,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":0},{"name":"setup_successful","mode":"restore"},{"name":"setup_failed","mode":"restore"},{"name":"setup_mode_end","mode":"restore"},{"name":"ready","mode":"restore"},{"name":"identification_start","mode":"blink","speed":1000,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":0},{"name":"identification_stop","mode":"restore"},{"name":"identification_blink","mode":"blink","speed":1000,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":1000},{"name":"identification_breathe","mode":"blink","speed":1000,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":15000},{"name":"identification_okay","mode":"blink","speed":700,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":1400},{"name":"identification_channel_change","mode":"blink","speed":8000,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":8000},{"name":"identification_finish_effect","mode":"restore"},{"name":"identification_stop_effect","mode":"restore"},{"name":"factory_reset_triggered","mode":"blink","speed":400,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":0},{"name":"forced_rollback_triggered","mode":"blink","speed":400,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":0},{"name":"driver_mode","mode":"blink","speed":1000,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":0},{"name":"test_mode_start","mode":"blink","speed":500,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":1500},{"name":"test_mode_complete","mode":"blink","speed":500,"color_select":2,"cct":50,"min_brightness":20,"max_brightness":100,"total_ms":3000}]},{"type":"ezc.product_common.factory_reset","subtype":2,"driver":{"input":1000},"auto_trigger":true}],"product":[{"type":"ezc.product.socket","subtype":1,"driver":{"input":1000,"output":1001,"indicator":1002},"data_model":{"power_default":1,"power_bootup":-1}}],"test_mode":[{"type":"ezc.test_mode.common","subtype":1},{"type":"ezc.test_mode.ble","subtype":1},{"type":"ezc.test_mode.socket","subtype":1}]}']
zerocode_product.config_version.title = "Config Version"
zerocode_product.config_version.description = "Product configuration version"

zerocode_product.pre_driver.title = "Pre Driver"
zerocode_product.pre_driver.description = "Peripheral settings required before initialising the drivers"

zerocode_product.driver.title = "Driver"
zerocode_product.driver.description = "Contains the Driver specifications"

zerocode_product.product_common.title = "Product Common"
zerocode_product.product_common.description = "Common product configurations"

zerocode_product.product.title = "Product"
zerocode_product.product.description = "Product specifications and configurations"

zerocode_product.test_mode.title = "Test Mode"
zerocode_product.test_mode.description = "Testing configurations"

zerocode_product.device_management.title = "Device Management"
zerocode_product.device_management.description = "Device Managmenet description"
