
# 元组 使用

# 基本定义            ***元组只有  查询, 和遍历的操作
# tuple1 = (1,2)
# 输出元素的值
# print(tuple1[1])

# 元组中只包含一个元素时,需要在元素后面添加逗号
# tuple2 = (1,)  # 如果不在后面添加逗号，则会自动推导 输出为实际类型而不是元组类型 报错
# print(tuple2[0])

# 元组应用
# 自动组包的默认类型是元组

# 给变量赋值时，如果值有多个，会自动组包（把多个字符转换成元组）
# a = 10, 20, 40
# print(a)
# print(type(a))

# 交换变量的值
# 如果左边变量 和 右边的变量 的个数是相同的  会自动解包  依次分别赋值给左边
# a = 10
# b = 20
# c = 30
# 要求:交换 a b 的值
# a, b = b, a  # 右边的赋值给左边    = 号的右边是自动组包成(b, a)
# print(a)
# print(b)
# a的值给b b的值给c c的值给a

# b, c, a = a, b, c
# print(a)
# print(b)
# print(c)

# 常规编写
# i = a
# a = b
# b = i
# print(a, b)

# 格式字符串
# people_1 = ("张三", 18)  # 当多个字符串需要格式化输出时 % () 括号即为打包成元组
# print("我是 %s,今年%s岁" % people_1)

# 元组中的元素为列表本身时
# list2 = [4, 6, 7]
# list1 = [1, 2, 3, 4, list2]
# tuple = (6, list1)

# 输出的是所有元组中元素的本身
# print(tuple)

# 增加元组中列表的元素  修改的是为列表的值与元组无关
# list1.append(20)
# print(tuple)

# 可以用  元组名[索引] 取出对应数据   -- 这里特殊的是  索引为1的元素是列表
# tuple[1].append(10)  # 增加元组内对应索引(列表)中的元素
# print(tuple)

# 元组与列表之间的转换

# 列表  →→   元组
# list_1 = [45, 8, 45, 12]
# tuple_1 = tuple(list_1)
# print(type(tuple_1))
# print(tuple_1)

# 元组 →→   列表
# tuple_1 = (10, 21, 15, 16, 14)
# list_1 = list(tuple_1)
# print(type(list_1))
# print(list_1)
#
# tuple_2 = tuple(tuple_1)
# print(type(tuple_2))
# print(tuple_2)