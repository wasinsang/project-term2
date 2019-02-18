int MotorR_1 = 8;
int MotorR_2 = 7;
int pwmr = 9;
int MotorL_1 = 5;
int MotorL_2 = 4;
int pwml = 3;
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
