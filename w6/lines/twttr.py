def main():
    origin = input("input: ")
    print(shorten(origin))

def shorten(word):
    for c in word[0:]:
        if c.lower() in ['a','e','i','o','u']:
            word = word.replace(c, "")
    return word

if __name__ == "__main__":
    main()
#see
