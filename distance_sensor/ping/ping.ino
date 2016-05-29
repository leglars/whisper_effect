#define trigPin 13
#define echoPin 12
#define led 10

int flag;
boolean command = false;

void setup() {
  Serial.begin (19200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  if (command) {
  	if(flag == 'P') {

  		ping();
  		command = false;
  		flag = 0;
  	}
  }
  delay(50);
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    flag = Serial.read();
    command = true;
    // Serial.println(flag);
    digitalWrite(led,HIGH);

    // }
  }
}

void ping() {
  long duration, dist_relay, dist_led, dist;
  digitalWrite(trigPin, LOW);  // Added this line
  delayMicroseconds(2); // Added this line
  digitalWrite(trigPin, HIGH);
  //  delayMicroseconds(1000); - Removed this line
  delayMicroseconds(10); // Added this line
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  dist = (duration/2) / 29.1;
  Serial.println(dist);
  digitalWrite(led,LOW);
}
