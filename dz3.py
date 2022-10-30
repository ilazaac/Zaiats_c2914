import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 50
        self.pet = pet()
        self.alive = True
        self.cat_died = False

    def to_study(self):
        print("Час навчатися")
        self.progress += 0.2
        self.gladness -= 5
        self.money -= 5
        self.pet.satiety -= self.pet.food_less
        self.pet.gladness += 5
        if self.pet.gladness >= 100:
            self.pet.gladness = 100

    def to_sleep(self):
        print("Піду спати")
        self.gladness += 3
        self.pet.satiety -= self.pet.food_less
        self.pet.gladness -= 5
        if self.gladness >= 100:
            self.gladness = 100

    def to_chill(self):
        print("Час відпочити")
        self.gladness += 5
        self.progress -= 0.05
        self.money -= 10
        self.pet.satiety -= self.pet.food_less
        self.pet.gladness += 5
        if self.pet.gladness >= 100:
            self.pet.gladness = 100
        if self.gladness >= 100:
            self.gladness = 100

    def to_work(self):
        print('Час попрацювати')
        self.progress -= 0.05
        self.money += 30
        self.gladness -= 3
        self.pet.satiety -= self.pet.food_less
        self.pet.gladness -= 3

    def to_feed_cat(self):
        print('Час годувати кота')
        self.money -= 10
        self.pet.satiety += self.pet.satiety_per_food
        if self.pet.satiety >= 100:
            self.pet.satiety = 100

    def to_play_with_cat(self):
        print('Час погратися з котом')
        self.gladness += 5
        self.pet.gladness += 20
        if self.pet.gladness >= 100:
            self.pet.gladness = 100
        if self.gladness >= 100:
            self.gladness = 100

    def is_alive(self):
        self.pet.is_pet_alive()
        if self.progress < -0.5:
            print("Вигнали…")
            self.alive = False
        if self.cat_died == False:
            if self.pet.is_pet_alive() == False:
                print('Кіт помер...')
                self.gladness -= 50
                self.cat_died = True
        elif self.gladness <= 0:
            print("Депрессія...")
            self.alive = False
        elif self.progress > 5:
            print("Здав екстерном...")
            self.alive = False
        elif self.money < 0:
            print("Занадто бідний...")
            self.alive = False

    def end_of_day(self):
        if self.pet.is_pet_alive() == True:
            print(f"Щастя кота = {self.pet.gladness}")
            print(f"Ситість кота = {self.pet.satiety}")
        print(f"Щастя = {self.gladness}")
        print(f"Прогрес ={round(self.progress, 2)}")
        print(f"Гроші = {self.money}")

    def live(self, day):
        day = "День " + str(day) + " з життя " + self.name
        print(f"{day:=^50}")
        if self.pet.is_pet_alive() == True:
            live_cube = random.randint(1, 6)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
            elif live_cube == 4:
                self.to_work()
            elif live_cube == 5:
                self.to_feed_cat()
            elif live_cube == 6:
                self.to_play_with_cat()
            self.end_of_day()
            self.is_alive()
        else:
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


class pet:
    def __init__(self):
        self.gladness = 50
        self.satiety = 50
        self.satiety_per_food = random.randint(30, 80)
        self.food_less = random.randint(1, 10)

    def is_pet_alive(self):
        if self.satiety <= 0:
            return False
        if self.gladness <= 0:
            return False
        else:
            return True


nick = Student(name="Нікіта")
for day in range(365):
    if not nick.alive:
        break
    nick.live(day)

