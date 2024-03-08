# iteration with list   len

"""
#1.

students = ["wangxue","ldp","aobai","turkey"]

for student in students:
    print(student)

#2.
students = ["wangxue","ldp","aobai","turkey"]

for i in range(len(students)):
    print(i + 1, students[i])
#range(len(students))先获得students这个列表的长度为4,将其作为参数传给range(4)
#然后循环print students[0],students[1],students[2],students[3]。由此可见,列表其实就是一个hash table，可以打印列表本身和通过索引打印列表中的内容。

"""

"""
students = {
    "wangxue":"chengdu",
    "ldp":"chengdu",
    "aobai":"chengdu",
    "turkey":"America", 
    }

#for student in students:
#    print(student)
#这种情况不会打印整个students dict.而是只打印其中的key。所以默认打印的其实是key

for student in students:
    print(student,students[student],sep=",")

"""
# 每个人都是一个dict，list里面插入dict

students = [
    {"name": "wangxue", "house": "chengdu", "age": "24"},
    {"name": "ldp", "house": "chengdu", "age": "28"},
    {"name": "aobai", "house": "chengdu", "age": "2"},
    {"name": "Turkey", "house": "America", "age": "2"},
]

for student in students:
    print(student["name"], student["house"], student["age"], sep=",")
