// Change the speed here if needed.
int speed = 255;

// Commands are:
// 'w' Drive forward. Straight direction.
// 's' Drive backward. Straight direction.
// 'a' No driving. Change direction to left.
// 'd' No driving. Change direction to right.
//
// 'q' Drive forward. Change direction to left.
// 'e' Drive forward. Change direction to right.
// 'z' Drive backward. Change direction to left.
// 'c' Drive backward. Change direction to right.
//
// 'x' Stop the car.


void drive(int);
void changeDirection(int);
void stopCar();

void setup()
{
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

  Serial.begin(9600); // Opens the serial port, sets data rate to 9600 bps
}

void loop()
{
  char direction;
  
  while (Serial.available() == 0){}
  direction = Serial.read();

  switch (direction)
  {
    case 'w':
    {
      drive(LOW);
      break;      
    }
    case 's':
    {
      drive(HIGH);
      break;
    }
    case 'a':
    {
      changeDirection(HIGH);
      break;
    }
    case 'd':
    {
      changeDirection(LOW);
      break;
    }
    case 'q':
    {
      drive(LOW);
      changeDirection(HIGH);
      break;      
    }
    case 'e':
    {
      drive(LOW);
      changeDirection(LOW);
      break;
    }
    case 'z':
    {
      drive(HIGH);
      changeDirection(LOW);
      break;
    }
    case 'c':
    {
      drive(HIGH);
      changeDirection(HIGH);
      break;
    }
    case 'x':
    {
      stopCar();
      break;
    }
    default:
    {
      break;
    }
  }
}

// Drive
void drive(int channelAState)
{
  digitalWrite(9, HIGH);  // Car stops moving when changing direction
  digitalWrite(12, channelAState); // Establishes forward/backward direction of Channel A
  digitalWrite(9, LOW);   // Disengage the Brake for Channel A
  analogWrite(3, speed);  // Spins the motor on Channel A at full speed

  // Direction changes to center
  digitalWrite(8, HIGH);
}

// Change Direction
void changeDirection(int channelBState)
{
  digitalWrite(8, HIGH);
  digitalWrite(13, channelBState);
  digitalWrite(8, LOW);
  analogWrite(11, speed);
}

// Stop vehicle
void stopCar()
{
  digitalWrite(9, HIGH);  // car stops moving
  digitalWrite(8, HIGH);  // tires go back to a neutral position
  analogWrite(3, 0);
  analogWrite(11, 0);
}


