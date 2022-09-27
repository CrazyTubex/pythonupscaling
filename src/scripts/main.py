from scripts.setup import setup
from scripts.upscale import upscale

def main():
    try:
        print("Input name of image in input folder, include the extension")
        name = input()
        sr = setup()
        #print(sr)
        if sr == False:
            raise Exception
        upscale(sr, name)
        #print(sr)
    except Exception as e:
        print("error" + str(e))
        exit()




if __name__ == "__main__":
    main()