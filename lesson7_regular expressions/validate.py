import re

'''1.检查email是否符合标准
email = input("What's your email?").strip()
username, domain = email.split("@")
if username and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")
'''


email = input("What's your email?").strip()


#.+@.+ 是正式表达式，.表示任意一个char，+表示至少一个或者更多。整个表达式表示在@前后至少要有一个以上char
#.+@.+ 和 ..*@..*效果一样————第一个.表示任意一个char，之后的.*表示任意的0或者多个char 

#如果要end with .edu , .+@.+.edu的方式不太合理,因为python无法将.区分究竟是表示任意char的.还是字面意思的.
#所以给 r“.+@.+\.edu” 加上反斜杠，同时加上r表示————.edu是按照原样传入的原始字符串。r在这里的作用类似于f

# r"^.+@.+\.edu$"  ————^表示以什么开头，$表示以什么结尾， 两个结合在一起用表示开头结尾都以这个格式，也即在此表达式之前和之后都不能插入其他东西

# r"[^@]+@[^@]+\.edu$" ————[]表示任意的字符，[^]表示出了某个东西的任意字符，[^@]就表示出了@的任意字符

# r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$"  [a-zA-Z0-9_]表示接受a-z的大小写字符和0-9的数字和_  
#也可以改成r"^\w+@\w+\.edu$"    \w表示任意单词字符a-z

# r"^\w+@\w+\.(edu|com|gov|net)$"   表示可以以edu，或com或gov结尾，用｜表示or可以了

# r"^(\w|\s)+@\w+\.(edu|com|gov|net)$"  ()表示group，里面\w|\s表示任意字符或者空白，也可以表示为这样  r"^[a-zA-Z0-9_ ]+@\w+\.(edu|com|gov|net)$"

#re.IGNORECASE 表示忽视大小写，所以当输入JENNIE@SICHUAN.EDU也是有效的

# r"^\w+@\w+\.\w\.edu$"  这个时候jennie@sichuan.some.edu也是可以的，但是当jennie@sichuan.edu又不行了，因为在正式表达式中域名中强制包括一个.和.edu
# r"^\w+@(\w+\.)?\w\.edu$"  可以解决的表示（）里面的内容可以出现一次或不出现 jennie@sichuan.edu和jennie@sichuan.some.edu都可以了
if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE): 
    print("valid")
else:
    print("invalid")





