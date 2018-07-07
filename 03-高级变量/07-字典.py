# 字典

# 字典的定义
# 字典名 = { key键1 : value值1, key键2 : value值2, ......}
# 字典中的值是无序的  也是无索引的

zhangsan_1 = {"name" : "zhangsan", "age" : 18, "sex" : "男", "weight" : 75}

# 可以换行也可以不换行
# **注意:键必须是唯一的(键名相同的时,会有覆盖情况,规范书写时唯一的键名)

# lisi = {"name" : "lisi",
#         "name" : "zhangsan",
#         "age" : 18}
# print(lisi["name"])   # 此处总是输出程序后执行的"name"


# 取出 字典中的值
# age_1 = zhangsan_1["name"]  # 取出值赋给一个变量age_1
# print(age_1)

# 修改 字典中的值
# zhangsan_1["age"] = 38
# print(zhangsan_1)

# 增加    *为常用方法*
# *修改时如果key1(键名)原字典中没有相同的键名 则为增加新的键值对*
# zhangsan_1["school"] = "深大"
# print(zhangsan_1)  # 增加只能一对键值对共同增加 key : value

# 删除

# 删除指定的键值对
# del zhangsan_1["age"]
# print(zhangsan_1)

# i = "age"  # 可以用变量来替代key   结果与上代码一样
# del zhangsan_1[i]
# print(zhangsan_1)

# *删除指定对应的键值对 并放回被删除的值*
# zhangsan_2 = zhangsan_1.pop("name")  # 删除key对应键值对 ,并返回删除的值,用一个变量接收
# print(zhangsan_2)

# 清空字典 删除字典中所有的元素
# zhangsan_1.clear()
# print(zhangsan_1)

# 修改
# *键存在就修改*
# zhangsan_1["age"] = 28
# print(zhangsan_1)

# 如果不存在,这添加键值对; 存在则不做处理
# zhangsan_1.setdefault("age_1", 38)
# print(zhangsan_1)

# 取出字典2(lisi)的键值对,键值对不存在,则添加键值对; 存在则修改值
# lisi = {"name" : "lisi", "age" : 58}
# zhangsan_1.update(lisi)
# print(zhangsan_1)

# 查询          都有返回值 一般定义一个变量来接收
# *根据键取值,键不对则报错*
# age_1 = zhangsan_1["age"]  # []中的"age" 在字典中 有对应的键值对
# print(age_1)

# 根据键取值，键值对不存在:不会报错,但会返回 None
# age_1 = zhangsan_1.get("age1")
# print(age_1)

# 获取所有键key   但是不会改变原键值对
# z_1 = zhangsan_1.keys()
# print(z_1)

# 获取所有的值value
a = zhangsan_1.values()
print(a)

# *获取所有的(键,值)* 可以理解为上叙两个的结合  可以进行遍历
# b = zhangsan_1.items()
# print(b)

# 取字典中的每个元素的key   == 把字典中的key 进行循环遍历
# for key in zhangsan_1:
#     a = key
#     print(a)

