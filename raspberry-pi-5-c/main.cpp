#include <vector>
#include <cstdint>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/spi/spidev.h>
#include <iostream>

#define DEVICE "/dev/spidev0.0"
#define SPI_MODE SPI_MODE_0
#define SPI_SPEED 25000000
#define BITS_PER_WORD 8

int main() {
    int fd = open(DEVICE, O_RDWR);
    if (fd < 0) {
        perror("Failed to open SPI device");
        return 1;
    }

    uint8_t mode = SPI_MODE;
    uint8_t bits = BITS_PER_WORD;
    uint32_t speed = SPI_SPEED;

    ioctl(fd, SPI_IOC_WR_MODE, &mode);
    ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, &bits);
    ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, &speed);

    // Example commands (fill these with your actual byte arrays)
    std::vector<std::vector<uint8_t>> commands = {
        {0x72, 0xFF, 0xFF, 0x00, 0x72, 0xFF, 0xFF, 0x00, 0x72, 0xFF, 0xFF, 0x00, 0x72, 0xFF, 0xFF, 0x00},
        {0x78, 0x80, 0x00, 0x00, 0x78, 0x80, 0x00, 0x00, 0x78, 0x80, 0x00, 0x00, 0x78, 0x80, 0x00, 0x00},
        {0x7C, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00},
        {0x72, 0x00, 0x00, 0x00, 0x72, 0x00, 0x00, 0x00, 0x72, 0x00, 0x00, 0x00, 0x72, 0x00, 0x00, 0x00},
        {0x7B, 0x00, 0x14, 0x00, 0x7B, 0x00, 0x14, 0x00, 0x7B, 0x00, 0x14, 0x00, 0x7B, 0x00, 0x14, 0x00},
        {0x74, 0xFF, 0xFF, 0x00, 0x74, 0xFF, 0xFF, 0x00, 0x74, 0xFF, 0xFF, 0x00, 0x74, 0xFF, 0xFF, 0x00}
    };

    for (size_t i = 0; i < commands.size(); i++) {
        spi_ioc_transfer tr{};
        tr.tx_buf = reinterpret_cast<unsigned long>(commands[i].data());
        tr.rx_buf = 0;
        tr.len = commands[i].size();
        tr.speed_hz = speed;
        tr.bits_per_word = bits;
        tr.delay_usecs = 0;

        if (ioctl(fd, SPI_IOC_MESSAGE(1), &tr) < 1) {
            std::cerr << "Failed to send SPI message #" << i + 1 << std::endl;
            close(fd);
            return 1;
        }

        std::cout << "Sent command #" << i + 1 << std::endl;
    }

    close(fd);
    return 0;
}