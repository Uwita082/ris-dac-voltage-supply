import time

from src.domain.dac2688_spi import DAC2688

if __name__ == '__main__':
    dac = DAC2688()
    dac.run()

    # while True:
    #     time.sleep(1)