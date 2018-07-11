class Money(object):
    a = 1
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if value >= 0:
          self.__money = value
          print("修改成功")
        else:
            print("error:请存放正确的数值")

    def print_price(self):
        print("调用删除")

    money = property(getMoney, setMoney, print_price)

# m = Money()
# val = m.getMoney()
# print(val)
#
# m.setMoney(100)

# m = Money()
#
# print(m.money)
#
# m.money = 100
#
#
# del m.money



