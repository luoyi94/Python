# 使用循环语句一句话搞定
# 定义循环次数初始值
# 编写循环判断条件 + 循环语句 + 改变循环次数值

# i = 1
# while i <= 1000:
#     print("媳妇儿,我错了!")
#     i = i + 1

# 计算 0 ~ 100 之间所有数字的累计求和结果
#0 + 1 + 2 + 3 + 4 + ...... + 100
# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i = i + 1
# print("0~100之间所有数字累计和为%d" % sum)

# 计算 0 ~ 100 之间所有偶数的累计求和结果
# 0 + 2 + 4 + 6 + 8 + .... + 100
# i = 1
# sum = 0  # 记录和
# while i <= 100:
#     if i % 2 == 0:  # 判断是否为偶数, True则执行下面相加 False则不执行
#         sum = sum + i
#     i = i + 1
# print("0~100之间所有偶数的累计求和结果: %d" % sum)

# break中断  达到某一条件直接跳出当前整个循环
# i = 0
# while i < 10:
#     if i == 3:  # 循环到i == 3,就不再继续下面循环
#         break
#     print(i)
#     i += 1
# print("over")

# continue继续 达到某个条件,跳过此次循环,而继续下个循环
#
# i = 0
# while i < 10:
#     if i == 7:  # 循环到i == 7,跳过此次循环(即不执行此次循环体),而继续下一循环
#         i += 1
#         continue
#     print(i)
#     i += 1

#课堂练习:
# i = 0
# while i < 10:
#     print("错! %d" % i)
#     i += 1
# print("都是我的错")

# 求1 ~ 100累计求和
# 1 + 2 + 3 + 4 + 5 ...... + 100
# sum_num = 0
# sum_num = sum_num + 1  # 1
# sum_nem = sum_num + 2  #  3

# i = 1
# sum_num = 0
# while i <= 100:
#     sum_num = sum_num + i
#     i += 1
# print(sum_num)

#求1 ~ 100偶数求和
# 2 + 4 + 6 + 8 + 10 + ... + 100
# i = 2
# sum_num = 0
# while i <= 10:
#     sum_num = sum_num + i
#     i += 2
# print(sum_num)

# 输出
# *
# **
# ***
# ****
# *****
# 在默认情况下，print 函数输出内容之后，会自动在  内容末尾增加换行
# 如果不希望末尾增加换行，可以在 print 函数输出内容的后面增加 , end=""
# row = 1  # 行数
# while row <= 5:
#     col = 1  # 列数
#     while col <= row:
#         print("*", end="")
#         col += 1
#     row += 1
#     print()
# print("完成")

#打印乘法口诀
# \t 在控制台输出一个 制表符，协助在输出文本时 垂直方向 保持对齐，但不会换行
# \n 在控制台输出一个 换行符
# row = 1  # 行数
# while row <= 9:
#     col = 1  # 列数
#     while col <= row:
#         print("%d X %d = %d" % (col, row, row * col), end="\t")  # 向控制台输入内容后,不会换行
#         col += 1
#     row += 1
#     print()  # 单纯的换行
# print("完成")
# i = [1, 2]
# for a in i:
#     print("输入第 %d次" % a)


A0 = dict(zip(("a","b","c","d","e"),(1,2,3,4,5)))
print(A0)

A1 = range(10)
print(A1)

A2 = [i for i in A1 if i in A0]

# i:0 ~ 10 A0: 1~5
print(A2)


