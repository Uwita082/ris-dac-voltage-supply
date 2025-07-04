from protocol.protocol_mock import ProtocolMock
from protocol.protocol_pico import ProtocolSpiPico


class Protocol:
    _protocol: ProtocolMock | ProtocolSpiPico

    def __init__(self):
        self._protocol = ProtocolSpiPico()

        self._protocol.open()

    def write(self, byte_list: bytearray) -> None:
        if len(byte_list) % 4 != 0:
            raise ValueError("The length of the given byte array is not divisible by 32.")

        self._protocol.write(byte_list)

    def close(self):
        self._protocol.close()