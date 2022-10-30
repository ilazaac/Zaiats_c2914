import random
var1 = int(input('Ваше число: '))


class Class1:
    var = var1

    def __init__(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        self.var += a
        self.var *= b
        self.var /= c


class Class2(Class1):
    def __init__(self):
        var2 = int(input('Показати початкове число (1 - так, інше - ні): '))
        if var2 == 1:
            print(f"Ваше початкове число: {self.var}")
            super().__init__()
        else:
            super().__init__()


int2 = Class2()
int1 = Class1()
print(f"Число після шифрування: {int1.var}")
