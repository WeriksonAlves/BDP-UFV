int lamp=9; int bot=8; int led=10;
int i=0; int j=11; int k=0;

void setup() {
  pinMode(lamp, OUTPUT);
  pinMode(bot, LOW);

}

void loop() {
  if (bot==HIGH){
    k = k+1;
  }
  if (k==0){
    digitalWrite(led, HIGH);
  }
    else-if (k==1){
      while(i<5){
        digitalWrite(lamp, HIGH);
        delay(500);
        digitalWrite(lamp, LOW);
        delay(500);
        i= i+1;
      }
    }
    else-if(k==1){
      while(i<5){
        digitalWrite(lamp, HIGH);
        delay(200);
        digitalWrite(lamp, LOW);
        delay(200);
        i= i+1;
      }
      while(j>6){
        digitalWrite(lamp, HIGH);
        delay(200);
        digitalWrite(lamp, LOW);
        delay(200);
        j = j-1;
      }
    }
    else-if(k==3){
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
    }
    else{
      i=0;
      j=11;
      k=0;
    }
}

