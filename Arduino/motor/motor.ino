
int FORWARDSPEED = 200;
int TURNSPEED = 150;
int command = 0; //Data received from the serial port. Initial Command

void setup() {
  Serial.begin(115200); // Start serial communication at 115200bps
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
    command = Serial.read();
  }
  else{
    reset();
  }
  send_command(command, time);
}

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.println("Awaiting input...");
    delay(1000);
  }
}

// Car drives forward
void forward(int time) {
   digitalWrite(12, LOW); // Establishes forward direction of Channel A
   analogWrite(3, FORWARDSPEED);  // Spins the motor on Channel A at full speed 
   delay(time);
}

// Car turns left
void left(int time){
  // Direction change (left)
  digitalWrite(13, HIGH);  //
  analogWrite(11, TURNSPEED);
  delay(time);
}

// Car turns right
void right(int time){
  // Direction change (right)
  digitalWrite(13, LOW);
  analogWrite(11, TURNSPEED);
  delay(time);
}

// Car drives reverse
void reverse(int time){
   digitalWrite(12, HIGH); // Establishes reverse direction of Channel A
   analogWrite(3, FORWARDSPEED);  // Spins the motor on Channel A at full speed 
}

// Car drives forward and right
void forward_right(int time){
  digitalWrite(12, LOW);
  digitalWrite(13, LOW);
  analogWrite(3, FORWARDSPEED);
  delay(time);
}

// Car drives forward and left
void forward_left(int time){
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  analogWrite(3, FORWARDSPEED);
  delay(time);
}

// Car drives reverse and left
void reverse_left(int time){
  digitalWrite(12, HIGH);
  digitalWrite(13, HIGH);
  analogWrite(3, FORWARDSPEED);
  delay(time);
}

// Car drives reverse and right
void reverse_right(time){
  digitalWrite(12, HIGH);
  digitalWrite(13, LOW);
  analogWrite(3, FORWARDSPEED);
  delay(time);
}


void send_command(int command, int time){
  switch (command){

     //reset command
     case 0: reset(); break;

     // single command
     case 1: forward(time); break;
     case 2: reverse(time); break;
     case 3: right(time); break;
     case 4: left(time); break;

     //combination command
     case 6: forward_right(time); break;
     case 7: forward_left(time); break;
     case 8: reverse_right(time); break;
     case 9: reverse_left(time); break;

     default: Serial.print("Inalid Command\n");
    }
}
