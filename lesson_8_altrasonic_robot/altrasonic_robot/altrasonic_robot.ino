#include <Ultrasonic.h>

Ultrasonic ultrasonic(12, 13); // 12 tric 13 echo

int Motor_R1 = 6;
int Motor_R2 = 5;
int Motor_L1 = 4;
int Motor_L2 = 3;
int pwmr = 7;
int pwml = 2;

int distance;

void setup() {
  pinMode (Motor_R1, OUTPUT);
  pinMode (Motor_R2, OUTPUT);
  pinMode (Motor_L1, OUTPUT);
  pinMode (Motor_L2, OUTPUT);
  pinMode (pwmr, OUTPUT);
  pinMode (pwml, OUTPUT);
  Serial.begin (9600);
}

void loop() {
  distance = ultrasonic.read();
  Serial.println(distance);
  if (distance <= 13)
  {
    digitalWrite (Motor_R1, 1);
    digitalWrite (Motor_R2, 0);
    analogWrite  (pwmr, 150);
    digitalWrite (Motor_L1, 0);
    digitalWrite (Motor_L2, 1);
    analogWrite  (pwml, 150);
    delay(500);
  }
  else
  {
    digitalWrite (Motor_R1, 1);
    digitalWrite (Motor_R2, 0);
    analogWrite  (pwmr, 250);
    digitalWrite (Motor_L1, 1);
    digitalWrite (Motor_L2, 0);
    analogWrite  (pwml, 250);
  }
  Serial.println(distance);
}

void Move_r()
{
  digitalWrite (Motor_R1, 1);
  digitalWrite (Motor_R2, 0);
  analogWrite  (pwmr, 150);
  digitalWrite (Motor_L1, 0);
  digitalWrite (Motor_L2, 1);
  analogWrite  (pwml, 150);
  delay(1000);
}
void Move_f()
{
  digitalWrite (Motor_R1, 1);
  digitalWrite (Motor_R2, 0);
  analogWrite  (pwmr, 250);
  digitalWrite (Motor_L1, 1);
  digitalWrite (Motor_L2, 0);
  analogWrite  (pwml, 250);
}
void stopp()
{
  digitalWrite (Motor_R1, 0);
  digitalWrite (Motor_R2, 0);
  digitalWrite (Motor_L1, 0);
  digitalWrite (Motor_L2, 0);
}
