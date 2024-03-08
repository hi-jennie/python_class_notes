"""新知识——
x, y = map(int, fraction.split('/'))，
map 是 Python 中的一个内置函数，用于对一个序列（例如列表、元组等）中的每个元素应用一个指定的函数。它会返回一个新的序列，其中包含了每次函数调用的结果。具体来说：

第一个参数 function 是一个函数，它会被应用到序列中的每个元素上。
第二个参数 iterable 是一个或多个序列，可以是列表、元组等。

 ZeroDivisionError
"""


def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split("/"))

            if y == 0 or x > y:
                main()
                continue

            percentage = (x / y) * 100
            rounded_percentage = round(percentage)

            if rounded_percentage <= 1:
                print("E")
                break
            elif rounded_percentage >= 99:
                print("F")
                break
            else:
                print(f"{rounded_percentage}%")
                break

        except ValueError:
            main()
        except ZeroDivisionError:
            main()


if __name__ == "__main__":
    main()
