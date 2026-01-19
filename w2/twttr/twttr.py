def main():
    origin = input("input: ")
    for c in origin[0:]:
        if c.lower() in ['a','e','i','o','u']:
            origin = origin.replace(c, "")

    print(origin)

main()
