void setup() {
  // put your setup code here, to run once:
pinMode (13 , OUTPUT);
pinMode (12 , OUTPUT);
pinMode (11 , OUTPUT);
pinMode (10 , OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
int i = 10;
for (i==10 ; i<=13 ; i++)
{
  digitalWrite(i,HIGH);
  delay(500);
  Serial.println(i);
}
for (i==13 ; i>=10 ; i--)
{
  digitalWrite(i,LOW);
  delay(500);
  Serial.println(i);
}
}
