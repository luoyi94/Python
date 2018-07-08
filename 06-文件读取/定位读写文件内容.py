f = open("1.txt", "r")
content = f.read(2)   # 特定数量的字符

print("读取的数据是：", content)  #  格式化输出

position = f.tell()
print("当前位置：", position)

conte = f.read(5)

pos = f.tell()
print("现在位置：", pos)  # pos=7  位置是累加的 第一次取出he已经走了2个位置了