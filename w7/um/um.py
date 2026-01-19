import re

def main():
    print(count(input("Text: ")))

def count(s):
    count =len(re.findall(r"(^|\W)um(\W|$)",s, re.IGNORECASE))
    return count

if __name__ == "__main__":
    main()
