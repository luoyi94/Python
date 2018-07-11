class Money(object):
    def __init__(self):
        self.money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if value >= 0:
            self.__money = value
        else:
            print("钱不能存负数")

    money1 = property(getMoney, setMoney)


m = Money()
print(m.money)

m.money1 = 100
print(m.money1)