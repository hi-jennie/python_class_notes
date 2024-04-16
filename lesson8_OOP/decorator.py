class Bmi():

    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.height / (self.height ** 2)

    @property
    def bmi2(self):
        return self.eight / (self.height ** 2)

Jennie = Bmi("Jennie",1.6,43)

#  其实是在调用bmi函数
print(Jennie.bmi())

# 通过属性的方式查看
print(Jennie.bmi2)