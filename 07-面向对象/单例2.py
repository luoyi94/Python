# class Singleton:
#     __instance = None
#     __has_init = False
#
#     def __new__(cls):
#         if cls.__instance is None:
#             print("创建对象")
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#     def __init__(self):
#         if not self.__hash__():
#             print("初始化")
#             self.type = "猫"
#             self.__has_init = True
#
#
# # 创建了两个对象 却只开辟了同一个内存地址
# s1 = Singleton()
# s1.type = "动漫人物"
# print(s1)
#
# s2 = Singleton()
# s1.type = "哈哈"
# print(s2)
#
#
#
# print(s1.type)


class Shoping:
    __instance = None
    __has_init = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
    def __init__(self):
        if Shoping.__has_init is False:
            self.total_price = 0
            Shoping.__has_init = True

cart1 = Shoping()
cart1.total_price = 200

