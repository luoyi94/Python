"""单例模式需要：通过某个类创建出来的N个对象 都是用一个内存地址"""
# 间接实现 new和init方法只执行一次


class ShoppingCart:
    __instance = None   # 标记对象是否已经创建过
    __has_init = False  # 标记有没有初始化过

    def __new__(cls, *args, **kwargs):

        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self):
        if ShoppingCart.__has_init is False:
            self.total_price = 0
            ShoppingCart.__has_init = True

cart1 = ShoppingCart()
cart1.total_price = 200
