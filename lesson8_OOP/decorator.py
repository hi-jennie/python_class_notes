from collections import Counter

shoes_number = int(input())
shoes_size = input().split()
purchase_number = int(input().strip())
inventory = dict(Counter(shoes_size))

total_money = []

def uesful_number(purchase_number):
    while purchase_number > 0:
        size, money = input().split()
        if size in inventory and int(inventory[size]) > 0:
            total_money.append(int(money))
            inventory[size] = int(inventory[size]) - 1
        else:
            pass
        purchase_number -=1 
    
uesful_number(purchase_number)

print(sum(total_money))