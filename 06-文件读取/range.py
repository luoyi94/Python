# range 主要配合for循环进行计数使用   range(开始位置，结束位置，步长)

# list_1 = range(5)  # rang(0, 5)   0,5)前闭后开区间
# print(list_1)


# list_1 = [ i for i in range(1,101)]  # 取出1~100所有的数
# print(list_1)


# 增加条件判断 ：取出生成 1~10之间偶数平方列表
# list2 = [i ** 2 for i in range(1,11) if i % 2 == 0]
# print(list2)

# list3 = ["888" for _ in range(1,9)]   # 可以不用for循环出来的数值
# print(list3)

# list4 = ["zhangsan", "lisi", "wangwu"]
# list4 = [name for name in list4 if len(name) > 4] # 输出名字长度大于4的名字
