import spidev                   # type: ignore[import]

from src.protocol.protocol_interface import ProtocolInterface


class ProtocolSpiDev(ProtocolInterface):
    def __init__(self, bus: int = 0, device: int = 0, max_speed_hz: int = 25000000):
        self.bus = bus
        self.device = device
        self.max_speed_hz = max_speed_hz
        self.spi = spidev.SpiDev()

    def open(self) -> None:
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = self.max_speed_hz
        self.spi.mode = 0b00  # Adjust if needed

    def close(self) -> None:
        self.spi.close()

    def write(self, byte_list: bytearray) -> None:
        self.spi.xfer2(list(byte_list))