import csv
'''1
with open("family.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",") #unpack
        print(f"{name} and {house}")
'''

'''2
students = []
with open("family.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",") #unpack
        student.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
#这个方法虽然最终也能够按照名字排序，但是是因为刚好这个句子的第一个单词是名字，如果按照house排序就无法实现  
'''    

'''3
students = []
with open("family.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",") #unpack
        student = {}
        student["name"] = name #变量name
        student["house"] = house
        #tighten:student = {"name":name, "house":house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]#也可以按照house排序

for student in sorted(students, key=get_name ):# key=lambda student:student["name"]
    print(f"{student['name']} is in {student['house']}")
'''

'''4
students = []
with open("family.csv") as file:
    reader = csv.reader(file) #csv library 在处理csv文件是可以分出，和“”
    for name,house in reader:
        students.append({"name":name,"house":house})

for student in sorted(students, key=lambda student:student["name"] ):
    print(f"{student['name']} is in {student['house']}")
'''


students = []
with open("family.csv") as file:
    reader = csv.DictReader(file) #将文件读为dict，所以这个时候需要给csv文件加上heading——cat，owner
    for row in reader:
        students.append({"name":row["cat"],"house":row["owner"]})
        #简化——students.append(row)——因为Dictreader是按照dict读取的，所以reader汇总每一个row实际都以一个dict，直接append row就可以了

for student in sorted(students, key=lambda student:student["name"] ):
    print(f"{student['name']} belongs to {student['house']}")