///////////////////////////////////////////////
//   DESENVOLVIDO POR        WERIKSON        //
//                BDP-2020                   //
///////////////////////////////////////////////

#include <SPI.h>
#include "RF24.h"

#define LED1 5
#define LED2 6
//#define LED3 3


RF24 transmissor (9, 10);
byte addresses[][6] = {"BDP", "car"}; //Endereço para envio dos pacotes

#define BUFFER_SIZE 10     //Tamanho dos dados enviados

struct Pacote {   //Pacote de dados para serem enviados por rádio
  int id;
  int vel[2];  //0 - esquerda e 1    - direita
};

Pacote pack1;
Pacote pack2;
Pacote pack3;
Pacote pack4;


void setup() {
  Serial.begin(115200);  // Abre a porta serial com o 'Baudrate' passado como parâmetro
  //-------->Inicia as variáveis-------------------//
  pack1.id = 1;
  pack2.id = 2;
  pack3.id = 3;
  pack3.id = 4;
  //-------->Inicia o rádio-------------------//
  transmissor.begin();
  transmissor.setChannel(83);
  transmissor.setPALevel(RF24_PA_MIN);
  transmissor.setDataRate( RF24_250KBPS ) ;
  transmissor.openWritingPipe( addresses[1]);

  pinMode(4, INPUT_PULLUP);
  pinMode(5, OUTPUT);

  
  //-------->Rotina de teste mecânico----------//
  //IntialMecanicRotine();
}

bool ok = 0;

String dados;
void loop() {
  
  if(digitalRead(4) == LOW){
    digitalWrite(5,HIGH);
    IntialMecanicRotine();
    digitalWrite(5,LOW);
    }

  
  if (Serial.available() > 0) {
    dados = Serial.readStringUntil('\n');

    if (dados.length() == BUFFER_SIZE - 1) { //Se os dados enviados estiverem corretos

      transmissor.stopListening();
      
      //-------->Pacote do primero rôbo<---------------//
      pack1.vel[0] = dados[2]; if (pack1.vel[0] < 0) pack1.vel[0] = pack1.vel[0] + 256;
      pack1.vel[1] = dados[3]; if (pack1.vel[1] < 0) pack1.vel[1] = pack1.vel[1] + 256;
      ok = transmissor.write(&pack1, sizeof(pack1));
      //-------->Pacote do segundo rôbo<---------------//
      pack2.vel[0] = dados[4]; if (pack2.vel[0] < 0) pack2.vel[0] = pack2.vel[0] + 256;
      pack2.vel[1] = dados[5]; if (pack2.vel[1] < 0) pack2.vel[1] = pack2.vel[1] + 256;
      ok = transmissor.write(&pack2, sizeof(pack2));
      //-------->Pacote do terceiro rôbo<--------------//
      pack3.vel[0] = dados[6]; if (pack3.vel[0] < 0) pack3.vel[0] = pack3.vel[0] + 256;
      pack3.vel[1] = dados[7]; if (pack3.vel[1] < 0) pack3.vel[1] = pack3.vel[1] + 256;
      ok = transmissor.write(&pack3, sizeof(pack3));

      transmissor.startListening();
    }
  }
}

void IntialMecanicRotine() {
  int i;
  int vetorDeDados[6];
  for (i = 50; i < 70; i++) {
    vetorDeDados[0] = 150+i;
    vetorDeDados[1] = 150+i;
    vetorDeDados[2] = 150+i;
    vetorDeDados[3] = 150-i;
    vetorDeDados[4] = 150+i;
    vetorDeDados[5] = 150-i;
    transmissor.stopListening();
      //-------->Pacote do primero rôbo<---------------//
    pack1.vel[0] = vetorDeDados[0]; if (pack1.vel[0] < 0) pack1.vel[0] = pack1.vel[0] + 256;
    pack1.vel[1] = vetorDeDados[1]; if (pack1.vel[1] < 0) pack1.vel[1] = pack1.vel[1] + 256;
    ok = transmissor.write(&pack1, sizeof(pack1));
    //-------->Pacote do segundo rôbo<---------------//
    pack2.vel[0] = vetorDeDados[2]; if (pack2.vel[0] < 0) pack2.vel[0] = pack2.vel[0] + 256;
    pack2.vel[1] = vetorDeDados[3]; if (pack2.vel[1] < 0) pack2.vel[1] = pack2.vel[1] + 256;
    ok = transmissor.write(&pack2, sizeof(pack2));
    //-------->Pacote do terceiro rôbo<--------------//
    pack3.vel[0] = vetorDeDados[4]; if (pack3.vel[0] < 0) pack3.vel[0] = pack3.vel[0] + 256;
    pack3.vel[1] = vetorDeDados[5]; if (pack3.vel[1] < 0) pack3.vel[1] = pack3.vel[1] + 256;
    ok = transmissor.write(&pack3, sizeof(pack3));
    transmissor.startListening();
    delay(30);
  }
  for (i = 50; i < 70; i++) {
    vetorDeDados[0] = 150-i;
    vetorDeDados[1] = 150-i;
    vetorDeDados[2] = 150-i;
    vetorDeDados[3] = 150+i;
    vetorDeDados[4] = 150-i;
    vetorDeDados[5] = 150+i;
    transmissor.stopListening();
      //-------->Pacote do primero rôbo<---------------//
    pack1.vel[0] = vetorDeDados[0]; if (pack1.vel[0] < 0) pack1.vel[0] = pack1.vel[0] + 256;
    pack1.vel[1] = vetorDeDados[1]; if (pack1.vel[1] < 0) pack1.vel[1] = pack1.vel[1] + 256;
    ok = transmissor.write(&pack1, sizeof(pack1));
    //-------->Pacote do segundo rôbo<---------------//
    pack2.vel[0] = vetorDeDados[2]; if (pack2.vel[0] < 0) pack2.vel[0] = pack2.vel[0] + 256;
    pack2.vel[1] = vetorDeDados[3]; if (pack2.vel[1] < 0) pack2.vel[1] = pack2.vel[1] + 256;
    ok = transmissor.write(&pack2, sizeof(pack2));
    //-------->Pacote do terceiro rôbo<--------------//
    pack3.vel[0] = vetorDeDados[4]; if (pack3.vel[0] < 0) pack3.vel[0] = pack3.vel[0] + 256;
    pack3.vel[1] = vetorDeDados[5]; if (pack3.vel[1] < 0) pack3.vel[1] = pack3.vel[1] + 256;
    ok = transmissor.write(&pack3, sizeof(pack3));
    transmissor.startListening();
    delay(30);
  }
}
