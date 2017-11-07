char val; // Data received from the serial port

int FORWARDSPEED = 150;
int TURNSPEED = 150;
char previousVal;

void setup() {
  Serial.begin(9600); // Start serial communication at 9600bps
  establishContact();  // send a byte to establish contact until receiver responds

  // Drive motors
  pinMode(12, OUTPUT); //Initiates Motor Channel A pin
  pinMode(9, OUTPUT); //Initiates Brake Channel A pin

  // Direction motors
  pinMode(13, OUTPUT); //Initiates Motor Channel B pin
  pinMode(8, OUTPUT); //Initiates Brake Channel B pin

  // Making sure the motors are fully stopped once the program loads
  digitalWrite(9, HIGH);  // car stops moving
  digitalWrite(8, HIGH);  // tires go back to a neutral position
  analogWrite(3, 0);
  analogWrite(11, 0);
}

void loop() {
  if (Serial.available()) { // If data is available to read
    previousVal = val;
    val = Serial.read();
  }

    switch (val) {
        case 'w':            forward();  //"w"   
                            break;
        case 'a':            left();   // "a"
                            break;
        case 's':            reverse();  // "s"   
                            break;
        case 'd':            right();   // "d"
                            break;
        case 'x':            stop();   // "x"
                            break;
    //Serial.print(inByte);
  }
  delay(10);
}

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.println("Awaiting input...");
    delay(1000);
  }
}

// Car drives forward
void forward() {
  if(previousVal == 'w'){
    return;
  }
  else if(previousVal == 's'){
    digitalWrite(9,HIGH); // Car stops moving to go from moving backwards to forwards
  }
   digitalWrite(12, LOW); // Establishes forward direction of Channel A
   digitalWrite(9, LOW);   // Disengage the Brake for Channel A
   if(val != 'a' || val != 'd'){
    digitalWrite(8, HIGH); // Direction changes to center
   }
   analogWrite(3, 255);  // Spins the motor on Channel A at full speed 
   delay(250);
   analogWrite(3, 50);
}

// Car drives forward and left
void left(){
  // Direction change (left)
  digitalWrite(8, HIGH);
  digitalWrite(13, HIGH);  //
  digitalWrite(8, LOW);
  analogWrite(11, TURNSPEED);
  //forward();
}

// Car drives forward and right
void right(){
  // Direction change (right)
  digitalWrite(8, HIGH);
  digitalWrite(13, LOW);
  digitalWrite(8, LOW);
  analogWrite(11, TURNSPEED);
  //forward();
}

// Car drives reverse
void reverse(){
  if(previousVal == 's'){
    return;
  }
  else if(previousVal == 'w'){
    digitalWrite(9,HIGH); // Car stops moving to go from moving backwards to forwards
  }
   digitalWrite(12, HIGH); // Establishes forward direction of Channel A
   digitalWrite(9, LOW);   // Disengage the Brake for Channel A
   if(val != 'a' || val != 'd'){
    digitalWrite(8, HIGH); // Direction changes to center
   }
   analogWrite(3, FORWARDSPEED);  // Spins the motor on Channel A at full speed 
}

// Car stops
void stop(){
  digitalWrite(9, HIGH);  // car stops moving
  digitalWrite(8, HIGH);  // tires go back to a neutral position
  analogWrite(3, 0);
  analogWrite(11, 0);
}
