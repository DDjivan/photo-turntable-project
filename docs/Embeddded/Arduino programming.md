### What?:
We need to communicate.
Arduino <=> PC
We will use the serial communication.

### resources used:
https://www.pyserial.com/docs/arduino-integration:
Maybe implement the "Find Arduino Port": 

```python
import serial.tools.list_ports

def find_arduino():
    """Find Arduino automatically"""
    for port in serial.tools.list_ports.comports():
        if 'Arduino' in port.description or 'CH340' in port.description:
            return port.device
    return None

port = find_arduino()
if port:
	print(f"Found Arduino on {port}")
else:
    print("Arduino not found")
```

https://www.youtube.com/playlist?list=PLb1SYTph-GZJb1CFM7ioVY9XJYlPVUBQy

https://www.geeksforgeeks.org/python/try-except-else-and-finally-in-python/

https://docs.arduino.cc/language-reference/en/structure/control-structure/switchCase/
Switch-Case-Statements can not be made with Strings

https://www.geeksforgeeks.org/python/python-strings-decode-method/

### Dependencies

For Microsoft Windows: the [latest stable python version](https://www.python.org/downloads/). 

Then we run the command line on Windows to install the [Python Serial Port Extension](https://pypi.org/project/pyserial/):

```
py -m pip install pyserial
```

on Linux or MacOS:

```
python -m pip install pyserial
```


### Arduino Testing explained
This some example Arduino code.
```cpp
String text;
void setup() {
  Serial.begin(9600);
}

void loop() {
	// checks if there is a Serial message available
	if (Serial.available() > 0) { 
		// sets the text variable to the newest serial message
	    text = Serial.readString(); 
	}
  
  // prints the message to serial over and over
  Serial.println(text); 
}
```


[Hello_WorldSerialPython.py](../../Embedded%20code%20testing/Hello_WorldSerialPython.py) (Test code)
```python
import sys
from time import sleep

while True:
	print("Hello World!")
	sleep(3)
	print("Bye World!")
	sys.exit()
```


[Arduino_Python_manual_message_recieving.py](../../Embedded%20code%20testing/Arduino_Python_manual_message_recieving/Arduino_Python_manual_message_recieving.py)
```python
TO BE UPDATED
```

[Arduino_Python_manual_message_recieving.ino](../../Embedded%20code%20testing/Arduino_Python_manual_message_recieving/Arduino_Python_manual_message_recieving.ino)

```c++
LOOK IN THE FILE
```



