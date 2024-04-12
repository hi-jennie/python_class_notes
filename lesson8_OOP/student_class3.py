class Student:
    
    def __init__(self, name, house, gender): 
        self.name = name
        self.house = house
        self.gender = gender #instance variable
        
    def __str__(self): 
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) #和无object创建hat一样，这个方法可以在无实物Student的情况下被使用
    
def main():
    student = Student.get()
    print(student)
    
if __name__ == "__main":
    main()