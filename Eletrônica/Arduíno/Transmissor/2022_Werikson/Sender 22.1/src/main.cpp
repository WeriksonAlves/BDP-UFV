#include <Arduino.h>
////////////////////////////////////////////////////////////////////////////
/*Autor: Wérikson Alves
  Código para transmissão do pacote de dados por rádio para BDP - UFV
  Data de início: 28/04/2022
  Data de finalização: ??/??/2022
  Versão: 22.1
  Descrição da alteração: Foi preenchido os comentarios e ajustado o código
*/
////////////////////////////////////////////////////////////////////////////
// Bibliotecas usadas: 

#include <SPI.h>  //Biblioteca para comunicação com o SPI
#include "RF24.h" //Biblioteca para comunicação com o rádio

////////////////////////////////////////////////////////////////////////////
// Definição das portas usadas: D3, D4, D5, D9, D10

#define LED1 5            //Define o pino do LED1
#define LED2 4            //Define o pino do LED2
#define BOT1 3            //Define o pino do botaão 1
RF24 transmissor (9, 10); //Define os pinos de comunicação com o rádio

////////////////////////////////////////////////////////////////////////////
// Definição de constantes e variáveis:

byte addresses[][6] = {"BDP", "car"};  //Endereço para envio dos pacotes
#define BUFFER_SIZE 10                 //Tamanho dos dados enviados
struct Pacote { int id; int vel[2]; }; //Pacote de dados para serem enviados
// por rádio; id = N; vel = 0 - Esquerda ou 1 - Direita
Pacote pack1;                          //Define o pacote 1
Pacote pack2;                          //Define o pacote 2
Pacote pack3;                          //Define o pacote 3
Pacote pack4;                          //Define o pacote 4
bool ok = 0;                           //Variável para verificar se o pacote
// foi enviado com sucesso
String dados;                          //Variável para armazenar os dados do
// pacote (recebe o conteudo ate o caracter que encerra a busca)
int i;
int vetorDeDados[6];

////////////////////////////////////////////////////////////////////////////
// Definição de protótipos de funções:
void IntialMecanicRotine(); //Função para inicializar as rotina de treino

////////////////////////////////////////////////////////////////////////////
void setup() { //Função setup
  Serial.begin(115200); // Abre a porta serial com o 'Baudrate' passado como
  // parâmetro

  //////////////////////////////////////////////////////////////////////////
  // Setup das constantes:
  pack1.id = 1; //Define o id do pacote
  pack2.id = 2; //Define o id do pacote
  pack3.id = 3; //Define o id do pacote
  pack3.id = 4; //Define o id do pacote

  // Setup do rádio:
  transmissor.begin();                        //Inicia o rádio
  transmissor.setChannel(83);                 //Define o canal do rádio
  transmissor.setPALevel(RF24_PA_MIN);        //Define o nível de potência  
  transmissor.setDataRate( RF24_250KBPS );    //Define a taxa de dados      
  transmissor.openWritingPipe( addresses[1]); //Define o endereço de escrita

  // Setup das portas:
  pinMode(BOT1, INPUT_PULLUP); //Define o pino 3 como entrada (Botão)
  pinMode(LED1, OUTPUT);       //Define o pino 5 como saída (LED1)
}

////////////////////////////////////////////////////////////////////////////
void loop() { //Função loop
  // Loop do botão:
  if(digitalRead(3) == LOW){ //Verifica se o botão foi pressionado
    digitalWrite(LED1,HIGH); //Aciona o LED1
    IntialMecanicRotine();   //Inicia a rotina de treino
    digitalWrite(LED1,LOW);  //Desliga o LED1
    } 
  
  // Loop do controle:
  if (Serial.available() > 0) {                                                         //Verifica se há dados na porta serial (não for vazia)
    dados = Serial.readStringUntil('\n');                                               //Lê os dados do pacote
    if (dados.length() == BUFFER_SIZE - 1) {                                            //Se o comprimento dos dados enviados estiverem corretos
      transmissor.stopListening();                                                      //Desliga o rádio de recepção
      
      // Pacote do rôbo 1:
      pack1.vel[0] = dados[2]; if (pack1.vel[0] < 0) pack1.vel[0] = pack1.vel[0] + 256; //Define a velocidade do lado esquerdo
      pack1.vel[1] = dados[3]; if (pack1.vel[1] < 0) pack1.vel[1] = pack1.vel[1] + 256; //Define a velocidade do lado direito
      ok = transmissor.write(&pack1, sizeof(pack1));                                    //Envia o pacote 1

      // Pacote do rôbo 2:
      pack2.vel[0] = dados[4]; if (pack2.vel[0] < 0) pack2.vel[0] = pack2.vel[0] + 256; //Define a velocidade do lado esquerdo
      pack2.vel[1] = dados[5]; if (pack2.vel[1] < 0) pack2.vel[1] = pack2.vel[1] + 256; //Define a velocidade do lado direito
      ok = transmissor.write(&pack2, sizeof(pack2));                                    //Envia o pacote 2

      // Pacote do rôbo 3:
      pack3.vel[0] = dados[6]; if (pack3.vel[0] < 0) pack3.vel[0] = pack3.vel[0] + 256; //Define a velocidade do lado esquerdo
      pack3.vel[1] = dados[7]; if (pack3.vel[1] < 0) pack3.vel[1] = pack3.vel[1] + 256; //Define a velocidade do lado direito
      ok = transmissor.write(&pack3, sizeof(pack3));                                    //Envia o pacote 3

      transmissor.startListening();                                                     //Reinicia o rádio de recepção
    }
  }
}

////////////////////////////////////////////////////////////////////////////
void IntialMecanicRotine() { //Função treino
  //int i;
  //int vetorDeDados[6];
  //Loop para enviar os dados
  for (i = 50; i < 70; i++) {                                                                //Variação de velocidade
    vetorDeDados[0] = 150+i;                                                                 //Define a velocidade do lado esquerdo - Rôbo 1
    vetorDeDados[1] = 150+i;                                                                 //Define a velocidade do lado direito - Rôbo 1
    vetorDeDados[2] = 150+i;                                                                 //Define a velocidade do lado esquerdo - Rôbo 2
    vetorDeDados[3] = 150-i;                                                                 //Define a velocidade do lado direito - Rôbo 2
    vetorDeDados[4] = 150-i;                                                                 //Define a velocidade do lado esquerdo - Rôbo 3
    vetorDeDados[5] = 150-i;                                                                 //Define a velocidade do lado direito - Rôbo 3
    transmissor.stopListening();                                                             //Desliga o rádio de recepção

    // Pacote do rôbo 1:
    pack1.vel[0] = vetorDeDados[0]; if (pack1.vel[0] < 0) pack1.vel[0] = pack1.vel[0] + 256; //Define a velocidade do lado esquerdo
    pack1.vel[1] = vetorDeDados[1]; if (pack1.vel[1] < 0) pack1.vel[1] = pack1.vel[1] + 256; //Define a velocidade do lado direito
    ok = transmissor.write(&pack1, sizeof(pack1));                                           //Envia o pacote 1

    // Pacote do rôbo 2:
    pack2.vel[0] = vetorDeDados[2]; if (pack2.vel[0] < 0) pack2.vel[0] = pack2.vel[0] + 256; //Define a velocidade do lado esquerdo
    pack2.vel[1] = vetorDeDados[3]; if (pack2.vel[1] < 0) pack2.vel[1] = pack2.vel[1] + 256; //Define a velocidade do lado direito
    ok = transmissor.write(&pack2, sizeof(pack2));                                           //Envia o pacote 2

    // Pacote do rôbo 3:
    pack3.vel[0] = vetorDeDados[4]; if (pack3.vel[0] < 0) pack3.vel[0] = pack3.vel[0] + 256; //Define a velocidade do lado esquerdo
    pack3.vel[1] = vetorDeDados[5]; if (pack3.vel[1] < 0) pack3.vel[1] = pack3.vel[1] + 256; //Define a velocidade do lado direito
    ok = transmissor.write(&pack3, sizeof(pack3));                                           //Envia o pacote 3

    transmissor.startListening();                                                            //Reinicia o rádio de recepção
    delay(30);                                                                               //Delay de 30ms
  }
}