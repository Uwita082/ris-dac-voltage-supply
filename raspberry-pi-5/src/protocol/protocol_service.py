from src.protocol.protocol_interface import ProtocolInterface
from src.protocol.protocols.protocol_ft232h import ProtocolFT232H
from src.protocol.protocols.protocol_mock import ProtocolMock


class Protocol:
    _protocol: ProtocolInterface

    def __init__(self):
        self._protocol = ProtocolMock()

        self._protocol.open()

    def write(self, byte_list: bytearray) -> None:
        if len(byte_list) % 4 != 0:
            raise ValueError("The length of the given byte array is not divisible by 32.")

        self._protocol.write(byte_list)     # Send all bytes

    def close(self):
        self._protocol.close()