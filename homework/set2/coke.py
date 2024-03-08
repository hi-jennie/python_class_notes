print("Amount Due : 50")
a = 50
while True:
    i = int(input("Insert Coin: "))
    if i in [50, 25, 10, 5]:
        a = a - i
        if a > 0:
            print(f"Amount Due: {a}")
        elif a == 0:
            print("Change Owed: 0")
            break
        elif a < 0:
            print(f"Change Owed: {-a}")
            break
    elif i not in [50, 25, 10, 5]:
        print(f"Amount Due: {a}")
