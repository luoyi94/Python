# 新建文件  并编辑内容  此两种方法会直接
# ① open

# # f = open("1.txt", "w")
# f.write("hello, i am here")
# f.close()


# ② with  不用考虑关闭文件，它会自动关闭文件
# with open("1.txt", "w") as f:
#     f.write("hellow world")

with open("1.txt", "r") as f:
    conten = f.read()   # 接收读取到的数据
    print(conten)