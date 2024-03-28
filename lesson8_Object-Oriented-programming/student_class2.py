#在class 类里面创建function method


class Student:
    
    def __init__(self, name, house, gender): 
        if not name:
            raise ValueError("Missing name")
        if house not in ["China","SiChuan","DeYang"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.gender = gender #instance variable
        
    def __str__(self): 
        return f"{self.name} from {self.house}"
    
    def gender_identify(self): # 可以在class里面写入一些自己定义的功能性函数
        match self.gender:
            case "female":
                return "👩🏼"
            case "male":
                return "👨‍🦰"
            case _:
                return "👶"
    
    @property  #作用是将def house装置称为setter
    #setter        
    def house(self):
        return self._house # 直接叫self.house会和instance variable 重叠，所以加一个_
    
    @house.setter
    # getter
    def house(self,house):
        # 这里的error check可以保证及时调用方即使在讲student。house修改为Chendu的情况下也可以raise ValueError
        
        if house not in ["China","SiChuan","DeYang"]: 
            raise ValueError("Invalid house ")
        self._house = house
    
def main():
    student = get_student()
    student.house = "ChenDu" # 通过这样的方式，调用class的人可以修改student这个boject里面的值，这样会比较危险,修改后的house.setter可以阻止这个行为
    # 注意：student.house 后面如果没有根“=”，那么他会直接调用（getter）student的instance variable————self._house
    #但是，如果student.house后面跟了“=”，计算机就会自动识别这是在重置setstudent.house的值，就会去找student类里面student.house的setter并阻止其修改行为
    print(f"{student.name} from {student.house}")
    print(student.gender_identify()) # 通过这样的方式调用自己定义的功能性函数
    
def get_student():
    name = input("Name:")
    house = input("House: ")
    gender = input("gender: ")
    return Student(name,house,gender)

main()