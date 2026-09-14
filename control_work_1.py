class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print("Звук животных:")

class Dog(Animal):
    def make_sound(self):
        print("Гав - гав")

class Cat(Animal):
    def make_sound(self):
        print("Мяу - мяу")

dog = Dog("Рекс", 5)
cat = Cat("Барсик", 3)

print(f"Собака - {dog.get_name()}, возвраст - {dog.get_age()}")
dog.make_sound()
print(f"Кот - {cat.get_name()}, возвраст - {cat.get_age()}")
cat.make_sound()

print()

dog.set_name("Муктар")
dog.set_age(4)
cat.set_name("Рыжик")
cat.set_age(2)

print(f"Собака - {dog.get_name()}, возвраст - {dog.get_age()}")
dog.make_sound()
print(f"Кот - {cat.get_name()}, возвраст - {cat.get_age()}")
cat.make_sound()