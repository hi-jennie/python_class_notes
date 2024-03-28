# 提示用户输入名字

name = input("What's your name?")

match name:
    case "Jennie" | "ldp" | "aobai" | "Turkey":
        print("SiChuan")

    case "wangqi":
        print("DeYang")

    case _:
        print("Who!")

# match case 比重复的if语句更简洁
