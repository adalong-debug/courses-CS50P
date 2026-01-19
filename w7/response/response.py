import validators

def main():
    print(valid(input("email: ")))

def valid(s):
    if validators.email(s):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()
