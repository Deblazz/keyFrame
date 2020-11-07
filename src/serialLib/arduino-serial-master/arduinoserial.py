import termios
import os
import base64
BPS_SYMS={115200: termios.B115200}
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
        bps_sym = BPS_SYMS[bps]
        attrs[ISPEED] = bps_sym
        attrs[OSPEED] = bps_sym
        attrs[CFLAG] &= ~termios.PARENB
        attrs[CFLAG] &= ~termios.CSTOPB
        attrs[CFLAG] &= ~termios.CSIZE
        attrs[CFLAG] |= termios.CS8
        attrs[CFLAG] &= ~termios.CRTSCTS
        attrs[CFLAG] |= termios.CREAD | termios.CLOCAL
        attrs[IFLAG] &= ~(termios.IXON | termios.IXOFF | termios.IXANY)
        attrs[LFLAG] &= ~(termios.ICANON | termios.ECHO | termios.ECHOE | termios.ISIG)
        attrs[OFLAG] &= ~termios.OPOST
        attrs[CC][termios.VMIN] = 0
        attrs[CC][termios.VTIME] = 20
        termios.tcsetattr(self.fd, termios.TCSANOW, attrs)
    def write(self, str):
        os.write(self.fd, str)
    def write_byte(self, byte):
        os.write(self.fd, chr(byte))
def main():
    port = "/dev/ttyACM0"
    bps = 115200
    port = SerialPort(port, bps)
    # with open("../../../img.jpeg", "rb") as f:
    #     send = base64.b64encode(f.read())
    with open("../../../helloworld.txt", "rb") as f:
        send = base64.b64encode(f.read())
    #print(send.decode('utf-8'))
    port.write(send)
if __name__ == "__main__":
    main()