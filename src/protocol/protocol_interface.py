from abc import ABC, abstractmethod

# Define an abstract class
class ProtocolInterface(ABC):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def set_cs(self, value: bool) -> None:
        pass

    @abstractmethod
    def write(self, byte_list: bytearray)  -> None:
        pass