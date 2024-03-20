
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