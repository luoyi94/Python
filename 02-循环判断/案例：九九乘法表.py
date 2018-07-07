# 第 1 步：用嵌套打印小星星
# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
# print("end")

# 用列row来控制总数 有多少列就有多少行col  只有 列 +1,对应 行 才 +1
row = 1
while row <= 9:
    col = 1
    while row >= col:
        print("%d X %d = %d" % (row, col, row * col),end="\t")
        col += 1
    print()
    row += 1
