class Foo01(object):
    def test(self):
        return 100


# f = Foo01()
# val = f.test()
# print(val)



###########
# 定义的时候是 方法，调用的时候通过属性的方式去调用


class Foo02(object):
    @property
    def test(self):
        return 100

# f = Foo02()
# print(f.test)








