#include <Wire.h>

int x = 0;
void setup() {
  Serial.begin(9600);
  Wire.begin(9); 
  Wire.onReceive(receiveEvent); // função auxiliar chamada se o dispositivo está recebendo
}
void receiveEvent(int quantos) {
  x = Wire.read();    // le a informacao do I2C
}
void loop() {
  Serial.println(x);
}
