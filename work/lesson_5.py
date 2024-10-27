# Классы (ООП) продожение

class Cat():
    "Атрибуты класса"
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age

    "Методы класса"
    def say_meow(self):
        return "Мяу!"

    def say_mur(self):
        return "Мррррр"

cat1 = Cat("Дворовая", "белый", 5) # экземпляр класса
cat2 = Cat("Британская", "серый", 3)

# print(cat1.say_mur(), cat2.say_meow())


class HomeCat(Cat):
    def __init__(self, breed, color, age, owner, name):
        super().__init__(breed, color, age)
        self.owner = owner
        self.name = name

    def breed(self):
        return self.breed
    def color(self):
        return self.color
    def age(self):
        return self.age
    def owner(self):
        return self.owner
    def name(self):
        return self.name

h_cat1 = HomeCat("Сиамская", "рыжий", 4, "Хозяин1", "Васька")
h_cat2 = HomeCat("Мейн-кун", "черный", 1, "Хозяин2", "Царь")

"""print(h_cat1.breed)
print(h_cat1.color)
print(h_cat1.age)
print(h_cat1.owner)
print(h_cat1.name)
print()
print(h_cat2.breed)
print(h_cat2.color)
print(h_cat2.age)
print(h_cat2.owner)
print(h_cat2.name)

print(h_cat1.say_meow())
print(h_cat2.say_mur())"""

