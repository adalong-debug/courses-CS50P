def main():
    fraction_user = input("Fraction: ")
    fraction = convert(fraction_user)
    result = gauge(fraction)
    print(result)

def convert(fraction):
    x, y = fraction.split("/")
    if int(x)<0 or int(y) <0:   #if not int , also raise
        raise ValueError
    elif int(x)/int(y) > 1:   #if not int , also raise
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    return int(int(x)/int(y) * 100)

def gauge(percentage):
    while True:
        try:
            if 100 >= percentage >= 99:
                return "F"
            elif 1 < percentage < 99:
                return (f"{percentage}%")
            elif 0 <= percentage <= 1:
                return "E"
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()
