
//------------------------------------------//
//       CÓDIGO TRANCA NERO 13/11/2020      //
//   MÓDULO RC 522 / CARTAO RFID 13,5 KHz   //
//------------------------------------------//

//  CARTAOES QUE EU TENHO NO CADASTRO: 
// "04 12 0F 23"
// "CB CE 31 01"

/* Definição das portas utilizadas
   Sensor RFID
     RST => D9
     SDA => D10
     MOSI => D11
     MISO => D12
     SCK => D13
   
   * Leds indicação
    Vermelho => D4 (Sinaliza entrada permitida)
    Verde => D2 (Sinaliza entrada não permitida)
  Buzzer => D5  
  Relé => D3
 * */

#include <SPI.h> 

//RFID: 
//VERIFICAR SAIDAS ICSP (11 12 13)
#include <MFRC522.h> //LEitor RFID
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

// Definição das variaveis 
int rele = 3;// PINO QUE CONTROLA O RELÉ 
int ledverde = 2; //  PINO QUE CONTROLA O LED 
int ledvermelho = 4; //  PINO QUE CONTROLA O LED 
int buzzer = 5; //  sinalização sonora 
int tempoled = 500; // TEMPO DE CONTROLE DO LED
int pulso = 200; // TEMPO DE PULSO


void setup() {
  Serial.begin(9600);   
  SPI.begin();
  mfrc522.PCD_Init();    // Init MFRC522 card
  Serial.println("iniciou o teste");

  // Definiçao do Estado das portas
  pinMode(rele,OUTPUT);
  pinMode(verde,OUTPUT);
  pinMode(vermelho,OUTPUT);
  pinMode(buzzer,OUTPUT);
}

void loop() {
   if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }
 
  Serial.print("Identificação do cartao:");
  String conteudo= "";
  byte letra;
  for (byte i = 0; i < mfrc522.uid.size; i++) {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  
  Serial.println();
  Serial.print("Mensagem : ");
  conteudo.toUpperCase();

  //Executa as ações a partir deste ponto
if (conteudo.substring(1) == "04 12 0F 23" || "CB CE 31 01") {
    Serial.print("LIBERADO !!! PODE PASSAR !!!");
    //Serial.println();
    //Serial.println("Cartão Aceito");
    digitalWrite(verde, HIGH);
    delay(tempoled);
    digitalWrite(verde, LOW);
    digitalWrite(rele, HIGH);
    delay(pulso);
    digitalWrite(rele, LOW);
    delay(pulso);
    }
}
