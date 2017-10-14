import time

import cv2
import mss
import numpy as np



sct = mss.mss()

def process_img(image):
    #original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 50, threshold2=50)
    return processed_img

def screen_record():
    # Part of the screen to capture
    monitor = {'top': 50, 'left': 0, 'width': 500, 'height': 500}

    while 'Screen capturing':
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        new_img = process_img(img)
        # Display the picture
        cv2.imshow('OpenCV/Numpy normal', img)


        print('fps: {0}'.format(1 / (time.time()-last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        
screen_record()
