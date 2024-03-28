# try/except需要连在一起用(当无法规范输入的格式时——可以预设到的error的处理方式),pass的运用

"""
1.
try:
    x = int(input("What's x ?"))
    print(f"x is {x}")
except ValueError:
    print("x is not a integer")

2.wrong
try:
    x = int(input("What's x ?"))
except ValueError:
    print("x is not a integer")
 print(f"x is {x}")
错误代码.nameerror
原因在于int(input("What's x ?")). 当输入cat时。不是int.则无法把它传给x。因此x其实是一个无效变量。未定以变量
因此print(f"x is {x}") 没有锁进,所以无论是int还是str都是执行,如果是str,{x}，这一步的{x}也就无法接受正确的参数

3.

try:
    x = int(input("What's x ?"))
except ValueError:
    print("x is not a integer")
else:
 print(f"x is {x}")

4.
while True:
    try:
       x = int(input("What's x ?"))
    except ValueError:
       print("x is not a integer")
    else:
        break

print(f"x is {x}")
#没有valueerror的时候就会break并执行最后的print
#不能else：  print(f"x is {x}")，这样就会一直循环知识打印的对象变了

5.
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
           x = int(input("What's x ?"))
           return x #return其实本身表示break and return
        except ValueError:
            pass    #print("x is not a integer")

main()
"""


def main():
    x = get_int("What's x?")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x  # return其实本身表示break and return
        except ValueError:
            pass  # print("x is not a integer")


main()
