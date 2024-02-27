#检验数值是奇数还是偶数

"""1.
x = int(input("what's x"))

#x/2的余数如果是0的话
if x % 2 == 0:
    print("Even")
    
else:
    print("Odd")

"""


def main():
   x = int(input("what's x"))
   if is_even(x):
       print("even")
   else:
       print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    #or
    #return True if n % 2 == 0 else False
    #return n % 2 == 0
    # 因为n%2本身就是自带true or false的bool，所以可以直接返回他的运算结果
    
main()
#bool在python表示true or false两种情况，因为在is_even函数的条件中我们定义的函数运算要求是余数为0
#所以成功执行命令并且return true的时候，如果不能成功执行return false则print odd表明其不是偶数
