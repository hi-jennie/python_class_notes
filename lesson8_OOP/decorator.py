from collections import namedtuple

def count_average_score():
    # 获取学生数量和学生信息的字段名
    student_number = int(input())
    Student = namedtuple('Student', input().split())

    # 获取所有学生的信息
    students = [Student(*input().split()) for _ in range(student_number)]

    # 计算平均分数
    marks = [int(student.MARKS) for student in students]
    print(sum(marks) / len(marks))