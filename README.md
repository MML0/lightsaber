# LED Rod Controller

A WiFi-controlled LED rod using ESP8266 and WS2812B LED strip. This project allows you to control up to 1000 LEDs through UDP communication.

## Features

- WiFi connectivity using ESP8266
- UDP-based control protocol
- Support for up to 1000 WS2812B LEDs
- Automatic LED timeout (turns off after 2 seconds of inactivity)
- Static IP configuration
- FastLED library for efficient LED control

## Hardware Requirements

- ESP8266 NodeMCU or similar board
- WS2812B LED strip (up to 1000 LEDs)
- Power supply suitable for your LED strip
- WiFi network

## Pin Configuration

- LED Data Pin: D1 (GPIO5)
- Board LED: D4 (built-in LED)

## Network Configuration

- Static IP: 192.168.43.101
- Gateway: 192.168.43.1
- Subnet: 255.255.255.0
- UDP Port: 8266

## Protocol

The LED control uses a simple UDP protocol:
- Sync byte: 0xAA
- Followed by RGB data for each LED (3 bytes per LED)

## Setup

1. Update the WiFi credentials in the code:
   ```cpp
   const char* ssid = "your_ssid";
   const char* password = "your_password";
   ```

2. Adjust the number of LEDs if needed:
   ```cpp
   #define NUM_LEDS 140  // Change this to match your LED count
   ```

3. Upload the code to your ESP8266

## Usage

Send UDP packets to the ESP8266's IP address on port 8266 with the following format:
- First byte: 0xAA (sync byte)
- Remaining bytes: RGB data for each LED (3 bytes per LED)

## Safety Notes

- Ensure proper power supply for your LED strip
- Consider adding a fuse for protection
- Be mindful of power consumption and heat generation

## License

This project is open source and available for personal and commercial use. 