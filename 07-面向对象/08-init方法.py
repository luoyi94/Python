class Dog:
    # 魔法方法(运算符重载方法) __xx__ 这样的方法都有特殊含义,在特定情况下,这样的方法,都会自动调用
    def __init__(self, name):  # init 初始化方法(构造方法) 创建完对象时,会自动调用,定义对象的属性
        self.type = "狗"
        self.name = name  # 自定义对象属性的初始值


# init 好处,对象创建出来就有相应的属性了
dog1 = Dog("旺财")
print(dog1.name)

dog2 = Dog("来福")
print(dog2.name)

