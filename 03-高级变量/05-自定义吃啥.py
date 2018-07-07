import random
eats = ["称菜米饭", "蒸菜", "沙县面条", "沙县米饭", "出门左拐", "泡面", "开水"]
i = len(eats) - 1
eat = random.randint(0,i)
day_eat = eats[eat]
print("今天吃啥? %s" % day_eat)
print(i)