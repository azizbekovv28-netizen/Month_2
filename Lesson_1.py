class Car:
    #метод конструктор, инициализатор
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to(self, destination):
        print(f"Машина цвета {self.color} поехала в {destination} ")

    def change_color(self, new_color):
        self.color = new_color

#Создание объекта путем "вызова" класса
car1 = Car("Kia", "серебристый") #Создание объекта вызывает __init__
car2 = Car("Bmw", "черный")
print(car1)
print(car2)
print(car1.model, car1.color) #Обращение к атрибутам/свойствам объекта
print(car2.model, car2.color)
car2.change_color("белый")
print(car2.color)
print(type(car1)) #тип объекта и его класс
print(type("Kia"), type(123))
car1.drive_to("Кант")
car1.model = "Subaru"
print(car1.model)
car2.fined = True #можно но не стоит так делать
print(car2.fined)
#print(car1.fined)
