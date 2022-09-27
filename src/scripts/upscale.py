from scripts.setup import cv2, time, progressbar


def read_image(name):
    try:
        return cv2.imread('/home/tubex/Documents/projects/upscaling/input/'+name)
    except:
        print("Error opening image")

def write_image(name, result):
    cv2.imwrite('/home/tubex/Documents/projects/upscaling/output/'+name, result)

def upscale(sr,name):
    try:
        animated_marker()
        img = read_image(name)
        result = sr.upsample(img)
        write_image(name, result)
        print("\n Done")
    except:
        print("Unable to upscale image")

def animated_marker():
    widgets = ['Upscaling: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)