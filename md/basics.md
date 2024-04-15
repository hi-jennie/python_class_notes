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
* 练习
```python
# 实现一个装饰器，限制改函数被调用的频率，如三秒一次
import time
def wrapper(func):
    start_time = 0
    def inner(*args,**kwargs):
        nonlocal start_time
        if time.time() - start_time >= 3:
            start_time = time.time()
            func(*args,**kwargs)
        else:
            print("被限制了")
    return inner

@wrapper
def func():
    print("execute successfully")
    
        
while True:
    func()
    time.sleep(1)


```
```python
'''
jd--Jennie:123
tb--Jennie:456
'''
login_dic = {
  "jd":False,
  "tb":False  
}
def auth(flag):
    def wrapper(func):
        def inner(*args,**kwargs):
            if login_dic[flag]:
                func(*args,**kwargs)
            else:
                # 这块登录功能最好是拿出去封装起来
                username = input("username: ")
                pwd = input("password: ")
                with open(flag, "r",encoding="utf-8") as fp:
                    for line in fp:
                        file_name, file_pwd = line.strip().split(":")
                        if file_name == username and file_pwd == pwd:
                            login_dic[flag] = True
                            print("login successfully")
                            func(*args,**kwargs)
                            break
                        else:
                            print("密码错误“)
        return inner
    return wrapper
@auth("jd")
def jd_index():
    print("This is jd index")

@auth("jd")
def jd_shopping():
    print("This is jd shopping")

@auth("tb")
def tb_index():
    print("This is tb index")

@auth("tb")
def tb_shopping():
    print("This is tb shopping")
func_dic = {
    "1": jd_index,
    "2": jd_shopping,
    "3": tb_index,
    "4": tb_shopping,
    "5": exit
 }  

while True:
    choose = input("command: ")
    if choose in func_dic:
        func_dic[choose]()
    else:
        print("please input right command")

```
# 2024.4.8
1. __模块的使用及导入__
    * 模块module:.py文件就是一个模块
        * 直接使用
        * 以文件的形式管理代码
        * 模块的分类：自定义模块/内置模块（标准库）/第三方模块（类库）

    自定义模块：自己写的.py文件
    * 导入方式1：import decorator——将文件中的所有内容都拿来 decorator.——访问里面具体的内容
                import decorator
                import decorator
                import decorator
                不管导入多少次，只执行一个

    * 导入方式2：
        * import _ from decorator(import _ from decorator as __)
        * from decorator inport * (也是导入所有)
        * from decorator inport _, __
    ```python
    # 导入绝对模块
    import sys
    sys.path.append("绝对路径")

    import 该绝对路径下的py文件

    ```
    * 导入顺序：内存 > 内置 > sys.path
    sys.modules——查看内存中所有的模块

    * 模块安装 ：pip install 模块名
    * 模块的用途：
        * 当做脚本被执行
        * __当做模块被执行__
        if __name__ == "__main__" 启动接口，不然在import decorator这一步函数就会被调用，加上启动接口，则需要通过decorator.进入之后才能调用

2. __time__ 
    time.time:拿到一个时间戳 浮点型
    time.sleep:睡眠
* 分类：
    * 时间戳——给程序猿做计算 19824.9238467 time.time()
    * 结构化时间 time.localtime()
    * 字符串时间——给用户看的 2024年4月8日19:56:55 time.localtime()
    ```python
    time.time() # 时间戳
    t = time.localtime(time.time()) # 结构化时间
    time.strftime("%Y-%m-%d %H:%M:%S",t) # 结构化时间转成字符串时间
    print(t.tm_year)

    str_time = "2024-4-8 19:56:55"
    t_time = time.strptime(str_time,"%Y-%m-%d %H:%M:%S") # 时间戳转为结构化时间
    print(time.mktime(t_time)) # 转为时间戳

    ```
3. datetime:封装了time，在time的基础上增加了新的功能
```python
from datetime import datetime
from datetime import timedelta
print(datetime.now()) # 获取当前时间(2024-04-08 20:31:41.740497)(时间对象)
str_time = "2024-4-8 19:56:55"
print(datetime(2024,4,8,19,56,14)) # 自定义时间
print(datetime.strptime(str_time,"%Y-%m-%d %H:%M:%S"))  # 将字符串时间转换成可以操作的时间(时间对象），比如时间的加减
print(datetime.strptime(str_time,"%Y-%m-%d %H:%M:%S") - date.time(2024,1,3))

import time 
t = time.time()
print(datetime.fromtimestamp(t) - datetime(2020,1,20)) # 时间戳转时间对象

print(date.time.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")) # 时间对象转成字符串时间
print(datetime.timestamp(datetime.now())) # 时间对象转换成时间戳

from datetime import timedelta
print(datetime.now() - timedelta(days=100))
```

4. random:随机数
应用场景：
验证码
```python
import random

print(random.random()) # 0-1随机小数
print(random.randint(1, 10)) # 1-10随机整数

lst = [1,2,3,4,5,6]

print(random.randrange(1,100,2))

print(random.choice(lst)) # 从列表选择一个

print(random.choice(lst,k=2)) # 从列表随机选两个，但是会有重复

print(random.sample(lst,k=2)) # 从列表随机选两个，不重复

print(random,shuffle(lst)) # 打乱list

print([chr(i) for i in range(65,91)]) # 字母大写
print([chr(i) for i in range(97,123)]) # 字母小写


lst1 = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + [i for i in range(10)]

new_lst = random.sample(lst1,k=4)
print("".join(new_lst))
```
5. 序列化（json，pickle）
序列化：将特殊的数据转换成字符串
反序列化：将字符串转换成特殊的数据（字典等）
文件：dump，load
字符串：dumps，loads

```python
import json
# 1.反序列,字符串转dic
# json要求所有的key和value用双引号,且只能序列dict和list，但是所有语言共有的
s = '{"Jennie":"Ruetin"}' # 知识看着像字典，实际上是string
new_s = json.loads(s)
print(new_s,type(new_s))


# 2.序列化，dic转字符串
dic = {"Jennie":"Ruetin"}
str_ = json.dumps(dic, ensure_ascii=False)
print(str_,repr(str_))

# 3.文件序列化
dic2 = {"Jennie":"Ruetin"}
f = open("Jennie.txt","a",encoding="utf-8")
f.write(json.dump(dic2) + "\n")

# 4.文件反序列化
f = open("Jennie.txt","r",encoding="utf-8")
for i in f:
    print(json.load(i))

```
```python
# pickle是python独有的，和其他语言的交互性不强
import pickle

def func():
    print(1)

# 转成对象
s = pickle.dumps(func)
print(s)

func1 = pickle.loads(s)
func1()

```

6. os——通过程序与操作系统交互
* 四个维度：
    * 文件夹（创建和删除）
        * os.makedirs("a/b/c/d") 递归创建多个文件夹 a下面是b文件夹，b下面又创建c文件夹
        * os.removedirs("a/b/c/d") 删除多个文件夹
        * os.mkdir("a") 创建一个文件夹
        * os.rmdir("a") 删除一个文件夹
        * os.listdir("文件夹绝对路径") 查看文件夹下文件
    * 文件
        * os.rename 重命名
        * os.remove 删除文件
    * 路径
        * os.getcwd() 获取当前文件工作路径  /Users/jennie/python_class_notes/lesson8_Object-Oriented-programming
        * os.chdir   cd切换文件夹
        * os.path.abspath   获取绝对路径
        * os.path.dirname(r"/Users/jennie/python_class_notes/lesson8_Object-Oriented-programming...py") 返回上一层
        * os.path.basename(r"/Users/jennie/python_class_notes/lesson8_Object-Oriented-programming...py")  拿到文件名
        * os.path.join("/Users/jennie/python_class_notes","lesson4","decorator.py") 路径拼接到一起
        * os.path.exists("/Users/jennie/python_class_notes") 判断路径是否存在
        * os.path.getsize(r"/Users/jennie/python_class_notes/lesson8_Object-Oriented-programming...py") 获取文件大小
        * os.path.isabs 判断是否是绝对路径
        * os.path.isdir() 判断是否是存在的文件夹
        * os.path.isfile() 判断是否是存在的文件
    * 其他

7. 与python解释器做交互

* import sys
    * sys.path 模块导入的顺序列表
    * sys.argv () command-line parameter,第一个参数是当前文件名[0]
    * sys.version 查看python的版本
    * sys.modules 查看已经加载的模块
    * sys.platform 查看什么系统  我的  darwin

8. hashlib :加密
md5,sha1,sha256,sha512——加密级别，逐步提高
Jennie：Jennie123 密码

加密：明文——字节——密文      不可逆，不能破解
明文如果是一致的，那么密文也是一致的

* 使用场景：
    * 用户注册的过程 Jennie123——字节——密文——存储
    * 登录： Jennie——字节——密文——读取——校验
```python
import hashlib
user = "Jennie"
pwd = "Jennie123"

# 1.存储
s = hashlib.md5()  # 初始化一个加密模板 hashlib.sha1(）等
s.update(pwd.encode("utf-8"))  # 添加要加密的字节
m = s.hexdigest() # 加密
print(m)
f = open("Jennie.txt","a",encoding="utf-8")
f.write(f"{user}:{m}\n")  # 存储进文件

# 2.登录
user = "Jennie"
pwd = "Jennie123"
s = hashlib.md5()  
s.update(pwd.encode("utf-8")) 
m = s.hexdigest()
f = open("Jennie.txt","r",encoding="utf-8")
for i in f:
    file_user,file_pwd = i.strip().split(":")
    if user == file_user and m == file_pwd:
        print("login")
        break
    else:
        print("wrong password")

# 动态加盐
def register():
    user = input("name: ")
    pwd = input("password: ")
    s = hashlib.md5(user.encode("utf-8"))  # 将用户名作为动态加盐  
    s.update(pwd.encode("utf-8")) 
    m = s.hexdigest()
    f = open("Jennie.txt","a",encoding="utf-8")
    f.write(f"{user}:{m}\n")  # 存储进文件

def login():
    user = input("name: ")
    pwd = input("password: ")
    s = hashlib.md5(user.encode("utf-8"))  # 将用户名作为动态加盐  
    s.update(pwd.encode("utf-8"))
    f = open("Jennie.txt","r",encoding="utf-8")
    for i in f:
        file_user,file_pwd = i.strip().split(":")
        if user == file_user and m == file_pwd:
            print("login")
            break
        else:
            print("wrong password") 

msg = '''
1.注册
2.登录

'''  
func_list = {
    "1":register,
    "2":login
} 

choose = input(msg)
if choose in func_list:
    func_list[choose]()
else:
    print("please choose correctly")
```

9. collections:额外的数据类型
```python
from collections import deque

# OrderedDict:有序字典
# deque：双端队列(两遍都可以操作)

lst = deque([1,2,3,4,5])
lst.append(6)  # list.append
lst.appendleft(0)  # list.insert(0,5) 列表用insert可以在任意位置加
print(lst)
lst.pop()  # 删掉右边一个数
lst.popleft() # 删掉左边一个数



lst1 = [1,2,3,4,5]
lst1.append(6)
lst1.insert(0,5)
print(lst1)
lst1.pop(4)  # 参数是index
print(lst1)
```

Counter计数器
```python
from collections import Counter
lst = [1,2,4,57,3,464,776,32,5,5,5,4,4,]
print(dict(Counter(lst)))

```
具名元祖（namedtuple）
```python
from collections import namedtuple
# 创建一个名为 Color 的具名元组，包含字段 r、g、b 和 alpha
Color = namedtuple("Color", "r g b alpha")
# "Color" 是一个字符串，它创建的 namedtuple 的名称
color = Color(r=50, g=205, b=50, alpha=1.0)
print(color.r)  # 输出：50
print(color.alpha)  # 输出：1.0

# 错误示例：无法添加新字段
color.e = 0  # AttributeError: 'Color' object has no attribute 'e'

```
defaultdict（默认值字典）
```python
from collections import defaultdict

# 假设 document 是一个包含单词的列表
document = ["apple", "banana", "apple", "orange", "banana", "apple"]

word_count = defaultdict(int)
for word in document:
    # 如果我们执行 word_count['apple'] += 1，即使 'apple' 不在 word_count 中，它也会自动创建 'apple' 键，并将其值从默认值0增加到1。
    word_count[word] += 1

print(word_count)
```

# 2024.4.10
1. regular expression(import re)
* findall : 查找所有，以列表形式返回
* search ：从字符串任意位置查找，找到一个后停止查找，找不到返回None
* match ：从字符串开头位置查找，找到一个后停止查找，找不到返回None
* sub : 替换
* split ：分隔
* finditer ：查找内容，返回一个迭代器
* group ： 分组取值
     * 示例1
```python
import re 
name = "JennieRuestin"
print(re.findall("Jennie",name))

```
  * 示例2
```python
import re
name = input("What's your name?").strip()

#注意，在正式表达中（）表示一个group，但是在这里表达另一层含义————捕获输入的name里符合(.+), (.+)里两个（）内的具体内容并将其返回给matches
matches = re.search(r"^(.+), ?(.+)", name) 
#matches = re.search(r"^(.+), *(.+)", name) 即使在括号后面输入很多white space的情况下也是可以运行的
if matches:
    name = matches.group(2) + " " + matches.group(1) #group(1）表示re.search(r"^(.+), (.+)", name)里面capture到一个（）里面的内容
print(f"hello, {name}")

```
  * 示例3
```python
import re
 #re.sub()5个参数
 
url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# ————这种情况下无法做bool值判断,当输入“https://www.google.com/"的网址时就不行，就是当无法找到要背替换的值会出错

matches = re.search(r"^(https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$ ", url, re.IGNORECASE)  # 最后的(.+)表示capture
#(?:www\.)表示不捕捉（）里面的东西，只表示这是一个group
if matches:
    print(matches.group(1))
```
  * 示例4
```python
import re
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

```
2. logging：日志
* 作用：
    * __记录程序执行的状态__
    * 记录一些重要信息——数据库
    * 热推——数据库
    * 个人喜好分析（大数据）——数据库
```python
import logging
# 从10级开始记录
logging.basicConfig(
    level=10, # 记录级别
    format="时间：%(asctime)s 日志级别：%(levelname)s 文件名：%(filename)s 错误信息:%(message)s", # 时间 级别 文件 错误信息
    filename="Jennie.log", # 存储进文件里面，就不再出现在屏幕中，不能以utf-8形式编码
    filemode="a" # 不支持编码（所以如果有中文无法显示，所以不要用中文）
)
logging.debug(" is debug") #10级往后依次递增
logging.info(" is info")

logging.warning(" is warning")
logging.error(" is debug")
logging.critical(" is critical")

输出
# 2024-04-10 17:12:13,374 DEBUG decorator.py  is debug
#  2024-04-10 17:12:13,374 INFO decorator.py  is info
# 2024-04-10 17:12:13,374 WARNING decorator.py  is warning
# 2024-04-10 17:12:13,374 ERROR decorator.py  is debug
# 2024-04-10 17:12:13,374 CRITICAL decorator.py  is critical
```
* 自定义日志解决两个问题：存储进文件里面，就不再出现在屏幕中，不能以utf-8形式编码
```python
import logging
def loger():
    loger = logging.Logger("loger") # 创建一个框架
    f = logging.FileHandler(filename="Jennie.log",mode="a",encoding="utf-8") # 创建Jennie.txt的文件句柄,自动创建 在lesson8
    s = logging.StreamHandler() # 在屏幕中显示
    format = logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(message)s")
    # 存储到文件和屏幕时的样式

    loger.setLevel(logging.INFO)  # 设置记录级别，从info开始记录，也可以loger.setLevel(logging.ERROR)

    f.setFormatter(format) # 给文件设置存储数据时的格式（以format的格式）
    s.setFormatter(format) # 屏幕中也以这种模式展示
    loger.addHandler(f) # 把文件句柄和loger对象进行绑定
    loger.addHandler(s) # 把屏幕句柄与loger对象进行绑定
    loger.info("is info")
    return loger

try:
    int(input("输入数字："))
except Exception:
    loger().error("类型转换错误")


```

# 2024.4.11
1. package(笔记中有自己创建的package)
    * modules：.py文件
    * package：具有__init__.py文件的文件夹

    * package的作用：以文件夹的形式管理文件

    * package的使用：文件夹.文件.功能()
            package wangxue
                文件__init__.py  每个package的头部文件，里面存储着与他统计的其他.py文件的功能
                文件Jennie.py
                    功能func()
    * 在导入package的过程中推荐使用绝对路径：从顶级包开始查找（带__init__.py）就是绝对路径
```python
import wangxue.jennie as j  # 注意，包可以用.进行访问

```

# 2024.4.15 oriented object programmaing
1. 面向对象的结构
* 变量
* 函数
通过类名操作类——通过对象操作类——一个类可以实例化为多个对象