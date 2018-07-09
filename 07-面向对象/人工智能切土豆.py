"""定义一个土豆  根据切了多少刀 判断输出总共有多少片"""
# 土豆
# 初始属性：土豆原始是完整的
#
# 切土豆的方法：
# 拿刀切
#
# 输出多少片
class Potato:
    def __init__(self):
        self.piace = 1

    def __str__(self):
        return "切成了%d片" % self.piace

    def sec(self, piace):
        self.piace = piace + 1


tudou1 = Potato()   # 定义一个对象 tudou1
tudou1.sec(5)       # 调用切土豆的方法 sec   并传入相应的参数  改变初始值
print(tudou1)