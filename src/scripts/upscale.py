from scripts.setup import cv2, time, progressbar
import os

def read_image(name, path_to_input):
    try:
        if os.path.isfile(path_to_input+name):
            return cv2.imread(path_to_input+name), True
        else:
            raise Exception
    except:
        print("Error opening image"+path_to_input+name)
        exit()

def write_image(name, result, path_to_output):
    try:
        cv2.imwrite(path_to_output+name, result)
        if os.path.isfile(path_to_output+name) == False:
            raise Exception
        else:
            return True
    except Exception as e:
        print("Not able to write "+str(e))
        exit()

def upscale(sr, name, path_to_input, path_to_output):
    try:
        animated_marker()
        img = read_image(name, path_to_input)[0]
        result = sr.upsample(img)
        write_image(name, result, path_to_output)
        print("\n Done")
        return True
    except Exception as e:
        print("Unable to upscale image"+str(e))
        return False

def animated_marker():
    widgets = ['Upscaling: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)