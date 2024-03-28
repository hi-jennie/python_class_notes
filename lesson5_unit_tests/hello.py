def main():
    name = input("what's your name ?")
    hello(name)
    print(hello(name))
    # 修改2:因为修改了hello函数，不会print，而只是返回一个值即f"hello,{to}",所以output接受这个返回值并将其打印出来


def hello(to="world"):
    return f"hello,{to}"
    # 修改1：print("hello,",to),会是test出现错误因为它知识print而没有返回值，无法将hello（name）== “hello，name”做比较


if __name__ == "__main__":
    main()

# 测试返回值而不是side effects
