# 函数基本使用 文档注释
# name = "小明"
#
#
# def say_hello():
#     print("hello 1")
#     print("hello 2")
#     print("hello 3")
#     print("hello 4")
# """打招呼"""
#
# print(name)
# say_hello()

# 书写规范:因为函数体相对比较独立，函数定义的上方，应该和其他代码（包括注释）保留 两个空行

# 在 定义函数 的下方，使用 连续的三对引号 编写对函数的说明文字
# 点中函数名，使用快捷键 CTRL + Q 可以查看函数的说明信息


# def sum_2_num():
#     """求和"""
#     unm1 = 10
#     unm2 = 20
#     sum2 = unm1 + unm2
#     print("%d + %d = %d" % (unm1, unm2, sum2))
#
#
# sum_2_num()

# 函数的参数


# def sum_2_num(num1, num2):
#     """相乘求积"""
#     sum3 = num1 * num2
#     print("%s * %d = %s" % (num1, num2, sum3))
#
#
# sum_2_num("-",30)


# return 的使用 ： 只能在内部使用，是函数给调用方提供的结果


# def sum(num1, num2):
#     return num1 * num2  # return表示返回，函数后续代码不会执行
#
#
# result = sum(30, 120)  # 使用变量来接收函数返回的结果
# print(result)

# 函数的嵌套调用
# 1定义一个 print_line 函数能够打印 * 组成的 一条分隔线


# def print_line():
#     print("*" * 50)


# print_line()


# 2 定义一个函数能够打印 由 任意字符 组成 的分隔线


# def print_2(int1):
#     print(int1 * 50)
#
#
# print_2("-")


# 3 定义一个函数能够打印 任意长度 的分隔线


# def print_line_1(long):
#     print("*" * long)
#
#
# print_line_1(100)

# 4 定义一个函数能够打印 5 行 的分隔线，分隔线要求符合需求 3


# def print_2(long):
#     i = 1
#     while i <= 5:
#         print_line_1(long)   # 函数的内部使用另一个函数进行输出，但是必须外面的形参和里面的形参 相同 才能传递到内部
#         i += 1
#
#
# print_2(20)


# 写一个函数求三个数的和


# def sum(int1, int2, int3):
#     """三个数求和"""
#     print(int1 + int2 + int3)
#
#
# sum(10, 50, 70)


# 写一个函数求三个数的平均值


# def mean(int1, int2, int3):
#     """求三个数的平均值"""
#     print((int1 + int2 + int3)/3)
#
#
# mean(50, 80, 90)


# 求输入的三个数的平均值 (嵌套上面的求和）




def sum(sum_1, sum_2, sum_3):
    """三个数求和"""
    return (sum_1 + sum_2 + sum_3)


int1 = int(input("请输入第一个数"))
int2 = int(input("请输入第二个数"))
int3 = int(input("请输入第三个数"))


def mean(int1, int2, int3):
    """求三个数的平均值"""
    sum_sum = sum(int1, int2, int3)/3
    print(sum_sum)


mean(int1, int2, int3)






