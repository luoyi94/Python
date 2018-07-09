class Qiang:
    """枪"""
    def __init__(self, title, power):
        self.title = title
        self.power = power
        self.bullet = 20

    def add_bullet(self):
        """加满子弹"""
        self.bullet += 20

    def shoot(self, people1):
        """射击"""
        if self.bullet == 0:
            print("没子弹了，正在添加")
            self.add_bullet()
        else:
            self.bullet -= 1
            people1.bruise(self)
        #people1受到伤害

    def __str__(self):
        return "枪支的型号:[%s]、伤害:[%d]、子弹数量[%d]" % (self.title, self.power, self.bullet)

class People:
    """玩家"""
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.gun = None
        self.state = "活"

    def fire(self, people1):
        self.gun.bullet -= 1
        if self.gun is None:
            print("你没有枪，大吼一身，吓死他")
        else:
            self.gun.shoot(people1)   # 调出开枪人的枪 使用shoot方法， （people1）受伤的人


    def bruise(self, people1):
        self.hp -= people1.power     # self为要受伤的人，people1为开枪人的枪
        if self.hp > 0:
            print("玩家%s受伤，当前血量%d" % (self.name, self.hp))
        else:
            self.hp = 0
            self.state = "go die"
            print("当前血量%d,玩家%s状态：%s" % (self.hp, self.name, self.state))

    def __str__(self):
        return "玩家：%s, 血量：%d, 状态：%s, 持有的枪：%s" % (self.name, self.hp, self.state, self.gun)


M416 = Qiang("M416", 70)

ly = People("罗伊")
tufei = People("土匪")
print(ly)
print(tufei)



ly.gun = M416
print(ly)
print(tufei)


ly.fire(tufei)


