import cv2
from cv2 import dnn_superres
import time
import sys
import progressbar
import time

sr = dnn_superres.DnnSuperResImpl_create()
sr.readModel("/home/tubex/Documents/projects/upscaling/models/EDSR_x4.pb")
sr.setModel("edsr", 4)

