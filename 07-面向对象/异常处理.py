

# try:
#     path = input("请输入要打开的文件:")
#     f = open(path)
#     content = f.read()
#     f.close()
# except FileExistsError as error:
#     print("文件未找到 %s" % error)
#
# except NameError as error:
#     print("变量未定义 %s" % error)
# #
# except:
#     print("所有异常都会捕获！")
#
# else:
#     print("当try里面的代码没有出错时就会执行")
# finally:
#     print("无论有没有都会执行")
# class Cu(Exception):

#     pass
#
# phone_num = input("请输入手机号码：")
# try:
#     if len(phone_num) != 11:
#         raise Cu("手机号位数不对")
#     elif phone_num.isdecimal() is False:
#         raise  Cu("输入不合法")
# except Cu as error:
#     print("提示: %s" % error)

# try:
#     f = open("123.txt", "r")  #  如果123.txt文件不存在，那么会产生 IOError 异常
#     f.read()
#     f.close()
#     print(num)   # 如果num变量没有定义，那么会产生 NameError 异常
# except:
#     print("所有异常都会捕获")
# except (IOError, NameError):
#     print("变量num没有定义 ")

# except Exception as  error:
#     print(error)
# finally:
#     print("有没有错都会执行")


# 自定义异常
class RaiseError(Exception):
    pass

phone_num = input("请输入号码：")
try:
    if len(phone_num) != 11:
        raise RaiseError("手机号码不对")
    elif phone_num.isdecimal() is False:
        raise RaiseError("不是纯数字")
except RaiseError as error:
    print("提示：%s" % error)
