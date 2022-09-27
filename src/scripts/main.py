from scripts.setup import setup
from scripts.upscale import upscale

def main():
    try:
        print("Input name of image in input folder, include the extension")
        name = input()
        sr = setup()
        if sr[0] == False:
            raise Exception
        upscale(sr[0], name, sr[2], sr[3])
    except Exception as e:
        print("error" + str(e))
        exit()




if __name__ == "__main__":
    main()