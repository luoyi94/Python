
# 继承
# class Dog:
#     def __init__(self):
#         self.gou = "狗"
#
#
# class XTQ(Dog):     # 第一次为定义 第二次为修改
#     def __init__(self):
#         self.gou = "大黑狗"  # 默认时，用当前类属性
#         super().__init__()   # super 重写下一个父类的属性
#     # pass
#
# Dog1 = XTQ()
# print(Dog1.gou)
# print(XTQ.__mro__)  # 查看当前类的继承链   上下继承关系


# 在子类中重写父类的属性 # 子类定义和父类同名的方法, 就叫重写父类方法
# class Dog:
#     def eat(self):   # 定义父类的方法eat
#         print("吃草")
#     def bark(self):
#         print("旺旺")
#
# class XTQ(Dog):
#     def eat(self):   # 修改父类的方法eat  覆盖
#         print("吃蟠桃")
#
#
# xiaotq = XTQ()
# xiaotq.eat()






# 多继承   此类需要继承多个父类
class DOG:
    def eat(self):
        print("吃草")

class GOD:
    def eat(self):
        print("吃仙丹")


class XTQ(GOD, DOG):  # 多继承  类名（父类1, 父类2） 优先级父类1-->父类2
    pass


xiaotq = XTQ()
xiaotq.eat()
print(XTQ.__mro__)  # 从继承关系中可以看出 写在前面的也对应在前面