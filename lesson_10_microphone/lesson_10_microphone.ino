int Analog = A0;
int Digital = 13;
void setup() {
  pinMode (Analog, INPUT);
  pinMode (Digital, INPUT);
  Serial.begin(9600);
}

void loop() {
  int ana ;
  int dig ;
  ana = analogRead (Analog);
  dig = digitalRead (Digital);
  Serial.print("Analog = ");
  Serial.println(ana);
  Serial.print("Digital = ");
  Serial.println(dig);
}
