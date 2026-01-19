def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    p = get_p("Item: ",menu)

def get_p(prompt,menu):
    price = 0
    while True:
        try:
            item = (input(prompt)).title()

            #check in menu or broke
            if item in menu:
                price += menu.get(item)
                print(f"Total: ${price:.2f}")
        except (ValueError, KeyError, ZeroDivisionError):
            pass

            #Ctrl-D (End of File) to stop the program
        except EOFError:
            print() # Move to a new line for a clean exit
            break
main()
