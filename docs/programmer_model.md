# Programmer's Model

The ESP32-C6 microcontroller features two processing cores: the High-Performance (HP) Core and the Low-Power (LP) Core. Each core serves a specific purpose in the device’s operation. The HP Core is primarily responsible for initializing and managing essential system functions, including the Wi-Fi, Bluetooth, and Matter protocol stacks. Once these systems are initialized, the HP Core also loads the firmware intended for the LP Core into memory.

The LP Core, in turn, communicates with the HP Core, enabling event-driven communication where it can both send and receive events to/from the HP Core. The firmware running on the device is specifically designed for the LP Core and is typically flashed using a low-code platform.

The initialization process begins with the HP Core, which sets up the necessary communication protocols and handles the firmware loading for the LP Core. Once the HP Core has completed its tasks, the LP Core is then initialized, ready to execute the firmware that has been loaded into memory.

Refer [ESP AMP](https://github.com/chiragatal/esp-amp/blob/main/README.md) for more details.

## Related Documents

* [Create LowCode Product](./create_product.md)
* [Getting Started: Codespaces](../README.md)
* [All Documents](./all_documents.md)
