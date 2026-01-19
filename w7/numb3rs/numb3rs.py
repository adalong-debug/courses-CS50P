import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    part = r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
    pattern = rf"^(?:{part}\.){{3}}{part}$"
    if re.search(pattern, ip):
        return True
    return False

if __name__ == "__main__":
    main()
