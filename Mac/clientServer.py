import socket

s = socket.socket()
host = '111.111.0.11' # needs to be in quote
port = 1247
s.connect((host, port))
print s.recv(1024)
inpt = raw_input('type anything and click enter... ')
s.send(inpt)
print "the message has been sent"
