def cal(x,op,y):
    x = float(x.strip().lower())
    y = float(y.strip().lower())
    if op == "+":
        print(x+y)
    elif op == "-":
        print(x-y)
    elif op == "*":
        print(x*y)
    elif op == "/":
        print(x/y)
    else:
        print("Err")


def main():
    exp = input("expression: ").strip().lower()
    x,op, y = exp.split(" ")
    cal(x,op,y)

main()
