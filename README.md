# SPI Interface for LTC2688 DAC

A Python 3.9 library to control the Linear Technology LTC2688 digital-to-analog converter via SPI. Supports daisy-chaining multiple LTC2688 devices, and can be used on Raspberry Pi (using `spidev`) or on Windows with import ignore for static analysis tools.

---

## Features

* Send commands and data to one or multiple LTC2688 DACs in a daisy-chain configuration.
* Simple `ProtocolInterface` abstraction for opening, closing, setting chip select, and writing data.
* Out-of-the-box support for Raspberry Pi via `spidev`.

---

## Requirements

* Python 3.9
* On Raspberry Pi: `spidev` and `RPi.GPIO` libraries

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/ltc2688-spi-interface.git
   cd ltc2688-spi-interface
   ```

2. (Raspberry Pi only) Install dependencies:

   ```bash
   sudo apt update
   sudo apt install python3-spidev python3-rpi.gpio
   ```

---

## Usage

## License

This project is licensed under the MIT License. See the [LICENSE](raspberry-pi-5/LICENSE) file for details.
