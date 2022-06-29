#include <Arduino.h>
#include <SPI.h>
#include "RF24.h"

#define LED1 5 //Define o pino do LED1
#define LED2 4 //Define o pino do LED2
#define BOT1 3 //Define o pino do botão 1
#define BUFFER_SIZE 10 //Define o tamanho do buffer
RF24 transmissor (9, 10); //Define os pinos de comunicação com o rádio

// Define a estrutura do pacote
struct Mensagem {
  int id;
  int speed[2];
};

// Declarar o pacote de mensagens
Mensagem packet_1; Mensagem packet_2; Mensagem packet_3;

// Declrar string de dados
String dados;

// Array de debug
bool checkMessage[3] = {0, 0, 0};
long packetLoss[3] = {0, 0, 0};
long countPackets = 0;
unsigned long currentTimeDebug = 0;
unsigned long lastTimeDebug = 0;

// Protótipo das funções
void MecanicRotine();
uint8_t SendMessage(String data, Mensagem packet, int robot);
uint8_t SendMessage(int data[6], Mensagem packet, int robot);
void debug(bool check[3]);


void setup() {
  //Inicia a comunicação serial com o usuário
  Serial.begin(115200); 

  // Define ID da mensagem
  packet_1.id = 1; packet_2.id = 2; packet_3.id = 3;

  // setup do rádio
  transmissor.begin();
  transmissor.setChannel(83);
  transmissor.setPALevel(RF24_PA_LOW);
  transmissor.setDataRate(RF24_250KBPS);
  
  // setup das portas
  pinMode(BOT1, INPUT_PULLUP);
  pinMode(LED1, OUTPUT);

  // Print do debug
  String titles[4] = {"Total", "LossR1%", "LossR2%", "LossR3%"};
  for(auto i: titles){
      Serial.print(String(i) + String("   "));
  }
  Serial.println("");
}

void loop() {
  // Iniciar teste mecanico e acender led
  // caso o botão esteja pressionado
  if(digitalRead(BOT1) == LOW){
    digitalWrite(LED1, HIGH);
    MecanicRotine();
    digitalWrite(LED1, LOW);
  }

  // Caso exista mensagem no buffer, enviar para o rádio
  if(Serial.available() > 0){
    dados = Serial.readStringUntil('\n');
    if(dados.length() > 0){
      // Desliga o rádio de recebimento
      transmissor.stopListening();

      // Envio dos dados
      SendMessage(dados, packet_1, 1);
      SendMessage(dados, packet_2, 2);
      SendMessage(dados, packet_3, 3);

      // Liga o rádio de recebimento
      transmissor.startListening();
    }
  }
}

// Implementação das funções
void MecanicRotine(){ // Função para teste mecanico

  // Variaveis de tempo
  unsigned long previousTime;

  // Define o vetor para o teste mecanico
  int mechanical_test[6];

  // Desliga o rádio de recebimento
  transmissor.stopListening();

  for(int i = 50; i < 70; i++){
    mechanical_test[0] = 100;
    mechanical_test[1] = 200;
    mechanical_test[2] = 100;
    mechanical_test[3] = 200;
    mechanical_test[4] = 100;
    mechanical_test[5] = 200;

    // Envio dos dados
    checkMessage[0] = SendMessage(mechanical_test, packet_1, 1);
    checkMessage[1] = SendMessage(mechanical_test, packet_2, 2);
    checkMessage[2] = SendMessage(mechanical_test, packet_3, 3);
    debug(checkMessage);


    // Aguarda 30 ms
    while(millis() - previousTime <= 30){
      // Não faz nada
    }
    previousTime = millis();

  }

  // Liga o rádio de recebimento
  transmissor.startListening();

}
uint8_t SendMessage(String data, Mensagem packet, int robot){ // Função para enviar mensagem
  transmissor.stopListening();
  if(robot == 1){
    byte address[][8] = {"BDPt", "CAR1"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    packet_1.speed[0] = data[2];
    if(packet_1.speed[0] < 0){
      packet_1.speed[0] = packet_1.speed[0]  + 256;
    }
    packet_1.speed[1] = data[3];
    if(packet_1.speed[1] < 0){
      packet_1.speed[1] = packet_1.speed[1]  + 256;
    }

    return transmissor.write(&packet_1, sizeof(packet_1));
  }

  else if(robot == 2){
    byte address[][8] = {"BDPt", "CAR2"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    packet_2.speed[0] = data[4];
    if(packet_2.speed[0] < 0){
      packet_2.speed[0] = packet_2.speed[0]  + 256;
    }
    packet_2.speed[1] = data[5];
    if(packet_2.speed[1] < 0){
      packet_2.speed[1] = packet_2.speed[1]  + 256;
    }

    return transmissor.write(&packet_2, sizeof(packet_2));
  }

  else if(robot == 3){
    byte address[][8] = {"BDPt", "CAR3"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    packet_3.speed[0] = data[6];
    if(packet_3.speed[0] < 0){
      packet_3.speed[0] = packet_3.speed[0]  + 256;
    }
    packet_3.speed[1] = data[7];
    if(packet_3.speed[1] < 0){
      packet_3.speed[1] = packet_3.speed[1]  + 256;
    }

    return transmissor.write(&packet_3, sizeof(packet_3));
  }
  return 0;
}

uint8_t SendMessage(int data[6], Mensagem packet, int robot){ // Função para enviar mensagem
  transmissor.stopListening();
  if(robot == 1){
    byte address[][8] = {"BDPt", "CAR1"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    packet_1.speed[0] = data[0];
    if(packet_1.speed[0] < 0){
      packet_1.speed[0] = packet_1.speed[0]  + 256;
    }
    packet_1.speed[1] = data[1];
    if(packet_1.speed[1] < 0){
      packet_1.speed[1] = packet_1.speed[1]  + 256;
    }

    return transmissor.write(&packet_1, sizeof(packet_1));
  }

  else if(robot == 2){
    byte address[][8] = {"BDPt", "CAR2"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    packet_2.speed[0] = data[2];
    if(packet_2.speed[0] < 0){
      packet_2.speed[0] = packet_2.speed[0]  + 256;
    }
    packet_2.speed[1] = data[3];
    if(packet_2.speed[1] < 0){
      packet_2.speed[1] = packet_2.speed[1]  + 256;
    }

    return transmissor.write(&packet_2, sizeof(packet_2));
  }

  else if(robot == 3){
    byte address[][8] = {"BDPt", "CAR3"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    packet_3.speed[0] = data[4];
    if(packet_3.speed[0] < 0){
      packet_3.speed[0] = packet_3.speed[0]  + 256;
    }
    packet_3.speed[1] = data[5];
    if(packet_3.speed[1] < 0){
      packet_3.speed[1] = packet_3.speed[1]  + 256;
    }

    return transmissor.write(&packet_3, sizeof(packet_3));
  }
  return 0;
}

void debug(bool check[3]){
  countPackets+=1;
  if(check[0] == 0){
    packetLoss[0]+=1;
  }

  if(check[1] == 0){
    packetLoss[1]+=1;
  }

  if(check[2] == 0){
    packetLoss[2]+=1;
  }

    if(millis() - lastTimeDebug >= 10000){
      Serial.print(String(countPackets) + "\t" + String(100.0 * packetLoss[0]/countPackets) + "    " + String(100.0 * packetLoss[1]/countPackets) + "    " + String(100.0 * packetLoss[2] / countPackets) + "\t\r");
      countPackets = 0;
      packetLoss[0] = 0;
      packetLoss[1] = 0;
      packetLoss[2] = 0;
      lastTimeDebug = millis();
    }
    
}