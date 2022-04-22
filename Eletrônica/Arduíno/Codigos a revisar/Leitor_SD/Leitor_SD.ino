// Autor: FILIPEFLOP
 
#include <SdFat.h>
 
SdFat sdCard;
SdFile meuArquivo;
 
// Pino ligado ao CS do modulo
const int chipSelect = 4;
 
void setup()
{
  Serial.begin(9600);
  // Define o pino do potenciometro como entrada
  pinMode(A5, INPUT);
  // Inicializa o modulo SD
  if(!sdCard.begin(chipSelect,SPI_HALF_SPEED))sdCard.initErrorHalt();
  // Abre o arquivo LER_POT.TXT
  if (!meuArquivo.open("ler_pot.txt", O_RDWR | O_CREAT | O_AT_END))
  {
    sdCard.errorHalt("Erro na abertura do arquivo LER_POT.TXT!");
  }
}
 
void loop()
{
  // Leitura da porta A5/Potenciometro
  int valor = analogRead(A5);
  Serial.print("Leitura Potenciometro: ");
  Serial.println(valor);
 
  // Grava dados do potenciometro em LER_POT.TXT
  meuArquivo.print("Leitura Potenciometro: ");
  meuArquivo.println(valor);
 
  if (valor <= 5)
  {
    // Interrompe o processo e fecha o arquivo
    Serial.println("Processo de gravacao interrompido. Retire o SD!");
    meuArquivo.close();
    while (1) {}
  }
  delay(2000);
}
