class Meat:
    """肉类"""
    def __init__(self):
        self.name = "肉"

class Ham(Meat):
    """火腿"""
    def __init__(self):
        super().__init__()
        self.name = "火腿"


class SweetPotato:
    """地瓜"""
    def __init__(self):
        self.name = "地瓜"
        pass

class People:
    """人"""
    def eat(self, meat):
        print("我要吃%s" % meat.name)


m1 = Meat()
h2 = Ham()  # h2.name = "火腿"
people1 = People()
people1.eat(h2)  # h2.name  对应上面的Ham类