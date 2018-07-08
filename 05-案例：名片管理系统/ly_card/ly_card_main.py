import ly_card_tools
ly_card_tools.load_cards()
while True:
    ly_card_tools.menu()
    action = input("请选择执行的操作：")
    print("你选择的功能: %s" % action)
    if action == "1":
        ly_card_tools.new_card()
    elif action == "2":
        ly_card_tools.show_cards()
    elif action == "3":
        ly_card_tools.find_cards()
    elif action == "4":
        ly_card_tools.save_cards()
    elif action == "0":
        break
    else:
        print("输入有误，请重新输入")
