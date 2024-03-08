# command-line arguments  sys.argv, sys.exit,slices[1:],[1:-1]表示从第二位开始到倒数第二位

import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments")

for arg in sys.argv[
    1:
]:  # [1:]slices就是取一个集合里面的自己8，[1:]表示取sys.argv里从第二位开始的所有arguments，不包括[0]
    print("hello,my name is", arg)


"""
1.
if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")

print("hello,my name is", sys.argv[1])
#!sys.exit表示在执行了too few/many arguments之后就会退出不在执行最后一行的print，从逻辑上看print是与if语句是并列关系


2.
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello,my name is", sys.argv[1])




3.
try:
    print("hello,my name is", sys.argv[1]) 
except IndexError:
    print("IndexEror,please type in your name")

#sys.argv[]是一个列表(list),用于在运行 Python 文件时从外部(terminal)传递参数给程序
#sys.argv[0] 通常是被调用的脚本文件名(即name.py)

ps:
通过 sys.argv 输入参数进行计算，例如计算 a + b,我们需要将 a 和 b 转换为整数.感觉有点儿像input
def test(argv):
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a + b
    d = int(a) + int(b)
    print('c =', c)
    print('d =', d)

if __name__ == "__main__":
    test(sys.argv)

运行以下命令：
python3 a.py 3 4
输出结果将是：
c = 34
d = 7
"""
