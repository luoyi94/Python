import bao1.ao2   # 导入全部
bao1.ao2.func2()  # 调用每次都得模块名

from bao1.ao2 import func3  # 只导入模块中某个特定的功能
func3()      # 直接使用
# func4()     # 报错



import sys
print(sys.path)

