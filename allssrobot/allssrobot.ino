#include <Ultrasonic.h>

Ultrasonic ultrasonic(12, 13); // 12 tric 13 echo

int MA_R = 6;
int MB_R = 5;
int MA_L = 4;
int MB_L = 3;
int pwm_R = 7;
int pwm_L = 2;

int distance;

void setup() {
  pinMode (MA_R, OUTPUT);
  pinMode (MB_R, OUTPUT);
  pinMode (MA_L, OUTPUT);
  pinMode (MB_L, OUTPUT);
  pinMode (9, INPUT);
  pinMode (8, INPUT);
  pinMode (pwm_R, OUTPUT);
  pinMode (pwm_L, OUTPUT);
  Serial.begin (9600);
}

void loop() {
  int sr = digitalRead(8);
  int sl = digitalRead(9);
  distance = ultrasonic.read();
  Serial.println(distance);
  if (distance <= 13)
  {
    digitalWrite (MA_R, 1);
    digitalWrite (MB_R, 0);
    analogWrite  (pwm_R, 150);
    digitalWrite (MA_L, 0);
    digitalWrite (MB_L, 1);
    analogWrite  (pwm_L, 150);
    delay(500);
  }
  else
  {
    if (sr == 1)
    {
      digitalWrite (MA_R, 1);
      digitalWrite (MB_R, 0);
      analogWrite (pwm_R, 0);
    }
    if (sl == 1)
    {
      digitalWrite (MA_L, 1);
      digitalWrite (MB_L, 0);
      analogWrite (pwm_L, 0);
    }
    if (sl == 0)
    {
      digitalWrite (MA_L, 1);
      digitalWrite (MB_L, 0);
      analogWrite (pwm_L, 255);
    }
    if (sr == 0)
    {
      digitalWrite (MA_R, 1);
      digitalWrite (MB_R, 0);
      analogWrite (pwm_R, 255);
    }
  }
  Serial.println(distance);
}
