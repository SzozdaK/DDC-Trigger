#!/usr/bin/env python

import serial
import subprocess
import time
import re

pn = 0 #Initialise past port number as 0. When script first runs, the monitor should flash.

def ddc_console(pn,cn):
    ddcmap = [0x19,0x0f,0x11,0x12] #Addresses of individual input sources for Dell UP2720Q: Thunderbolt, DisplayPort, HDMI 1, and HDMI 2, respectively.
    if cn != pn:
        subprocess.run(f'/usr/bin/ddcutil setvcp 60 {ddcmap[cn-1]}',shell=True) #Switch input source is feature 60 of the MCCS.
    return cn

port = serial.Serial('/dev/ttyUSB0') #Serial port is a USB-to-RS485 cable.
while True:
    time.sleep(0.2)
    port.write(b'info\r') #Send 'info' to Aten US3344i switch; it will respond with the command status, port number, and current firmware version.
    o = b''
    while port.inWaiting() > 0:
        o += port.readline()
    try:
        cn = int(re.findall(b'PORT: 0.',o)[0].decode()[-1]) #Extract current port number of switch.
        pn = ddc_console(pn,cn) #Update past port number and send corresponding DDC command to switch input source.
    except IndexError:
        continue
