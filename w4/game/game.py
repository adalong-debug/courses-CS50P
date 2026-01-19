import random

def main():
# 1. Get a valid Level If the user does not input a positive integer, the program should prompt again.
    while True:
        try:
            level = int(input("Level: "))
            #get i want
            if level > 0:
                break
        except:
            pass

# Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
    result = random.randint(1,level)

#Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    while True:
        try:
            guess = int(input("Guess: "))
            # Skip everything below and ask again
            if guess < 1:
                continue
            if guess < result:
                print("Too small!")
            elif guess > result:
                print("Too large!")
            elif guess == result:
                print("Just right!")
                break
        except:
            pass

if __name__ == "__main__":
    main()

