int  led1=10, led2=12;
int pinobotao1=8, pinobotao=9;
int botao1=HIGH, botao2=HIGH;
int val;

void setup() {
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  botao1=digitalRead(8);
  botao2=digitalRead(9);
 if(botao1==LOW)(
  digitalWrite(led1, HIGH);
  delay(2000)
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  while(true){
    }
 }
 if(botao2==LOW)(
  digitalWrite(led2, HIGH);
  delay(2000)
  digitalWrite(led2, LOW);
  digitalWrite(led1, LOW);
  while(true){
    }
 }
}
