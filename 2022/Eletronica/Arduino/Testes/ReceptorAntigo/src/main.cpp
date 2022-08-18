#include <Arduino.h>
#include <SPI.h>  //Biblioteca para comunicação com o SPI
#include "RF24.h" //Biblioteca para comunicação com o rádio


#define ENABLE1 5    //Pino do PWM A do motor ...
#define ENABLE2 6    //Pino do PWM B do motor ...
#define MOTORET 1    //Pino do motor esquerdo trás
#define MOTOREF 0    //Pino do motor esquerdo frente
#define MOTORDT 7    //Pino do motor direito trásdigitalWrite(abc, HIGH);
#define MOTORDF 8    //Pino do motor direito frentedigitalWrite(abc, HIGH);
#define BIT1 A1      //Dip Switch de escolha do robô
#define BIT2 A2      //Dip Switch de escolha do robô
#define LED 4        //Pino do LED
#define TIME_MECHANICAL 2000   //Tempo de espera para o robô parar
#define TIME_TURN_OFF 150 // Tempo de espera para o robô parar


RF24 receptor(9,10); //Define os pinos de comunicação com o rádio


// Define a estrutura do pacote
struct Mensagem {
  int id;
  int speed[2];
};

// Declarar o pacote de mensagens
Mensagem packet;

// ID do robô
int8_t id_robot = 3;

// Tempo para o robô parar
unsigned long turnoffMotorTime = 0;

// Endereço do robô
byte address[][8] = {"BDPt","CAR3"};

// Protótipo das funções
void MecanicRotine();
void EsquerdaFrente(int speed);
void EsquerdaTras(int speed);
void DireitaFrente(int speed);
void DireitaTras(int speed);
void DesligaMotores();

void setup() {
  //Inicia a comunicação serial com o usuário
  Serial.begin(115200);

  // setup da ponte H
  pinMode(MOTOREF, OUTPUT); //Define o pino do motor esquerdo frente como saída
  pinMode(MOTORET, OUTPUT); //Define o pino do motor esquerdo trás como saída
  pinMode(MOTORDF, OUTPUT); //Define o pino do motor direito frente como saída
  pinMode(MOTORDT, OUTPUT); //Define o pino do motor direito trás como saída
  pinMode(ENABLE1, OUTPUT); //Define o pino de PWM do motor ... como saída
  pinMode(ENABLE2, OUTPUT); //Define o pino de PWM do motor ... como saída
  pinMode(LED, OUTPUT); //Define o pino do LED como saída


  // Inicio teste mecanico
  MecanicRotine();

  // setup do rádio
  delay(200);
  receptor.begin();
  receptor.setChannel(83);
  receptor.setPALevel(RF24_PA_LOW);
  receptor.setDataRate(RF24_250KBPS);
  receptor.openReadingPipe(1, address[1]);
  receptor.startListening();
  receptor.printDetails();  

}

void loop() {
  // Caso exista mensagem no buffer do rádio
  Serial.println(receptor.available());
  while(receptor.available()){
    // Le o pacote
    digitalWrite(LED, HIGH);
    receptor.read(&packet, sizeof(packet));

    if(packet.id == id_robot){

      // Define a velocidade e sentido de rotacao do motor esquerdo
      if(packet.speed[0] <= 150){EsquerdaFrente(packet.speed[0]);}
      else{EsquerdaTras(packet.speed[0]);}

      // Define a velocidade e sentido de rotacao do motor direito
      if(packet.speed[1] <= 150){DireitaFrente(packet.speed[1]);}
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

// Implementação das funções
void MecanicRotine(){
  unsigned long time = millis();
  while(millis() - time < TIME_MECHANICAL){
    // Gira o robô sentido horário
    if(millis() - time <= TIME_MECHANICAL/2){
      EsquerdaFrente(100);
      analogWrite(ENABLE1, 100);
      DireitaTras(100);
      analogWrite(ENABLE2, 100);
    }
    // Gira o robô sentido anti-horário
    else{
      EsquerdaTras(100);
      analogWrite(ENABLE1, 100);
      DireitaFrente(100);
      analogWrite(ENABLE2, 100);
    }
  }
  DesligaMotores();
}

void EsquerdaFrente(int speed){
  analogWrite(ENABLE1, map(speed, 150, 50, 0, 255));
  digitalWrite(MOTOREF, HIGH);
  digitalWrite(MOTORET, LOW);
}

void EsquerdaTras(int speed){
  analogWrite(ENABLE1, map(speed, 151, 250, 1, 255));
  digitalWrite(MOTOREF, LOW);
  digitalWrite(MOTORET, HIGH);

}

void DireitaFrente(int speed){
  analogWrite(ENABLE2, map(speed, 150, 50, 0, 255));
  digitalWrite(MOTORDF, HIGH);
  digitalWrite(MOTORDT, LOW);

}

void DireitaTras(int speed){
  analogWrite(ENABLE2, map(speed, 151, 250, 1, 255));
  digitalWrite(MOTORDF, LOW);
  digitalWrite(MOTORDT, HIGH);

}

void DesligaMotores(){
  analogWrite(ENABLE1, 0);
  analogWrite(ENABLE2, 0);
  digitalWrite(MOTOREF, LOW);
  digitalWrite(MOTORET, LOW);
  digitalWrite(MOTORDF, LOW);
  digitalWrite(MOTORDT, LOW);

}