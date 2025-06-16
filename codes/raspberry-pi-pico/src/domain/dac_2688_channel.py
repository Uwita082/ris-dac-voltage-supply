from math import floor

from utils.queue import Queue


class ChannelValue:
    channel_index: int

    def __init__(self, channel_index: int):
        self.channel_index = channel_index

class ChannelWriteValue(ChannelValue):
    value_code: int

    def __init__(self, channel_index: int, value_code: int):
        super().__init__(channel_index)
        self.value_code = value_code

class ChannelSettingValue(ChannelValue):
    mode: int
    dit_ph: int
    dit_per: int
    td_sel: int
    span: int

    def __init__(self, channel_index: int, mode: int, dit_ph: int, dit_per: int, td_sel: int, span: int):
        super().__init__(channel_index)
        self.mode = mode
        self.dit_ph = dit_ph
        self.dit_per = dit_per
        self.td_sel = td_sel
        self.span = span


class QueueChannelUpdate:
    _no_daisy_chain: int
    _channels_daisy_chain: int
    _queue_list: list[Queue]

    def __init__(self, no_daisy_chain: int, channels_daisy_chain: int):
        self._no_daisy_chain = no_daisy_chain
        self._channels_daisy_chain = channels_daisy_chain

        self._queue_list = []
        for i in range(no_daisy_chain):
            self._queue_list.append(Queue())

    def register_command_write_channel(self, channel: int, value: int):
        index: int = floor(channel / self._channels_daisy_chain)
        channel_dac: int = channel % self._channels_daisy_chain

        self._queue_list[index].put(ChannelWriteValue(channel_dac, value))

    def register_command_setting_channel(self, channel: int, mode: int, dit_ph: int, dit_per: int, td_sel: int, span: int):
        if not (0 <= channel < self._channels_daisy_chain * self._no_daisy_chain):
            raise ValueError("The specified channel number must be a number between 0 and {}".format(self._channels_daisy_chain * self._no_daisy_chain - 1))

        index: int = floor(channel / self._channels_daisy_chain)
        channel_dac: int = channel % self._channels_daisy_chain

        self._queue_list[index].put(ChannelSettingValue(channel_dac, mode, dit_ph, dit_per, td_sel, span))

    def get_command_write(self) -> list[ChannelValue | None]:
        list_commands_daisy_chain: list[ChannelValue | None] = []

        for i in range(self._no_daisy_chain):
            item = self._queue_list[i].get()

            list_commands_daisy_chain.append(item)


        return list_commands_daisy_chain

