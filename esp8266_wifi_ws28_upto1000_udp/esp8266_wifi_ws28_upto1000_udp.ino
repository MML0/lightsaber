#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <FastLED.h>

#define LED_PIN D1  // Changed to D1 (GPIO5) - safe pin for WS2812B
#define NUM_LEDS 140  // Total number of LEDs in the strip
#define LED_TYPE WS2812B
#define COLOR_ORDER GRB
#define BOARD_LED D4  // Built-in LED pin

CRGB leds[NUM_LEDS];
uint8_t Data[NUM_LEDS * 3];
unsigned long lastDataTime = 0;  // To track last data reception time
const unsigned long ledOffDelay = 2000; // 10 seconds timeout to turn off LEDs

const char* ssid = "."; // Replace with your network SSID
const char* password = "12345678an";           // Replace with your network password
const IPAddress staticIP(192, 168, 43, 200);   // Static IP for the ESP8266 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,
const IPAddress gateway(192, 168, 43, 1);      // Default gateway
const IPAddress subnet(255, 255, 255, 0);      // Subnet mask

unsigned int localPort = 8266;  // Local port to listen for UDP packets
WiFiUDP udp;
void setup() {
  Serial.begin(115200);
  pinMode(BOARD_LED, OUTPUT);
  
  WiFi.config(staticIP, gateway, subnet);
  WiFi.begin(ssid, password);

  Serial.println(".");
  Serial.println("connecting...");

  while (WiFi.status() != WL_CONNECTED ) {
    digitalWrite(BOARD_LED, LOW);  // LED ON
    delay(100);
    digitalWrite(BOARD_LED, HIGH); // LED OFF
    delay(100);
    Serial.print(".");
  }
  Serial.println("connected ...");

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nWiFi connected");
    Serial.print("ESP IP Address: ");
    Serial.println(WiFi.localIP());
    digitalWrite(BOARD_LED, HIGH);  // Turn off the board LED after connection
    
    // Start UDP only if WiFi is connected
    udp.begin(localPort);
    Serial.printf("Listening for UDP packets on port %d\n", localPort);
  } else {
    Serial.println("\nWiFi connection failed! Running in offline mode.");
  }

  FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  FastLED.setBrightness(255);

  fill_solid(leds, NUM_LEDS, CRGB::Black);
  FastLED.show();


}

void loop() {
  int packetSize = udp.parsePacket();
  if (packetSize) {
    lastDataTime = millis(); // Reset timeout timer
    
    byte startByte = udp.read();
    int pixles_count = ((packetSize - 1)/ 3); // Subtract 1 for the start byte
    int chunk_count = 140/pixles_count;
    // Check for sync byte (0xAA)
    if (startByte == 0xAA) {   
      udp.read(Data, NUM_LEDS * 3);  // Read RGB data




      // Process RGB data if no special sequence is found
      for (int i = 0; i < NUM_LEDS; i++) {
        byte r = Data[(int(i/chunk_count))*3 + 0];
        byte g = Data[(int(i/chunk_count))*3 + 1];
        byte b = Data[(int(i/chunk_count))*3 + 2];
        leds[i] = CRGB(r, g, b);  // Set color for LED
      }

      FastLED.show();
    }
  }

  // If no data is received for 2 seconds, turn off the LEDs
  if (millis() - lastDataTime > ledOffDelay) {
    lastDataTime = millis(); // Reset timeout timer
    fill_solid(leds, NUM_LEDS, CRGB::Black);
    FastLED.show();
  }
}
