import re
name = input("What's your name?").strip()

#注意，在正式表达中（）表示一个group，但是在这里表达另一层含义————捕获输入的name里符合(.+), (.+)里两个（）内的具体内容并将其返回给matches
matches = re.search(r"^(.+), ?(.+)", name) 
#matches = re.search(r"^(.+), *(.+)", name) 即使在括号后面输入很多white space的情况下也是可以运行的
if matches:
    name = matches.group(2) + " " + matches.group(1) #group(1）表示re.search(r"^(.+), (.+)", name)里面capture到一个（）里面的内容
print(f"hello, {name}") 

'''
if matches := re.search(r"^(.+), ?(.+)", name):
这是 Python 3.8+ 中的 walrus operator（海象运算符）。
它将 re.search() 的结果赋值给 matches 变量，并在同一行中进行条件判断。
如果找到匹配项，matches 将被赋值为匹配对象，否则为 None。
     name = matches.group(2) + " " + matches.group(1) 
print(f"hello, {name}") 
'''
