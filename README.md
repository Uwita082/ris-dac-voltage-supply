# Voltage Supply for Liquid Crystal Reconfigurable Intelligent Surface Biasing

This project implements a high-speed, scalable voltage supply control system using four LTC2688 DACs in daisy-chain SPI configuration. It is designed to provide precise voltage control for LC-RIS (Liquid Crystal Reconfigurable Intelligent Surface) applications, using modular hardware and software components.

For a complete explanation of the **design methodology**, **system behavior**, and **response time** analysis between the high-level and low-level implementations included in this repository, please refer to the accompanying research paper:

📄[Read the Research Paper](https://example.com)

_(Includes design choices, system analysis, and benchmarking results)_

### Technical Requirements

## 📁 PCB

Contains all necessary files for PCB fabrication and component placement:
- **Gerber files** for board manufacturing.
- **Footprint schematics** for precise layout and reference.
- **Bill of Materials (BOM)** for easy component sourcing and assembly.

## 📁 Circuit Schematic

Includes detailed circuit schematics showing:
- The configuration of the four **LTC2688** DACs in **daisy-chain SPI mode**.
- Power distribution components used for supply regulation.
- Interfacing between the control system (MCU or PC) and the DACs via SPI.
- Connection of an **oscillator** to the **toggle** pin of the LTC2688 to enable automatic switching between two voltage levels (Toggle A and Toggle B), allowing the generation of square waveforms in hardware.

## 📁 Simulations

LTSpice simulation files used to:
- Test and validate the on-board power supply performance.
- Test and validate the on-board oscillator performance.
- Evaluate design correctness under varying conditions.
- Reduce trial-and-error in hardware prototyping.

## 📁 Codes

High-level **Python** codebase with object-oriented architecture:
- Interfaces for Raspberry Pi Pico, Raspberry Pi 5, and PC with FT232H USB-to-SPI.
- Strategy pattern to dynamically select the correct SPI implementation.
- A queue-based system efficiently tracks and updates only the required DAC channels.
- Designed for maintainability, flexibility, and easy scaling.

## 📁 Script

Low-level implementation in **Python** and **C** focused on performance:
- Interfaces for Raspberry Pi Pico, Raspberry Pi 5, and PC with FT232H USB-to-SPI.
- Direct raw-byte command sequences for updating DACs.
- Minimal overhead to maximize SPI communication speed.
- Intended for time-sensitive deployment scenarios.
- Less readable, but significantly faster in response time (see paper for benchmarks).

## License

This project is licensed under the MIT License. See the [LICENSE](raspberry-pi-5/LICENSE) file for details.
