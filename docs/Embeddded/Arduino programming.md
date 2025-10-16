```cpp
String text;
void setup() {
  Serial.begin(9600); //make sure this is the same as the Baud Rate in Godot.
}

void loop() {

  if (Serial.available() > 0) { //checks if there is a Serial message available
    text = Serial.readString(); // sets the text variable to the newest serial message
  }
  
	Serial.println(text); // prints the message to serial
}
```



