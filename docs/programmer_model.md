# Programmer's Model

ESP LowCode was born out of the need to contain development complexity that that developers needs to be exposed to, while building connected products. The ESP LowCode project attempts to expose a simpler setup-loop kind of development framework, that reduces development complexity and lightens the debug overhead. This is achieved by utilising the cores in the ESP32-C6 in an asymmetric manner.

The ESP32-C6 microcontroller features two processing cores: the High-Performance (HP) Core and the Low-Power (LP) Core. ESP LowCode assigns a specific purpose in the device’s operation. In ESP LowCode, developers write firmware for the LP Core. They have full control on the firmware running on this core. The firmware runs within a single thread of execution thus simplifying product development considerations. Further, the memory between the two cores is compartmentalised, thus ensuring that one core cannot easily corrupt the memory of the other, thereby reducing debug considerations.

The HP Core does the heavy-lifting of the Matter and the typical operations of connected devices. It is primarily responsible for initializing and managing essential system functions, including the Wi-Fi, Bluetooth, and Matter protocol stacks. Once these systems are initialized, the HP Core also loads the firmware intended for the LP Core into memory. The firmware running on the HP Core is a typical IDF firmware with multiple threads of execution. For a faster edit-debug cycle, ESP LowCode includes a pre-built firmware image for the HP Core that is available in the pre_built_binaries directory.

The two cores communicate with each other using messages. The messages can be sent from the LP Core to the HP Core and vice versa. Refer [ESP AMP](https://github.com/espressif/esp-amp/blob/main/README.md) for more details about the HP Core and LP Core split and the communication model.

In LowCode, the messages are primarily of two types:

1. **Events**: These are system level events that define the state of the device. For example, the HP Core sends an event to the LP Core to indicate that the device is ready. Or the LP Core sends an event to the HP Core to factory reset the device.
2. **Feature Data**: These are updates to the features of the device. For example, the LP Core sends an event to the HP Core when the power state of the device changes. Or HP Core sends a message to the LP Core when some Ecosystem is used to change the power state of the device.

## Related Documents

* [Create LowCode Product](./create_product.md)
* [Getting Started: Codespaces](../README.md)
* [All Documents](./all_documents.md)
