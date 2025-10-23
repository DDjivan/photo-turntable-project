#include "Servo.h" // Include the library
Servo myservo; // Create the servo object
const int pinServo = 9;
int pos = 0;


void setup() { // Setup section to run once
  myservo.attach(pinServo); // attach the servo to our servo object
  myservo.write(pos); // stop the motor
}

void turnDegrees(int pMaxDeg, int pSteps = 1){
	for(pos;pos<= pMaxDeg;pos += pSteps){
      myservo.write(pos);
      //delay(15);
    }
}

void loop() 
{
  turnDegrees(180,10);
}