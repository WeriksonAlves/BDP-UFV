#include <Wire.h>
int valor = 0;
void setup() {
  Wire.begin(); //Inicia como Master
  Serial.begin(9600);
  
}
void loop() {
  int sensorValue = analogRead(A0);
  valor = sensorValue;
  Wire.beginTransmission(9); // envia para o dispositivo 9
  Wire.write(valor);              //envia x 
  Wire.endTransmission();    // encerra transmissão
  Serial.println(valor);
  delay(100);
  }
