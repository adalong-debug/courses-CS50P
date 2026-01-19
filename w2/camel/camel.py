
def main():
    camel = input("camel: ")
    snake = []  #build a list to help
    for c in camel[0:]:
        if c.isupper():
            snake.append('_')
            snake.append(c.lower())
        else:
            snake.append(c)
    snake = "".join(snake)
    print(snake)

main()
