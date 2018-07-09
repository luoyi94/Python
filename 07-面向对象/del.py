class Dog:
    def __init__(self):
        self.name = "狗"

    def __del__(self):
        print("%s 要释放了" % self.name)


dog1 = Dog()
a = dog1
del dog1