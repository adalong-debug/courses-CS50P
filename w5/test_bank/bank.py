def value(greeting):
    if greeting.strip().lower()[:5] == "hello":
        return 0
    elif greeting.strip().lower()[0] == "h":
        return 20
    else:
        return 100

def main():
    user = input("Greetings? ")
    print(f"${value(user)}")

if __name__ == "__main__":
    main()
