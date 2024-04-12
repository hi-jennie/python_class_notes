# 面向对象编程————object-oriented-programming————创建自己的date type————可以mutable或者immutable

class Student:
    #  gender=None 表示gender这个参数是optional的
    def __init__(self, name, house, gender=None): #methods 如果要存第三个名字，可以创建第三个attribute，但是最后还是将这个name以list的方式传入
        if not name:
            raise ValueError("Missing name")
        if house not in ["China","SiChuan","DeYang"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.gender = gender
    
    def __str__(self): #    相当于给object本身的一个定义，否则他会呈现object在计算机中的位置
        return "a student"
        # return f"{self.name} from {self.house}"
    # 有了__str__，在print（student）的时候就不会显示object student在计算中的位置，因为class Student本身会返回“a student”字符串
    

    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    # print（student） 如果直接打印student这个object则会打印出该object在计算机中的位置
    # 有了__str__，在print（student）的时候就不会显示object student在计算中的位置，因为class Student本身会返回“a student”字符串 

def get_student():
    
    # Student()是一个类class，相当于一个blueprint，而创建的student则是一个object，是一个物体或者载体，承载class思想的载体
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    # return student
    name = input("Name:")
    house = input("House: ")
    return Student(name,house)


if __name__ == "__main__":
    main()