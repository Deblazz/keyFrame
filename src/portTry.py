import termios, os, base64, serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "Arduino" in p.description:
        port = str(p)
        port = port.split(" ")
        print(port)

port = port[0]
print(port)