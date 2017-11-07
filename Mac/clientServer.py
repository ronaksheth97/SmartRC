import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    clientsocket.connect(('localhost', 8089))
    inpt = raw_input('type anything and click enter... ')
    clientsocket.send(inpt)
    print "the message has been sent"
