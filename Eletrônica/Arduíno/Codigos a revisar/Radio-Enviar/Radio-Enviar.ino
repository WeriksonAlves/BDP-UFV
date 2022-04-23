/*
#include <nRF24L01.h>
#include <printf.h>
#include <RF24.h>
#include <RF24_config.h>
*/

#include <SPI.h>
#include "RF24.h"


RF24 transmissor(9,10);
byte addresses[][6] = {"BDP", "car"}; //Enderços

#define BUFFER_SIZE 10 //Tamnho dos dados enviados

void setup() {
  //Serial.begin(115200);
  transmissor.begin();
  transmissor.setChannel(83);
  transmissor.setPALevel(RF24_PA_LOW);
  transmissor.setDataRate(RF24_250KBPS);
  transmissor.openWritingPipe(addresses[1]);
  Serial.println("Iniciou o envio");
  transmissor.startListening();
}

bool cont = 0;

void loop() {
  if (transmissor.available() > 0){
    digitalWrite(LED,HIGH);
    dados = Serial.readStringUntil('\n');

    if (dados.length() == BUFFER_SIZE -1){
      trasmissor.stopListening();
      if (cont){
        Serial.print("Tempo de uso");
        Serial.println
      }
    }
  }
  if (val == LOW){
//    radio.write("1");
    delay(500);
  } else if (val == HIGH){
    radio.startwrite("2");
    delay(500);
  }
}
