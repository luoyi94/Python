class People:
    def __init__(self):
        self.__name = None


    def set(self, age):
            if 0 < age < 100:
                self.__age = age
            else:
                print("年龄输入有误")

    def get(self):
        return self.__age




p1 = People()
p1.set(1050)


            #
            # class Dog:
            #     def __init__(self):
            #         # 在属性名前前面添加 双下划线__ 就会把属性变成私有属性
            #         self.__age = None  # 私有化属性
            #
            #     # 给比较敏感的属性加上一对set和get方法在赋值前进行安全判断，合法才赋值到属性上
            #     # 给属性私有后，类的外部无法直接访问，但可以提供一对set和get方法让外面的对象来间接访问私有属性
            #
            #     def set_age(self, age):  # 安全判断
            #         if age > 0:
            #             self.__age = age  # 间接传给私有化的属性修改值 self.__age
            #         else:
            #             self.__info("age")
            #
            #     def get_age(self):
            #         return self.__age  # 返回私有化的self.__age的值
            #
            #     def __info(self, property_name):  # 私有化方法
            #         print("%s属性没有赋值成功" % property_name)
            #
            # dog1 = Dog()  # dog1不能直接调用私有属性
            # dog1.set_age(0)  # age = 10 调用set.age方法进行判断
            # # print(dog1.get_age())