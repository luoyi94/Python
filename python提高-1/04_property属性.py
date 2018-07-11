# 定义的时候是方法  调用的时候属性的方式调用
class Foo01(object):
    def test(self):
        return 100

f = Foo01()
val = f.test()
print(val)

#############

class Foo02(object):
    @property
    def test(self):
        return 100

f = Foo02()
print(f.test)

