import sys
import random
from pyfiglet import Figlet

def main():
    #calls the __init__ method to set up the object
    figlet = Figlet()
    list = figlet.getFonts()

    #Zero if the user output text in a random font.
    if len(sys.argv) == 1:
        font = random.choice(list)

    #Two if a specific font, first -f or --font, second name of the font.
    elif len(sys.argv) == 3 and (sys.argv[1] in ["-f","--font"]):
        font= sys.argv[2]
        if font not in list:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

    #Get text and render
    text = input("Input: ")
    figlet.setFont(font=font)
    print(figlet.renderText(text))
main()
