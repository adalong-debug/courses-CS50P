import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            print(operate(sys.argv[1]))
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def operate(file):
    try:
        with open(file) as f:
            reader = csv.reader(f)
            return (tabulate(reader, headers="firstrow", tablefmt="grid"))   #(the whole list, header not in list)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
