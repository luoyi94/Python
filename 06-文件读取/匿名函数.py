
# f = lambda num1:num1**2  # 求数值的二次方
# print(f(5))


# list5 = (lambda *args: [arg**2 for arg in args])(1, 2, 3)
# print(list5)




# 递归函数 输出1~100的数

#
# def func(num):
#     if num >1:
#         print(num, end=" ")
#         return num * func(num - 1)
#     else:
#         return 1
#
#
# func(100)


c = lambda a, b:a+b


def fun(a, b, opt):
    print("a = %s" % a)
    print("b = %s" % b)
    print("result = %d" % opt(a, b))


fun(1, 2, c)

