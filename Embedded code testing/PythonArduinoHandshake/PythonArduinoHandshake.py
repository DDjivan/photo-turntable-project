import serial
import sys
import time


ser = serial.Serial('COM5', baudrate = 9600, timeout=2)
time.sleep(0.1)

def send_command(cmd):
        ser.write(('p' + cmd + '\n').encode())
        arduinoMessage = ser.readline().decode('utf-8').strip()
        return arduinoMessage

def compare_Message(Message):
        switch={
                'A': lambda: print(Message),
                "Stop": lambda: print("Tschüss"),
                }
        func = switch.get(Message.strip())

        if func:
                func()

print(send_command("Ping"))

while 1:
        if ser.in_waiting > 0:
                compare_Message(ser.readline().decode('utf-8').strip())
        time.sleep(0.1)
	
