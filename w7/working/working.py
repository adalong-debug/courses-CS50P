import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    hour = r"(?:1[0-2]|[0-9])"
    min = r"(?:[0-5][0-9])"
    if match := re.search(rf"^({hour}):?({min}?) (A|P)M to ({hour}):?({min}?) (A|P)M$",s):
        # Logic: If min is empty, use "00".
        m1 = match.group(2) if match.group(2) else "00"
        m2 = match.group(5) if match.group(5) else "00"
        # Logic: If PM +12
        h1 = int(match.group(1))
        h2 = int(match.group(4))
        if match.group(3) == "P" and h1 != 12: h1 += 12
        elif match.group(3) == "A" and h1 == 12: h1 = 0
        if match.group(6) == "P" and h2 != 12: h2 += 12
        elif match.group(6) == "A" and h2 == 12: h2 = 0
        # :02d to ensure 09:00 instead of 9:00
        return f"{h1:02}:{m1} to {h2:02}:{m2}"
    raise ValueError

if __name__ == "__main__":
    main()
