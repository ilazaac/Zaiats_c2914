import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 50
        self.alive = True

    def to_study(self):
        print("Час навчатися")
        self.progress += 0.2
        self.gladness -= 5
        self.money -= 5

    def to_sleep(self):
        print("Піду спати")
        self.gladness += 3

    def to_chill(self):
        print("Час відпочити")
        self.gladness += 5
        self.progress -= 0.05
        self.money -= 10

    def to_work(self):
        print('Час попрацювати')
        self.progress -= 0.05
        self.money += 30
        self.gladness -= 3

    def is_alive(self):
        if self.progress < -0.5:
            print("Вигнали…")
            self.alive = False
        elif self.gladness <= 0:
            print("Депрессія...")
            self.alive = False
        elif self.progress > 5:
            print("Здав екстерном...")
            self.alive = False
        elif self.money < 0:
            print("Занадто бідний...")
            self.alive = False
        elif self.money > 700:
            print("Заплатив за всі оцінки...")
            self.alive = False

    def end_of_day(self):
        print(f"Щастя = {self.gladness}")
        print(f"Прогрес ={round(self.progress, 2)}")
        print(f"Гроші = {self.money}")

    def live(self, day):
        day = "День " + str(day) + " з життя " + self.name
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()


nick = Student(name="Нікіта")
for day in range(365):
    if not nick.alive:
        break
    nick.live(day)
