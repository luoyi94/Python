class A(object):
    def __init__(self):
        print('A.__init__')


class B(A):
    def __init__(self):
        super().__init__()
        # A.__init__(self)     # 调用父类A类里面的__init__属性
        print('B.__init__')


class C(A):
    def __init__(self):
        # super().__init__()
        A.__init__(self)       # 调用父类A类里面的__init__属性
        print('C.__init__')


# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
class D(B, C):
    def __init__(self):
        # super().__init__()
        super(B,self).__init__()    # 告诉super以B为基础继续B的下一个继承
        print('D.__init__')


# print(D.mro())  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

d = D()



