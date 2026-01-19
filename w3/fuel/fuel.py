def main():
    fraction = get_fraction("Fraction: ")
    print(fraction)

def get_fraction(prompt):
     while True:
        try:
            x,y = (input(prompt)).split("/")
            x, y = int(x), int(y)   #check if both int. do not use if int(x) cuz if x=0, view as False
            fraction = int(round(int(x)*100/int(y),0))  #round is for float so output 67.0 not 67
            if 100 >= fraction >= 99:
                return "F"
            elif 1 < fraction < 99:
                return (f"{fraction}%")
            elif 0 <= fraction <= 1:
                return "E"
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass
main()
