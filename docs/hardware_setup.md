# Hardware Setup

* [Hardware Setup](#hardware-setup)
* [Port Permissions for USB to Serial Converters](#port-permissions-for-usb-to-serial-converters)
* [Driver Installation](#driver-installation)
* [Linux](#1-linux)
* [MacOS](#2-macos)
* [Windows](#3-windows)

## Port Permissions for USB to Serial Converters

This guide provides instructions on how to set up the correct port permissions for ESP32 boards with USB to serial converters, ensuring proper access to the serial port for communication on different operating systems (Linux, macOS, and Windows).

> Note: Make sure that the jumpers on your ESP32-C6 DevKit are properly set. Without the correct jumper configuration, flashing the board will fail.

---

### Driver Installation

Most ESP32 boards use one of the following USB to serial converter chips:

* **CP210x**:
  For CP210x USB to UART Bridge, download the necessary drivers from the official Silicon Labs site:  
  [CP210x USB to UART Bridge VCP Drivers](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads)

* **FTDI**:
  For FTDI USB to UART converters, download the drivers from the official FTDI website:
  [FTDI Virtual COM Port Drivers](https://ftdichip.com/drivers/vcp-drivers/)

For more information, refer to the Espressif documentation: [ESP32 Serial Connection Guide](https://docs.espressif.com/projects/esp-idf/en/release-v5.3/esp32c6/get-started/establish-serial-connection.html)

To ensure the current user has the proper permissions to access the serial port over USB, follow the appropriate steps below based on your operating system.

---

### 1. **Linux**

On most Linux distributions, you need to add your user to the **dialout** group to have the necessary permissions for accessing the serial port.

**Steps:**

1. Open a terminal.
2. Run the following command to add your user to the dialout group:

   ```bash
   sudo usermod -a -G dialout $USER
   ```

### 2. **MacOS**

On MacOS, the system should automatically recognize the USB to serial converter. However, if you face permission issues, you may need to ensure the correct device permissions are set.

(Note: MacOS should automatically handle the driver installation for common USB to serial chips like CP210x or FTDI, but you can manually install drivers if needed.)

**Steps:**

1. Plug in your ESP32 board via USB.
2. Check which device the board is connected to by running:

    ```bash
    ls /dev/cu.*
    ```

3. The ESP32 board should show up as something like /dev/cu.usbserial-XXXXX. If you're encountering permission issues, you can adjust the device's access using the following command:

    ```bash
    sudo chmod 666 /dev/cu.usbserial-XXXXX
    ```

    Replace XXXXX with the actual serial port identifier.

### 3. Windows

On Windows, most ESP32 boards with USB to serial converters (like CP210x or FTDI) should automatically install the necessary drivers. If you experience issues with port access, you may need to manually configure the device.

**Steps:**

1. Ensure that you have installed the correct drivers for your USB to serial converter. Download the drivers for your chip:

    * **CP210x**:
      For CP210x USB to UART Bridge, download the necessary drivers from the official Silicon Labs site:  
      [CP210x USB to UART Bridge VCP Drivers](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads)

    * **FTDI**:
      For FTDI USB to UART converters, download the drivers from the official FTDI website:
      [FTDI Virtual COM Port Drivers](https://ftdichip.com/drivers/vcp-drivers/)

2. Once the drivers are installed, open Device Manager (press Win + X and select Device Manager).

3. Locate the Ports (COM & LPT) section and ensure that your ESP32 board appears there as a COM port (e.g., COM3 or COM4).

4. Right-click the device, select Properties, and check the Port Settings to ensure correct configuration.
