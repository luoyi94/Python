class Gear:
    def __init__(self, grear_name, area):
        self.name = grear_name
        self.area = area

    def __str__(self):
        return "家具的类型：%s,家具的占用面积：%d" % (self.name, self.area)


sofa = Gear("沙发", 2)
print(sofa)

class Home:
    """房子类"""
    def __init__(self, home_address, home_area):
        self.address = home_address
        self.area = home_area
        self.remain_area = home_area  # 房子的剩余面积
        self.gear = []

    def __str__(self):
        return "房子的地址%s,占地面积%d" % (self.address, self.area)

    def add_gear(self, gear):
        """添加家具"""
        remain_area = self.remain_area - gear.area
        if remain_area > 0:
            print("家具%s添加成功" % gear.name)
            self.gear.append(gear)
            self.remain_area -= gear.area
        else:
            print("家具%s添加失败" % gear.name)

house = Home("上南",25)


house.add_gear(sofa)


