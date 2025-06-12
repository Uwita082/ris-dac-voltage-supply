from src.protocol.protocol_interface import ProtocolInterface


class ProtocolMock(ProtocolInterface):
    def open(self) -> None:
        pass

    def close(self) -> None:
        pass

    def write(self, byte_list: bytearray)  -> None:
        print(byte_list)
        bits = ''.join(f'{byte:08b}' for byte in byte_list)
        print(bits)
        print("\n")