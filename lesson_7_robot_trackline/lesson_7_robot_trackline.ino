int ssr = 12;
int ssl = 13;
int MA_R = 6;
int MB_R = 5;
int pwm_R = 7;
int MA_L = 4;
int MB_L = 3;
int pwm_L = 2;
void setup() {
  pinMode (ssr, INPUT);
  pinMode (ssl, INPUT);
  pinMode (MA_R, OUTPUT);
  pinMode (MB_R, OUTPUT);
  pinMode (MA_L, OUTPUT);
  pinMode (MB_L, OUTPUT);
  pinMode (pwm_R, OUTPUT);
  pinMode (pwm_L, OUTPUT);
}

void loop() {
  int sr = 0;
  int sl = 0;
  sr = digitalRead (ssr);
  sl = digitalRead (ssl);
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
