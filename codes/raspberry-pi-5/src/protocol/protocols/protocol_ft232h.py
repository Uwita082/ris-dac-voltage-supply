from src.protocol.protocol_interface import ProtocolInterface
from typing import Optional
import board
import busio
import digitalio
import time

dir(board)


class ProtocolFT232H(ProtocolInterface):
    def __init__(self):
        self.spi: Optional[busio.SPI] = None
        self.cs: Optional[digitalio.DigitalInOut] = None

    def open(self) -> None:
        self.spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        self.cs = digitalio.DigitalInOut(board.C0)
        self.cs.direction = digitalio.Direction.OUTPUT
        self.cs.value = True

        # Wait for SPI to be ready
        while not self.spi.try_lock():
            pass

        self.spi.configure(baudrate=25000000, phase=0, polarity=0)

    def close(self) -> None:
        if self.spi is not None:
            self.spi.unlock()
            self.spi.deinit()

        if self.cs is not None:
            self.cs.deinit()

        self.spi = None
        self.cs = None

    def write(self, byte_list: bytearray) -> None:
        if self.cs is None or self.spi is None:
            self.close()
            raise Exception("SPI communication has not been set up successfully")

        self.cs.value = False
        self.spi.write(byte_list)
        self.cs.value = True
