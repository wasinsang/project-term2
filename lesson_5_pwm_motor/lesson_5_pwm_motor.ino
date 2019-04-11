int MotorR_1 = 11;
int MotorR_2 = 12;
int pwmr = 13;
int MotorL_1 = 8;
int MotorL_2 = 9;
int pwml = 10;
void setup() {
  pinMode (MotorR_1, OUTPUT);
  pinMode (MotorR_2, OUTPUT);
  pinMode (pwmr, OUTPUT);
  pinMode (MotorL_1, OUTPUT);
  pinMode (MotorL_2, OUTPUT);
  pinMode (pwml, OUTPUT);
}
void loop() {
  digitalWrite(MotorR_1, 1);
  digitalWrite(MotorR_2, 0);
  analogWrite(pwmr, 255);
  digitalWrite(MotorL_1, 1);
  digitalWrite(MotorL_2, 0);
  analogWrite(pwml, 255);
  delay(2000);
  digitalWrite(MotorR_1, 0);
  digitalWrite(MotorR_2, 1);
  analogWrite(pwmr, 255);
  digitalWrite(MotorL_1, 0);
  digitalWrite(MotorL_2, 1);
  analogWrite(pwml, 255);
  delay(2000);
}
