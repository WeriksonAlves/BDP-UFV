int led=10;
float analogPin=A3;
float val=0;
void setup() {
  Serial.begin(9600);
  Serial.print("val");

}

void loop() {
  val=analogRead(A3);
  val=map(val,0,1023,0,255);
  Serial.println(val);
  analogWrite(led, val);
}
