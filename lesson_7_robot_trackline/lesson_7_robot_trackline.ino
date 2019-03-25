int ssr = A2;
int ssl = A0;
int MA_R = 9;
int MB_R = 8;
int pwm_R = 11;
int MA_L = 7;
int MB_L = 6;
int pwm_L = 10;
int LED_A =4; 
int LED_B =3;
void setup() {
  pinMode (LED_A, OUTPUT);
  pinMode (LED_B, OUTPUT);
  pinMode (ssr, INPUT);
  pinMode (ssl, INPUT);
  pinMode (MA_R, OUTPUT);
  pinMode (MB_R, OUTPUT);
  pinMode (MA_L, OUTPUT);
  pinMode (MB_L, OUTPUT);
  pinMode (pwm_R, OUTPUT);
  pinMode (pwm_L, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sr = 0;
  int sl = 0;
  sr = digitalRead (ssr);
  sl = digitalRead (ssl);
  Serial.print(sr);
  Serial.println(sl);
  
  if (sr == 0)
  {
    digitalWrite (MA_R, 1);
    digitalWrite (MB_R, 0);
    digitalWrite (LED_B, 0);
    analogWrite (pwm_R, 0);
  }
  if (sl == 0)
  {
    digitalWrite (MA_L, 1);
    digitalWrite (MB_L, 0);
    digitalWrite (LED_A, 0);
    analogWrite (pwm_L, 0);
  }
  if (sl == 1)
  {
    digitalWrite (MA_L, 1);
    digitalWrite (MB_L, 0);
    digitalWrite (LED_A, 1);
    analogWrite (pwm_L, 255);
  }
  if (sr == 1)
  {
    digitalWrite (MA_R, 1);
    digitalWrite (MB_R, 0);
    digitalWrite (LED_B, 1);
    analogWrite (pwm_R, 255);
  }
}
