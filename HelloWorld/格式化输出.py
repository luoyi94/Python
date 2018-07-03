"""
定义变量保持小明的个人信息
姓名：小明
年龄：18岁
性别：是男生
身高：1.75米
体重：75.0公斤
"""
# 定义变量
name = "小明"
age = 18
sex = "男"
height = 1.75
weight = 75
print("我的名字是 %s,年龄 %d岁,性别 %s,身高 %.2fM,体重 %.1f公斤." % (name, age, sex, height, weight))

# 需求
#
# 定义字符串变量 name，输出 我的名字叫 小明，请多多关照！
# name = "小明"
# print("我的名字叫 %s，请多关照！ " % name)

# 定义整数变量 student_no，输出 我的学号是 000001
# student_no = 1
# print("我的学号是 %06d" % student_no)

# 定义小数 price、weight、money，输出 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元
price = 9
weight = 5
money = 45
print("苹果单价 %.02f元/斤，购买了 %.02f斤，需要支付 %.02f元" % (price,weight,money))

# 定义一个小数 scale，输出 数据比例是 10.00%
# scale = 10
# print("数据比例是%.02f%%" % scale)

