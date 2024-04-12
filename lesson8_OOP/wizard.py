
#inheritance————子类、父类的继承关系（parant class/super class

class wizard():
    def __init__(self, name):
        if not name:
            raise ValueError("Miassing name")
        self.name = name

class student(wizard):
    def __init__(self, name, house):
        # super.是访问该class对于的父类方法
        super.__init__(name)
        self.house = house
        
class professor(wizard):
    def __init__(self, name, position):
        super.__init__(name)
        self.position = position