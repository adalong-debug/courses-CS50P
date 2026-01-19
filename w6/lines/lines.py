import sys

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            print(count_lines(sys.argv[1]))
        else:
            sys.exit("Not a Python file")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def count_lines(file):
    try:
        count = 0   #Put before loop
        with open(file) as f:
            #lines = f.readlines()
            for line in f:
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
