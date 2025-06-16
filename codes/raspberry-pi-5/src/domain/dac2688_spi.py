from typing import List, Optional

from src.domain.dac_2688_channel import QueueChannelUpdate, ChannelSettingValue, ChannelWriteValue, ChannelValue
from src.protocol.protocol_service import Protocol
from src.utils.math import map_value


class DAC2688:
    _spi_protocol: Protocol
    _queue_write_commands: QueueChannelUpdate

    _resolution: int
    _no_daisy_chain: int
    _channels: int

    def __init__(self):
        self._spi_protocol = Protocol()

        self._resolution = 12
        self._no_daisy_chain = 4
        self._channels = 16

        self._queue_write_commands = QueueChannelUpdate(self._no_daisy_chain, self._channels)

    def close(self):
        self._spi_protocol.close()

    def run(self):
        # Select input register B of all channels and write the code respective for 0 Volts to it
        self.set_register_b_to_zero()
        #
        # # The TGP0 pin is thus selected as the toggle clock input.
        self.set_settings_dac()

        # Test Analysis of signal quality
        self.set_values_dac(0, 200)
        self.write_all_values_dac()

        # # Test Analysis of square wave
        # # The channels now can be toggled
        # self.enable_all_pins_toggle_mode()
        #
        # self.set_values_dac(0, 2890)
        # self.write_all_values_dac()

        # # Impact of using internal reference
        # self.set_values_dac(0, 0)
        # self.set_values_dac(16, 0)
        # self.set_values_dac(32, 0)
        # self.set_values_dac(48, 0)
        # self.write_all_values_dac()

        # # Analysis of settling time & Analysis Response time
        # while True:
        #     self.set_values_dac(0, 0)
        #     self.write_all_values_dac()
        #     self.set_values_dac(0, 4095)
        #     self.write_all_values_dac()

        # # Analysis Response time
        # while True:
        #     for i in range(64):
        #         self.set_values_dac(i, map_value(i, 0, 63, 0, 4095))
        #     self.write_all_values_dac()
        #
        #     for i in range(64):
        #         self.set_values_dac(i, map_value(i, 0, 63, 4095, 0))
        #     self.write_all_values_dac()



    def update_all_channels(self) -> None:
        list_instructions: bytearray = bytearray([])

        for i in range(self._no_daisy_chain):
            list_instructions += (self._command_update_all_channels())

        self._spi_protocol.write(list_instructions)

    def set_register_b_to_zero(self) -> None:
        code_zero: int = 2048

        list_instructions: bytearray = bytearray([])

        for i in range(self._no_daisy_chain):
            list_instructions += (self._command_write_ab_select_register(65535))

        self._spi_protocol.write(list_instructions)

        list_instructions = bytearray([])

        for i in range(self._no_daisy_chain):
            list_instructions += (self._command_write_code_channel_all(code_zero))

        self._spi_protocol.write(list_instructions)

        list_instructions = bytearray([])

        for i in range(self._no_daisy_chain):
            list_instructions += (self._command_update_all_channels())

        self._spi_protocol.write(list_instructions)

        list_instructions = bytearray([])

        for i in range(self._no_daisy_chain):
            list_instructions += (self._command_write_ab_select_register(0))

        self._spi_protocol.write(list_instructions)

    def set_settings_dac(self) -> None:
        # Sets the span voltage between -15 and +15 Volts
        # Sets TGP0 pin for toggle mode

        list_instructions: bytearray = bytearray([])

        for i in range(self._no_daisy_chain):
            list_instructions += (self._command_write_setting_update_channel_all(0, 0, 0, 0b01, 0b0100))

        self._spi_protocol.write(list_instructions)

    def set_settings_dac_channel(self, channel) -> None:
        list_instructions: bytearray = bytearray([])

        for i in range(self._no_daisy_chain):
            list_instructions += (self._command_write_setting_channel(channel, 0, 0, 0b00, 0b01, 0b0100))

        self._spi_protocol.write(list_instructions)


    def enable_all_pins_toggle_mode(self) -> None:
        list_instructions: bytearray = bytearray([])

        for i in range(self._no_daisy_chain):
            list_instructions += (self._command_write_toggle_enable_register(65535))

        self._spi_protocol.write(list_instructions)

    def set_values_dac(self, channel: int, value: int) -> None:
        if not (0 <= value <= 4095):
            raise ValueError("Data must be in a 12-bit resolution representation.")

        self._queue_write_commands.register_command_write_channel(channel, value)

    def set_setting_dac(self, channel: int, mode: int, dit_ph: int, dit_per: int, td_sel: int, span: int):
        self._queue_write_commands.register_command_setting_channel(channel, mode, dit_ph, dit_per, td_sel, span)

    def write_values_dac(self) -> None:
        list_instructions: Optional[bytearray] = self._retrieve_write_commands()

        if list_instructions is None:
            return

        self._spi_protocol.write(list_instructions)

    def write_all_values_dac(self) -> None:
        flag: bool = True
        while flag:
            list_instructions: Optional[bytearray] = self._retrieve_write_commands()
            if list_instructions is None:
                flag = False
            else:
                self._spi_protocol.write(list_instructions)

    def _retrieve_write_commands(self) -> Optional[bytearray]:
        list_write_commands: List[Optional[ChannelValue]] = self._queue_write_commands.get_command_write()
        list_write_commands.reverse()

        if len(list_write_commands) != self._no_daisy_chain:
            raise ValueError("List of write commands should have the length of the number of daisy chain devices.")

        list_instructions: bytearray = bytearray([])

        for elem in list_write_commands:
            if elem is None:
                list_instructions += self._no_operation()
            else:
                if isinstance(elem, ChannelWriteValue):
                    list_instructions += self._command_write_update_code_channel(elem.channel_index, elem.value_code)
                elif isinstance(elem, ChannelSettingValue):
                    list_instructions += self._command_write_setting_channel(elem.channel_index, elem.mode, elem.dit_ph, elem.dit_per, elem.td_sel, elem.span)
                else:
                    list_instructions += self._no_operation()

        return list_instructions

    def _command_write_code_channel(self, channel: int, data: int) -> bytearray:                     # Command 0
        return self._write_data_to_channel(0b0000, channel, data)

    def _command_update_channel(self, channel: int) -> bytearray:                                    # Command 6
        return self._write_data_to_channel(0b0110, channel, 0)

    def _command_write_update_code_channel(self, channel: int, data: int) -> bytearray:              # Command 4
        return self._write_data_to_channel(0b0100, channel, data)

    def _command_write_code_channel_update_all(self, channel: int, data: int) -> bytearray:          # Command 5
        return self._write_data_to_channel(0b0101, channel, data)

    def _command_update_all_channels(self) -> bytearray:                                             # Command 18
        return self._write_data_to_channel(0b0111, 0b1100, 0)

    def _no_operation(self) -> bytearray:                                                            # Command 32
        return self._write_data_to_channel(0b1111, 0b1111, 0)

    def _command_write_setting_channel(self, channel: int, mode: int, dit_ph: int, dit_per: int, td_sel: int, span: int) -> bytearray:       # Command 1
        return self._write_setting_to_channel(0b0001, channel, mode, dit_ph, dit_per, td_sel, span)

    def _command_write_code_channel_all(self, data: int) -> bytearray:                               # Command 14
        return self._write_data_to_channel(0b0111, 0b1000, data)

    def _command_write_setting_channel_all(self, mode: int, dit_ph: int, dit_per: int, td_sel: int, span: int) -> bytearray:                 # Command 16
        return self._write_setting_to_channel(0b0111, 0b1010, mode, dit_ph, dit_per, td_sel, span)

    def _command_write_setting_update_channel_all(self, mode: int, dit_ph: int, dit_per: int, td_sel: int, span: int) -> bytearray:          # Command 17
        return self._write_setting_to_channel(0b0111, 0b1011, mode, dit_ph, dit_per, td_sel, span)

    def _command_write_ab_select_register(self, channels_selected: int) -> bytearray:                # Command 9
        return self._write_data_setting_to_channel(0b0111, 0b0010, channels_selected)

    def _command_write_toggle_enable_register(self, channels_selected: int) -> bytearray:            # Command 11
        return self._write_data_setting_to_channel(0b0111, 0b0100, channels_selected)

    @staticmethod
    def _write_setting_to_channel(command: int, channel: int, mode: int, dit_ph: int, dit_per: int, td_sel: int, span: int) -> bytearray:
        # 2) pack the fields into a 12-bit value [11:0]
        fields = (
                ((command & 0xF) << 20) |
                ((channel & 0xF) << 16) |
                ((mode & 0x1) << 11) |
                ((dit_ph & 0x3) << 9) |
                ((dit_per & 0x7) << 6) |
                ((td_sel & 0x3) << 4) |
                ((span & 0xF) << 0)
        ) << 8

        # 4) break into three bytes (MSB first)
        b1 = (fields >> 24) & 0xFF
        b2 = (fields >> 16) & 0xFF
        b3 = (fields >> 8) & 0xFF
        b4 = (fields >> 0) & 0xFF

        return bytearray([b1, b2, b3, b4])

    @staticmethod
    def _write_data_setting_to_channel(command: int, channel: int, data: int):
        if not (0 <= command <= 15):
            raise ValueError("Command number must be between 0 and 15.")

        if not (0 <= channel <= 15):
            raise ValueError("Channel number must be between 0 and 15.")

        if not (0 <= data <= 65535):
            raise ValueError("Data must be in a 16-bit resolution representation.")

        fields = (
                         ((command & 0xF) << 20) |
                         ((channel & 0xF) << 16) |
                         ((data & 0xFFFF) << 0)
                 ) << 8

        # 4) break into three bytes (MSB first)
        b1 = (fields >> 24) & 0xFF
        b2 = (fields >> 16) & 0xFF
        b3 = (fields >> 8) & 0xFF
        b4 = (fields >> 0) & 0xFF

        return bytearray([b1, b2, b3, b4])


    @staticmethod
    def _write_data_to_channel(command: int, channel: int, data: int):
        if not (0 <= command <= 15):
            raise ValueError("Command number must be between 0 and 15.")

        if not (0 <= channel <= 15):
            raise ValueError("Channel number must be between 0 and 15.")

        if not (0 <= data <= 4095):
            raise ValueError("Data must be in a 12-bit resolution representation.")

        command_code = (command << 4) | channel

        data_code = data << 12

        return bytearray([
            command_code,
            (data_code >> 16) & 0xFF,  # Most significant byte
            (data_code >> 8) & 0xFF,  # Middle byte
            data_code & 0xFF  # Least significant byte
        ])
