from scripts.setup import cv2, time, progressbar
import os

def read_image(name):
    try:
        if os.path.isfile('/home/tubex/Documents/projects/upscaling/input/'+name):
            return cv2.imread('/home/tubex/Documents/projects/upscaling/input/'+name), True
        else:
            raise Exception
    except:
        print("Error opening image")
        exit()

def write_image(name, result):
    cv2.imwrite('/home/tubex/Documents/projects/upscaling/output/'+name, result)

def upscale(sr,name):
    try:
        animated_marker()
        img = read_image(name)[0]
        result = sr.upsample(img)
        write_image(name, result)
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