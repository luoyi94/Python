import ao2   # 导入全部
ao2.func2()#  调用每次都得模块名

from ao2 import func3  # 只导入模块中某个特定的功能
func3()      # 直接使用

from ao2 import *
func2()    # 只能导入ao2中all列表中的特有的功能
func3()
# func4()
