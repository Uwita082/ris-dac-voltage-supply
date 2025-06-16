#include <array>
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

int send_spi_command(int fd, const uint8_t* data, size_t len) {
    struct spi_ioc_transfer tr{};
    tr.tx_buf = reinterpret_cast<unsigned long>(data);
    tr.rx_buf = 0;
    tr.len = len;
    tr.speed_hz = SPI_SPEED;
    tr.bits_per_word = BITS_PER_WORD;
    tr.delay_usecs = 0;

    if (ioctl(fd, SPI_IOC_MESSAGE(1), &tr) < 1) {
        perror("SPI transfer failed");
        return -1;
    }
    return 0;
}

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

    // Using std::array to avoid dynamic memory allocation
    const std::array<std::array<uint8_t, 16>, 5> commands = {{
        {0x72, 0xFF, 0xFF, 0x00, 0x72, 0xFF, 0xFF, 0x00, 0x72, 0xFF, 0xFF, 0x00, 0x72, 0xFF, 0xFF, 0x00},
        {0x78, 0x80, 0x00, 0x00, 0x78, 0x80, 0x00, 0x00, 0x78, 0x80, 0x00, 0x00, 0x78, 0x80, 0x00, 0x00},
        {0x7C, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00},
        {0x72, 0x00, 0x00, 0x00, 0x72, 0x00, 0x00, 0x00, 0x72, 0x00, 0x00, 0x00, 0x72, 0x00, 0x00, 0x00},
        {0x7B, 0x00, 0x14, 0x00, 0x7B, 0x00, 0x14, 0x00, 0x7B, 0x00, 0x14, 0x00, 0x7B, 0x00, 0x14, 0x00}
    }};

    for (const auto& cmd : commands) {
        if (send_spi_command(fd, cmd.data(), cmd.size()) < 0) {
            break;
        }
    }

    const std::array<uint8_t, 16> cmd1 = {0x40, 0xFF, 0xF0, 0x00}; //Channel index 2 <> -15 V
    const std::array<uint8_t, 16> cmd2 = {0x40, 0x00, 0x00, 0x00}; //Channel index 2 <> +15 V

    while (true) {
        send_spi_command(fd, cmd1.data(), cmd1.size());
        send_spi_command(fd, cmd2.data(), cmd2.size());
    }

    close(fd);
    return 0;
}
