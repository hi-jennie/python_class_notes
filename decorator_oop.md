1. 装饰器公式————其实就是一个闭包
```python
def outer(func):
    functools.wraps()
    def inner(*arge, **kargs):
        # 增加原函数执行前的相应操作
        res = func(*arge, **kargs) # 调用原来的函数
        # 增加原函数执行前的相应操作
        return res
    return inner

@outer
def Jennie():
    print("Jennie")
    """这是原函数的注释"""
```
Jennie()函数被作为参数传入到outer里面
Jennie.__name__：这个是获取Jennie函数的名字，在没有装饰器的情况下，名字就是Jennie，加了@outer装饰器名字就会变成inner
Jennie.__doc__：获取Jennie的注释，在没有装饰器的情况下，注释就是“这是原函数的注释”，加了@outer装饰器注释就会变成# 增加原函数执行前的相应操作，# 增加原函数执行前的相应操作
* 可以通过加上functools.wraps(),这样的话inner.__name__和Jennie.__name__就不是一个东西了Jennie（）就可以保留自己的元数据



2. 闭包
 * 特点
**能够访问外部函数内的变量**：闭包允许内部函数访问其所在作用域中的变量，即使在外部函数调用完成后，这些变量仍然可以被访问和修改。
**外部函数返回了内部函数**：通常外部函数的返回值是内部函数，这样就形成了闭包。
```python 
def create_counter():
    count = 0  # 这是一个局部变量，在外部函数中定义

    def increment_counter():
        nonlocal count  # 声明 count 不是内部函数的局部变量，而是外部函数的变量
        count += 1
        return count

    return increment_counter

# 创建一个计数器
counter = create_counter()

# 调用计数器函数
print(counter())  # 输出：1
print(counter())  # 输出：2
print(counter())  # 输出：3
```
当外部函数返回内部函数时，实际上它返回的是**内部函数的引用**，而**不是内部函数的执行结果**。这意味着每次调用外部函数时，都会创建一个新的内部函数实例，而不是重置现有的内部函数。

具体来说：

每次调用外部函数时，都会创建一个新的闭包，其中包含了外部函数的局部变量和内部函数的引用。
每个闭包都有自己独立的内部函数实例，它们共享外部函数的局部变量，但互相之间不会影响。

3. 闭包与装饰器的关系
* 共同点：
闭包和装饰器都是函数式编程中的概念。
装饰器本质上是一种闭包的应用，只不过传递的是函数。
**（此时外部函数传给内部函数的不是一个具体的值而是一个待处理函数本身）————装饰器有点像函数加工厂**
通过闭包，装饰器可以在不修改原函数定义的前提下，增加现有函数的功能。
* 闭包：
闭包是指在一个函数内部引用了外部函数定义的非全局变量。
闭包允许内部函数访问外部函数的局部变量，即使外部函数调用完成后，这些变量仍然可以被访问和修改。
闭包的经典应用是将外部函数的局部变量与内部函数关联起来，使其在多次调用过程中保持持久性。
* 装饰器：
装饰器是一种用于增强函数功能的技术。
装饰器可以在不改变原函数定义的情况下，对已有函数进行额外的功能扩展，例如计算函数运行时间、打印函数名称等。
装饰器的本质就是一个闭包，它接收一个函数作为参数，然后返回一个新的函数，通常用于修饰其他函数。
```python
def makeitalic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@makeitalic
def hello():
    return "Hello, world!"

print(hello())  # 输出：<i>Hello, world!</i>
```
在这个示例中，makeitalic 是一个装饰器，它将函数 hello 传递给内部函数 wrapper，并返回被包装后的 hello 函数。这个过程实际上就是通过闭包实现的。
