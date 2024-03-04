#作用：eval() 函数的作用是将一个字符串解析为有效的表达式，并计算其值。它可以执行字符串中包含的 Python 代码并返回计算结果1。
#用法：eval() 函数接受一个字符串作为参数，将其视为有效的 Python 表达式，然后计算并返回结果。例如，如果你有一个字符串 "3 + 5"，eval("3 + 5") 将返回 8


number = input("Expression:").split()

x = int(number[0])
y = number[1]
z = int(number[2])

if y == "+":
    print(f"{ x + z:.1f}")
elif y == "-":
    print(f"{ x - z:.1f}")
elif y == "*":
    print(f"{ x * z:.1f}")
elif y == "/":
    print(f"{ x / z:.1f}")
else:
    pass

"""更简单的方式
expression = input("Expression:")
try:
    result = eval(expression)
    print(f"{result:.1f}")
except:
    print("Invalid expression")
    """

