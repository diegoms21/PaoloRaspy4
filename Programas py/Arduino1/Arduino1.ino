int led = 13;

void setup () {
  Serial.begin(9600);
  
  pinMode(led, OUTPUT);
}

void loop () {
  if (Serial.available()>0) {
    
    char c = Serial.read();
    Serial.print(c);
    if (c == 'E') {
      digitalWrite(led, HIGH);
    }
    if (c == 'A') {
      digitalWrite(led, LOW);
    }
  }
}
