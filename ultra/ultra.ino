const int trigpin = 12;
const int echopin = 13;
long duration;
int distance;
void setup() {
  pinMode (trigpin, OUTPUT);
  pinMode (echopin, INPUT);
  Serial.begin (9600);
}
void loop() {
  // clears the trigpin
  digitalWrite (trigpin, LOW);
  delayMicroseconds (2);
  // Sets the trigpin on HIGH state
  digitalWrite (trigpin, HIGH) ;
  delayMicroseconds (10);
  digitalWrite (trigpin, LOW);
  // Reads the echopin, returns the
  duration = pulseIn (echopin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // prints the distance on the Seri
  Serial.print ("Distance: ");
  Serial.println (distance);
}
