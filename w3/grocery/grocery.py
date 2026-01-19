def main():
    list = {}
    get_l("",list)

def get_l(prompt,list):
    while True:
        try:
            #get item
            grocery = (input(prompt)).upper().strip()

            #put new in list
            if grocery not in list:
                points = 0

            #put old in list
            points += 1
            list.update({grocery: points})

        except (ValueError, KeyError, ZeroDivisionError):
            pass

            #Ctrl-D (End of File) to stop the program
        except EOFError:
            break

    for grocery,points in sorted(list.items()):
        print(f"{points} {grocery}")

main()
