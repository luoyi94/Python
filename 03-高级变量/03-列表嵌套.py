"""
应用
一个学校，有3个办公室，
现在有8位老师等待工位的分配，
请编写程序:
1> 完成随机的分配
2> 获取办公室信息 (每个办公室中的人数，及分别是谁)
"""
# import random
# teacher = ["A", "B", "C", "D", "E", "F", "G", "H"]  # 这是每个老师的编号
# a = random.randint(0, 7)  # 随机取一个值  用作列表teacher 的索引
# b = teacher[a]  # 取出对应索引的中的元素
# # print(b)
# room = [1, 2, 3]  # 这是教师的编号
# a1 = random.randint(0,2)  # 随机取一个值  作为列表room的索引
# b1 = room[a1]  # 取出对应索引的中的元素
# # print(b1)
#
# i = 0
# while a1

import random

# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

# 完成随机分配
for name in names:    # 依次取出每一个老师
    office_num = random.randint(0, (len(offices)-1))  # 随机生成的办公室对应的 索引
    office = offices[office_num]           # 取出随机的办公室
    office.append(name)
# 获取办公室信息 2> 获取办公室信息 (每个办公室中的人数，及分别是谁)
i = 1
for office_1 in offices:
    print("第 %d个办公室共有 %d人,分别为：" % (i, len(office_1)))
    i += 1
    for name_num in office_1:
        print("%s " % name_num, end="")
    print()



    # index = random.randint(0,2)
    # offices[index].append(name)  # 把name中某一个人的名字元素 增加  到offices 随机索引对应的 嵌套列表中

# 获取办公室信息
# i = 1
# for tempNames in offices:
#     print('办公室%d的人数为:%d'%(i, len(tempNames)))
#     i+=1
#     for name in tempNames:
#         print("%s" % name, end='')
#     print("\n")
#     print("-"*20)