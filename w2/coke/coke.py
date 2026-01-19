
def main():
    money_due = 50
    while money_due > 0:
        print(f"Amount Due: {money_due}")
        coin = int(input()) #just once. if not 0 will be reuse!!
        if coin in [25, 10, 5]:
            money_due -= coin
        else:
            coin = 0    #or one coin uses many times!!

    print(f"Change Owed: {-money_due}")

main()
