/*
  Quantum Bioelectronic Nose - ESP32 Arduino Template
  Features:
    - Reads multiple gas sensors via TCA9548A I2C MUX
    - Sends data over Serial/Bluetooth
    - Ready for TinyML integration
*/

#include <Wire.h>
#define MUX_ADDR 0x70  // Default I2C address for TCA9548A

// Sensor channels
#define MQ3_CHANNEL     0
#define MQ135_CHANNEL   1
#define GRAPHENE_CHANNEL 2

int readSensor(uint8_t channel, int analogPin) {
  Wire.beginTransmission(MUX_ADDR);
  Wire.write(1 << channel);
  Wire.endTransmission();
  delay(10); // Allow switching
  return analogRead(analogPin);
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  analogReadResolution(12); // Optional: higher resolution for ESP32
}

void loop() {
  int mq3_val = readSensor(MQ3_CHANNEL, 34);
  int mq135_val = readSensor(MQ135_CHANNEL, 34);
  int graphene_val = readSensor(GRAPHENE_CHANNEL, 34);

  Serial.print("MQ3: ");
  Serial.print(mq3_val);
  Serial.print(" | MQ135: ");
  Serial.print(mq135_val);
  Serial.print(" | Graphene: ");
  Serial.println(graphene_val);

  delay(1000); // Read interval
}
