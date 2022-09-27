import cv2
from cv2 import dnn_superres
import time
import sys
import progressbar
import time
import os

def setup():
    try:
        if os.path.isfile("/home/tubex/Documents/projects/upscaling/models/EDSR_x4.pb") and os.path.isdir('/home/tubex/Documents/projects/upscaling/input/') and os.path.isdir('/home/tubex/Documents/projects/upscaling/output/'):
            sr = dnn_superres.DnnSuperResImpl_create()
            sr.readModel("/home/tubex/Documents/projects/upscaling/models/EDSR_x4.pb")
            sr.setModel("edsr", 4)
            return sr, True
        else:
            raise Exception
    except Exception as e:
        print("Unable to setup the model, error " + str(e))
        return e, False
