# 读取1.txt中的全部内容  默认
# with open("1.txt", "r") as f:
#     content = f.read()
#     print(content)

# 大文件分类查看部分内容

# with open("1.txt", "r") as f:
#     content = f.read(4)   # ()括号内为读取的字符串数量
#     print(content)
# with open("1.txt", "w") as f:
#     f.write("hello world.\n i am here")  # 修改文件的内容变成两行

# readline()默认读取第一行全部数据    当括号(i)里面有数字i时则读取第i行全部数据

# with open("1.txt", "r") as f:
#     content = f.readline(2)
#     print(content)