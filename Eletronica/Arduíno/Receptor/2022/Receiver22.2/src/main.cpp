#include <Arduino.h>
////////////////////////////////////////////////////////////////////////////
/*Autor: Wérikson Alves
  Código de recepção do pacote de dados por rádio para BDP - UFV
  Data de início: 28/04/2022
  Data de finalização: ??/??/2022
  Versão: 22.1
  Descrição da alteração: Foi preenchido os comentarios e ajustado o código
*/
////////////////////////////////////////////////////////////////////////////
// Bibliotecas:
#include <SPI.h>  //Biblioteca para comunicação com o SPI
#include "RF24.h" //Biblioteca para comunicação com o rádio

////////////////////////////////////////////////////////////////////////////
// Definições básicas:

#define PWMA 5    //Pino PWMA => motor direito
#define MTDF 1    //Pino AIN2 => direito frente
#define MTDT 0    //Pino AIN1 => direito trás
#define MTET 8    //Pino BIN1 => esquerdo trás
#define MTEF 7    //Pino BIN2 => esquerdo frente
#define PWMB 6    //Pino PWMB => motor esquerdo
#define BIT1 A1      //Dip Switch de escolha do robô
#define BIT2 A2      //Dip Switch de escolha do robô
#define LED 4        //Pino do LED para teste
#define ROBOID 1     //Identificação do Robô
#define TIME_MECHANICAL 2000   //Tempo de espera para o robô parar
#define TIME_TURN_OFF 150 // Tempo de espera para o robô parar
RF24 receptor(9, 10); //Define os pinos de comunicação com o rádio

struct Package { int id; int speed[2]; }; //Define a estrutura do pacote recebido
////////////////////////////////////////////////////////////////////////////
// Constantes e variáveis:
Package packet;
int8_t id_robot;
unsigned long turnoffMotorTime = 0;
byte address[][8] = {"BDPt","CAR3"};

////////////////////////////////////////////////////////////////////////////
// Protótipo das funções:
void IntialMecanicRotine(int TEMPO);
void EsquerdaFrente(int speed);
void EsquerdaTras(int speed);
void DireitaFrente(int speed);
void DireitaTras(int speed);
void DesligaMotores();
void AndaFrente();
void AndaTras();
void GiraHorario();
void GiraAntiHorario();


////////////////////////////////////////////////////////////////////////////
//Função setup
void setup() {
  // Setup das portas da Ponte H:
  pinMode(MTEF, OUTPUT); //Define o pino do motor esquerdo frente como saída
  pinMode(MTET, OUTPUT); //Define o pino do motor esquerdo trás como saída
  pinMode(MTDF, OUTPUT); //Define o pino do motor direito frente como saída
  pinMode(MTDT, OUTPUT); //Define o pino do motor direito trás como saída
  pinMode(PWMA, OUTPUT); //Define o pino de PWM do motor direito como saída
  pinMode(PWMB, OUTPUT); //Define o pino de PWM do motor esquerdo como saída

  //Setup do Teste mecânico:
  IntialMecanicRotine(1000);  // Teste mecânico
  
  // Setup do rádio:
  delay(200);                                //Espera 200ms para inicializar o rádio
  receptor.begin();                          //Inicializa o rádio
  receptor.setChannel(83);                   //Define o canal do rádio
  receptor.setPALevel(RF24_PA_MIN);          //Define o nível de potência do rádio
  receptor.setDataRate( RF24_250KBPS );      //Define a taxa de transmissão do rádio
  receptor.openReadingPipe(1, address[1]); //Define o endereço de recepção
  receptor.startListening();                 //Inicia a recepção de pacotes
  receptor.printDetails();                   //Imprime os detalhes do rádio

  //Indentificação do robô:
  /* pinMode(BIT1, INPUT);
  pinMode(BIT2, INPUT);
  
  if(!digitalRead(BIT1) && digitalRead(BIT2)) {id_robot = 1; address[][8] = {"BDPt","CAR1"};}
  else if(digitalRead(BIT1) && !digitalRead(BIT2)) {id_robot = 2; address[][8] = {"BDPt","CAR2"};}
  else if(digitalRead(BIT1) && digitalRead(BIT2)) {id_robot = 3; address[][8] = {"BDPt","CAR3"};}
 */
  if(ROBOID == 1) {id_robot = 1; address[1][8] = '1'; }//{"BDPt","CAR1"};}
  else if(ROBOID == 2) {id_robot = 2; address[1][8]  = '2'; }// {"BDPt","CAR2"};}
  else if(ROBOID == 3) {id_robot = 3; address[1][8]  = '3'; }// {"BDPt","CAR3"};}
}

////////////////////////////////////////////////////////////////////////////
//Função loop
void loop() {
  // Caso exista mensagem no buffer do rádio
  Serial.println(receptor.available());
  while(receptor.available()){
    // Le o pacote
    digitalWrite(LED, HIGH);
    receptor.read(&packet, sizeof(packet));

    if(packet.id == id_robot){
 
      // Define a velocidade e sentido de rotacao do motor esquerdo
      if(packet.speed[0] >= 150){EsquerdaFrente(packet.speed[0]);}
      else{EsquerdaTras(packet.speed[0]);}

      // Define a velocidade e sentido de rotacao do motor direito
      if(packet.speed[1] >= 150){DireitaFrente(packet.speed[1]);}
      else{DireitaTras(packet.speed[1]);}

      turnoffMotorTime = millis();
    }
  }

  // Caso o robô não tenha recebido nenhuma mensagem, em 150ms, para os motores
  if(millis() - turnoffMotorTime > TIME_TURN_OFF){
    DesligaMotores();
    digitalWrite(LED, LOW);
  }
}
////////////////////////////////////////////////////////////////////////////
// Implementação das funções
void IntialMecanicRotine(int TEMPO){
  delay(3000);
  AndaFrente();
  delay(TEMPO);
  DesligaMotores();
  AndaTras();
  delay(TEMPO);
  DesligaMotores();
  GiraHorario();
  delay(TEMPO);
  DesligaMotores();
  GiraAntiHorario();
  delay(TEMPO);
  DesligaMotores();
}

void EsquerdaFrente(int speed){ 
  analogWrite(PWMB, map(speed, 150, 250, 0, 255)); 
  digitalWrite(MTEF, HIGH); 
  digitalWrite(MTET, LOW); }

void EsquerdaTras(int speed){ 
  analogWrite(PWMB, map(speed, 149, 50, 0, 255)); 
  digitalWrite(MTEF, LOW); 
  digitalWrite(MTET, HIGH); }

void DireitaFrente(int speed){ 
  analogWrite(PWMA, map(speed, 150, 250, 0, 255)); 
  digitalWrite(MTDF, HIGH); 
  digitalWrite(MTDT, LOW); }

void DireitaTras(int speed){ 
  analogWrite(PWMA, map(speed, 149, 50, 0, 255)); 
  digitalWrite(MTDF, LOW); 
  digitalWrite(MTDT, HIGH); }

void DesligaMotores(){ analogWrite(PWMA, 0); analogWrite(PWMB, 0); digitalWrite(MTEF, LOW); digitalWrite(MTET, LOW); digitalWrite(MTDF, LOW); digitalWrite(MTDT, LOW); }

void AndaFrente(){ DireitaFrente(200); EsquerdaFrente(200); }

void AndaTras(){ EsquerdaTras(100); DireitaTras(100); }

void GiraHorario(){ EsquerdaFrente(230); DireitaTras(70); }

void GiraAntiHorario(){ EsquerdaTras(70); DireitaFrente(230); }