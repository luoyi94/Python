"""
需求

定义字符串变量 name，输出 我的名字叫 小明，请多多关照！
定义整数变量 student_no，输出 我的学号是 000001
定义小数 price、weight、money，输出 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元
定义一个小数 scale，输出 数据比例是 10.00%
"""
# name = "小明"
# print("我的名字叫 %s,请多关照!" % name)
# student_no = 1
# print("我的学号是 %06d" % student_no)
# price = 9
# weight = 5
# money = price * weight
# print("苹果的单价 %.2f元/斤,购买了 %.2f斤,需要支付 %.2f元" % (price, weight, money))

"""
收银员输入 苹果的价格，单位：元／斤
收银员输入 用户购买苹果的重量，单位：斤
计算并且 输出 付款金额
"""

# # 获取用户输入的数据
# price_str = input("苹果价格:")
# weight_str = input("苹果的重量:")
#
# # 转换数据的类型
# price = float(price_str)
# weight = float(weight_str)
#
# # 数据的计算
# money = price * weight
#
# # 输出结果
# print("苹果价格: %.2f元/斤,苹果重量: %.2f斤,需要付款金额: %.2f元" % (price, weight, money))

price = float(input("请输入价格"))
weight = float(input("请输入重量:"))
money = price * weight
print("苹果的价格: %.2f,苹果的重量: %.2f,付款: %.2f" % (price, weight, money))