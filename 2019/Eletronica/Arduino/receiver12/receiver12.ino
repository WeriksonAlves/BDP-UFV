///////////////////////////////////////////////
//   DESENVOLVIDO POR MATEUS ARMOND SANTOS   //
//                BDP-2019                   //
///////////////////////////////////////////////

#include <SPI.h> 
#include "RF24.h"

#define ENABLE1 5
#define ENABLE2 6
#define MOTORET 1   //Pino do motor esquerdo trás
#define MOTOREF 0   //Pino do motor esquerdo frente
#define MOTORDT 7   //Pino do motor direito trásdigitalWrite(abc, HIGH);
#define MOTORDF 8   //Pino do motor direito frentedigitalWrite(abc, HIGH);

#define BIT1 A1 //Dip Switch de escolha do robô
#define BIT2 A2 //Dip Switch de escolha do robô

#define LED 4 //Pino do LED

int ROBO = 1; //Número do rôbo

#define ROBOD 1

RF24 receptor(9,10);
byte addresses[][6] = {"BDP", "car"}; //Endereço para envio dos pacotes

struct Pacote{
  int id=0;
  int vel[2];
};

Pacote pack;



void setup() 
{
  //Serial.begin(115200); // Abre a porta serial com o 'Baudrate' passado como parâmetro
  //---------->Configura as portas-------------//
  pinMode(MOTOREF, OUTPUT);
  pinMode(MOTORET, OUTPUT);
  pinMode(MOTORDF, OUTPUT);
  pinMode(MOTORDT, OUTPUT);
  pinMode(ENABLE1, OUTPUT);
  pinMode(ENABLE2, OUTPUT);

  //pinMode(BIT1, INPUT);
  //pinMode(BIT2, INPUT);

  //-------->Rotina de teste mecânico----------//
  IntialMecanicRotine();
  
  
  //-------->Inicia o rádio-------------------//
  delay(200);
  receptor.begin();
  receptor.setChannel(83);
  receptor.setPALevel(RF24_PA_MIN);
  receptor.setDataRate( RF24_250KBPS ) ;
  receptor.openReadingPipe(1, addresses[1]);
  receptor.startListening();
  receptor.printDetails();  

  //-------->Define Robô-------------------//
  if(!digitalRead(BIT1) && digitalRead(BIT2)){
    ROBO = 1;
  }
  else if(digitalRead(BIT1) && !digitalRead(BIT2)){
    ROBO = 2;
  }
  else if(digitalRead(BIT1) && digitalRead(BIT2)){
    ROBO = 3;
  }
  else if(!digitalRead(BIT1) && !digitalRead(BIT2)){
    ROBO = 4;
  }

  ROBO = 1;
  
  //retirar depois
    Serial.println("iniciou receiver");
    Serial.print("iniciou robo: ");
    Serial.println(ROBO);
}

bool turnOffMotor = 0; //Desliga o motor após algum tempo
unsigned long int turnOffMotorTime = 0; //Conta o tempo para desligar o motor


void loop()  
{
  while ( receptor.available()>0) 
  {
    digitalWrite(LED, HIGH);
    receptor.read( &pack, sizeof(pack));  
    Serial.print("Recebeu pacote id: ");
    Serial.println(pack.id);
    if(pack.id == ROBO){        //Verifica se o pacote é o correto para o rôbo
      Serial.println("Recebeu pack1");
      Serial.print("Robo 1: "); Serial.print(pack.vel[0]); Serial.print(" "); Serial.println(pack.vel[1]);
      if(pack.vel[0] <= 150){
        analogWrite(ENABLE1, map(pack.vel[0], 150, 50, 0, 255));
        digitalWrite(MOTOREF, HIGH);
        digitalWrite(MOTORET, LOW);
      }
      else{
        analogWrite(ENABLE1, map(pack.vel[0], 151, 250, 1, 255));
        digitalWrite(MOTOREF, LOW);
        digitalWrite(MOTORET, HIGH);
      }
      if(pack.vel[1] <= 150){
        analogWrite(ENABLE2, map(pack.vel[1], 150, 50, 0, 255));
        digitalWrite(MOTORDF, HIGH);
        digitalWrite(MOTORDT, LOW);  
      }
      else{
        analogWrite(ENABLE2, map(pack.vel[1], 151, 250, 1, 255));
        digitalWrite(MOTORDT, HIGH);
        digitalWrite(MOTORDF, LOW);
      }
        
      turnOffMotorTime = millis();
    }
  }
  if(millis() - turnOffMotorTime > 150){ turnOffMotor = 1; }
  if(turnOffMotor){;
    analogWrite(ENABLE1, 0);
    analogWrite(ENABLE2, 0);
    digitalWrite(MOTORET, 0);
    digitalWrite(MOTORDT, 0);
    digitalWrite(MOTOREF, 0);
    digitalWrite(MOTORDF, 0);
    turnOffMotor = 0;
    digitalWrite(LED, LOW);
    
  }
}


void IntialMecanicRotine(){
     #define TEMPO 2000
     int initial_time = millis();
     while(millis() - initial_time < TEMPO){
      
        if(millis() - initial_time < TEMPO/2){
          //Roda motor da esquerda para frente
          analogWrite(ENABLE1, 128);
          digitalWrite(MOTOREF, HIGH);
          digitalWrite(MOTORET, LOW);
          //Roda motor da direita para trás
          analogWrite(ENABLE2, 128);
          digitalWrite(MOTORDF, LOW);
          digitalWrite(MOTORDT, HIGH);
        } else {
          //Roda motor da esquerda para trás
          analogWrite(ENABLE1, 128);
          digitalWrite(MOTOREF, LOW);
          digitalWrite(MOTORET, HIGH);
          //Roda motor da direita para frente
          analogWrite(ENABLE2, 128);
          digitalWrite(MOTORDF, HIGH);
          digitalWrite(MOTORDT, LOW);
        }      
        
     }

    analogWrite(ENABLE1, 0);
    analogWrite(ENABLE2, 0);
    digitalWrite(MOTORET, 0);
    digitalWrite(MOTORDT, 0);
    digitalWrite(MOTOREF, 0);
    digitalWrite(MOTORDF, 0);
     
}
