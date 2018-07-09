# class Dog:
#     def eat(self):
#         print("吃%s" % self.happy)
#
#
#
# dog1 = Dog()
# dog1.happy = "嗨皮"
# dog1.eat()
#
# dog2 = Dog()
# dog2.happy = "嗨皮2"
# dog2.eat()


# class Dog:
#     def __init__(self, name):
#         self.type = "狗"
#     def __str__(self):
#         return "这个狗的名字叫： %s" % self.name
#
#
# dog1 = Dog("来福")
# print(dog1)
#
#
# dog2 = Dog("旺财")
# print(dog2.type)


class Dog:
    # 魔法方法(运算符重载方法) __xx__ 这样的方法都有特殊含义,在特定情况下,这样的方法,都会自动调用
    def __init__(self, name):  # init 初始化方法(构造方法) 创建完对象时,会自动调用,定义对象的属性
        self.type = "狗"
        self.name = name  # 自定义对象属性的初始值


# init 好处,对象创建出来就有相应的属性了
dog1 = Dog("旺财")
dog1.name
print(dog1.name)

dog2 = Dog("来福")
print(dog2.name)


