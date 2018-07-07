#定义一个列表
list1 = [10, 20, 30, 40, 50, 25]
# 索引    0   1   2   3   4    下标

# 列表基础 从列表中取出值
# print(list1[3])

# 取值时 如果超出索引范围,程序就会报错
# print(list1[5])  # 索引最大为4 没有5 会报错 out of range超过范围

# 列表常用操作 增 删 改 查

# 1,增加
# *重点(1)格式: 列表.append(数据)  作用:默认在末尾增加数据
# list1.append(300)
# print(list1)

# (2)格式: 列表.insert(索引,数据)  作用:在指定位置增加数据
# list1.insert(0,500)
# print(list1)

# (3)格式: 列表.extend(iterable)可将迭代对象中的元素追加到列表

# 2,删除
# (1)格式: del 列表[索引]  作用:删除指定索引的数据
# del list1[0]
# print(list1)

# *重点(2)格式: 列表.remove(数据) 作用:默认删除第一个指定的数据
# list1.remove(5)
# print(list1)

# (3)格式: 列表.pop() 作用:默认删除末尾数据,返回被删除的元素
# list1.pop()
# print(list1)

# (4)格式: 列表.pop(索引)  作用:删除指定索引数据
# list1.pop(2)
# print(list1)

# (5)格式: 列表.clear 作用:清空列表
# list1.clear()
# print(list1)

# 3,修改
# *重点用(1)格式: 列表[索引] = 数据 作用:修改指定索引的数据,数据不存在不会报错
# list1[1] = 80
# print(list1)

# 4,查询 查询都是有返回值得  需要用一个变量接受 否则看不到效果
# *重点用(1)格式: 列表[索引] 作用:根据索引取值,索引不存在会报错
# i = list1[1]
# print(i)

# (2)格式: 列表.index(数据) 作用:根据数据查询索引，返回首次出现时的索引，没有查到会报错
# i = list1.index(30)
# print(i)

# (3)格式: 列表.count(数据) 作用:数据在列表中出现的次数
# i = list1.count(30)
# print(i)

# *重点用(4)格式: len(列表) 作用:列表长度
# i = len(list1)
# print(i)

# 重点用(5)格式: if数据 in 列表 作用:检查列表是否包含某个元素
# i = 40
# if i in list1:  # 判断列表中是否包含 i 对应的数据
#     print("数据包含 %d" % i)
# else:
#     print("不包含 %d" % i)

# 5,排序
# *重点用(1)格式: 列表.sort()  作用:让列表中的数据升序排列
# list1.sort()
# print(list1)

# (2)格式: 列表.sort(reverse=True) 作用:让列表中的数据降序排列
# list1.sort(reverse=True)
# print(list1)

# (3)格式: 列表.reverse() 作用:逆序/反序 让数据颠倒
# list1.reverse()
# print(list1)

# 重点联系
# 增
# list1.append(90)
# print(list1)
#
# #删
# list1.remove(25)
# print(list1)
#
# #改
# list1[2] = 100
# print(list1)
#
# #查
# i = list1[4]  # 数据查询
# print(i)
#
# long = len(list1)  # 查询列表的个数
# print(long)
#
# ele = 30
# if ele in list1:
#     print("数据中有 %d" % ele)
# else:
#     print("数据中没有 %d" % ele)
#
# #排序
#
# import keyword
# print(keyword.kwlist)