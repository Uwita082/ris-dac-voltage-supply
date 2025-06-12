import time

from src.protocol.protocol_interface import ProtocolInterface
from src.protocol.protocol_mock import ProtocolMock
from src.protocol.protocol_spidev import ProtocolSpiDev


class Protocol:
    _protocol: ProtocolInterface
    _t5 = 8e-9                              # CS/LD pulse width
    _t6 = 5e-9                              # LSB SCK high to CS/LD high
    _t7 = 5e-9                              # CS/LD low to SCK high

    def __init__(self):
        self._protocol = ProtocolSpiDev()

        self._protocol.open()

    def write(self, byte_list: bytearray) -> None:
        if len(byte_list) % 4 != 0:
            raise ValueError("The length of the given byte array is not divisible by 32.")

        # self._protocol.set_cs(False)        # Set CS to low
        # time.sleep(self._t7)                # Wait CS/LD low to SCK high

        self._protocol.write(byte_list)     # Send all bytes
        #
        # time.sleep(self._t6)                # Wait LSB SCK high to CS/LD high
        # self._protocol.set_cs(True)         # Set CS to low
        # time.sleep(self._t5)                # Wait CS/LD pulse width for next transaction

    def close(self):
        self._protocol.close()