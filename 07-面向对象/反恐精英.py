class Gun:
    """枪支类"""
    def __init__(self, model, damage):
        self.model = model   # 枪名字
        self.damage = damage    # 枪的伤害
        self.bullet_count = 20  # 子弹数量

    def add_bullet_count(self, count):
        """添加子弹"""
        self.bullet_count += count

    def shoot(self, enemy):
        """射击"""
        if self.bullet_count == 0:
            print("没子弹了，自动加子弹")
            self.add_bullet_count(10) # 自动添加子弹
            # TODO 击中后敌人受伤
            # enemy.hurt(self)
        else:
            enemy.hurt(self)
            self.bullet_count -= 1

    def __str__(self):
        return "本枪是%s,威力为%d,子弹数量为%d" % (self.model, self.damage, self.bullet_count)


# AK74 = Gun("AK74",10)
# AK74.shoot()
# print(AK74)


class Player:
    """玩家类"""
    def __init__(self, name):
        """角色属性"""
        self.name = name   # 玩家角色
        self.hp = 100      # 血量
        self.gun = None    # 玩家拥有的枪
        self.state = "活"   # 默认是活的

    def fire(self, enemy):   # 对战玩家enemy
        """开火"""
        if self.gun is None:
            print("玩家%s没有枪，无法射击" % (self.name))
        else:  # 有枪
            self.gun.shoot(enemy)  # 使用自己的枪self.gun这是一个枪对象,调用shoot 射击


    def hurt(self, enemy_gun):  # self为要被伤害的  enemy为开枪射击的玩家
        """敌人受伤"""
        self.hp -= enemy_gun.damage  # 自己血量是减敌人枪的伤害值
        if self.hp <= 0:
            self.hp = 0   # 挂了就是0血量  不让它显示负数血量
            self.state = "挂了"
            print("玩家%s死亡" % self)
        else:
            print("玩家%s受到了%d点伤害, 剩余%d" % (self.name, enemy_gun.damage,self.hp))

    def __str__(self):
        return "玩家：%s, 状态:%s, 血量:%d, 所持枪:%s" % (self.name,self.state, self.hp, self.gun)


ak74 = Gun("Ak74", 50)
m24 = Gun("m24", 100)

player1 = Player("policemen")
player2 = Player("bandit")

print(player1)
print(player2)



player1.gun = ak74

player1.fire(player2)
print(player1)
print(player2)