# LTC2688 SPI Control with Raspberry Pi Pico

This project is a C-based firmware for the Raspberry Pi Pico that interfaces with four **LTC2688** DACs in a daisy-chained SPI configuration. It initializes the DACs with configuration commands and continuously toggles voltage outputs to measure timing performance using an oscilloscope.

## 🧰 Hardware Setup

- **Microcontroller**: Raspberry Pi Pico
- **DACs**: 4x LTC2688 (16-channel, 16-bit, ±15V DAC)
- **Interface**: SPI (daisy chain)
- **SPI Pins**:
  - `SCK`: GPIO 2
  - `MOSI`: GPIO 3
  - `MISO`: GPIO 4
  - `CS`: GPIO 5

## 📦 Features

- Configures each LTC2688 with:
  - Output span: **±15V** (`SPAN = 7`)
  - Toggle function set to `TG0`, but not enabled yet
  - All Register B values initialized to code `2048` (0V output)
- Sends fast voltage update commands to DAC channels for timing measurement
- Optional test for full write throughput with all commands

## 📂 File Overview

- `main.c`: Contains the SPI configuration, command structure, and main control logic
