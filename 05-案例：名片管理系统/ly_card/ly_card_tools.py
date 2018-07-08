import os

cards = []

# 欢迎菜单


def menu():
    """主菜单"""
    print("*" * 30)
    print("1,新建名片")
    print("2,显示全部")
    print("3,查询名片")
    print("4,保存名片\n")
    print("0,退出系统")
    print("*"* 30)


# 用户输入1  action = 1
# 新建名片


def new_card():
    """新键名片"""
    print("功能：新建名片")
    card_1 = {}
    card_1["name"] = input("请输入姓名：")
    card_1["phone"] = input("请输入电话：")
    card_1["QQ"] = input("请输入QQ号码：")
    card_1["email"] = input("请输入邮箱：")
    print("添加%s的名片成功" % card_1["name"])
    cards.append(card_1) # 添加到元素到列表中

# 用户输入2  action = 2
def show_cards():
    """显示全部"""
    print("功能：显示全部")
    if len(cards) == 0:
        print("没有任何名片记录")
    else:
        print("*" * 30)
        print("姓名\t\t电话\t\tQQ\t\t邮箱")
        print("-" * 30)
        for show_cards_1 in cards:
            print("%s\t\t%s\t\t%s\t\t%s" % (show_cards_1["name"], show_cards_1["phone"], show_cards_1["QQ"], show_cards_1["email"]))
        print("-" * 30)

# 用户输入3  action = 3
def find_cards():
    """查询名片"""
    print("功能：查询名片")
    find_1 = input("请输入查询的姓名：")
    for find_2 in cards:
        if find_2["name"] == find_1:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("-" * 30)
            print("%s\t\t%s\t\t%s\t\t%s" % (find_2["name"], find_2["phone"], find_2["QQ"], find_2["email"]))
            print("-" * 30)
            # ***对查询到的fan_2进行高级操作***
            upda_cards(find_2)
        else:
            print("没有找到%s" % find_1)
            continue



def upda_cards(find_2):
    "高级操作"
    while True:
        adv = input("请输入对名片的操作：1，修改/ 2，删除 / 0.放回上一级")
        if adv == "1":
            find_2["name"] = input("请输入姓名：")
            find_2["phone"] = input("请输入电话：")
            find_2["QQ"] = input("请输入QQ号码：")
            find_2["email"] = input("请输入邮箱：")
            print("修改%s的名片成功" % find_2["name"])
            break
        elif adv == "2":
            cards.remove(find_2)
            print("删除成功")
            break
        elif adv == "0":
            break
        else:
            print("输入有误请重新输入")


def save_cards():
    """保存名片"""
    print("功能：保存名片")
    with open("save.txt", "w") as f:
        f.write(str(cards))

def load_cards():
    if os.path.exists("save.txt"):
        with open("save.txt", "r") as f:
            content  = f.read()
            global cards
            cards = eval(content)



