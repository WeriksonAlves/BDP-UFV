#include <Arduino.h>

////////////////////////////////////////////////////////////////////////////
/*Autor: Wérikson Alves
  Código de transmissão do pacote de dados por rádio para BDP - UFV
  Data de início: 06/08/2022
  Data de finalização: ??/08/2022
  Versão: 22.2
  Portas usadas: D3, D5, D6, D9, D10
  Descrição da alteração: Revisão do código
*/
////////////////////////////////////////////////////////////////////////////
// Bibliotecas:
  #include <SPI.h>  //Biblioteca para comunicação com o SPI
  #include "RF24.h" //Biblioteca para comunicação com o rádio

////////////////////////////////////////////////////////////////////////////
// Definições básicas:
  #define LEDGREEN 5        //Define o pino do LED1
  #define LEDRED 6          //Define o pino do LED2
  #define BUTTON 3          //Define o pino do botaão 1
  #define BUFFER_SIZE 10    //Tamanho dos dados enviados
  RF24 transmissor (9, 10); //Define os pinos de comunicação com o rádio
  struct Package { int id; int speed[2]; }; //Define a estrutura do pacote enviado

////////////////////////////////////////////////////////////////////////////
// Constantes e variáveis:
  Package pack1; Package pack2; Package pack3; //Declara o pacote de mensagens
  String data; //Armazena os dados do pacote para serem enviados

  // Array de debug
  bool checkMessage[3] = {0, 0, 0};
  long packLoss[3] = {0, 0, 0};
  long countPack = 0;
  unsigned long currentTimeDebug = 0; // Armazena o tempo atual
  unsigned long lastTimeDebug = 0; // Armazena o tempo anterior
  
  unsigned long previousTime; // Variaveis de tempo
  int mechanical_test[6]; // Define o vetor para o teste mecanico

////////////////////////////////////////////////////////////////////////////
// Protótipo das funções:
void IntialMecanicRotine(); //Função para inicializar as rotina de treino
uint8_t SendMessage(String data, Package pack, int robot);
uint8_t SendMessage(int data[6], Package pack, int robot);
void debug(bool check[3]);

////////////////////////////////////////////////////////////////////////////
//Função setup
void setup() { 
  Serial.begin(115200); //Inicia a comunicação serial com o 'Baudrate' como parâmetro
  pack1.id = 1; pack2.id = 2; pack3.id = 3; // Define ID do Pacote

  // Configurações do rádio:
  transmissor.begin();                        //Inicia o rádio
  transmissor.setChannel(83);                 //Define o canal do rádio
  transmissor.setPALevel(RF24_PA_MIN);        //Define o nível de potência  
  transmissor.setDataRate( RF24_250KBPS );    //Define a taxa de dados

  // Configurações das portas:
  pinMode(BUTTON, INPUT_PULLUP); //Define o pino 3 como entrada (Botão)
  pinMode(LEDRED, OUTPUT);       //Define o pino 5 como saída (LED Vermelho)
  pinMode(LEDGREEN, OUTPUT);     //Define o pino 6 como saída (LED Verde)

  // Apresenta a depuração
  String titles[4] = {"Total", "LossR1%", "LossR2%", "LossR3%"};
  for(auto i: titles){
      Serial.print(String(i) + String("   "));
  }
  
  Serial.println("");
}
////////////////////////////////////////////////////////////////////////////
//Função loop
void loop(){
  //Rotina de teste de envio de mensagens
  if(digitalRead(BUTTON) == LOW){ //Verifica se o botão está pressionado
    digitalWrite(LEDGREEN,HIGH);
    IntialMecanicRotine(); //Inicializa as rotinas de treino
    digitalWrite(LEDGREEN,LOW);
  }

  // Caso exista algum dado a ser enviado para o rádio
  if(Serial.available() > 0){
    data = Serial.readStringUntil('\n');
    if(data.length() == BUFFER_SIZE - 1){
      // Desliga o rádio de recebimento
      transmissor.stopListening();

      // Envio dos dados
      SendMessage(data, pack1, 1);
      SendMessage(data, pack2, 2);
      SendMessage(data, pack3, 3);

      // Liga o rádio de recebimento
      transmissor.startListening();
    }
  }
}
////////////////////////////////////////////////////////////////////////////
// Função para teste de comunicação
void IntialMecanicRotine(){ 
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
    checkMessage[0] = SendMessage(mechanical_test, pack1, 1);
    checkMessage[1] = SendMessage(mechanical_test, pack2, 2);
    checkMessage[2] = SendMessage(mechanical_test, pack3, 3);
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
////////////////////////////////////////////////////////////////////////////
// Função para enviar mensagens
uint8_t SendMessage(String data, Package packet, int robot){
  transmissor.stopListening();
  if(robot == 1){
    byte address[][8] = {"BDPt", "CAR1"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    pack1.speed[0] = data[2];
    if(pack1.speed[0] < 0){
      pack1.speed[0] = pack1.speed[0]  + 256;
    }
    pack1.speed[1] = data[3];
    if(pack1.speed[1] < 0){
      pack1.speed[1] = pack1.speed[1]  + 256;
    }

    return transmissor.write(&pack1, sizeof(pack1));
  }

  else if(robot == 2){
    byte address[][8] = {"BDPt", "CAR2"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    pack2.speed[0] = data[4];
    if(pack2.speed[0] < 0){
      pack2.speed[0] = pack2.speed[0]  + 256;
    }
    pack2.speed[1] = data[5];
    if(pack2.speed[1] < 0){
      pack2.speed[1] = pack2.speed[1]  + 256;
    }

    return transmissor.write(&pack2, sizeof(pack2));
  }

  else if(robot == 3){
    byte address[][8] = {"BDPt", "CAR3"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    pack3.speed[0] = data[6];
    if(pack3.speed[0] < 0){
      pack3.speed[0] = pack3.speed[0]  + 256;
    }
    pack3.speed[1] = data[7];
    if(pack3.speed[1] < 0){
      pack3.speed[1] = pack3.speed[1]  + 256;
    }

    return transmissor.write(&pack3, sizeof(pack3));
  }

  return 0;
}
////////////////////////////////////////////////////////////////////////////
// Função para enviar mensagem
uint8_t SendMessage(int data[6], Package packet, int robot){ 
  transmissor.stopListening();
  if(robot == 1){
    byte address[][8] = {"BDPt", "CAR1"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    pack1.speed[0] = data[0];
    if(pack1.speed[0] < 0){
      pack1.speed[0] = pack1.speed[0]  + 256;
    }
    pack1.speed[1] = data[1];
    if(pack1.speed[1] < 0){
      pack1.speed[1] = pack1.speed[1]  + 256;
    }

    return transmissor.write(&pack1, sizeof(pack1));
  }

  else if(robot == 2){
    byte address[][8] = {"BDPt", "CAR2"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    pack2.speed[0] = data[2];
    if(pack2.speed[0] < 0){
      pack2.speed[0] = pack2.speed[0]  + 256;
    }
    pack2.speed[1] = data[3];
    if(pack2.speed[1] < 0){
      pack2.speed[1] = pack2.speed[1]  + 256;
    }

    return transmissor.write(&pack2, sizeof(pack2));
  }

  else if(robot == 3){
    byte address[][8] = {"BDPt", "CAR3"};
    transmissor.openWritingPipe(address[1]);

    // Definindo a mensagem
    pack3.speed[0] = data[4];
    if(pack3.speed[0] < 0){
      pack3.speed[0] = pack3.speed[0]  + 256;
    }
    pack3.speed[1] = data[5];
    if(pack3.speed[1] < 0){
      pack3.speed[1] = pack3.speed[1]  + 256;
    }

    return transmissor.write(&pack3, sizeof(pack3));
  }
  return 0;
}
////////////////////////////////////////////////////////////////////////////
void debug(bool check[3]){
  countPack+=1;
  if(check[0] == 0){
    packLoss[0]+=1;
  }

  if(check[1] == 0){
    packLoss[1]+=1;
  }

  if(check[2] == 0){
    packLoss[2]+=1;
  }

    if(millis() - lastTimeDebug >= 10000){
      Serial.print(String(countPack) + "\t" + String(100.0 * packLoss[0]/countPack) + "    " + String(100.0 * packLoss[1]/countPack) + "    " + String(100.0 * packLoss[2] / countPack) + "\t\r");
      countPack = 0;
      packLoss[0] = 0;
      packLoss[1] = 0;
      packLoss[2] = 0;
      lastTimeDebug = millis();
    }
    
}
////////////////////////////////////////////////////////////////////////////