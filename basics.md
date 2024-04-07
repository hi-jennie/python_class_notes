# 2024.3.31

# 小数据池（-5——256）用的是同一块空间
字符串：自己定义的内容一致————就是一块空间
a == b 和 a is b的区别
驻留机制：节省内存开销提高效率————终端中走小数据池，pycharm中走的代码块

# 深浅拷贝
**赋值：多个变量名指向同一个内存地址，如果这个内存地址的值发生变化，那么三个变量也会更着变动**
a = 10
b = 10
c = 10
a、b、c同时指向10

a1 = 10
b1 = a1
c1 = b1
也是a1 b1 c1 同时指向10

**浅拷贝copy()：只拷贝第一层元素的内存地址————再声明一块地址，一个变量，所以互不干扰**

1. 添加——
```python
list = [1,2,3[]]
list1 = list.copy() #浅拷贝
list.append(5)
print(list) #[1,2,3,[],5]
print(list1) #[1,2,3,[]]
```
list1新开了一块memory ，所以二者内存地址不一样，所以对list本身增加操作是不会影响list1,因为1、2、3是最终存储区域，再往下走不再有可存储地址

2. 在可变数据类型中添加————不修改其内存地址
```python
list[-1].append(5)
print(list) #[1,2,3,[5]]
print(list1) #[1,2,3,[5]]
# 这一步虽然是浅拷贝，但是拷贝的是[]的地址，list和list1中的[]指向的是同一块地址，所以在list中对[]进行修改会影响list1中[]的值

# 举例：
list = [1,2,3，[1，[],3]]
list1 = list.copy()

list[-1][-2].append(2)
print(list) # list = [1,2,3，[1，[2],3]]
print(list) # list = [1,2,3，[1，[2],3]]
# 对list的修改还是修改到list1了，是因为[]是可变的，纯粹取决于修改对象——数据类型本身是否可变，[]{}都是可变的
```

3. 修改——从根源上将地址换了
```python
list = [1,2,3，[1，[],3]]
list1 = list[:] # **这也是浅拷贝，和copy效果一样**
list = 20
print(list) # list = [1,2,3,20]
print(list) # list = [1,2,3，[1，[],3]]
```
**深拷贝deepcopy()：不管嵌套多少层，不可变数据类型公用，可变数据类型开辟新的空间——相当于从最底层拿数据给新变量，然后开辟新的空间，而不是拿的地址**

```python
import copy
list = [1,2,3,[2,3]]
list1 = copy.deepcopy(list)

list[3].append(4)
print(list) # [1,2,3,[2,3,4]]
print(list) # [1,2,3,[2,3]]
```
4. append的是data的地址
```python
data_list = []
data = {}
for i in range(10):
    data["user"] = i
    data_list.append(data)
print(data_list)
```
**这里的每一次循环加入list的都是data本身即data的地址，所以结果为10个["user":9]**

5. 每一循环都创建了一个新的data地址然后加入list里面
```python
data_list = []
for i in range(10):
    data = {}
    ata["user"] = i
    data_list.append(data)
print(data_list)
```
**和上面的4不太一样，字典里面是user:1-10**

6. 
```python
a = [1,2,3,4,5,6,7]
b = {}
for i in a :
    if i < 4:
        continue
    if "k1" not in b:     
        b["k1"] = i
    else:
        b["k1"] = i
print(b) # {"k1":7}
```   

# 2024.4.1（二次编码——cipher/decipher）

# 二次编码
ascii:不支持中文，英文一个字节
gbk：英文一个字节，中文两个
unicode：中英文都是四个——媒介桥梁
utf-8:英文一个，欧洲2个，亚洲三个

**将英文转换为byte类型的两种方法**：
s = "hello,world" #字符串类型
s1 = b"hello,world" # 方法1——直接加b"" ：中文不能直接加b
print(s.encode("utf-8")) #结果：b"hello,world" ——方法2：用encode

**bype也支持字符串的一般方法**
```python
s2 = s1.upper() 
print(s2) # 结果： b"HELLO,WORLD"
s3 = s1.replace(b"h",b"m")
print(s3) #结果：b"mello,world" 
print（s1 + s2）# 结果：b"hello,worldHELLO,WORLD"
print（s1 * 2） # 结果：b"hello,worldhello,world"
```

**文件存储和网络传输使用的都是字节**

1. 用什么编用什么解——不会出现错误
```python
s = "你好"
s1 = s.encode("utf-8") #以什么样的方式上锁cipher——编码
print(type(s1))
print(s1)
s2 = s1.decode("utf-8")  # 解码
print(s2) 
```

2. 
```python
s = "你好"
s1 = s.encode("gbk") 
print(type(s1))
print(s1) # b"\xc4\xc3"
s2 = s1.decode("utf-8")  # 出现错误
print(s2) 
```

3. 
```python
s = b"\xc4\xc3"
s1 = s.decode("gbk")
print(s1) # 你
```

4. 
```python
s = "你好，小王”
s1 = s.encode("utf-8") #编码为12个 \xc4 这样子的东西
print(s1)
s2 = s1.decode("gbk") # 将s1解码为gbk模式，不在是“你好，小王”，而是gbk模式下其他6个中文字
s2 = s1.decode("gbk") # 这样的方式也无法decipher，会出现错误
```

**作用**
文件操作：指定以什么编码进行存储
网络编程：发送消息只能发送字节类型

# 文件操作（文件操作的作用——持久化存储）
* **read**——全部读完之后就读不到了——光标已经到末尾了
1. 读文本：
f = open(file="cat.txt", mode="r",encoding="utf-8")
f = open("cat.txt", "r",encoding="utf-8")
c = f.read() # **全部读取存入c**

2. 读字节——rb读字节，wb清空写字节，ab追加写字节
    f = open("cat_picture.jpg", "rb") # 没有encoding

    d = f.read(6) #读取6个str，每次读取都是从光标开始的位置开始读

    m = f.readline() # **读取一行：常用**
    m = f.readline() # 读取第2行

3. 路径：文件位置
相对路径：相对某个内容查找 （之前在学js是里面的template即使相对路径查找）../就是返回上一级文件../../ 返回上上级
绝对路径：从某个磁盘进行查找
路径转义
f = open("jennie:\PYTHON_CLASS_NOTES\basics.md", "r") 
f = open("jennie:\\PYTHON_CLASS_NOTES\\basics.md", "r") # 多加的\是转意，跟regular expression中是一样的
f = open(r"jennie:\PYTHON_CLASS_NOTES\basics.md", "r")  # 或者加一个r转意


* **write**
    w：清空写：先清空，再写内容
    a：追加写 **使用频率更高**
    w和a模式都会创建文件(文件存在时不创建，不存在时创建有点像code)
```python
f = open("Jennie.txt","w",encoding="utf-8") # 每一次这一步都会把文件清空
f = f.write(“[1,2,3,4]\n")
f = f.write(“[1,2,3,4]\n")  # 写的必须都是字符串
f.close()

f = open("Jennie.txt","a",encoding="utf-8")
f.write("my name is Jennie\n")
f.write("I'm 24 years old\n") # 这个是在之前的基础上append，因为现在时a模式
```

* a+, w+, r+
a+:写+读
w+:写+读
r+:读+写

1. r+ 先读后写
```python
f = open("Jennie.txt","r+",encoding="utf-8")
print(f.read())
f.write("My boyfriend is Rustin")
2. r+ 先写后读
```python
f = open("Jennie.txt","r+",encoding="utf-8")
f.write("My boyfriend is Rustin") # 这个就会写在最前面，因为这个时候还没读，光标在最前面
print(f.read())
```

3. a+ 自动创建文件，读和写的功能——应用场景：
```python
user = input("name:")
pwd = input("psaaword:")

f = open("Jennie.txt","a+",encoding="utf-8")
f.seek(0) # 将光标移到最前面
for i in f:
    print(i)
    file_user, file_pwd = i.split(":")
    if user == file_user:
        print("username exist")
        break
else:
    f.write(f"{user}:{pwd}\n")
    print("register successfully")
```

**先筛选有无user，没有就新写入，写入成功就print提示，否则有可能没有成功注册，但是又显示了成功注册就会有问题**

4. 如果不是a+，就要操作两遍open
```python
f = open("Jennie.txt","r",encoding="utf-8")
f.seek(0) # 将光标移到最前面
for i in f:
    print(i)
    file_user, file_pwd = i.split(":")
    if user == file_user:
        print("username exist")
        f.close()
        break
else:
    f = open("Jennie.txt","a",encoding="utf-8")
    f.write(f"{user}:{pwd}\n")
    print("register successfully")
```

5. 光标操作
**移动光标**：
两个参数——
seek(0，0)——移动到头部
seek(0，1)——移动到当前
seek(0，2)——移动到末尾

一个参数——
**seek(0):也是移动到当前**
seek(3):按照字节移动，取决于编码方式，比如中文在三种编码方式中的不同字节数，英文就是一个

**查看光标**：
    f = open("Jennie.txt","r",encoding="utf-8")
    print(f.read(3)) # 读三个字符
    print(f.tell()) # 返回刚刚读取的三个字符的字节数


# 上下文管理器（with——自动开关）
1. 作用1：自动关闭文件
```python
with open("Jennie.txt","r",encoding="utf-8") as fp:
    c = fp.read(3)
    print(c)
```

2. 作用2：同时操作多个文件(\表示前后是🙆层级)
```python
with open("Jennie.txt","r",encoding="utf-8") as fp,\
    open("Rustin.txt","r",encoding="utf-8") as fp2:
    c = fp.read(3)
    c1 = fp2.read(3)
    print(c)
```

3. 文件的修改

第一步：打开源文件
第二步：找到修改的内容，进行替换
第三步：写入新文件中
第四步：给原文件备份（防止数据丢失），将新文件修改为源文件的名字

```python
import os
with open("Jennie.txt","r",encoding="utf-8") as fp,\
    open("Jennie1.txt","r",encoding="utf-8") as fp2:
    for i in fp:
        i = i.replace("Jennie", "Rustin")
        fp2.write(i)
        # 将修改后的内容和剩余的原内容写入fp2

# 重命名
# 先把源文件改成其他名字
os.rename(“Jennie","Jennie2")  
# 再把修改后的Jennie1改文Jennie
os.rename(“Jennie1","Jennie")  
```


# 2024.4.2（函数）
# 1. 函数
    函数的作用：减少重复代码，提高复用性
    函数执行完，函数打开的内存memory就自动清楚了
    **return :终止函数——不是循环/返回值（保留数据）——没有返回值的时候返回none/返回多个值的时候以tuple返回**
    要注意有些没有return的内置函数


```python
# 错误写法——是拿一行文件对比输入
def log_in():
    with open("Jennie.txt","r",encoding="utf-9") as fp:              
            for line in fp:
                name1, pwd1 = line.strip.split(":")
                for _ in range(3):
                    name = input("Name:")
                    pwd = input("password: ")
                    if name == name1 and pwd == pwd1:
                        return f"log in successfully"

# 正确写法——用输入去一行一行对比文件    
def log_in():
    with open("Jennie.txt","r",encoding="utf-9") as fp:              
        for _ in range(3):
            f.seek(0)  # 文件读过一次光标就在最后，就读不到了，将光标移到最前面
            name = input("Name:")
            pwd = input("password: ")
            for line in fp:
                name1, pwd1 = line.strip.split(":")
                if name == name1 and pwd == pwd1:
                    return f"log in successfully"
```

# 2. 三元运算

print(1 if 3 > 2 else 2) # 结果 1
如果条件3>2成立，那就是1，否则就是2

```python
# 比较返回大值
def func(a, *，b=10)
    return a if a > b else b

func(10,9)

```

# 3. 参数：位置参数——必须一一对应——都遵循参数优先级——先位置后关键字
**形参**：在函数定义（位置、默认）
位置参数：def func(a, b)
默认参数：def func(a=1, b=2)
混合参数：def func(a, b=2)

**实参**：在函数调用（位置、关键字）
位置参数：def func(10, 20)
关键字参数：def func(a=1, b=2)
混合参数：def func(a, b=2)

open("Jennie.txt","r",encoding="utf-8")
open(file="Jennie.txt",mode="r",encoding="utf-8")
```python

def func(file_name:str, old:str, new:str):
    import os 
    # 这里的file_name没有打引号的原因是file_name是一个变量
    with open(file_name,"r",encoding="utf-8") as fp,\ 
        open(file_name+"1","a",encoding="utf-8") as fp1:
        for i in fp:
            i = i.replace(old, new)
            fp1.write(i)
        
        os.rename(file_name, file_name+"bank")
        os.rename(file_name+"1",file_name)

func("jennie.txt","wang", "xue")
```
        
**动态参数**

*args 接受多余的位置参数（以tuple的方式），在unpack时可以用“*varible”的方式接受多余的value

```python
def func(*args):
    print(args)
# *是聚合打包为tuple，可以接受任意数量的位置参数
func(a,b,c,d,e,f,g,h,i)
# 像这种情况下*就很省事



def func1(*args,a,b)
    print(args,a,b)
func1(a,b,c,d,e,f,g,h,i)
# 这种情况会导致所有参数a,b,c,d,e,f,g,h,i，被*args打包，导致形参a，b无法分到参数


def func1(a,b,*args)
    print(a,b,args)
func1(a,b,c,d,e,f,g,h,i)
# 这种情况形式参数a，接受a，形参b接收b，*args接收c,d,e,f,g,h,i

```

**kwargs 接受多余的key word arguments（以dict的方式）

```python
def def func1(a,b,**kwargs)
    print(a,b,kwargs)

func1(a=1,b=2,c=3,d=4,e=5)
# **kwargs 接受c=3,d=4,e=5
```

**万能传参**——convention，可以改但是不建议改
```python
def func(*args, **kwargs) # 将传入过来的实参打包成tuple，仅针对*args，position args
    print(args, kwargs) # 再打散传入函数体部分，仅针对*args，position args

func(1,2,3,4,5,a=1,b=2,c=3,d=4) # 实参部分时打散的参数

# *args:(1,2,3,4,5)
# **kwargs {"a":1,"b":2,"c":3,"d":4}


list = [1,2,3,4,5]
dict = {"key":1, "key2":2}
def func1(*args, **kwargs) 
    print(args, kwargs)

func1(*list,**dict)
```
**动态参数优先级**
func(a,b,*args,c=1,**kwargs)——优先级
实际写代码过程中使用最多的还是位置参数，动态参数很少用基本不用

```python
def func(a,b,c=1,*args)
    print(a,b,c,args)

func(12,13,14)
# *args 拿不到参数，14覆盖了c=1的默认值
# 12，13，1，（）

def func1(a,b,*args，c=1)
    print(a,b,args，c)

func(12,13,14)
# 12，13，1，（14）

def func(a,b,*args,c=1,**kwargs)
    print(a,b,args,c,kwargs)

func(12,13,14,d=15,e=20)
```

# 名称空间
局部可以使用全局或内置但是不能修改

* 内置空间——print()/len()等python自带的内容和功能
* 全局空间——自己写的python文件
* 局部空间——自定义的函数体空间

加载顺序：内置>全局>内置
取值顺序：和加载顺序相反


```python
a = 10          # 1
def func():     # 2
    print(a)

func()          # 3 到三这一步就会进入到func的局部空间
                # 从里面取print和a

# 10

a = 10
def func1():
    a = 5
    print(a)
# 英文def func() 从内向外取，所以先会取到a = 5
func()

# 5
```
**作用域**
**global/nonlocal的关系**
* 全局作用域：内置空间+全局空间
* 局部作用域：局部空间

```python
a = 10   # 全局变量       

def func():
    a = a+1   # 在局部空间里修改全局变量，无法修改，如果可以修改，那么之后def的每一个函数都可以修改就很危险。
    print(a)

  
def func1():
    global a # 声明a是全局变量后可以修改，有了global才能突破局部空间修改全局变量
    a = a+1   
    print(a)


```

# 函数嵌套

**函数的第一类对象及使用**
* 函数名可以当做值被赋值
* 函数名可以当做另外一个函数的返回值
* 函数名可以当做另一个函数的参数
* 函数名当做值存入容器中
谁调用就把值返回给谁
```python
def func():
    print(1)
a = func()  # 即使在函数没有返回值的的情况下，也可以给函数声明变量
a() # 调用a()和调用func()的效果一样


def foo():
    def func():
        print(1)
    return func
a = foo() # a 接收了foo函数返回的函数func()
a()       #调用func()



# 函数名可以当做另一个函数的参数 map函数就是这样 map(func,iterable)
def foo(a):
    a()
foo(func) # func作为参数传入foo



list = [func,func,func]
for i in list:
    i() # 调用i

```

**函数**、
**交叉：一层def**
* 示例1
```python
def foo():
    print(1)

def func():
    foo()

func()
```
* 示例2

```python
def foo(a):
    print(a)

def func(b):
    foo(b)

func(2)
```
* 示例3
```python
def foo(a):
    print(a)
    return 1

def fi(b):
    ret = foo(b) # 接收 1
    return 2

def func(c):
    f1(c) # 接收 2
    # func没有返回值，默认返回3

ret1 = func(3)
print(ret1)
# 结果： 3, None
```
* 示例4
```python
def foo(a):
    print("is foo")
    return a()

def fi():
    print("is fi")
    return “execute fi"

def func(c,b):
    return c(b)

ret1 = func(foo,fi) # 最终接收到“execute fi"
print(ret1)
# 结果： 
# is foo
# is fi
# execute fi
```
**嵌套：多层def** 
* 示例5
```python
def func():
    print(5)
    def foo():
        print(1)
# 调用func(),不会触发foo()
func()
# 结果：5


def func():
    print(5)
    def foo():
        print(1)
    foo()
# 调用func(),不会触发foo()
func()
# 结果：5和1
```
* 示例6
```python
a = 10
def func(a1):
    def foo(c):
        b = c+1
        def f1(b):
            print(b)
        fi(c)
    foo(a1)
func(a)
# 输出10
```

* 示例6
```python
a = 10
def func(a1):
    a = 10
    def foo(c):
        a = 5
        def f1():
            print(a)
            return "123"
        ret = fi()
        return ret
    foo()
ret = func() 
# 因为func没有返回值
print(ret)
# 输出10、5、None
```

# global/nonlocal
**global：当全局中没有变量时，可以创建，有的时候可以修改**
```python
#修改
a = 10
def func1():
    a = 5
    def foo():
        global a # a 是全局量10
        a = a+1   
        print(a) # 11
    foo()
    print(a) # 5
func1()

#创建
def func():
    global b
    b = 10
    print(locals()) # 查看局部空间
func()
print(b)
# 10
print(globals()) # # 查看全局空间
```


**nonlocal:在局部内，修改离nonlocal最近的一层，如果上一层没有就继续向上找，且声明nonlocal本层不能有与nonlocal变量相同的变量名**
```python
#只能修改，不能创建
a = 10
def func1():
    a = 5
    def foo():
        nonlocal a # a 上一层变量5
        a = a+1   
        print(a) # 6
    foo()
    print(a) # 5
func1()
```
* 作业
```python
 name = "jennie"
 def func():
    name = "rustin"
    def inner():
        print(name)
    for inner in range(10):
        pass
    inner() # 通过循环，最后inner变成了9， 9()

func()

#会报错
name = "jennie"
def func():  
    print(name)
    name = "rustin"
func()
# 从语法上看def 里面没有错，print现在内部找name，确实找到了，
# 但是执行print时，还没走到哪层name定义的那一句

# 修改后
name = "jennie"
def func():
    name = "rustin"  
    print(name)
    
func()


def List_number(val,list=[]): # 可变数据类型
    list.append(val)
    return list

list1 = List_number(10) #加到默认列表
list2 = List_number(2,[]) # 加到新列表
list3 = List_number('a') # 加到默认列表

print(list1) # [10,a]
print(list2) # [2]
print(list3) # [10,a]
```

# 2024.4.4 

# 1、匿名函数：lambda

def 函数名(x):
    return x

lambda x: x (不需要写return，但是可以直接return)
结构：lanmda 参数 ：返回值
只能返回一种类型，如果要返回多个，必须用tuple或者list包起来（以容器的形式返回）
m = lambda *args,*kwargs : ("jennie","rustin")

```python
f = lambda x, y : x + y
print(f(3,6))
# 结果 9


# 传入两个参数返回较大值
m = lambda x, y : x if x > y else y
print((lambda x, y : x if x > y else y)(1,3))
# 以上是常用方式

# 传入一个列表，返回列表后三位
print((lambda x : x[-3:])([1,2,3,4,5,6]))

n = lambda  : 5
print(n())
# 结果 5
```


# 2、python内置函数

* 以下是不太常用
    1. all():判断里面的元素是否都为真，传入tierable，返回bool值
    all([1,2,3,4,5])
    all([1,0,3,4,5])

    2. any():判断iterable里面是否有一个为真
    any([1,0,False,"",[],{},set(),None]) 
    1 是True，所以结果是True

    3. bytes():将str转为字节
    print（bytes("你好“，encoding="utf-8")
    print("你好“.encode("utf-8"))

    4. callable():判断是否可调用——函数等，返回bool值

    5. chr(20200):通过数字码位找对应的char
    6. ord("你“)：通过char找对应的码位
    可以做个随机验证码

    7. complex(20):找出数字的实部和虚部

    8. divmod(5,2):返回5/2的商数和余数

    9. eval("3+2*3"):计算
    eval("abc888")  输出888

    10. exec():

    11. frozenset():冻结集合——冻结可变数据类型不让变

    12. globals():查看全局空间的内存地址
    13. local():查看局部空间

    14. hash():

    15. id():查看内存地址


    16. help(list.append):询问list.append的使用说明

    17. iter():迭代
    18. next():取迭代器中的值

    19. oct(9):10进制转换成8进制并返回
    20. bin(9):10进制转换成2进制并返回
    21. hex(9):10进制转换成16进制并返回

    22. pow(4,2):幂制转换——4的2进值———返回16**——   4**2也可以实现幂制转换
    pow(4,2,3):有第三个参数时是返回16/3的余数


    23. repr("123")/repr(123):查看到底是str还是int

    24. round(6.4736735,2):保留两位小数

* 以下是常用

    1. abs(-20):求绝对值——20
    2. format(12,"08b"):将12从10进制格式化为二进制，总长度为8位，不够用0 补齐并返回——00001010
        * format(12,"08c")——转换为八进制
        * format(12,"08x")——转换为16
        * format(12,"d")——转换为10进制
        * format(2.35436,".2f")——保留两位——2.35
        * format("hell0",">20")——hello左边20个whitespace——右对齐
         <20:右边20——左对齐
         ^20:居中

    
    3. enumerate():枚举
    ```python
    lst = ["jennie","rustin","aobai","turkey"]
    for i, c in enumerate(lst,start=1): # 起始数，默认起始值为0
        print(i, c)
    ```

    4. float()

    5. **reversed()——反转不影响元数据，开辟新的空间（但是lst.sort(),这个就是原地修改,sorted就是开辟新空间）**
    ```python
    lst1 = [1,2,3,4,5,6]
    lst2 = list(reversed(lst1))
    print(lst1)
    # [1,2,3,4,5,6]
    print(lst2)
    # [6, 5, 4, 3, 2, 1]
    lst = [1,2,3]
    lst.reverse()  #这个就是原地修改
    print(lst)
    ```

    6. sum():iterable,起始值——求数字之和
    ```python
    sum([1,2,3,4,5,6],start=100)
    # 100+1+2+3+4+5+6
    ```

    7. zip() ——可以用创建字典
    ```python
    lst1 = [1,2,3,4,5,6]
    lst2 = [2,3,4,5,6,7]
    print(dict(zip(lst1,lst2))) # 字典创建方式1（这里不仅可以加两个lst）
    # {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}
    print(list(zip(lst1,lst2)))
    # [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
     ```
     字典创建方式2
     ```python
     d = dict(a=1,b=2,c=3)
     print(d)
    # {'a': 1, 'b': 2, 'c': 3}
    ```

    8. dir():查看当前内容都有什么方法
    dir(str):查看str的所有方法

    9. 其他比较熟悉的方法
        * open()
        * range()
        * str()
        * len()
        * list()
        * print()
        ```python
        print(1,"wangxue",sep="***",end="/",file=open("jennie.txt","a",encoding="utf-8"))
        # sep 是分隔
        # file 是将打印内容打印至指定文件（内容输出）
        ```
        
    10. **sorted(iterable，key=排序规则,reverse=True) :开辟新空间/sort是原地修改**
    ```python
    def foo(x):
        return abs(x)
    lst = [1,2,3,4,5,34,-20,40]
    print(sorted(lst,key=foo))
    print(sorted(lst,key=lambda x : abs(x)))
    print(sorted(lst,key=abs)
    # [1, 2, 3, 4, 5, -20, 34, 40] 不用list也能返回排序后的结果


    dic = {1:"acvb",2:"cchert",3:"bg"}
    print(sorted(dic))
    # [1, 2, 3]
    print(sorted(dic.values()，key=len)) # dic.values() 是将dic的values拿出来形成一个新的iterable
    # ['bg', 'acvb', 'cchert']

    dic1 = [
        {"id":1, "name":"jennie","age":25},
        {"id":2, "name":"rustin","age":28},
        {"id":3, "name":"aobai","age":2},
        {"id":4, "name":"turkey","age":1}
    ]
    print(sorted(dic1,key = lambda x :x["age"]))
    # [{'id': 4, 'name': 'turkey', 'age': 1}, {'id': 3, 'name': 'aobai', 'age': 2}, {'id': 1, 'name': 'jennie', 'age': 25}, {'id': 2, 'name': 'rustin', 'age': 28}]
    ```
    11. **filter(func——过滤条件，iterable——一个一个放进func里)：过滤**
    filter帮我们自动实现for循环，循环的把iterable的值拿出来作为参数将其传入func里，最后做bool值判断，将结果为True的筛选出来
    ```python
    filter(lambda x: x > 5, [1,23,4,5,6])
    print(list(filter(lambda x: x > 5, [1,23,4,5,6])))
    # [23, 6]
    # filter帮我们实现x>5的bool值判断，符合条件的删选出来
    ```
    12. **map(func, iterable)：映射,和zip类似，可以无限往后加iterable作为func的多个参数**
    ```python
    print(list(map(lambda x : x**2, [1,2,3,4,5])))
    # [1, 4, 9, 16, 25]
    print(list(map(lambda x ,y :( x+y,y-x), [1,2,3,4,5],[6,7,8,9,10])))
    # [(7, 5), (9, 5), (11, 5), (13, 5), (15, 5)]
    ```
    13. max(iterable, key=):直接返回最大值max(iterable, key=abs/str)
    14. min():求最小值
    15. **reduce():累积计算**
    ```python
    from functools import reduce
    lst = [1,2,3,4,5]
    def func(x,y):
        return x * y # 累乘 x1*y2=2,x2*y3=6,x6*y4=24
    print(func, lst)    
    ```
# 3. 练习
    ```python
    lst = [1,2,3,4,67,32,46,4,2,32]
    def func(x):
        return lst.count(x) == 1 # 获取bool值
    print(sum(filter(func,lst)))
    print(sum(filter(lambda x :lst.count(x)==1,lst)))
    ```
# 2024.4.5
# 1.closure(函数嵌套):使用非全局变量也非本层变量（中间变量）——保证数据的安全性（避免全局变量容易被修改）和干净性
1. closure的作用
```python
def foo():
    lst = [] # 避免因为设为全局变量导致数据被修改
    def func(money):
        lst.append(money)
        print(sum(lst) / len(lst))
    return func

func = foo() #创建了lst空间并保留，接收foo返回的函数func
func(1000)
func(2000)
lst = [1,2,3,4] # 即使有重复的变量名lst也不会被修改和覆盖

```
2. closure的使用方法
```python
def foo(num):
    a = []
    def func(num):
        a.append(num)
    func(num) # 这个不是closure，英文func是在foo内部执行的
    print(a)
foo(1) # 没有return func，所以开辟foo空间后会销毁
foo(2) # 当再次调用时会重新开辟空间，开辟（a），所以无法将上个不走的1保留在列表里面


def foo():
    a = []
    def func(num):
        a.append(num)
        print(a)
    return func # 将func函数扔到外部执行
foo()(1) # 这也是调用foo和func函数的方法
foo()(2)
# 注意和下面执行方式的区别在于:上面从头到尾执行两遍foo，而下面执行一遍foo，执行两遍func

ret = foo()  # foo()的调用的主要作用是开辟一块foo内部不会变的变量a=[]
ret(1) # 调用内部func函数对[]进行处理
ret(2)
```

3. 传参和不传参的区别
```python
def foo():
    # b = 10   传参时的隐形赋值 b 是foo内部的局部变量，a还是全局变量，只是将a的值给了b
    def func(b):
        # b = 10
        print(b)
    return func
a = 10
ret = foo()
ret(a)
print(globals())  # a 依旧是全局变量
# 所以a是全局变量，b是func本层变量，没有中间变量

# 以下修改后是closure
def foo(b):
    def func():
        print(b) # 这一层的b是来源于上一层foo开辟的空间——上一层变量
    print(func.__closure__) # 查看是否是闭包
    return func
a = 10
ret = foo(a)
ret()
```
判断closure
* 内层函数（实际操作层）是有有形参数
* 内层函数是否定义变量
* 内层函数使用的变量是否是全局变量
* 总的来说，内层函数的变量只能是来源于中间层def和def之间
# 2.推导式——编写一些有规律性的——结构——[结果 for 条件]
1. 列表推导式
 ```python
lst = []
for i in range(1,11):
    lst.append(i)
print(lst)

# 普通循环模式
print([i for i in range(1,11)])

#筛选模式——这种简单的常用
print([i for i in range(1,11) if i > 5])

# 结合三元运算模式[三元运算 for循环 条件]-多重筛选——其实不常用
print([i if i > 5 else "jennie" for i in range(1,11) if i > 2 if i > 4])
print([i if i > 5 else "jennie" for i in range(1,11) if i%2 == 0])

# 双层循环
lst = []
for i in range(3):
    for j in range(2):
        lst.append(j)
print(lst)

print([j for i in range(3) for j in range(2)])

# 和lambda的结合使用
ret = [lambda x :x * i for i in range(4)] # [lambda,lambda,lambda,lambda] i 为3的四个lambda函数
ret1 = [em(2) for em in ret] # 将2作为lambda函数的参数x传入lambda函数
print(ret1)
# [6,6,6,6]

# 为什么上面的lambda函数中不能保留i的四个值0，1，2，3，因为他是循环四次lambda函数定义，示例如下(一样的实现效果)
for i in range(4):
    def func():
        print(i)
[func(),func(),func(),func()]


for i in range(4):
    def func():
        print(i)
    func()



# 
ret = (lambda x :x * i for i in range(4)) # 现在是生成器,ret 实际上是一个地址
ret1 = [em(2) for em in ret] # 生成器具有惰性机制，在此行的for循环里一次粗发ret
print(ret1)
# [0, 2, 4, 6]
 ```
2. 集合推导式{},注意集合的去重性质
 ```python
 # 普通循环模式
print({i for i in range(1,11)})

#筛选模式——这种简单的常用
print({i for i in range(1,11) if i > 5})

 ```
 3. 字典推导式 以 : 区分字典和集合
 ```python
print({i:i for i in range(1,11)})
 ```
 4. tuple没有，只有看着像tuple的生成器对象，所有取的时候可以转成list或者用next取
 ```python
print(list((i for i in range(1,11))))
# 形成一个生成器
  ```
# 3.iterator——注意区分iterator和iterable
1. **iterable：只有__iter__方法**
    具有iter方法的就是可以迭代的；
    能用for循环的；str,[],{}
    不可迭代的：int

```python
lst = [1,2,3,4]
new_list = lst.__iter__() # new_list 现在是一个iterator对象,__iter__()就是讲iterable变成iterator
print(new_list)
print(new_list.__next__())
print(new_list.__iter__()) # 对iterator本身使用iter方法后还是new_list他自己
```

2. **iterator ：具有__iter__和__next__方法（iter()和next()——推荐）**
    * 优点：next一个一个拿，节省空间
    * 缺点：使用不灵活，没有append等方法——
            一次性迭代完就无法使用了（open）
            不可逆，只能从上往下走

```python
# 循环的本质
s = [1,23,4,556]
s1 = s.__iter__()
while True:
    try:
        print(s1.__next__())
    else StopIterarion:
        break
iter(s) # 和 s.__iter__() 是一样的实现效果

f = open("jennie.txt", "r","utf-8") # 这里的文件句柄f就是一个迭代器
print(f.__next__())
print(f.__next__())
for i in f:
    ···
# 迭代器也支持for循环
```
 
# 4.生成器——generetor（yield），本质就是迭代器
 * 迭代器是内置的
 * 生成器是认为定义的
 * 作用：节省空间（惰性机制）——尤其是大数据数据库，yield记录执行位置
 * 定义：
    1. 基于函数
    2. 基于生成器表达式
```python
# 函数
def func():
    return 1 # 中止函数

# 生成器gennerator
def func1():
    print(1)
    yield 1 # 不中止函数，yield将值返回，并记录执行的位置
    print(2)
    yield 2
    print(3)
    yield 3

g = func1() # 产生一个generetor，将其内存地址赋给g
print(g) # 生成器对象地址
print(g.__next__()) # 1
print(g.__next__()) # 2
print(g.__next__()) # 3


def func2():
    lst = []
    lst.append(1)
    yield lst
print(func2().__next__()) # [1]
print(func2().__next__()) # [1]
print(func2().__next__()) # [1] 调用三次func2，创建三个生成器地址

def func3(a):
    lst = []
    for i in range(a):
        lst.append(i)
        yield lst
store = func3(8)
print(store.__next__())
print(store.__next__())
print(store.__next__())
print(store.__next__())
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# next取值要和yield出的数量保持一致，否则stopiteration

def func4():
    lst = [1,2,3,4,5,6]
    for i in lst:
        yield i

g = func4()
for j in g:
    print(j)


# 用yield from转换——将可迭代对象逐个返回
def func6():
    lst = [1,2,3,4,5]
    yield from lst

g = func6()
print(g.__next__())
print(g.__next__())
```
使用场景
* 当数据量较大时
* 数据传输时

总结：iterator和generetor
* 有yield的是生成器
* 生成器是自定义的迭代器
* 通过对象内存地址（print可以显示）
* __通过send方法来判断，只有生成器有send方法__

# 2024.4.6
# 1.标准版装饰器——在不修改源代码的情况下，额外增加新的功能
1. 开发封闭原则
* 对新增的功能是开发
* 对源代码及调用方式是封闭
```python
import time

def run_time(f):
    start_time = time.time() # 记录当下时间
    f()
    time.sleep(2) # 睡眠两秒
    stop_time = time.time()
    print(f"running time : {stop_time - start_time}")

def func():
    lst = []
    for i in range(3):
        for j in range(2):
            lst.append(j)
run_time(func)
```

```python
import time

def run_time(f):
    def inner()
        start_time = time.time() # 记录当下时间
        f()
        time.sleep(2) # 睡眠两秒
        stop_time = time.time()
        print(f"running time : {stop_time - start_time}")
    return inner

def func():
    lst = []
    for i in range(3):
        for j in range(2):
            lst.append(j)

func = run_time(func)
func() # 调用func实际执行的是inner——满足调用方式不变的原则

```

2. 标准版装饰器
```python
def outer(func):
    functools.wraps()
    def inner(*args, **kargs):
        # 增加原函数执行前的相应操作
        res = func(*args, **kargs) # 调用原来的函数
        # 增加原函数执行前的相应操作
        return res
    return inner

@outer  # Jennie = outer(Jennie) # 返回被装饰后的Jennie函数
def Jennie():
    print("Jennie")
    return jennie
    """这是原函数的注释"""

Jennie()

# 这也是装饰器
def func():
    print(1)
    print(2)
    return f

@func # foo = func(foo)
def foo():
    print(3)

foo()
```
3. 装饰器应用场景
* 面向对象
* 登录认证
* falsk路由全都是有参装饰器
# 2.有参数装饰器——很少用
```python
def auth(arg): # arg = 10
    def outer(func):
        functools.wraps()
        def inner(*args, **kargs):
            if arg == True:
                print("开始装饰")
                res = func(*args, **kargs) 
                print("装饰成功")
            else:
                res = func(*args, **kargs) 
            return res
        return inner
    return outer

@auth(True)  # outer = auth(True)  Jennie = outer(Jennie)  合并：Jennie = auth(True)(Jennie) 
def Jennie():
    print("Jennie")
    return jennie
    """这是原函数的注释"""

Jennie()
```
# 3.多个装饰器装饰一个参数
```python
def wrapper(func):
    def inner(*args,**kwargs):
        print(1)
        ret = func(*args,**kwargs)
        print(2)
        return ret
    return inner

def wrapper1(func):
    def inner(*args,**kwargs):
        print(3)
        ret = func(*args,**kwargs)
        print(4)
        return ret
    return inner1

@wrapper
@wrapper1  # 从下往上装饰 foo = wrapper1(foo) inner1
# foo = wrapper1(foo)
# foo = wrapper(foo)
def foo():
    print(5)

foo()
```

# 4.recursion
递归
递：一直传参数
归：返回
* 不断调用自己本身
* 有明确的终止条件
1. 递归的最大深度——官方说明：1000，实际测试：997-998
```python
# 死递归——无效递归，没有终止条件
def func():
    print(1)
    func()
func()

def func1(n):
    if n == 3:
        return "Jennie"
    return func(n+1)

func1(1)
    return func1(2)
            return func(3)
                if i == 3: # 满足条件
                    return "Jennie"

def age(n):
    if n == 3:
        return 38
    return age(n+1)-2
age(1) # 34


name = ["wangxue","Jennie",["王雪","刘晓波",["鳌拜","turkey"]]]

def print_name(lst):
    for name in lst:
        if type(i) == list:
            print_name(name)
        else:
            print(i)
print_name(name)
        
```

# 2024.4.7
