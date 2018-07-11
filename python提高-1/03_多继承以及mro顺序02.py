class Parent(object):
    def __init__(self, name):
        self.name = name
        print('parent的init结束被调用')

class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        self.age = age
        super().__init__(name,*args, **kwargs)
        print('Son1的init结束被调用')

class Son2(Parent):
    def __init__(self, name, gender,*args, **kwargs):
        self.gender = gender
        super().__init__(name,*args, **kwargs)
        print('Son2的init结束被调用')

class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


print(Grandson.__mro__)
g = Grandson("123", 18, "nan")
