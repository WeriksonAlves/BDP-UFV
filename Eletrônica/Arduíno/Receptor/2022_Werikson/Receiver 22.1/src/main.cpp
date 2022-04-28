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
// Bibliotecas usadas:

#include <SPI.h>  //Biblioteca para comunicação com o SPI
#include "RF24.h" //Biblioteca para comunicação com o rádio

////////////////////////////////////////////////////////////////////////////
// Definição das portas usadas: D3, D4, D5, D9, D10

#define ENABLE1 5    //Pino do PWM do motor ...
#define ENABLE2 6    //Pino do PWM do motor ...
#define MOTORET 1    //Pino do motor esquerdo trás
#define MOTOREF 0    //Pino do motor esquerdo frente
#define MOTORDT 7    //Pino do motor direito trásdigitalWrite(abc, HIGH);
#define MOTORDF 8    //Pino do motor direito frentedigitalWrite(abc, HIGH);
#define BIT1 A1      //Dip Switch de escolha do robô
#define BIT2 A2      //Dip Switch de escolha do robô
#define LED 4        //Pino do LED
#define ROBOD 1      //Pino do robô
#define TEMPO 2000   //Tempo de espera para o robô parar
RF24 receptor(9,10); //Define os pinos de comunicação com o rádio

////////////////////////////////////////////////////////////////////////////
// Definição de constantes e variáveis:

int ROBO = 1;                           //Número do rôbo
byte addresses[][6] = {"BDP", "car"};   //Endereço para envio dos pacotes
struct Pacote { int id; int vel[2]; };  //Pacote de dados para serem enviados
// por rádio; id = N; vel = 0 - Esquerda ou 1 - Direita
Pacote pack;                            //Define o pacote
float val; 
float conv;
bool turnOffMotor = 0;                  //Desliga o motor após algum tempo
unsigned long int turnOffMotorTime = 0; //Conta o tempo para desligar o motor

////////////////////////////////////////////////////////////////////////////
// Definição de protótipos de funções:
void IntialMecanicRotine(); //Função para inicializar as rotina de treino

////////////////////////////////////////////////////////////////////////////
void setup() { //Função setup
  Serial.begin(115200); // Abre a porta serial com o 'Baudrate' passado como parâmetro

  // Setup das portas da Ponte H:
  pinMode(MOTOREF, OUTPUT); //Define o pino do motor esquerdo frente como saída
  pinMode(MOTORET, OUTPUT); //Define o pino do motor esquerdo trás como saída
  pinMode(MOTORDF, OUTPUT); //Define o pino do motor direito frente como saída
  pinMode(MOTORDT, OUTPUT); //Define o pino do motor direito trás como saída
  pinMode(ENABLE1, OUTPUT); //Define o pino de PWM do motor ... como saída
  pinMode(ENABLE2, OUTPUT); //Define o pino de PWM do motor ... como saída

  //Setup do Teste mecânico:
  IntialMecanicRotine();  // Teste mecânico
  
  // Setup do rádio:
  delay(200);                                //Espera 200ms para inicializar o rádio
  receptor.begin();                          //Inicializa o rádio
  receptor.setChannel(83);                   //Define o canal do rádio
  receptor.setPALevel(RF24_PA_MIN);          //Define o nível de potência do rádio
  receptor.setDataRate( RF24_250KBPS );      //Define a taxa de transmissão do rádio
  receptor.openReadingPipe(1, addresses[1]); //Define o endereço de recepção
  receptor.startListening();                 //Inicia a recepção de pacotes
  receptor.printDetails();                   //Imprime os detalhes do rádio

  // Setup das portas do Dip Switch e identificação do rôbo:
  //pinMode(BIT1, INPUT);                                         //Define o pino como entrada
  //pinMode(BIT2, INPUT);                                         //Define o pino como entrada
  if(!digitalRead(BIT1) && digitalRead(BIT2)){ ROBO = 1; }      // Define o rôbo como 1
  else if(digitalRead(BIT1) && !digitalRead(BIT2)){ ROBO = 2;}  // Define o rôbo como 2
  else if(digitalRead(BIT1) && digitalRead(BIT2)){ ROBO = 3;}   // Define o rôbo como 3
  else if(!digitalRead(BIT1) && !digitalRead(BIT2)){ ROBO = 4;} // Define o rôbo como 4
  ROBO = 1; // Define o rôbo como 1 manualmente

  // Verificação do nivel da bateria
  pinMode(A4, INPUT);
  pinMode(A5, OUTPUT); 
  val = analogRead(A4);
  conv = ((2*val)/204.60);
  if (conv <= 6.00){
    digitalWrite(4, HIGH);
    } else{
      digitalWrite(4, LOW);
    }
  
  //retirar depois
  Serial.println("iniciou receiver");
  Serial.print("iniciou robo: ");
  Serial.println(ROBO);
}
////////////////////////////////////////////////////////////////////////////
void loop() { //Função loop
  // Loop do controle:
  while ( receptor.available()>0) { //Enquanto houver pacotes para serem lidos
    digitalWrite(LED, HIGH);             //Liga o LED
    receptor.read( &pack, sizeof(pack)); //Lê o pacote 
    Serial.print("Recebeu pacote id: "); //Imprime o informe
    Serial.println(pack.id);             //Imprime o número do pacote
    if(pack.id == ROBO){                 //Verifica se o pacote é o correto para o rôbo
      Serial.println("Recebeu pack1");   //Imprime o informe
      Serial.print("Robo 1: "); Serial.print(pack.vel[0]); Serial.print(" "); Serial.println(pack.vel[1]);//Imprime os dados do pacote
      if(pack.vel[0] <= 150){ //Verifica se a velocidade do robô é menor que 150
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
        
      turnOffMotorTime = millis(); //Define o tempo para desligar o motor
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
////////////////////////////////////////////////////////////////////////////
void IntialMecanicRotine(){
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