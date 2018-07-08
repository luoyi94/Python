list1 = [1, 5, 3, 1, 3, 6, 3, 2, 1]

list2 = set(list1)    # 将列表转换成无序列表  来实现去重的功能
print(list2)

# 利用index第一次出现的角标，第一次出现角标的元素一定是唯一

# 练习：用循环和   list.index(元素，开始索引，结束索引）不指定开始和结束，则默认获取第一次出现的角标
i = len(list1) - 1  # 获取长度  然后用来控制循环次数
list4 = []        # 用来存放已经去重的列表
while i >= 0:
    if not(list1[i] in list4):
        a = list1.index(list1[i])  # 获取list[i]元素第一次出现的角标
        list4.append(list1[a])  # 将第一次出现的元素放入列表
    i -= 1
print(list4)


# list2  = []
# for i in range(len(list1)):
#     elment = list[i]
#     index = list1.append(elment)
#     if i == index:


# class Dog:
#     def eat(self):
#         print("吃")
#
#
# dog1 = Dog()
#
# dog1.eat()

