#include <Arduino.h>
#include <Wire.h>
#include <HMC5883L_Simple.h>

HMC5883L_Simple Compass; //Criando uma Bússola

void setup() {
  Serial.begin(9600);
  Wire.begin();

  Compass.SetDeclination(23, 10, 'W');
  Compass.SetSamplingMode(COMPASS_SINGLE);
  Compass.SetScale (COMPASS_SCALE_130);
  Compass.SetOrientation(COMPASS_HORIZONTAL_Y_NORTH);
}

void loop() {
  float heading = Compass.GetHeadingDegrees();
  
  Serial.print("Heading: \t");
  Serial.println( heading );   
  delay(1000);
}
