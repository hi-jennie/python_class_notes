import random

class Hat:
    houses = ["Chian","SiChuan","ChenDu"] # 相当于这是该class下所有methods都可以使用的value
    
    @classmethod
    def sort(cls, name): # cls指的是这个sort方法本身，因为他是不可访问Hat/class本身的方法，所cls相当于之前的self
        print(name,"is in", random.choice(cls.houses))


Hat.sort("Jennie")  #  @classmethod的使用使得class Hat即使没有object的情况下也可以执行print

                    # 这样如果想多次频繁使用sort方法，不用创建很多的实体的hat，只是讲Hat class作为容器来捆绑houses列表
                      