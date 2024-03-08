def main():
    time = input("What time is it ?")
    x = convert(time)
    if 7 < x <= 8:
        print("breakfast time")
    elif 12 < x <= 13:
        print("lunch time")
    elif 18 < x <= 19:
        print("dinner time")
    else:
        pass


def convert(m):
    number = m.replace(":", " ").split()
    n = int(number[0]) + int(number[1]) / 60
    return n


if __name__ == "__main__":
    main()
