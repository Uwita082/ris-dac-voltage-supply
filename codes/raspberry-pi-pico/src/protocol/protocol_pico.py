from machine import SPI, Pin        # type: ignore[import]


class ProtocolSpiPico:
    def __init__(
        self,
        spi_id: int = 0,
        baudrate: int = 30000000,
        sck_pin: int = 2,
        mosi_pin: int = 3,
        miso_pin: int = 4,
        cs_pin: int = 5
    ):
        self.spi_id = spi_id
        self.baudrate = baudrate
        self.sck_pin = sck_pin
        self.mosi_pin = mosi_pin
        self.miso_pin = miso_pin
        self.cs_pin = cs_pin

        self.spi: SPI = None
        self.cs: Pin = None

    def open(self) -> None:
        self.spi = SPI(
            self.spi_id,
            baudrate=self.baudrate,
            polarity=0,
            phase=0,
            bits=8,
            firstbit=SPI.MSB,
            sck=Pin(self.sck_pin),
            mosi=Pin(self.mosi_pin),
            miso=Pin(self.miso_pin)
        )
        self.cs = Pin(self.cs_pin, Pin.OUT)
        self.cs.value(1)

    def close(self) -> None:
        if self.spi:
            self.spi.deinit()
            self.spi = None
        if self.cs:
            self.cs.value(1)
            self.cs = None

    def write(self, byte_list: bytearray) -> None:
        if not self.spi or not self.cs:
            raise RuntimeError("SPI interface not open.")
        self.cs.value(0)
        self.spi.write(byte_list)
        self.cs.value(1)