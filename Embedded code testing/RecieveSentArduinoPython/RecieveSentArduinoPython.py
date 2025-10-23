import serial
import sys
import time


ser = serial.Serial('COM5', baudrate = 9600, timeout=1)
time.sleep(2)

def send_Message(pMessage):
        print("Send: " + pMessage)
        ser.write((pMessage + '\n').encode('utf-8'))

def recieve_Message():
        if ser.in_waiting > 0:
                incoming_Message = ser.readline().decode('utf-8').strip()
                print("Recieved: " + incoming_Message)

                if incoming_Message == "Arduino: Ready!": print("We are ready to communicate")
                elif incoming_Message == "Pong": print("You can excecute any command")                                     
                elif incoming_Message == "bla": send_Message("bla")
                elif incoming_Message == "Bye": print("")
                elif incoming_Message == "Hello": print("")
                
                else: print("recieved unknown Message: " + incoming_Message)

try:
        send_Message("Ping")
        while 1:
                recieve_Message()
                time.sleep(0.1)
except KeyboardInterrupt:
        print("\nProgramm stoped.")
finally:
        ser.close()
        print("Serial closed.")
	
