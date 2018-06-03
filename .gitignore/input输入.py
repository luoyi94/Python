# 需求
#
# 收银员输入 苹果的价格，单位：元／斤
# 收银员输入 用户购买苹果的重量，单位：斤
# 计算并且 输出 付款金

# price = float(input("请输入苹果单价："))
# weight = float(input("请输入苹果重量："))
# money = price * weight
# print(money)

# 需求
#
# 在控制台依次提示用户输入：姓名、公司、职位、电话、邮箱
# 按照以下格式输出：
# **************************************************
# 公司名称
#
# 姓名 (职位)
#
# 电话：电话
# 邮箱：邮箱
# *************************************************

name = str(input("姓名："))
company = str(input("公司："))
position = str(input("职位："))
phone = str(input("电话："))
email = str(input("邮箱："))

print("*" * 50)
print("%s\n" % company)
print("%s(%s)\n" % (name,position))
print("电话：%s" % phone)
print("邮箱：%s" % email)
print("*" * 50)