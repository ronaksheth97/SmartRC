# Adapted from https://github.com/Sentdex/pygta5
# Changed the method of tracking keypresses (for OSX instead of Windows)
# Changed the method of capturing screen (for OSX instead of Windows)


import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
nk = [0,0,0,0,0,0,0,0,1]

starting_value = 1

while True:
    file_name = 'training_data-{}.npy'.format(starting_value)

    if os.path.isfile(file_name):
        print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)
        
        break


def key_to_output(key):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    output = [0,0,0,0,0,0,0,0,0]

    if key == 'w':
        output = w
    elif key == 's':
        output = s
    elif key == 'a':
        output = a
    elif key == 'd':
        output = d
    else:
        output = nk
    return output


def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    print('STARTING!!!')
    while(True):
        
        if not paused:
            screen = grab_screen(region=(0,40,1920,1120))
            last_time = time.time()
            # resize to something a bit more acceptable for a CNN
            screen = cv2.resize(screen, (480,270))
            # run a color convert:
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            
            key = key_check()
            output = key_to_output(key)
            training_data.append([screen,output])

            #print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
##            cv2.imshow('window',cv2.resize(screen,(640,360)))
##            if cv2.waitKey(25) & 0xFF == ord('q'):
##                cv2.destroyAllWindows()
##                break

            if len(training_data) % 100 == 0:
                print(len(training_data))
                
                if len(training_data) == 500:
                    np.save(file_name,training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
                    file_name = 'X:/pygta5/phase7-larger-color/training_data-{}.npy'.format(starting_value)

                    
        key = key_check()
        if key == 't':
            if(paused):
                print('Still Paused')
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)
        elif key == 'y':
            if(paused == False):
                print('Already Unpaused')
            else:
                print('Unpausing!')
                paused = False
                time.sleep(1)

main(file_name, starting_value)
