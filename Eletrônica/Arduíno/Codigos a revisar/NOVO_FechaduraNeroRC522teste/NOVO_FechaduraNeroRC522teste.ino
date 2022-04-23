//------------------------------------------//
//       CÓDIGO TRANCA NERO 20/11/2020      //
//   MÓDULO RC 522 / CARTAO RFID 13,5 KHz   //
//------------------------------------------//

/*
CARTAOES QUE EU TENHO NO CADASTRO:
 Id principal => "CB CE 31 01" => cadastrado na minha carterinha (Celso)!
 // "04 12 0F 23"
 
Definição das portas utilizadas
   Sensor RFID
     RST => D9
     SDA => D10
     MOSI => D11
     MISO => D12
     SCK => D13
     
   Leds indicação
    Vermelho => D4 (Sinaliza entrada permitida)
    Verde => D2 (Sinaliza entrada não permitida)
   Buzzer => D5
   Relé => D3
*/

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
int tempoled = 2000; // TEMPO DE CONTROLE DO LED
int pulso = 200; // TEMPO DE PULSO
String leitura = " ";
// Lista de cartões disponíveis no Laboratorio do Nero
String myStrings[] =  {"CB CE 31 01", "42 16 9B 1E", "F6 FB 4D 1A", "06 89 B3 1B", "06 AB E3 1B", "06 46 FD 1B", "06 72 BA 1B", "1B 83 45 0D", "C6 EE 1F 1A", "06 3C FC 1B",
                       "C3 70 CD 1A", "C6 EB 53 1A", "C6 FF 2D 1A", "C6 B8 F0 1A", "D6 86 08 1A", "C6 E3 B2 1A", "69 3E 4F 8C", "41 97 72 20", "41 AC 07 20", "41 77 87 20",
                       "51 2B 9F 20", "41 C3 2D 20", "41 33 3D 20", "31 1C 16 20", "51 BC EB 20", "9A FE 9C 16", "79 30 58 8D", "D6 5F 49 1A", "D6 31 1C 1A", "06 71 29 1B",                       
                       "D6 10 6A 1A", "D6 7C 0E 1A", "D6 61 28 1A", "D6 44 36 1A", "C6 B9 40 1A", "06 BC D7 1B", "06 78 26 1B", "06 5F 7B 1B", "D6 65 AB 1E", "E9 AF 28 8C",
                       "D6 65 E9 1A", "C6 C7 BB 1A", "D6 57 29 1A", "C6 BA 3C 1A", "4B FE B0 0E" };

//Cartões que bugam o sistema: "D6 9C F1 1A", "8B D2 46 0D", "AB 22 17 0F", "7B 3C 3A 0D", "9B 78 39 0D", "1B DA 44 0D", "6B 79 15 0F", "2B 2F 33 0D"

void setup() {
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();    // Init MFRC522 card
  Serial.println("iniciou o teste");

  //digitalWrite(ledverde, HIGH);

  // Definiçao do Estado das portas
  pinMode(rele, OUTPUT);
  pinMode(ledverde, OUTPUT);
  pinMode(ledvermelho, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  Serial.print("Identificação do cartao:");
  String conteudo = "";
  byte letra;
  //String aux = "";
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
    conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
    conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  
  bool verifica = false;
  Serial.println();
  Serial.print("Mensagem : ");
  conteudo.toUpperCase();
  int j;
  //Executa as ações a partir deste ponto
  for (j = 0; j <= 100; j++) {
    if(j<100){
      if (conteudo.substring(1) == myStrings[j]) {
      Serial.println("Cartão Aceito");
      Serial.println(" ");
      digitalWrite(ledverde, HIGH);
      delay(tempoled);
      digitalWrite(ledverde, LOW);
      digitalWrite(rele, HIGH);
      delay(pulso);
      digitalWrite(rele, LOW);
      verifica = true;
      conteudo = "";
      break;
      }
    }
    else {
      if (conteudo.substring(1) != myStrings[j]) {
        Serial.println("Cartão Recusado");
        Serial.println(" ");
      }
    }
  }
    delay(1000);      
}
