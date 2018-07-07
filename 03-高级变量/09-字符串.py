# 字符串

# string = "hello Python"   # 一串字符 表示文本的数据类型
# print(string)
#
# string_1 = '''hello
# h
# e
# l
# l
# o
#
# python'''           # 如果想要字符串换行显示  可用''' 文本 '''  编写  中间即可任意换行
# print(string_1)

# 4.2 字符串的常用操作
#
# 1) 判断
#
# 方法	说明
# string.isalpha()	如果 string 至少有一个字符并且所有字符都是字母则返回 True
# string.isdecimal()	如果 string 只包含数字则返回 True
# string.islower()	如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True
# string.isupper()	如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True
# string.startswith(str)	检查字符串是否是以 str 开头，是则返回 True
# string.endswith(str)	检查字符串是否是以 str 结束，是则返回 True
# 2) 查找和替换
#
# 方法	说明
# **string.find(str, start=0, end=len(string))**	检测 str 是否包含在 string 中，如果 start 和 end 指定范围，
# 则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回 -1
# string.rfind(str, start=0, end=len(string))	类似于 find()，不过是从右边开始查找
# string.index(str, start=0, end=len(string))	跟 find() 方法类似，不过如果 str 不在 string 会报错
# string.rindex(str, start=0, end=len(string))	类似于 index()，不过是从右边开始
# **string.replace(old_str, new_str, num=string.count(old))**	返回一个新字符串，把 string 中的 old_str 替换成 new_str，
# 如果 num 指定，则替换不超过 num 次
# 3) 拆分和连接
#
# 方法	说明
# string.partition(str)	返回元组，把字符串 string 分成一个 3 元素的元组 (str前面, str, str后面)
# string.rpartition(str)	类似于 partition() 方法，不过是从右边开始查找
# **string.split(str="", num)**	返回列表，以 str 为分隔符拆分 string，如果 num 有指定值，则仅分隔 num + 1 个子字符串，
# str 默认 包含 '\r', '\t', '\n' 和空格
# string.splitlines()	返回列表，按照行('\r', '\n', '\r\n')分隔
# string1 + string2	拼接两个字符串
# string.join(seq)	返回字符串，以 string 作为分隔符，将 seq 中所有的元素（的字符串表示）合并为一个新的字符串
# 4) 大小写转换
#
# 方法	说明
# string.lower()	返回新字符串，转换 string 中所有大写字符为小写
# string.upper()	返回新字符串，转换 string 中的小写字母为大写
# 5) 文本对齐
#
# 方法	说明
# string.ljust(width)	返回新字符串，基于原字符串左对齐，并使用空格填充至长度 width
# string.rjust(width)	返回新字符串，基于原字符串右对齐，并使用空格填充至长度 width
# string.center(width)	返回新字符串，基于原字符串居中，并使用空格填充至长度 width
# 6) 去除空白字符
#
# 方法	说明
# string.lstrip()	返回新字符串，截掉 string 左边（开始）的空白字符
# string.rstrip()	返回新字符串，截掉 string 右边（末尾）的空白字符
# string.strip()	返回新字符串，截掉 string 左右两边的空白字符