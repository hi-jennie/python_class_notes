#operator overloading————如何运用“+”将两个class加起来 重置运算符“+”，其他运算符也可以哈（相当于自定义）

class Vault:
    
    # galleons=0, sickles=0, knuts=0 表示default value
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"{self.galleons}galleons, {self.sickles}sickles, {self.knuts}knuts "
        
     # self 指的是+左边的Vault，other指的是+右边的Vault   
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        # 注意 因为是两个Vault的相加，所以返回了一个全新的Vaule
        return Vault(galleons, sickles, knuts)
 
 
Jennie = Vault(100, 50, 25)
print(Jennie)

Rustin = Vault(25, 50, 100)
print(Rustin)

total = Jennie + Rustin
print(total)


   
    