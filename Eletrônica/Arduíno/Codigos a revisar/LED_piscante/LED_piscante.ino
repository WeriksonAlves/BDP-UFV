int lamp=10;
int i=0;
int j=10;

void setup() {
  pinMode(lamp, OUTPUT);

}

void loop() {
  while(i<5){
    digitalWrite(lamp, HIGH);
    delay(500);
    digitalWrite(lamp, LOW);
    delay(500);
    i= i+1;
  }
  while(j>6){
    digitalWrite(lamp, HIGH);
    delay(100);
    digitalWrite(lamp, LOW);
    delay(100);
    j = j-1;
  }
  i=0;
  j=11;
}
