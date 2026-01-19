import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if match := re.search(r"<iframe *src=\"https?://(www\.)?youtube\.com/embed/(?P<keyurl>\w+)\"",s):
        return "https://youtu.be/" + match.group("keyurl")
    return None

if __name__ == "__main__":
    main()
