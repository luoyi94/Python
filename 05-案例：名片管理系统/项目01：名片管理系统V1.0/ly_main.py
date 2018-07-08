"""此文件负责菜单显示"""
"""
1, 显示菜单选项
2，根据用户输入的做相应的操作  判断
3，提示语句
"""
import ly_tools  # 调用工具模块

ly_tools.read_file()
while True:
    # 1, 显示菜单选项
    ly_tools.menu()

    # 2， 判断用户输入的值调用不同的工具，显示不同的结果或操作

    # 提示用户输入
    user_1 = input("请选择执行的操作：")
    # 每次都会显示用户输入的值
    print("您选择的功能：%s" % user_1)

    if user_1 == "1": # 新建名片
        ly_tools.add()  # TODO 添加完成，累加到全局数列中
    elif user_1 == "2":  # 查询所有名片
        ly_tools.show_list()
    elif user_1 == "3":  # 查询名片
        ly_tools.find_news()
    elif user_1 == "4":  # 存入名片
        ly_tools.save_news()
    elif user_1 == "0":  # 退出系统
        print("退出系统")
        break
    else:
        # 输入的是除1,2,3以为的字符或者空值 则提示：
        print("输入有误，请重新输入")




