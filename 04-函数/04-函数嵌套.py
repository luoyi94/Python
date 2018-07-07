# 打印单行


def print_line(length, char):
    print(char * length)

# print_line(20, "&")


def print_lines(char, length, row1):  # 1，取调用函数 的实参数值 赋给 形参
    row = 1
    while row <= row1:
        print_line(length,char)    # 2，将print_lines形参拿到的值 赋给 调用print_line的实参
        row += 1


# 打印输入字符char   输入个数length   输入的行数row

print_lines("#", 3, 3)