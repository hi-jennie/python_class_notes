
# python方法笔记(笔记整理）

1. super() 方法
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