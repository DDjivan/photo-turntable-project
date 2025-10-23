String checkMessage = "";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //make sure this is the same as the baud rate in Python script.
  Serial.write("Hello, Arduino Ready!" + '\n');
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0) {
    checkMessage = (Serial.readString());
    checkMessage.trim();

      if (checkMessage == "pPing")
        Serial.println("Pong");

  }
}