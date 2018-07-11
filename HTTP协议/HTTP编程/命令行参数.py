import sys


# print(sys.argv)
# 运行python3 命令行参数.py a ly c
# 打印了以列表方式返回['命令行参数.py', 'a', 'ly', 'b', 'c']
# py后面的数当做前面的的行数的参数传入

def main():
    print(sys.argv)

    # 判断后面跟的参数是否为两个
    if len(sys.argv) != 2:
        print("error, usage: xxx port")
        return

    port = int(sys.argv[1])
    print("port = ", port)




if __name__ == '__main__':
    main()
