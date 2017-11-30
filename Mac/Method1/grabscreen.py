import cv2
import numpy as np
import mss

def grab_screen(region=None):

    sct = mss.mss()
    
    if region:
            top,left,width,height = region
            
    else:
        width = 500
        height = 500
        left = 0
        top = 0

    img = np.array(sct.grab(region))
    return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

