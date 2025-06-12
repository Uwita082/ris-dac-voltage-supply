import spidev                   # type: ignore[import]
import RPi.GPIO as GPIO         # type: ignore[import]

from src.protocol.protocol_interface import ProtocolInterface


class ProtocolSpiDev(ProtocolInterface):
    def __init__(self, bus: int = 0, device: int = 0, max_speed_hz: int = 25000000, cs_pin: int = 8):
        self.bus = bus
        self.device = device
        self.max_speed_hz = max_speed_hz
        self.cs_pin = cs_pin
        self.spi = spidev.SpiDev()

    def open(self) -> None:
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.cs_pin, GPIO.OUT, initial=GPIO.HIGH)  # CS inactive initially
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = self.max_speed_hz
        self.spi.mode = 0b00  # Adjust if needed

    def close(self) -> None:
        self.spi.close()
        GPIO.cleanup(self.cs_pin)

    def set_cs(self, value: bool) -> None:
        pass
        # Active-low logic: CS LOW to enable
        # GPIO.output(self.cs_pin, GPIO.LOW if value else GPIO.HIGH)

    def write(self, byte_list: bytearray) -> None:
        self.spi.xfer2(list(byte_list))