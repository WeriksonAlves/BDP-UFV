///////////////////////////////////////////////
//   DESENVOLVIDO POR MATEUS ARMOND SANTOS   //
//                BDP-2018                   //
///////////////////////////////////////////////

#include <SPI.h>
#include "RF24.h"

RF24 transmissor (9, 10);
byte addresses[][6] = {"BDP", "carros"}; //Endereço para envio dos pacotes

#define BUFFER_SIZE 10     //Tamanho dos dados enviados

struct Pacote {   //Pacote de dados para serem enviados por rádio
  int id;
  int vel[2];  //0 - esquerda e 1    - direita
};

Pacote pack1;
Pacote pack2;
Pacote pack3;

void setup() {
  Serial.begin(115200);  // Abre a porta serial com o 'Baudrate' passado como parâmetro
  //-------->Inicia as variáveis-------------------//
  pack1.id = 1;
  pack2.id = 2;
  pack3.id = 3;
  //-------->Inicia o rádio-------------------//
  //delay(100);
  transmissor.begin();
  transmissor.setChannel(83);
  transmissor.setPALevel(RF24_PA_MAX);
  transmissor.setDataRate( RF24_250KBPS ) ;
  transmissor.openWritingPipe( addresses[1]);
  //delay(100);
  //retirar depois
  Serial.println("iniciou sender");
}

//////Teste de performace////////
int contLostPacks = 0, contSendPacks = 0;
bool contTime = 0, showTotal = 0;
unsigned int Time = 0, timeTotal = 0;

/////////////////////////////////
bool ok = 0;

String dados;
void loop() {

  if (Serial.available() > 0) {
    dados = Serial.readStringUntil('\n');

    if (dados.length() == BUFFER_SIZE - 1) { //Se os dados enviados estiverem corretos

      transmissor.stopListening();
      //////Teste de performace////////
      if (contTime) {
        Serial.print("Tempo de perda: ");
        Serial.println(millis() - Time);
        contTime = 0;
      }
      showTotal = 1; timeTotal = millis();
      contSendPacks++;                      //Conta os pacotes enviados
      /////////////////////////////////
      Serial.println(dados);

      Serial.print("vel roda1 before: "); Serial.println(pack1.vel[0]);
      Serial.print("vel roda2 before: "); Serial.println(pack1.vel[1]);
      
      //-------->Pacote do primero rôbo<---------------//
      pack1.vel[0] = dados[2]; if (pack1.vel[0] < 0) pack1.vel[0] = pack1.vel[0] + 256;
      pack1.vel[1] = dados[3]; if (pack1.vel[1] < 0) pack1.vel[1] = pack1.vel[1] + 256;
      Serial.print("vel roda1  "); Serial.println(pack1.vel[0]);
      Serial.print("vel roda2  "); Serial.println(pack1.vel[1]);
      ok = transmissor .write(&pack1, sizeof(pack1));
      if (ok) Serial.println("Pack1: ok"); else Serial.println("Pack1: failed");
      //-------->Pacote do segundo rôbo<---------------//
      pack2.vel[0] = dados[4]; if (pack2.vel[0] < 0) pack2.vel[0] = pack2.vel[0] + 256;
      pack2.vel[1] = dados[5]; if (pack2.vel[1] < 0) pack2.vel[1] = pack2.vel[1] + 256;
      ok = transmissor .write(&pack2, sizeof(pack2));
      if (ok) Serial.println("Pack2: ok"); else Serial.println("Pack2: failed");
      //-------->Pacote do terceiro rôbo<--------------//
      pack3.vel[0] = dados[6]; if (pack3.vel[0] < 0) pack3.vel[0] = pack3.vel[0] + 256;
      pack3.vel[1] = dados[7]; if (pack3.vel[1] < 0) pack3.vel[1] = pack3.vel[1] + 256;
      ok = transmissor .write(&pack3, sizeof(pack3));
      if (ok) Serial.println("Pack3: ok"); else Serial.println("Pack3: failed");
      //-------->Envio dos pacotes<--------------------//
      //Serial.print("Robo 1: "); Serial.print(pack1.vel[0]); Serial.print(" "); Serial.println(pack1.vel[1]);
      //Serial.print("Robo 2: "); Serial.print(pack2.vel[0]); Serial.print(" "); Serial.println(pack2.vel[1]);
      //Serial.print("Robo 3: "); Serial.print(pack3.vel[0]); Serial.print(" "); Serial.println(pack3.vel[1]);
      Serial.write("");
      transmissor.startListening();
    }
    else {
      //////Teste de performace////////
      if (!contTime) {
        Time = millis();
        contTime = 1;
      }
      contLostPacks++;
      Serial.print("Pacotes Perdidos: ");
      Serial.println(contLostPacks);
      /////////////////////////////////
      //while(Serial.available()){ Serial.read(); } //Limpa o buffer
    }
  }
  //////Teste de performace////////
  if (millis() - timeTotal > 2000 && showTotal) {
    Serial.print("Pacotes Total Perdidos: ");
    Serial.println(contLostPacks);
    Serial.print("Pacotes Total Enviados: ");
    Serial.println(contSendPacks);
    contLostPacks = 0;
    contSendPacks = 0;
    showTotal = 0;
  }
  /////////////////////////////////
  //delay(90);
}
