# 需求
#
# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# 比较胜负
import random

computer_unm = random.randint(1,3)
player = int(input("请出拳-石头（1）／剪刀（2）／布（3）:"))

if (player == 1 and computer_unm == 2) or (player == 2 and computer_unm == 3) or (player == 3 and computer_unm == 1):
    print("赢咯!")
elif(player == computer_unm):
    print("平局!")
else:
    print("下次努力!")