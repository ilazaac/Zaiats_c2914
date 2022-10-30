import random

petlist = {
    "Parrot": {"satiety_per_food": 30, "food_less": 5, "sleep_less": 10},
    "Cat": {"satiety_per_food": 50, "food_less": 15, "sleep_less": 40},
    "Dog": {"satiety_per_food": 25, "food_less": 10, "sleep_less": 20},
    "Hamster": {"satiety_per_food": 70, "food_less": 30, "sleep_less": 30},
}


class pet:
    def __init__(self, petlist, name=None, breed=None):
        self.name = name
        self.breed = breed
        self.gladness = 50
        self.satiety = 50
        self.breed = random.choice(list(petlist))
        self.satiety_per_food = petlist[self.breed]["satiety_per_food"]
        self.food_less = petlist[self.breed]["food_less"]
        self.sleep_less = petlist[self.breed]["sleep_less"]

    def info(self):
        print(self.breed)

    def live(self, day):
        dice = random.randint(1, 2)
        if dice == 1:
            self.gladness += 20
        if dice == 2:
            self.food += self.satiety_per_food

    def days_indexes(self, day):
        day_pr = f" Today the {day} of {self.breed} 's life "
        print(f"{day_pr:=^50}", "\n")
        pet_indexes = self.breed + "'s indexes"
        print(f"{pet_indexes:^50}", "\n")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")


bob = pet(name="Vick")
for day in range(1, 350):
    if bob.live(day) == False:
        break

