
# 需求
#
# 定义一个整数变量记录年龄
# 判断是否满 18 岁 （>=）
# 如果满 18 岁，允许进网吧嗨皮


# age = int(input("年龄："))
# if age >= 18:
#     print("可以进网吧嗨皮......")
# else:
#     print("未成年人，禁止入内！")

# num = int(input("请输入数字："))
# if num != 0:
#     print("数字非零")
# else:
#     print("数字为零")
# print("结束")

# 逻辑运算演练
#
# 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确 要求人的年龄在 0-120 之间
# age = int(input("请输入你的年龄："))
# if age>0 and age<120:
#     print("你的年龄是 %d 岁" % age)
# else:
#     print("请正确输入年龄！")

# 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩要求只要有一门成绩 > 60 分就算合格
# python_score = int(input("请输入Python成绩："))
# c_score = int(input("请输入C语言成绩："))
# if python_score > 60 or c_score > 60:
#     print("恭喜你！及格了")
# else:
#     print("没及格！滚去学习")

# 练习3: 定义一个布尔型变量 is_employee，编写代码判断是否是本公司员工如果不是提示不允许入内

# is_employee = True
# if is_employee:
#     print("欢迎光临!")
# else:
#     print("不允许入内")

# 需求
#
# 定义 holiday_name 字符串变量记录节日名称
# 如果是 情人节 应该 买玫瑰／看电影
# 如果是 平安夜 应该 买苹果／吃大餐
# 如果是 生日 应该 买蛋糕
# 其他的日子每天都是节日啊……
# holiday_name = str(input("请输入节日："))
# if holiday_name == "情人节":
#     print("买玫瑰")
#     print("看电影")
# elif holiday_name == "平安夜":
#     print("买苹果")
#     print("吃大餐")
# elif holiday_name == "生日":
#     print("买蛋糕")
# else:
#     print("其他每天都是节日……")

# 需求
#
# 定义布尔型变量 has_ticket 表示是否有车票
# 定义整型变量 knife_length 表示刀的长度，单位：厘米
# 首先检查是否有车票，如果有，才允许进行 安检
# 安检时，需要检查刀的长度，判断是否超过 20 厘米
# 如果超过 20 厘米，提示刀的长度，不允许上车
# 如果不超过 20 厘米，安检通过
# 如果没有车票，不允许进门

# has_ticket = True
# knife_length = 50
#
# if has_ticket:
#     print("有车票，可以安检")
#     if knife_length > 20:
#         print("刀的长度%sCM,不允许上车" % knife_length)
#     else:
#         print("通过")
# else:
#     print("没车票，回去补票")