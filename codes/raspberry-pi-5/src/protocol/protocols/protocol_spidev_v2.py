import spidev                   # type: ignore[import]
import gpiod                    # type: ignore[import]

from src.protocol.protocol_interface import ProtocolInterface

class ProtocolSpiDev2(ProtocolInterface):
    def __init__(self, bus: int = 0, device: int = 0, max_speed_hz: int = 25000000, cs_pin_offset: int = 8, chip_name: str = "gpiochip0"):
        self.bus = bus
        self.device = device
        self.max_speed_hz = max_speed_hz
        self.cs_pin_offset = cs_pin_offset
        self.chip_name = chip_name
        self.spi = spidev.SpiDev()
        self.line = None

    def open(self) -> None:
        # Open SPI and disable automatic CS
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = self.max_speed_hz
        self.spi.mode = 0b00
        self.spi.no_cs = True

        # Setup gpiod line for manual CS control
        chip = gpiod.Chip(self.chip_name)
        self.line = chip.get_line(self.cs_pin_offset)
        self.line.request(consumer="spi-cs", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[1])

    def close(self) -> None:
        self.spi.close()
        if self.line:
            self.line.set_value(1)  # CS HIGH
            self.line.release()

    def write(self, byte_list: bytearray) -> None:
        self.line.set_value(0)
        self.spi.xfer2(list(byte_list))
        self.line.set_value(1)