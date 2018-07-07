# 演练需求
#
# 字符串[开始索引:结束索引:步长]

# 截取从 2 ~ 5 位置 的字符串
# 截取从 2 ~ 末尾 的字符串
# 截取从 开始 ~ 5 位置 的字符串
# 截取完整的字符串
# 从开始位置，每隔一个字符截取字符串
# 从索引 1 开始，每隔一个取一个
# 截取从 2 ~ 末尾 - 1 的字符串
# 截取字符串末尾两个字符

# 字符串的逆序（面试题）

# num_str = "0123456789"
#   -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# 步数为负数的时候 从后面开始取

# num_str_1 = num_str[:-2:-1]

# print(num_str_1)
# num_str = num_str[::-1]
# print(num_str)

# num_str_1 =  num_str[2:6]   # 切片的区间是一个 左闭右开区间
# print(num_str_1)

# num_str_1 = num_str[0:6]
# print(num_str_1)

# num_str_1 =  num_str[0:len(num_str)+1]
# print(num_str_1)

# i = 1  #控制次数 比并判断输出
# for num_str_1 in num_str:  # 用for循环遍历 字符
#     if i % 2 == 0:
#         print(num_str[0:i])  #每一次if成立 截取字符
#     i += 1


# i = 1
# for num_str_1 in num_str:
#     if i % 2 == 0:  # 先输出每隔一个字符截取字符串
#         # print(i)
#         if i == 2:  # 得到规律每次 i = 2时不输出
#             i += 1
#             continue  # 结束此次循环 而进行下此循环
#         print(num_str[0:i-1])
#     i += 1

# i = len(num_str)
# print(num_str[2:i - 1])

# i = 1
# for num_str_1 in num_str:
#     if i == 1 or i == 10:  # 执行第1次 或者第10次 才进行输出
#         print(num_str_1)
#     i += 1

# 字符串的逆序（面试题）
num_str = "0123456789"
# 逆序:9 8 7 6 5 4 3 2 1
i = len(num_str)  # 获取字符长度/个数 10
for num_str_1 in num_str:
    print(num_str[i-1:i],end="")   # 如: num_str[10-1:10] 刚好输出9
    i -= 1  # 依次减小   依次输出越来越小的索引

