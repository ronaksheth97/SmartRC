import os
import pygame
from pygame.locals import *
import serial

def pygameSetup():
    pygame.init()
    screen = pygame.display.set_mode((468, 60))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Drive yo' Car", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()


def main():

    pygameSetup()

    # Ensure this is the proper serial port from the 'Tools' tab in Arduino IDE
    ser = serial.Serial('/dev/cu.usbmodem1421', 115200, timeout=1)
    send_inst = True

    clock = pygame.time.Clock()

    while send_inst:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    key_input = pygame.key.get_pressed()

                    # complex orders
                    if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                        print("Forward Right")
                        ser.write(chr(6))

                    elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                        print("Forward Left")
                        ser.write(chr(7))

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                        print("Reverse Right")
                        ser.write(chr(8))

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                        print("Reverse Left")
                        ser.write(chr(9))

                    # simple orders
                    elif key_input[pygame.K_UP]:
                        print("Forward")
                        ser.write(chr(1))

                    elif key_input[pygame.K_DOWN]:
                        print("Reverse")
                        ser.write(chr(2))

                    elif key_input[pygame.K_RIGHT]:
                        print("Right")
                        ser.write(chr(3))

                    elif key_input[pygame.K_LEFT]:
                        print("Left")
                        ser.write(chr(4))

                    # exit
                    elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                        print 'Exit'
                        send_inst = False
                        ser.write(chr(0))
                        ser.close()
                        break

                elif event.type == pygame.KEYUP:
                    ser.write(chr(0))

if __name__ == '__main__': 
    main()
