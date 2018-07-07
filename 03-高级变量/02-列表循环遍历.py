# while循环来实现列表的遍历
# i = 0
list_name = ["张三", "李四", "王五"]
# list_long = len(list_name)
# while i < list_lon)g:
#     list_name1 = list_name[i]
#     print(list_name1)
#     i += 1
# print("全部人名"

# for循环来实现遍历   for循环的本质就是迭代器
# for 重复执行循环体,条件不满足时 跳出循环 输出结果
for list_name1 in list_name:
    # 在列表list_name中的数据以此调出来 并按顺序交给变量 list_name1
    print(list_name1)