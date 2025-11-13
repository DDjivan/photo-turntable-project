#!/bin/env python

import sys
from serial import Serial
import serial.tools.list_ports


def main() -> None:

    for p in serial.tools.list_ports.comports():
        # print(p)
        # print(p, p.description, p.device)
        # print(p.hwid)
        # print(p.interface, p.location, p.manufacturer)
        # print(p.pid)
        # print(p.product)
        # print(p.serial_number, p.subsystem, p.vid)
        print(p.device, p.description, p.hwid, p.location)

    return

if __name__ == "__main__":
    main()
