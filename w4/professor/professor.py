import random

def main():
    eqn = 10
    score = 0
    chances = 3
    lvl = get_level()
    while eqn != 0:
        if chances == 3: # User have 3 chances to answer each equation
            # Only generate_integer for new equation if chances == 3
            x = generate_integer(lvl)  #get return value!!!!
            y = generate_integer(lvl)
        try:
            user_answer = int(input(f"{x} + {y} = "))   #not str!!!!
            answer = x + y
            if user_answer == answer:  #or str!= int
                eqn = eqn - 1
                score = score + 1
                chances = 3 # Reset chances to generate new equation in case user input the right answer on 2nd/3rd try
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances -= 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {answer}"))
            chances = 3 # Reset chances to generate new equation
            eqn = eqn - 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level  = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    else:
        lower = 10**(level - 1)
        upper = (10**level) - 1
        return random.randint(lower, upper)

if __name__ == "__main__":
    main()
