def main():
    x = int(input("What's x ?"))
    print("x squared is", square(x))


def square(n):
    return n * n


if (
    __name__ == "__main__"
):  # 保障这个main函数在被调用以后其内部的函数时，main这个主函数不会自动执行。
    main()
