#from __future__ import print_function
import termios
import os
#import sys
#import time
#import getopt
import base64

BPS_SYMS={115200: termios.B115200}

# Indices into the termios tuple.
IFLAG = 0
OFLAG = 1
CFLAG = 2
LFLAG = 3
ISPEED = 4
OSPEED = 5
CC = 6

def bps_to_termios_sym(bps):
    return BPS_SYMS[bps]

class SerialPort(object):
    
    def __init__(self, serialport, bps):
    
        self.fd = os.open(serialport, os.O_RDWR | os.O_NOCTTY | os.O_NDELAY)
        attrs = termios.tcgetattr(self.fd)

        # bps_sym = bps_to_termios_sym(bps)
        bps_sym = BPS_SYMS[bps]

        # Set I/O speed.
        attrs[ISPEED] = bps_sym
        attrs[OSPEED] = bps_sym

        # 8N1
        attrs[CFLAG] &= ~termios.PARENB
        attrs[CFLAG] &= ~termios.CSTOPB
        attrs[CFLAG] &= ~termios.CSIZE
        attrs[CFLAG] |= termios.CS8
        # No flow control
        attrs[CFLAG] &= ~termios.CRTSCTS

        # Turn on READ & ignore contrll lines.
        attrs[CFLAG] |= termios.CREAD | termios.CLOCAL
        # Turn off software flow control.
        attrs[IFLAG] &= ~(termios.IXON | termios.IXOFF | termios.IXANY)

        # Make raw.
        attrs[LFLAG] &= ~(termios.ICANON | termios.ECHO | termios.ECHOE | termios.ISIG)
        attrs[OFLAG] &= ~termios.OPOST

        # It's complicated--See
        # http://unixwiz.net/techtips/termios-vmin-vtime.html
        attrs[CC][termios.VMIN] = 0
        attrs[CC][termios.VTIME] = 20
        termios.tcsetattr(self.fd, termios.TCSANOW, attrs)

    def write(self, str):
        os.write(self.fd, str)

    def write_byte(self, byte):
        os.write(self.fd, chr(byte))

def main():
    mystring = " "
    b = bytes(mystring, 'utf-8')
    port = "/dev/ttyACM1"
    bps = 115200
    port = SerialPort(port, bps)
    with open("../../../pizza.jpg", "rb") as img:
        send = base64.b64encode(img.read())

    #print(send.decode('utf-8'))
    port.write(send)

if __name__ == "__main__":
    main()