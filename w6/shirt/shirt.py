import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) == 3:
        if sys.argv[1][-4:] in [".jpg",".png"]:
            if sys.argv[1][-4:] == sys.argv[2][-4:]:
                operation(sys.argv[1], sys.argv[2])
            elif sys.argv[2][-4:] in [".jpg",".png"]:
                sys.exit("Input and output have different extensions")
            else:
                sys.exit("Invalid output")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def operation(file1,file2):
    try:
        #need to open every img
        shirt = Image.open("shirt.png")
        with Image.open(file1) as old:
            new = ImageOps.fit(old, shirt.size)
            new.paste(shirt, mask = shirt)
            new.save(file2)
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
