import serial


ser = serial.Serial('COM5', baudrate = 9600, timeout=1)

def getSerialText():
        ser.write(b'P')        
        arduinoMessage = ser.readline().decode('utf-8')
        return arduinoMessage

while 1:

        userInput = input('get data points?')
        
        if userInput == 'y':
                print(getSerialText())
	
        if userInput == 'N':
                print("Serial closed")
                ser.close
