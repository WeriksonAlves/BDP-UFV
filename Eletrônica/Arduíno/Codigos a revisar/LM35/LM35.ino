float analogPin=3;
float val=0;
float Temperatura=0;
void setup() {
  Serial.begin(9600);
  Serial.print("val");
  }
  
void loop() {
  val=analogRead(3);
  val=(val/1023)*5;
  Temperatura=map(val,0,1023,0,500);
  Serial.println(Temperatura);
    
}
