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

