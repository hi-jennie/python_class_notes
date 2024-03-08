# 错误检查


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


"""     
def is_valid(s):
        if len(s) < 2 or len(s) > 6:
            return False
        if not s[0].isalpha():
            return False
     
        foundNumber = "not found"
        for c in s:
            if not c.isdigit() and not c.isalpha():
                return False
            elif c.isdigit() and foundNumber != "found":
                if c == "0":
                    return False
                foundNumber = "found"
            elif c.isalpha() and foundNumber == "found":
                return False
        return True                    
"""


def is_valid(s):
    m = len(s)
    if m < 2 or m > 6 or not s[0].isalpha():
        return False
    for i in range(1, len(s)):
        if not s[i].isdigit() and not s[i].isalpha():
            return False
        elif s[i - 1].isdigit() and s[i].isdigit() and s[i - 2].isalpha():
            if s[i - 1] == "0":
                return False
        elif s[i].isalpha() and s[i - 1].isdigit():
            return False

    return True


main()
