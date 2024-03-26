
# python方法笔记(笔记整理）

1. **super() 方法**
是用于调用父类（超类）的一个方法。它在解决多重继承问题时非常有用。当我们使用单继承时，直接使用类名调用父类方法没有问题。但是如果涉及到多重继承，就会涉及到查找顺序（MRO，Method Resolution Order）和重复调用（钻石继承）等问题。
具体来说：
    * super() 方法用于解决多重继承中的调用问题。
    * 它可以直接调用父类的方法。
    * 在 Python 3 中，我们可以直接使用 super().method_name 来调用父类的方法，而不需要显式地指定父类名。
    * 在 Python 2 中，我们需要使用 super(Class, self).method_name 的形式来调用。
以下是一个示例，展示了如何使用 super() 方法：
```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):#表示Child是Parent的子类
    def greet(self):
        super().greet()  # 调用父类的 greet 方法
        print("Hello from Child")

child = Child()
child.greet()
```
执行结果：
Hello from Parent
Hello from Child

在这个示例中，Child 类继承自 Parent 类。通过 super().greet()，我们成功调用了父类的 greet 方法。

2. **join()方法**
join() 函数在 Python 中用于将序列中的元素以指定的字符连接生成一个新的字符串。这是一个非常有用的方法，特别是在处理字符串、列表或元组时。让我们详细了解一下 join() 的用法和参数：
    
    - **对列表进行join。tuple，dict也同理，但是dict合并的是key**
    ```python
    seq1 = ['hello', 'good', 'boy', 'doiido']
    print(' '.join(seq1))  # 输出：hello good boy doiido
    print(':'.join(seq1))  # 输出：hello:good:boy:doiido
    ```

    - **对字符串进行操作：**

    ```python
    seq2 = "hello good boy doiido"
    print(':'.join(seq2))  # 输出：h:e:l:l:o: :g:o:o:d: :b:o:y: :d:o:i:i:d:o
    ```
3. **sorted() 方法**
    * 基本排序：
    使用 sorted() 函数可以轻松地对列表进行升序排序。**它返回一个新的排序后的列表**：
    ```python
    numbers = [5, 2, 3, 1, 4]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)  # 输出：[1, 2, 3, 4, 5]

    a = [5, 2, 3, 1, 4]
    a.sort()
    print(a)  # 输出：[1, 2, 3, 4, 5]。直接修原始列表
    ```

    * 自定义排序
    使用 key 参数可以指定一个函数，该函数将在比较之前应用于每个列表元素。例如，按年龄对学生进行排序：
    ```python
    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10)
    ]
    sorted_students = sorted(student_tuples, key=lambda student: student[2]) #student指的是每一行tuple，student[2]指按第三位数字排序
    print(sorted_students)
    # 输出：[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    ```

    * 对字典进行排序
    1. **按键（key）排序**：
    ```python
    def sort_by_key():
    key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
    print("按键（key）排序:")
    for i in sorted(key_value):#直接sorted dict就可以了
        print((i, key_value[i]), end=" ")

    def main():
        sort_by_key()

    if __name__ == "__main__":
        main()
    ```

    2. **按值（value）排序**(注意：按照value拍，第一个参数需要列出dict的items)
    ```python
    def sort_by_value():
    key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
    print("按值（value）排序:")
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))

    def main():
        sort_by_value()

    if __name__ == "__main__":
        main()
    ```
    输出结果为：按值（value）排序: [(1, 2), (5, 12), (6, 18), (4, 24), (2, 56), (3, 323)]

    在这个代码片段中，(kv[1], kv[0]) 是一个排序键，用于指定如何对字典中的项进行排序。让我解释一下：

    key=lambda kv: (kv[1], kv[0]) 部分是一个排序函数，它告诉 Python 如何比较字典中的项。（同理下面的age和name）
    kv[1] 表示字典项的值，而 kv[0] 表示字典项的键。
    因此，(kv[1], kv[0]) 的含义是：首先按照值（value）进行排序，如果值相同，则按照键（key）进行排序。这样可以确保在排序时，如果值相等，那么按照键的顺序来排列。
   示例中，sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])) 将字典 key_value 按照值升序排序，如果值相同，则按照键升序排序。这就是为什么输出结果是按值排序的。


    3. 按值（value）和键（key）排序：
    ```python
    lis = [
    {"name": "Taobao", "age": 100},
    {"name": "Runoob", "age": 7},
    {"name": "Google", "age": 100},
    {"name": "Wiki", "age": 200},
    ]

    # 先按 age 升序排序，再按 name 排序
    print("列表通过 age 和 name 排序:")
    print(sorted(lis, key=lambda i: (i["age"], i["name"])))

    # 按 age 降序排序
    print("列表通过 age 降序排序:")
    print(sorted(lis, key=lambda i: i["age"], reverse=True))
    ```
    输出结果为：
    列表通过 age 和 name 排序: [{‘name’: ‘Runoob’, ‘age’: 7}, {‘name’: ‘Google’, ‘age’: 100}, {‘name’: ‘Taobao’, ‘age’: 100}, {‘name’: ‘Wiki’, ‘age’: 200}]
    列表通过 age 降序排序: [{‘name’: ‘Wiki’, ‘age’: 200}, {‘name’: ‘Taobao’, ‘age’: 100}, {‘name’: ‘Google’, ‘age’: 100}, {‘name’: ‘Runoob’, ‘age’: 7}]


4. **enumerate() 函数**
是Python的内置函数之一，它可以将一个可迭代对象转化为一个枚举对象，返回的枚举对象包含了索引和值。默认索引值从0开始，可以用第二个参数start=d改变

```python
# 示例1：遍历列表并获取索引和值
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for index, value in enumerate(seasons):
    print(f"Season {index}: {value}")

# 示例2：从1开始的索引
for index, value in enumerate(seasons, start=1):
    print(f"Season {index}: {value}")
```


5. product()方法——有点类似多个iterable的打包工具 from itertools import product
product(*iterables, repeat=1)  repeat 参数（可选）表示元素的重复次数。

```python
对列表获取多个无穷循环器的笛卡尔积：
a = ['a', 'b', 'c']
b = [1, 2, 3]
for i, j in itertools.product(a, b):
    print(i, j)

对元组获取多个无穷循环器的笛卡尔积
c = ('e', 'f', 'g')
d = (4, 5, 6)
for i, j in itertools.product(c, d):
    print(i, j)

对字典获取多个无穷循环器的笛卡尔积：
e = {'青鸟': '最美', '世子': '纨绔'}
j = {'xiaofeng': '1', '废物': '2'}
for i, j in itertools.product(e, j):
    print(i, j)  # 字典只对键进行笛卡尔积交换

```


6. islice()方法 from itertools import product
islice() 函数位于 Python 的 itertools 模块中，用于对可迭代对象进行切片操作
    **功能**：
    islice() 函数用于从迭代器中获取指定范围的元素，类似于切片操作。
    它允许你灵活地截取迭代器中的一部分数据，而不需要将整个迭代器加载到内存中。
    **语法**：
    itertools.islice(iterable, start, stop[, step])
    iterable：表示需要进行切片的可迭代对象。
    start：表示开始切片的索引，如果为 None，则从序列开头开始。
    stop：表示切片截止的索引，如果为 None，则切片到序列末尾。
    step：表示步长，默认为 1。
    islice() 不支持负值的 start、stop 或 step。
    它适用于从内部结构已被展平的数据中提取相关字段，例如从多行报告中每隔几行列出一个名称字段。

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
iter_my = iter(my_list)
for i in islice(iter_my, 0, None, 2):
    print(i)
```
在上面的示例中，islice(iter_my, 0, None, 2) 表示从第一个元素开始，到最后一个元素，以步长 2 进行切片输出，结果是：0 2 4 6 8。


7. takewhile()方法

itertools.takewhile() 是 Python 中的一个函数，它允许你从一个序列中获取项目，直到指定的条件首次变为 False。让我们来看看这个函数的用法和示例：
语法：takewhile(predicate, iterable)
predicate 是一个内置函数或用户自定义的函数，甚至可以是 lambda 函数。
iterable 是一个可迭代对象，通常是列表或字符串。
这个函数的作用是在满足指定条件的情况下，从可迭代对象中取出元素，直到条件首次变为 False。它属于“终止迭代器”类别，因为它的输出不能直接使用，通常需要转换为其他可迭代形式，比如列表。

```python
#假设我们有一个整数列表，我们只想保留其中的偶数。我们可以使用 takewhile() 来实现
from itertools import takewhile

def even_nos(x):
    return x % 2 == 0

li = [0, 2, 4, 8, 22, 34, 6, 67]
new_li = list(takewhile(even_nos, li))
print(new_li)  # 输出：[0, 2, 4, 8, 22, 34, 6]


#假设我们有一个包含数字和字母的字符串，我们需要提取连续的数字部分。我们可以这样做：

from itertools import takewhile

def test_func(x):
    return x.isdigit()

for i in takewhile(test_func, "11234erdg456"):
    print("Output:", i)
# 输出：
# Output: 1
# Output: 1
# Output: 2
# Output: 3
# Output: 4
```

8. **chain()方法**  from itertools import chain
itertools.chain() 是 Python 中的一个函数，用于将多个可迭代对象连接在一起，形成一个新的可迭代对象。这个新的可迭代对象可以逐个访问原始可迭代对象中的元素。

以下是关于 itertools.chain() 的用法和示例：

基本用法： 

```python
#1——假设我们有两个列表 a 和 b，我们想要将它们连接在一起。我们可以使用 itertools.chain() 来实现这个目标：
from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)
# 输出：1 2 3 4 x y z


#2——使用 chain() 的一个常见场景是当你想对不同的集合中的所有元素执行某些操作时。例如，我们可以使用 chain() 来处理活动项目和非活动项目：
# 假设有一些活动和非活动的项目
active_items = set()
inactive_items = set()

# 遍历所有项目
for item in chain(active_items, inactive_items):
    # 处理项目
    pass


##3——使用 lambda 函数： 你也可以使用 lambda 函数来指定条件，例如提取直到遇到某个特定元素为止：
st = "GeeksforGeeks"
li = list(chain(takewhile(lambda x: x != 's', st)))
print(li)
# 输出：['G', 'e', 'e', 'k']
```


9. zip_longest()

itertools.zip_longest 是 Python 中的一个函数，它位于 itertools 模块中。这个函数的作用类似于内置的 zip 函数，但有一些不同之处。
功能：
zip_longest 函数用于将多个迭代器中的元素一一对应地打包成元组。
与 zip 函数不同的是，当最短的输入迭代器耗尽时，zip_longest 可以使用填充值来填充缺失的值。
参数：
必传参数：iterables，包含输入迭代器的可迭代对象。
可选参数：fillvalue，用于填充缺失值的对象，默认为 None。

```python
import itertools

# 示例数据
numbers = [1, 2, 3]
letters = ['a', 'b', 'c', 'd']

# 使用 zip_longest 打包元素
for item in itertools.zip_longest(numbers, letters, fillvalue=None):
    print(item)
```


10. file.read()方法
在 Python 中，你可以使用 while 循环和 read() 方法来分块读取文件。这对于处理大文件或避免内存不足非常有用。如果文件没有换行，这种方法相当于手动换行，接受的参数相当于每次读取的步长。

首先，让我们看一下如何使用 read() 方法分块读取文件。以下是一个示例代码：
```python
with open("data.csv", "r", encoding="utf-8") as file:
    chunk_size = 10  # 每次读取的行数
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        # 对 chunk 进行数据处理
        print(chunk)
```
在这个示例中，我们打开了名为 data.csv 的文件，每次读取 10 行数据，并对每个数据块进行处理。


11. partial ()方法 from functool 
在 Python 中，partial 函数允许我们固定某个函数的一部分参数，从而生成一个新的函数。这对于处理大文件、简化回调、参数固定和代码重用非常有用。让我们来详细了解一下 partial 函数的
```python
#示例1
from functools import partial

def f(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x

g = partial(f, 3, 1, 4)
print(g(5))  # 输出：3145

#示例2
from functools import partial

def add(a, b, c):
    return 100 * a + 10 * b + c

add_part = partial(add, c=2, b=1)
print(add_part(3))  # 输出：312

```

12. @lru_cache 装饰器
在 Python 中，你可以使用 @lru_cache 装饰器来实现缓存功能，从而提高函数的性能。这个装饰器使用**最近最少使用（LRU）**策略，将函数的结果缓存起来，避免重复计算。**第二次使用同样的参数调用函数，他会直接将上次计算后的结果缓存起来，避免再次出发计算逻辑。**
```python 
from functools import lru_cache

@lru_cache(maxsize=None)  # maxsize 参数决定缓存的大小
def expensive_calculation(n):
    # 假设这里有一个昂贵的计算
    return n * n

result1 = expensive_calculation(5)  # 第一次计算
result2 = expensive_calculation(5)  # 直接从缓存中获取结果

print(f"结果1: {result1}")
print(f"结果2: {result2}")

```
使用 @lru_cache 可以优化递归函数、I/O 密集型操作、数据库查询等。
注意：@lru_cache 只在同一个 Python 进程中有效，不适用于多个子进程或多次运行相同脚本的情况。
通过使用 @lru_cache，你可以有效地提高函数的性能，避免不必要的计算，从而优化你的 Python 代码。

13.functools.wraps() 
functools.wraps 是 Python 中的一个装饰器，用于保留被装饰函数的元数据。让我们深入探讨一下它的作用和实现。

作用：
@wraps(func) 的主要目的是**消除装饰器对原函数造成的影响**，确保被装饰的函数保留原来的函数名和文档字符串。
**当一个函数被修饰时，它的 __name__ 属性将保持为装饰器函数的名字，而不是被修饰函数的名字**.
实现：
```python 假设我们有一个装饰器，它记录函数的执行时间：
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def slow_function():
    # Simulate a time-consuming operation
    time.sleep(2)
    print("Slow function executed.")

slow_function()
print(f"Function name after decoration: {slow_function.__name__}")

```
在这个例子中，timing_decorator 是一个装饰器，它测量被装饰函数的执行时间并打印出来。我们使用 @wraps(func) 来确保被装饰的函数 slow_function 保留了原来的函数名和文档字符串。如果我们不使用 @wraps，slow_function 的 __name__ 属性将变成 wrapper，而不是我们期望的 slow_function。

运行上述代码，你会看到类似以下的输出：

Slow function executed.
Function 'slow_function' took 2.0003 seconds to execute.
Function name after decoration: slow_function

14. reduce 函数
reduce 是 Python 内置的高阶函数之一，用于将一个二元操作函数（接受两个参数）应用于序列的元素，从而将序列归约为单一的值1.
它的主要目的是对数据集合（链表、元组等）中的所有数据进行累积操作。具体来说，**reduce 会先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用函数运算，最终得到一个结果**
```python
#假设我们有一个列表 [1, 2, 3, 4, 5]，我们想计算它们的和。我们可以使用 reduce 来实现这个目标：


from functools import reduce

def add(x, y):
    return x + y

result = reduce(add, [1, 2, 3, 4, 5])
print("列表和:", result)  # 输出：15

#另一种使用匿名函数的方式：


result_lambda = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print("使用 lambda 匿名函数:", result_lambda)  # 输出：15
```

15. group 函数：
在 Python 中，正则表达式的 group 和 groups 方法是非常有用的函数，用于处理匹配结果的分组信息。

**group 函数**：
group 方法是 re.MatchObject 类中的一个函数，用于返回匹配对象的整个匹配结果或特定的分组匹配结果。
当 group 方法不带参数时，它将返回整个匹配结果。
例如，以下代码将匹配字符串中的数字和字母，并返回整个匹配结果：
```python
import re
text = "abc123def456"
pattern = "\\w+"
match = re.search(pattern, text)
print(match.group())
```
这段代码将输出：abc123def456。在这个例子中，正则表达式 \\w+ 匹配了整个字符串中的所有数字和字母，group 方法返回了整个匹配结果。

group 方法还可以用于返回指定分组的匹配结果。每个分组都可以通过小括号括起来，用于将匹配结果分成多个组。例如，以下代码将匹配字符串中的数字和字母，并返回匹配到的第一个数字和字母：
```python
text = "abc123def456"
pattern = "(\\d+) (\\w+)"
match = re.search(pattern, text)
print(match.group(1))  # 输出：123
print(match.group(2))  # 输出：def
```
在这个例子中，正则表达式 (\\d+) (\\w+) 匹配了字符串中的一个或多个数字和字母。(\\d+) 匹配了一个或多个数字，(\\w+) 匹配了一个或多个字母。
当正则表达式没有匹配到字符串中的任何内容时，调用 group 方法将会抛出 AttributeError 异常。因此，在调用 group 方法之前，应该先使用 re.search 等方法进行匹配，并使用返回值检查是否有匹配结果。

**groups 函数**：
groups 方法是 re.MatchObject 类的一个函数，用于返回所有分组匹配结果组成的元组。
该方法不接受任何参数。
例如，以下代码将匹配字符串中的电话号码，并返回其中的区号和电话号码：
```python
text = "My phone number is (123)456-7890"
pattern = r"(\d{3}) (\d{3}-\d{4})"
match = re.search(pattern, text)
print(match.groups())  # 输出：('123', '456-7890')
```

16. map() 和 filter()
**map() 函数**：
功能：map() 函数用于映射，将一个序列的每个元素映射到指定的函数中，然后返回一个迭代对象。
使用格式：map(function, iterable...)
示例：
```python
def square(x):
    return x**2

# 使用map将square函数应用到列表中的每个元素
result = list(map(square, [1, 2, 3]))
print(result)  # 输出：[1, 4, 9]

# 也可以使用匿名函数lambda
result_lambda = list(map(lambda x: x**2, [1, 2, 3]))
print(result_lambda)  # 输出：[1, 4, 9]
```
注意：要使用list()将迭代对象转换为列表。


**filter() 函数**：
功能：filter() 函数用于过滤，将一个序列的每个元素映射到指定的函数中，返回结果为 True 的元素。
使用格式：filter(function, iterable...)
示例：
```python
# 过滤出能被2整除的元素
filtered_result = list(filter(lambda x: x % 2 == 0, [1, 2, 3]))
print(filtered_result)  # 输出：[2]
```
17. itemgetter()： 用于从序列（如列表、元组、字典等）中获取指定的元素。

    功能：
    itemgetter() 用于从序列中获取指定的元素。
    它可以根据索引或键来提取元素。
    如果提取的是多个值，函数会将它们放在一个元组中返回。

    使用格式：
    itemgetter(item) 或 itemgetter(*item)
    参数可以是序列中的索引或键。


```python
# 1.从列表中获取元素
import operator

sampleList = ["macOS", "Windows", "Linux"]
# 获取索引为2的元素
result = operator.itemgetter(2)(sampleList)
print(result)  # 输出：Linux

# 2.从字典中获取键对应的值：

sampleDict = {'Product': 'iPhone 13 Pro Max', 'Company': 'Apple'}
# 获取键为'Product'的值
result_dict = operator.itemgetter('Product')(sampleDict)
print(result_dict)  # 输出：iPhone 13 Pro Max

# 3.对字典列表按键排序：

phones = [
    {'PhoneName': 'Apple', 'PhonePrice': 113000},
    {'PhoneName': 'Samsung', 'PhonePrice': 109999},
    {'PhoneName': 'OnePlus', 'PhonePrice': 69000}
]
# 按照'PhoneName'键排序
sorted_phones = sorted(phones, key=operator.itemgetter('PhoneName'))
print(sorted_phones)
# 输出：[{'PhoneName': 'Apple', 'PhonePrice': 113000},
#        {'PhoneName': 'OnePlus', 'PhonePrice': 69000},
#        {'PhoneName': 'Samsung', 'PhonePrice': 109999}]
```


