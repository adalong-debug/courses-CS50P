import sys
import csv

def main():
    if len(sys.argv) == 3:
        #can't argv[1:2].   only str .endswith
        if sys.argv[1].endswith(".csv"):
            operation(sys.argv[1], sys.argv[2])
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def operation(file1,file2):
    try:
        with open(file1) as old, open(file2, "w") as new:
            reader = csv.DictReader(old)
            writer = csv.DictWriter(new, fieldnames = ["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                writer.writerow({"first":first, "last":last, "house":house})

    except FileNotFoundError:
        sys.exit(f"Could not read {file1}")

if __name__ == "__main__":
    main()
