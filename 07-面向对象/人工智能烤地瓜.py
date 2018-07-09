class SweetPotato:
    def __init__(self):
        """地瓜类的属性"""
        self.state = "生的"
        self.coking_time = 0


    def __str__(self):
        """输出地瓜信息"""
        return "烧烤状态%s,烧烤总时间%d" % (self.state, self.coking_time)

    def cook(self, time):
        """烧烤方法"""

        self.coking_time += time     # 烧烤总时间
        if 0 <= self.coking_time < 3:
            self.state = "生的"
        elif 3 <= self.coking_time < 6:
            self.state = "半生不熟"
        elif 6 <= self.coking_time < 8:
            self.state = "熟了"
        else:
            self.state = "烤糊了"


tudou1 = SweetPotato()
tudou1.cook(10)
print(tudou1)