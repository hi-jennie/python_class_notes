# 2024.4.15 oriented object programmaing
1. 面向对象的结构
* 变量
* 函数
* __通过类名操作类__
* __通过对象操作类__
* 一个类可以实例化为多个对象
```python
class JenNie():
    name = "Jennie"
    
    def print_(self):
        print("24")

J = JenNie()
del J.name

print(J.name)  
# 并没有在类里面找到Jennie

```