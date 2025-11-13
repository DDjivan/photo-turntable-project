char checkMessage;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //make sure this is the same as the Baud Rate in Python script.

}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0) {

    checkMessage = Serial.read();

      if(checkMessage == 'P'){
        Serial.println("Arduino: Hello Python!");
      }
  }
}