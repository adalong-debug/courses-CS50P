def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s[0:2].isalpha():
        return False
    if not (2 <= len(s) <= 6):
        return False
    if not s.isalnum():
        return False

    #have checked letter starts, now check num part
    i = 0
    while i < len(s):
        if s[i].isdigit():
            # If it's a number, it can't be '0' if it's the first one
            if s[i] == '0':
                return False
            # Once a number starts, the rest MUST be numbers
            if not s[i:].isdigit():
                return False
            break
        i += 1
    return True

if __name__ == "__main__":
    main()
