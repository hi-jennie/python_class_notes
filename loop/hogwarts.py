# iteration with list   len

"""
1.

students = ["wangxue","ldp","aobai","turkey"]

for student in students:
    print(student)
"""

students = ["wangxue","ldp","aobai","turkey"]

for i in range(len(students)):
    print(i + 1, students[i])
#range(len(students))先获得students这个列表的长度为4，将其作为参数传给range(4）
#然后循环print students[0],students[1],students[2],students[3]。由此可见，列表其实就是一个hash table，可以打印列表本身和通过索引打印列表中的内容。











