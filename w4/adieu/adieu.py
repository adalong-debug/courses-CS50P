def main():
    # prompts the user for names, one per line, until control-d.
    list = []
    while True:
        try:
            names = input("Name: ")
            list.append(names)
        except EOFError:
            print()
            break

    # bid adieu to those names, 𝑛 names with 𝑛 −1 commas and one and
    if len(list) == 1:
        result = "Adieu, adieu, to "+ list[0]
    elif len(list) == 2:
        result = "Adieu, adieu, to "+ list[0] + " and " + list[-1]
    elif len(list) > 2:
        result = "Adieu, adieu, to "+", ".join(list[:-1]) + ", and " + list[-1]
    print(result)
main()
