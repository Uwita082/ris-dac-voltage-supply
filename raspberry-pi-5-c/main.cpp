#include <cstdint>
#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/spi/spidev.h>
#include <cstring>

#define DEVICE "/dev/spidev0.0"
#define SPI_MODE SPI_MODE_0
#define SPI_SPEED 500000
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

    if (ioctl(fd, SPI_IOC_WR_MODE, &mode) == -1) {
        perror("Failed to set SPI mode");
        return 1;
    }

    if (ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, &bits) == -1) {
        perror("Failed to set bits per word");
        return 1;
    }

    if (ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, &speed) == -1) {
        perror("Failed to set max speed");
        return 1;
    }

    uint8_t tx[] = { 0x9F };
    uint8_t rx[sizeof(tx)] = {0};

    struct spi_ioc_transfer tr{};
    tr.tx_buf = reinterpret_cast<unsigned long>(tx);
    tr.rx_buf = reinterpret_cast<unsigned long>(rx);
    tr.len = sizeof(tx);
    tr.speed_hz = speed;
    tr.bits_per_word = bits;
    tr.delay_usecs = 0;

    if (ioctl(fd, SPI_IOC_MESSAGE(1), &tr) < 1) {
        perror("Failed to send SPI message");
        return 1;
    }

    std::cout << "Received: ";
    for (uint8_t byte : rx) {
        std::cout << "0x" << std::hex << static_cast<int>(byte) << " ";
    }
    std::cout << std::endl;

    close(fd);
    return 0;
}
