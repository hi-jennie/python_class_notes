#针对输入的第一个单词是否是hello，h开头的词和非h开头的词的三种结果，运用到的函数有split，将输入的字符串以空格为依据拆分成一个列表。


user_input = input("Greeting:").strip()

words = user_input.split()
word = words[0]

if "HELLO" in words[0].upper():
    print("$0")
elif word[0].upper() == "H":
    print("$20")
else:
    print("$100")