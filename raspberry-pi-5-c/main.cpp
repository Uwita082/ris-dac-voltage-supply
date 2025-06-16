#include <vector>
#include <cstdint>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/spi/spidev.h>
#include <iostream>
#include <chrono>
#include <iomanip>

#define DEVICE "/dev/spidev0.0"
#define SPI_MODE SPI_MODE_0
#define SPI_SPEED 25000000
#define BITS_PER_WORD 8

int send_spi_command(int fd, const std::vector<uint8_t>& cmd) {
    struct spi_ioc_transfer tr{};
    tr.tx_buf = reinterpret_cast<unsigned long>(cmd.data());
    tr.rx_buf = 0;
    tr.len = cmd.size();
    tr.speed_hz = SPI_SPEED;
    tr.bits_per_word = BITS_PER_WORD;
    tr.delay_usecs = 0;

    if (ioctl(fd, SPI_IOC_MESSAGE(1), &tr) < 1) {
        perror("Failed to send SPI message");
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

    // Example commands (fill these with your actual byte arrays)
    std::vector<std::vector<uint8_t>> commands = {
        {0x72, 0xFF, 0xFF, 0x00, 0x72, 0xFF, 0xFF, 0x00, 0x72, 0xFF, 0xFF, 0x00, 0x72, 0xFF, 0xFF, 0x00}, // Select Register B all channels
        {0x78, 0x80, 0x00, 0x00, 0x78, 0x80, 0x00, 0x00, 0x78, 0x80, 0x00, 0x00, 0x78, 0x80, 0x00, 0x00}, // Write channel all code 2048 <> 0 V
        {0x7C, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00}, // Update all channels
        {0x72, 0x00, 0x00, 0x00, 0x72, 0x00, 0x00, 0x00, 0x72, 0x00, 0x00, 0x00, 0x72, 0x00, 0x00, 0x00}, // Select Register A all channels
        {0x7B, 0x00, 0x14, 0x00, 0x7B, 0x00, 0x14, 0x00, 0x7B, 0x00, 0x14, 0x00, 0x7B, 0x00, 0x14, 0x00}, // Set TGP pin for toggle mode and select span -+ 15 V
        // {0x74, 0xFF, 0xFF, 0x00, 0x74, 0xFF, 0xFF, 0x00, 0x74, 0xFF, 0xFF, 0x00, 0x74, 0xFF, 0xFF, 0x00} // Enable all channels toggle mode
    };

    for (size_t i = 0; i < commands.size(); i++) {
        send_spi_command(fd, commands[i]);
        std::cout << "Sent command #" << i + 1 << std::endl;
    }

    // std::vector<uint8_t> cmd1 = {0x42, 0xFF, 0xF0, 0x00}; //Channel index 2 <> -15 V
    // send_spi_command(fd, cmd1);

    std::vector<uint8_t> cmd1 = {0x42, 0xFF, 0xF0, 0x00}; //Channel index 2 <> -15 V
    std::vector<uint8_t> cmd2 = {0x42, 0x00, 0x00, 0x00}; //Channel index 2 <> +15 V

    auto start = std::chrono::steady_clock::now();

    while (true) {
        if (send_spi_command(fd, cmd1) < 0) break;
        if (send_spi_command(fd, cmd2) < 0) break;

        // auto now = std::chrono::steady_clock::now();
        // if (std::chrono::duration_cast<std::chrono::seconds>(now - start).count() >= 60) {
        //     std::cout << "Finished 60 seconds of sending." << std::endl;
        //     break;
        // }
    }

    // std::vector<std::vector<uint8_t>> byte_vectors;
    //
    // for (uint8_t i = 0; i < 16; ++i) {
    //     std::vector<uint8_t> vec;
    //     for (uint8_t j = 0; j < 4; ++j) {
    //         uint8_t first_byte = 0x40 | (i & 0x0F); // Most significant 4 bits = 0b0100
    //         vec.push_back(first_byte);
    //         vec.push_back(0xFF);
    //         vec.push_back(0xF0);
    //         vec.push_back(0x00);
    //     }
    //     byte_vectors.push_back(vec);
    // }
    //
    // for (uint8_t i = 0; i < 16; ++i) {
    //     std::vector<uint8_t> vec;
    //     for (uint8_t j = 0; j < 4; ++j) {
    //         uint8_t first_byte = 0x40 | (i & 0x0F); // Most significant 4 bits = 0b0100
    //         vec.push_back(first_byte);
    //         vec.push_back(0x00);
    //         vec.push_back(0x00);
    //         vec.push_back(0x00);
    //     }
    //     byte_vectors.push_back(vec);
    // }

    // auto start = std::chrono::steady_clock::now();
    //
    // while (true) {
    //     for (size_t i = 0; i < byte_vectors.size(); i++) {
    //         send_spi_command(fd, byte_vectors[i]);
    //     }
    //
    //     auto now = std::chrono::steady_clock::now();
    //     if (std::chrono::duration_cast<std::chrono::seconds>(now - start).count() >= 60) {
    //         std::cout << "Finished 60 seconds of sending." << std::endl;
    //         break;
    //     }
    // }

    close(fd);
    return 0;
}