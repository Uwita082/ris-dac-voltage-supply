# PCB Project Overview

This folder contains the essential design and configuration files for the PCB project. Below is a breakdown of the contents and their purpose, along with tables for component reference and system functionality.

## 📁 Folder Contents

- `./Gerber_PCB_Research Project.zip`  
  Directory containing all the necessary Gerber files required for PCB fabrication.

- `./PCB_PCB_Research Project_2025-06-20.json`  
  A JSON configuration file for importing the board design into [EasyEDA](https://easyeda.com) or other compatible EDA tools.

- `./PCB_Assembly_Research Project_2025-06-20.pdf`  
  A PDF showing the PCB footprint, including designator labels for all components to aid in manual placement or inspection.

## 📋 Bill of Materials (BOM)

Below is a placeholder BOM table listing the components used on the board based on their designators.

| **ID** | **Designator** | **Part Description** | **Footprint** |
|--------|----------------|----------------------|----------------|
| **1** | C1, C47 | Ceramic Capacitor 22μF, 25V | 1206 (3216 Metric) |
| **2** | C2, C48 | Ceramic Capacitor 22nF, 25V | 0603 (1608 Metric) |
| **3** | C3, C4 | Ceramic Capacitor 0.01μF, 25V | 0402 (1005 Metric) |
| **4** | C7 | Ceramic Capacitor 0.01μF, 10V | 0402 (1005 Metric) |
| **5** | C8 | Ceramic Capacitor 10μF, 10V | 0402 (1005 Metric) |
| **6** | C9 | Ceramic Capacitor 0.1μF, 25V | 0402 (1005 Metric) |
| **7** | C10, C11, C12, C14, C22 | Ceramic Capacitor 0.1μF, 25V | 0603 (1608 Metric) |
| **8** | C23, C24, C25, C26, C29, C30, C32, C33, C46 | Ceramic Capacitor 0.1μF, 10V | 0402 (1005 Metric) |
| **9** | C19, C20, C21 | Ceramic Capacitor 2.2μF, 25V | 0805 (2012 Metric) |
| **10** | C38, C39, C40, C41, C42, C43, C44, C45 | Ceramic Capacitor 1μF, 25V | 0603 (1608 Metric) |
| **11** | C16, C27, C28, C31, C34, C35, C36, C37 | Ceramic Capacitor 1μF, 10V | 0603 (1608 Metric) |
| **12** | C5, C6, C13, C15, C50, C51 | Ceramic Capacitor 10μF, 25V | 1206 (3216 Metric) |
| **13** | C17, C18 | Ceramic Capacitor 4.7μF, 25V | 0603 (1608 Metric) |
| **14** | C49 | Ceramic Capacitor 10μF, 10V | 1206 (3216 Metric) |
| **15** | Q1, Q2, Q3, Q4 | MOSFET 2N7002 | SOT-23_L2.9-W1.3-P0.95-LS2.4-BR |
| **16** | LED1, LED2, LED3, LED4 | Red, clear, light emitting diode (LED) | 0603 (1608 Metric) |
| **17** | R1, R2 | Resistor 1%, 1/10 W, 53.6k | 0603 (1608 Metric) |
| **18** | R3 | Resistor 1%, 1/10 W, 210k | 0603 (1608 Metric) |
| **19** | R4 | Resistor 1%, 1/10 W, 226k | 0603 (1608 Metric) |
| **20** | R5, R8 | Resistor 1%, 1/10 W, 64.9k | 0603 (1608 Metric) |
| **21** | R6, R7 | Resistor 1%, 1/10 W, 4.7k | 0603 (1608 Metric) |
| **22** | R9, R17, R18, R22 | Resistor 1%, 1/10 W, 1k | 0603 (1608 Metric) |
| **23** | R10 | Resistor 1%, 1/10 W, 2000k | 0603 (1608 Metric) |
| **24** | R11, R12, R13, R14, R15, R16, R19, R20, R21, R23, R24, R25 | Resistor 1%, 1/10 W, 4.99k | 0603 (1608 Metric) |
| **25** | R27, R28 | Resistor 1%, 1/10 W, 200k | 0603 (1608 Metric) |
| **26** | R29, R30, R31, R32 | Resistor 1%, 1/10 W, 10k | 0603 (1608 Metric) |
| **27** | U1 | LTM8049EY#PBF | BGA-77_L15.0-W9.0-R11-C7-P1.27-TL |
| **28** | U2 | LT3032EDE#PBF | DFN-14_L4.0-W3.0-P0.50-BL_ADI_DE14MA |
| **29** | U3 | LT1763IDE-5#PBF | DFN-12_L4.0-W3.0-P0.50-BL-EP |
| **30** | U4 | LT6656BCDC-4.096#TRMPBF | TSOT-23-6_L2.9-W1.6-P0.95-LS2.8-BR |
| **31** | U5 | LTC6900CS5#TRPBF | SOT-23-5_L3.0-W1.7-P0.95-LS2.8-BL |
| **32** | U6, U11, U13, U17 | LTC2688CUJ-12#PBF | QFN-40_L6.0-W6.0-P0.50-TL-EP4.5-1 |
| **33** | U8, U12, U14, U36 | DAC debug pins, FAULT and MUX | 2 pin connector |
| **34** | U7, U10, U16, U20, U39, U40, U41, U42 | DAC output | 8 pin connector |
| **35** | U15 | LTM8049 power good debug | 2 pin connector |
| **36** | U9, U18, U19, U21, U22, U23, U32, U33, U34, U35, U37, U45 | Jumper selection | 3 pin connector with jumper |
| **38** | U24, U26, U27, U28, U29, U30, U31, U43 | Terminal Turret Connector Single End 3.96mm Tin | 1593-2 |
| **39** | U44 | SPI header | 8 pin connector |
| **40** | CN1, CN2 | Banana Jack Connector Standard | 575-4 |

## ⚙️ System Function Table

This section explains key components by their designators and describes their function in the system, including how they may be configured or used during operation.

| **Designator** | **Part Name** | **Part Description** |
|----------------|---------------|------------------------|
| CN1, U29 | VIN | Primary power input for the board. Accepts a voltage in the range of 3.7 V to 18 V to supply power to all board components. |
| CN2, U31, U43 | GND | Common electrical ground reference for all power and signal circuits. |
| U24 | V- | External negative analog supply rail for the LTC2688 DACs. To activate, set jumper U19 to the EXT position. Recommended input range: -17.5 V to -22 V. |
| U27 | V+ | External positive analog supply rail for the LTC2688 DACs. To activate, set jumper U18 to the EXT position. Recommended input range: +17.5 V to +22 V. |
| U26 | V_REF (VREF) | External voltage reference input for the LTC2688 DACs. Activate by setting jumper U22 and jumpers U32–U35 to EXT. Acceptable input range is -0.3 V to VCC. |
| U28 | V_LOGIC (VCC) | External Analog logic voltage supply for the LTC2688s. Connect via jumper U23 set to EXT. Operates within 4.75 V to 5.25 V. |
| U30 | TRIG | External square wave signal input used to toggle between registers in the LTC2688 during toggle mode. The signal should swing between 0 V and IOVCC (determined by U44’s SPI header). |
| U44 | SPI Interface and IOVCC | Provides SPI control signals: CS, SCK, MOSI, MISO, LDAC, CLR, VCC, and GND. VCC defines the digital logic level for the LTC2688s. If U45 is set to EXT, VCC is supplied externally via SPI header. If unavailable, set U45 to INT to use internal voltage. |
| U15 | LTM8049 PG Debug | Provides two Power-Good (PG) indicators for positive and negative rails, signaling proper operation of the LTM8049 module. Outputs reflect VIN level when operating correctly. |
| U8, U12, U14, U36 | LTC2688 MUX and FAULT Pins | Each LTC2688 has dedicated FAULT and MUX pins. The FAULT pin is pulled up to IOVCC and indicates error status. When triggered, corresponding LEDs (LED1–LED4) are activated. MUX pin allows channel selection via SPI. |
| U7, U10, U16, U20, U39, U40, U41, U42 | OUT0–OUT63 | Analog voltage outputs from each DAC channel on the LTC2688 devices in daisy-chain configuration. |
| U9 | Daisy-Chain Selector | Sets board daisy-chain functionality. Leave jumper at NC for standalone mode. Set to C when chaining multiple boards. |
| U45 | IOVCC Selector | Supplies digital logic voltage for the LTC2688s. Select EXT to use voltage from SPI header. Select INT to use internal VCC (analog logic supply). Voltage must be less than analog VCC and greater than 1.71 V. |
| U21 | TRIG Selector | Routes toggle signal (TGP0) to LTC2688s. Select EXT to use external signal via U30. Select INT to use internal oscillator from LTC6900. |
| U22 | VREF Selector | Configures voltage reference source for LTC2688 DACs. Set to EXT to use external reference from U26. Set to INT to use on-board LT6656 reference. |
| U23 | VCC Selector | Configures analog logic supply source for the LTC2688s. Set to EXT for external 5 V source. Set to INT to use on-board LT1763 regulator. |
| U37 | LTC6900 Frequency Selector | Determines frequency of the internal LTC6900 oscillator. Set to N=100 for 1 kHz, leave jumper open for 10 kHz, or set to N=1 for 100 kHz output. |
| U19 | V- Selector | Selects source for negative analog rail of the LTC2688s. Set to EXT for external supply or INT to use LTM8049 rail via LT3032. |
| U18 | V+ Selector | Selects source for positive analog rail of the LTC2688s. Set to EXT for external supply or INT to use LTM8049 rail via LT3032. |
| U32, U33, U34, U35 | Reference Voltage Selector | Selects voltage reference (internal or external) for each LTC2688. Set to INT for internal DAC reference, or EXT to use shared V_REF input. |

## 🛠️ Notes

- Please ensure the Gerber files are verified with your PCB manufacturer before ordering.
- When importing the `./PCB_PCB_Research Project_2025-06-20.json` into EasyEDA, double-check footprint scaling and layer alignment.
- The `./PCB_PCB_Research Project_2025-06-20.json` file is provided to assist in manual assembly or inspection of component placement.