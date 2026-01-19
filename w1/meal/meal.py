def convert(time):
    x,y = time.split(":")
    x,y = float(x), float(y)    #need!or no return value
    return x+(y/60)

def main():
    time = input("time: ")
    time = convert(time)    #get return value
    if 7<=time<=8:
        print("breakfast time")
    elif 12<=time<=13:
        print("lunch time")
    elif 18<=time<=19:
        print("dinner time")

if __name__ == "__main__":
    main()
