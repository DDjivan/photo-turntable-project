#!/bin/env python

from serial import Serial
import sys
from time import sleep



def send_Message(ser:Serial, pMessage:str) -> None:
    print(f"Send: {pMessage}")
    ser.write((pMessage + '\n').encode('utf-8'))
    return

def recieve_Message(ser:Serial) -> None:
    if ser.in_waiting <= 0:
        return
    
    incoming_Message = ser.readline().decode('utf-8').strip()
    print("Recieved: " + incoming_Message)

    match incoming_Message:
        case "Arduino: Ready!":
            print("We are ready to communicate")
        case "Pong":
            print("You can excecute any command")
        case "bla":
            send_Message(ser, "bla")
        case "Bye":
            print("")
        case "Hello":
            print("")
        case _:
            print("recieved unknown Message: " + incoming_Message)

    return



def main() -> None:
    # on MS Windows:    "COM###"
    # on Linux:         "/dev/ttyUSB###"
    port_device = "/dev/ttyUSB0"
    myser = Serial(port_device, baudrate = 9600, timeout = 1)
    sleep(2)

    try:
        send_Message(myser, "Ping")
        while True:
            recieve_Message(myser)
            sleep(0.1)

    except KeyboardInterrupt:
        print("")
        print("Programm stoped.")

    finally:
        myser.close()
        print("Serial closed.")

    return

if __name__ == "__main__":
    main()
