
"""
1.
i = 3
while i != 0:
    print("meow")
    i = i-1

2.
i = 0
while i < 3:
    print("meow")
    i = i + 1
    #i += 1

3.
for _ in range(3):
     print("meow")

4.
print("meow\n" * 3,end="")



while True:
    n = int(input("What's n ?"))
    if n > 0:
        break
    
for _ in range(n):
     print("meow")

while True 是一个无限循环的命令。而是if n > 0是给定的打破这个无限循环的条件
"""


def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What's n ?"))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")
    #range是数值0，1，2
main()   


  

 