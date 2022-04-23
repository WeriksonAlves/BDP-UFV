 /*
  * 
  * Compass.ino - Exemplo de esboço para ler um cabeçalho de um magnetômetro 
  * de eixo triplo HMC5883L.
  * 
  * GY-273 Módulo de bússola  ->  Arduino
  * VCC  -> VCC  (Ver nota abaixo)
  * GND  -> GND
  * SCL -> A5 / SCL, (use o pino 21 no Arduino Mega)
  * SDA -> A4 / SDA, (use o pino 20 no Arduino Mega)
  * DRDY -> Não conectado (neste exemplo)
  * 
  * Nota de tensão
  * ~~~~~~~~~~~~
  * A placa GY-273 possui um regulador 3v3, e o SDA / SCL é puxado para cima, 
  * de modo que não há problema em usar o Arduino 5v.
  *
  * Se você estiver usando qualquer outra interrupção, ou o IC bruto, precisará 
  * usar 3v3 para fornecer e sinalizar!
  *
  * Datasheet: http://goo.gl/w1criV 
  * 
  *  Copyright (C) 2014 James Sleeman
  * 
  * É concedida permissão, gratuitamente, a qualquer pessoa que obtenha um cópia 
  * deste software e arquivos de documentação associados (o "Software"), negociar 
  * no Software sem restrições, incluindo, sem limitação os direitos de usar, 
  * copiar, modificar, mesclar, publicar, distribuir, sublicenciar, e / ou vender 
  * cópias do Software e permitir pessoas a quem o O Software é fornecido para isso, 
  * sujeito às seguintes condições:
  * 
  * O aviso de direitos autorais acima e este aviso de permissão serão incluídos no
  * todas as cópias ou partes substanciais do software.
  *
  * O SOFTWARE É FORNECIDO "TAL COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA 
  * OU IMPLÍCITA, INCLUINDO MAS NÃO SE LIMITANDO A GARANTIAS DE COMERCIALIZAÇÃO,
  * ADEQUAÇÃO A UM OBJETIVO ESPECÍFICO E NÃO INFRACÇÃO. EM NENHUM CASO A AUTORES OU 
  * TITULARES DE DIREITOS AUTORAIS SÃO RESPONSÁVEIS POR QUALQUER REIVINDICAÇÃO, 
  * DANOS OU OUTROS RESPONSABILIDADE, SEJA EM AÇÃO DE CONTRATO, TORT OU DE OUTRA
  * FORMA, DECORRENTE DE, FORA OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTROS
  * NEGÓCIOS EM O SOFTWARE.
  * 
  * @author James Sleeman, http://sparks.gogo.co.nz/
  * @license MIT License
  * 
  */

#include <Arduino.h>
#include <Wire.h>
#include <HMC5883L_Simple.h>

// Crie uma bússola
HMC5883L_Simple Compass;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // Declinação magnética é a correção aplicada de acordo com a sua localização atual
  // para obter o norte verdadeiro do norte magnético, isso varia de um lugar para outro.
  //
  // A declinação para sua área pode ser obtida em http://www.magnetic-declination.com/
  // Pegue a linha "Declinação magnética" que ela fornece nas informações,
  //
  // Exemplos:
  //  Ubá, -23 ° 7 'OESTE
  //  Viçosa, -23 ° 10 'OESTE
  //  Rodeiro, -23 ° 8 'OESTE
  //  Auckland, 19 ° 30 'LESTE

  Compass.SetDeclination(23, 10, 'W');  

  // O dispositivo pode operar no modo SINGLE (padrão) ou CONTINUOUS
  //  SINGLE significa simplesmente que é necessária uma leitura quando você solicita uma.
  //  CONTINUOUS significa que está sempre fazendo leituras.
  // para a maioria dos propósitos, SINGLE é o que você deseja.
  
  Compass.SetSamplingMode(COMPASS_SINGLE);
  
  // A escala pode ser ajustada para um de vários níveis, você pode deixá-la no padrão.
  // Essencialmente, isso controla a sensibilidade do dispositivo.
  //    As opções são 088, 130 (padrão), 190, 250, 400, 470, 560, 810
  // Especifique a opção como COMPASS_SCALE_xxx
  // Valores mais baixos são mais sensíveis, valores mais altos são menos sensíveis.
  // O padrão provavelmente está bom, funciona para mim. Se parecer muito barulhento 
  // (pulando), aumente a escala para uma mais alta.

  Compass.SetScale (COMPASS_SCALE_130);
  
  // A bússola tem 3 eixos, mas dois deles devem estar próximos da superfície da Terra
  // para lê-la (não compensamos a inclinação, isso é uma coisa complicada) - assim 
  // como uma bússola real tem uma agulha flutuante, você pode imaginar que a bússola 
  // digital também a tem.
  //
  // Para permitir que você monte a bússola de diferentes maneiras, você pode especificar
  // a orientação:
  //
  // COMPASS_HORIZONTAL_X_NORTH (padrão), a bússola é orientada horizontalmente, com
  //      a parte superior para cima. Ao apontar para o norte, a seta da serigrafia X 
  //      apontará para o norte.
  // COMPASS_HORIZONTAL_Y_NORTH, de cima para cima, Y é a agulha, ao apontar para o 
  //      norte a seta da serigrafia Y apontará para o norte.
  // COMPASS_VERTICAL_X_EAST, montado verticalmente (alto) olhando para o lado superior,
  //      quando virado para o norte, a seta da serigrafia X apontará para o leste.
  // COMPASS_VERTICAL_Y_WEST, montado verticalmente (largo), olhando para o lado superior,
  //      quando virado para o norte, a seta da serigrafia Y aponta para oeste.
  Compass.SetOrientation(COMPASS_HORIZONTAL_X_NORTH);
}

// Nosso loop principal do programa.
void loop() {
  float heading = Compass.GetHeadingDegrees();
   
   Serial.print("Heading: \t");
   Serial.println( heading );   
   delay(1000);
}
