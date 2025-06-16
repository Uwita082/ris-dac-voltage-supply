from domain.dac2688_spi import DAC2688

if __name__ == '__main__':
    dac = DAC2688()
    dac.run()
    dac.close()