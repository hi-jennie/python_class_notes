def hello(to="world"):
    print("hello,", to)
    # to="world"是避免在调用hello函数时不传入参数设定的默认值world


name = input("what't your name?")
hello(name)

# hello(name)里面name占据了to的位置，to其实也就相当相当于一个函数的占位符，等待具体的参数的传入


# def main():
#    name = input("what't your name?")
#    hello(name)
# def hello(to="world"):
#    print("hello,", to)
# main()

# 设立一个main函数就可以从下往下读，但是要注意def完之后要调用
