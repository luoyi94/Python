"""此文件负责细节操作工具"""
import os

news = []   # 储存此次运行的所有用户  news [{用户1}, {用户2}, {用户3}, {用户4}]
que_new = {}  # 储存查询到的那个特定的用户i放入全局变量   函数

# 显示菜单选项
def menu():
    """菜单界面"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0!")
    print()
    print("1, 新建名片")
    print("2, 显示全部")
    print("3, 查询名片")
    print("4, 存入名片\n")
    print("0,退出系统")
    print("*" * 50)

# 执行相应功能
def add():
    """添加名片"""
    print("功能：新键名片")

    """小白版"""

    # # 新建一个字典来储存用户输入的值
    # news_1 = {}
    # # 接收每个用户输入的值
    # name = input("请输入你的姓名：")
    # phone = input("请输入你的电话：")
    # qq = input("请输入你的QQ号码：")
    # email = input("请输入邮箱：")
    # # 把每个值储存到字典的  value 中
    # new_1 = {"name": name, "phone": phone, "qq": qq, "email": email}

    """进阶版"""
    # 新建一个空字典来储存用户输入的值
    new_1 = {}
    # 根据字典的定义 如果字典本身该键key  则为  添加键值对 ：
    new_1["name"] = input("请输入的姓名：")
    new_1["phone"] = input("请输入的电话：")    # 程序总是从右边开始运行 ← 先获取到输入的值 赋给对应键的值value
    new_1["qq"] = input("请输入的QQ号码：")
    new_1["email"] = input("请输入的邮箱：")
    # 提示用户添加成功
    print("添加%s的名片成功" % new_1["name"])
    # 把储存用户的字典添加到到 news 的列表中   news [{用户1}, {用户2}, {用户3}, {用户4}]
    news.append(new_1)  # 在函数内部给全局变量的列表增删改元素是不会修改对应的id 所以不是使用全局变量 不用golabl    只有用 "=” 号赋值的时候需要申明


def show_list():
    """显示全部"""
    """判断是否为空列表"""
    print("功能：查询所有名片")
    if len(news) == 0:  # 判断列表中是否含有元素  即长度是否为0
        return print("没有任何名片")  # 列表长度为0（列表为空）返回提示错误   利用放回值return 让后面的代码不再执行 而 结束函数
    # 有元素则上面if 不成立  自动执行下面的代码：
    print("姓名\t\t电话\t\tQQ\t\t邮箱")
    print("-" * 30)
    # 使用for循环遍历列表中每一个字典  让每一个字典个都格式化输出
    for news_1 in news:
        print("%s\t\t%s\t\t%s\t\t%s" % (news_1["name"], news_1["phone"], news_1["qq"], news_1["email"]))
    # 遍历输出完所有的用户信息字典后  打印一排"-"
    print("-" * 30)


def find_news():
    """查询名片"""
    print("功能：查询名片")
    find_1 = input("请输入查询的名字：")     # 用户输入的数据
    for news_1 in news:                    # 遍历用户数据
        if news_1["name"] == find_1 :      # 判断用户想要进行查询和修改的名片news_1字典
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("-" * 30)
            print("%s\t\t%s\t\t%s\t\t%s" % (news_1["name"], news_1["phone"], news_1["qq"], news_1["email"]))
            print("-" * 30)
            # 申明变量为全局变量
            global que_new
            # 把查询到的对应名片信息取出 储存到全局变量que_new中     从而修改全局的值que_new
            que_new = news_1

            # 对查询到的名片进行高级处理 (修改、删除）
            mode_news()

        # 判断用户要查询的名片不存在情况 提示没有找到
        else:
            print("没有找到 %s的名片" % find_1)
            break


def mode_news():
    """查询到的名片进行操作"""
    while True:
        mode_1 = input("请输入对名片的操作：1.修改 /2.删除 /0.返回上一级")
        if mode_1 == "1":
            alter_news()   # 调用修改函数
            break
        elif mode_1 == "2":
            delete_news()  # 删除函数
            break
        elif mode_1 == "0":  # 结束循环
            break
        else:
            print("输入错误，请重新输入")


def delete_news():
    """查询到名片进行删除"""
    news.remove(que_new)  # .remove 删除列表表中指定的元素
    print("删除成功")


def alter_news():
    """修改名片"""
    que_new["name"] = input("请输入的姓名：")  # 修改字典 对应的键值对
    que_new["phone"] = input("请输入的电话：")
    que_new["qq"] = input("请输入的QQ号码：")
    que_new["email"] = input("请输入的邮箱：")
    print("修改成功")

def save_news():
    """存入名片"""
    with open("save.txt", "w") as f:
        f.write(str(news))


def read_file():
    if os.path.exists("save.txt"):
        with open("save.txt", "r") as f:
            content = f.read()
            global news
            news = eval(content)






















