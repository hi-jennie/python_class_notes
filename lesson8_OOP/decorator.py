times = int(input())

value_list = []
while times > 0:
    m, n = input().strip().split()
    try:
        value_list.append(round(int(m) / int(n)))
    except ZeroDivisionError:
        value_list.append("Error Code: integer division or modulo by zero")
    except ValueError:
        x = (i for i in [m,n] if not i.isdigit())
        value_list.append(f"Error Code: invalid literal for int() with base 10:'{next(x)}'")
    times -=1

for item in value_list:
    print(item)