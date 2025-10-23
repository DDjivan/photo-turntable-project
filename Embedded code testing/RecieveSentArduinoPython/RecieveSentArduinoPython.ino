String incomingMessage;

void sendMessage(String pMessage){
  Serial.println(pMessage);
}

void recieveMessage(){
  if (Serial.available() > 0){
    incomingMessage = Serial.readString(); //reads the serial
    incomingMessage.trim();    //trims invisible Chars

    if (incomingMessage == "Ping") sendMessage("Pong");
    else if (incomingMessage == "bla") sendMessage("bla");
    else if (incomingMessage == "Hello") sendMessage("Bye");
  }
}
void setup() {
  Serial.begin(9600); //make sure this is the same as the baud rate in Python script.
  sendMessage("Arduino: Ready!");
}

void loop() {
  recieveMessage();
}