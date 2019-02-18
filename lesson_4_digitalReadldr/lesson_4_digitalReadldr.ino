int SS = 12;
void setup() {
  pinMode (SS, INPUT);
  Serial.begin(9600);
}

void loop() {
  int i ;
  i = digitalRead (SS);
  Serial.println(i);
}
