# 2024.4.15 oriented object programmaing
1. 面向对象的结构
* 变量：有共有和私有
* 函数
* __通过类名操作类__
* __通过对象操作类__
* 一个类可以实例化为多个对象
```python
class StudentInfo():
    name = "Jennie"
    
    def print_(self):
        print("24")

J = StudentInfo()
del J.name  # 删了，所以拿不到了。没删就能拿到name

print(J.name)  
# 并没有在类里面找到Jennie

```
2. self的做作用：就是实例化对象本身,然后作为隐形参数传到class中——和cls，**args，**kwargs很像，是约定俗称，可以修改，但是不建议修改
* 共有和私有类变量：增加一点灵活性——动态
* init 给对象空间进行的封装
```python
class StudentInfo():
    # 共有——类变量：可以在对象中使用
    grade = "4" 

    # 类私有变量：加上__就是类私有，只能在类里面操作，无法通过对象找到
    __grade = "4"

    # __init__是JenNie():时触发的函数——其实就是创建一个对象时默认触发函数 
    def __init__(self,name,gender):
        print(StudentInfo.__grade)  # 这样可以拿到类的私有变量
        self.name = name
        self.gender = gender

# Jennie = StudentInfo() 触发init
Jennie = StudentInfo("Jennie","female")  # 创建一个名为Jennie的对象
Rustin = StudentInfo("Rustin","male")
print(Jennie.name,Jennie.gender)

print(Jennie.grade) # 都能取到类变量grade：4
print(Rustin.grade) # 都能取到类变量grade：4

# 打印 Jennie female


print(StudentInfo.__grade) # 也无法拿到私有变量，反正就是只能在类的内部进行操作
```
3. 函数也分共有和私有
```python
class StudentInfo():
    def __init__(self,name):
        self.name = name

    def func(self):
        print(f"public:welcome{self.name}")
        # 但是，可以在共有的方法中去使用私有方法，比如
        self.__foo()


    def __foo(self):
        print("private")

Jennie = StudentInfo("Jennie")

Jennie.__foo()
# 无法调用__foo()
    

```
4. 依赖关系：将一个对象传递到类中使用就是依赖关系

5. 类方法，静态方法，实例对象方法
```python
class A():
    pass
    

    def func(self): # 实例方法
        print("a")

    @classmethod # 类方法
    def func1(cls):
        print("a")

    @staticmethod # 静态方法
    def func3():
        print("a")



a = A()
a.func() # 隐形传参
# func()的调用时通过a这个对象来的，他是属于对象的方法——对象方法

# 如果通过类来调用，必要要跟参数
# A.func1(1)
# 但是，如果加上@classmethod 就不用传参
A.func1()
```

6. 
```python
class Bmi():

    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / self.height ** 2

    @property # 伪装成属性，但本质还是方法
    def bmi2(self):
        return self.weight / self.height ** 2

    @bmi2.setter 
    def bmi2(self,value):
        self.bmi2 = value

    @bmi2.deleter 
    def bmi2(self):
        del self.bmi2

Jennie = Bmi("Jennie",1.6,43)

#  其实是在调用bmi函数,加()
print(Jennie.bmi())

# 通过属性的方式查看,没加(  )
print(Jennie.bmi2)


# 属性支持增删改
print(Jennie.bmi2) # 查看@property
Jennie.bmi2 = 20  # 修改@bmi2.setter
del Jennie.bmi2 # 删除@bmi2.deleter

```