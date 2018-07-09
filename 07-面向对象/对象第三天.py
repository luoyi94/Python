# class Dog:
#     def __init__(self):
#         self._age = None
#
#     def set_age(self, age):
#         if age  > 0:
#             self._age = age
#
#     def get_age(self):
#         return self._age
#
#     def __del__(self):
#         print("(()))))")
#
#
# dog1 = Dog()
# print(dog1.set_age(10))

# print("完成")



# 重写父类的方法
# class Dog:  # 经典类写法
#
#     def eat(self):
#         print("吃xiang")
#
#     def bark(self):
#         print("汪汪叫")
#
#
# class XTQ(Dog):  # 类名(要继承的类/基类/父类)
#
#     def eat(self):  # 子类定义和父类同名的方法, 就叫重写父类方法
#         print("吃蟠桃")
#
# # 如果有继承时 调用方法的顺序 优先当前类---> 父类 -->.. -->object
# xiantq = XTQ()
# xiantq.eat()


# 调用被重写的父类方法
# class Dog:
#     def eat(self):
#         print("吃东西")
#     def brek(self):
#         print("汪汪")
#
#
# class XTC(Dog):  # XTC继承了父类Dog的属性和方法
#     def eat(self):
#         # Dog.eat(self)  # 1，手动调用父类的方法
#         # super(XTC, self).eat()  # super(指定类, slef)指定类在继承链中的下一个类
#         super().eat()    # 一般都是用第二种 单个 多层继承
#         # print("吃蟠桃")
#
#
# XTC1 = XTC()
# XTC1.eat()  # 是可以调用父类的方法
#
# XTC1.brek()

"""
私有属性不会被继承,但是可以间接去通过调用父类的方法 取到父类私有属性的值
私有方法不会被继承,但可以间接去通过调用父类的公有方法, 间接去调用父类自己的私有方法
"""
class Dog:
    def __init__(self):
        self.__type = "狗"
        self.name = "旺财"

    def eat(self):
        # print(self)
        # print(self.__type)
        self.__info()

    def __info(self):
        print("我是私有的")


class XTQ(Dog):
    pass
    # def eat(self):
    #     pass

xiaotq = XTQ()
xiaotq.eat()
