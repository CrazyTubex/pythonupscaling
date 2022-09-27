import cv2
from cv2 import dnn_superres
import time
import sys
import progressbar
import time
import os
from pathlib import Path


def setup():
    directory = os.getcwd()
    dir_root = Path(directory).parent

    path_to_model = str(dir_root) + "/models/EDSR_x4.pb"
    path_to_input = str(dir_root)+'/input/'
    path_to_output = str(dir_root)+'/output/'

    try:
        if os.path.isfile(path_to_model) and os.path.isdir(path_to_input) and os.path.isdir(path_to_output):
            sr = dnn_superres.DnnSuperResImpl_create()
            sr.readModel(path_to_model)
            sr.setModel("edsr", 4)
            return sr, True, path_to_input, path_to_output
        else:
            raise Exception
    except Exception as e:
        print("Unable to setup the model, error " + str(e))
        return e, False
