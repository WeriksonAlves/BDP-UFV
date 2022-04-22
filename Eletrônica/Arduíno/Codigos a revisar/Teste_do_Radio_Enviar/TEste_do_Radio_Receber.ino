#include <SPI.h> 
#include "RF24.h"

#define LED 4 //Pino do LED

int ROBO = 1; //Número do rôbo

RF24 receptor(9,10);
byte addresses[][6] = {"uno"}; //Endereço para envio dos pacotes

struct Pacote{
  int id=0;
  int vel[2];
};

void setup() {
  delay(200);
  receptor.begin();
  receptor.setChannel(83);
  receptor.setPALevel(RF24_PA_MIN);
  receptor.setDataRate( RF24_250KBPS ) ;
  receptor.openReadingPipe(1, addresses[1]);
  receptor.startListening();
  receptor.printDetails();  
}

