#[3] Quản lý Động Vật
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def sound(self, species):
        if self.species == "dog":
            print("Woof!")
        elif self.species == "cat":
            print("Meow!")
        else: print("Not dog and cat")

a = Animal("lu", "dog", 2)
a.sound("dog")
b = Animal("mimi", "cat", 2)
b.sound("cat")
c = Animal("Xiao", "panda", 2)
c.sound("panda")