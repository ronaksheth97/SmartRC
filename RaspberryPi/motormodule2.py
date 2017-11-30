import os
import pygame
from pygame.locals import *
import serial
import socket


def main():

    pygame.init()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.43.53', 7001))
    server_socket.listen(0)

    # accept a single connection
    (connection, connection_addr) = server_socket.accept()

    
    
    # Ensure this is the proper serial port from the 'Tools' tab in Arduino IDE
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

    send_inst = True

    clock = pygame.time.Clock()
    while send_inst:
        try:
            key_input = connection.recv(128)
        except socket.error, e:
            print("Error")
            break
        if key_input == '':
            print("Connection Closed")
            break
        elif key_input == "240":         # For some reason when no key is pressed
            print(int(key_input))        # '240' is sent to Arduino constantly
        elif key_input == "9":           # Will look into this more thoroughly later
            send_inst = False
            ser.write('x')
            break
        else:
            print(key_input)
            ser.write(key_input)

    connection.close()
    server_socket.close()
            

if __name__ == '__main__': 
    main()
