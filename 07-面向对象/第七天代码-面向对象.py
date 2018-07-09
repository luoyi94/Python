# 定义一个类（其中有这个类共同的方法)


class Cat:
    def jump(self):
        print("you jump - i jump")

# 创建一个具有类属性的对象


tom = Cat()


# 调用对象的一个方法
tom.jump()

# 首次赋值属性 ，会新定义一个新属性
tom.happy = "嗨皮"
#  再次定义会修改该属性
tom.happy = "very嗨皮"

print(tom.happy)

