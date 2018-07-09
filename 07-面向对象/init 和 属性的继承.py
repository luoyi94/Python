# 属性和方法都是可以被子类调用的
class Dog:
    def __init__(self):
        self.name = "狗"


class XTQ(Dog):
    def __init__(self):
        self.name = "大黑狗"  # 第一此为定义
        # 调用父类的方法
        super().__init__()  # 第二次为修改

        self.color = "black"


xiaotq = XTQ()
print(xiaotq.name)
print(xiaotq.color)