```cpp
String text;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //make sure this is the same as the Baud Rate in Godot.

}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0) {
    text = Serial.readString();
  }
  
	Serial.println(text);
}
```



