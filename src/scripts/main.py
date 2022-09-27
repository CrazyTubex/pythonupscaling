from scripts.setup import sr
from scripts.upscale import upscale

def main():
    print("Input name of image in input folder, include the extension")
    name = input()
    upscale(sr, name)




if __name__ == "__main__":
    main()