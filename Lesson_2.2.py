#Родительский класс, суперкласс
class Car:
    #метод конструктор, инициализатор
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.max_speed = 100

    def drive_to(self, destination):
        print(f"Машина цвета {self.color}, модели {self.model} поехала в {destination} ")

    def change_color(self, new_color):
        self.color = new_color

#Дочерние классы, подклассы, потомки класса 'Car'
class Bus(Car):
    def drive_to(self, destination):
        print(f"Автобус цвета {self.color} поехала: {destination} ")


class ElectricCar(Car):
    def __init__(self, model, color, battery):
        super().__init__(model, color)
        self.battery = battery
    def charge (self):
        self.battery += 15
        if self.battery > 100:
            self.battery = 100

    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Электро машина модели {self.model} поехала на {destination} ")

car_1 = Car("Kia", "gray")
tesla_1 = ElectricCar("Tesla", "black", 80)
bus35 = Bus("Mercedes", "green")

# car_1.drive_to("Кара Балта")
# tesla_1.drive_to("Кара Балта")
# bus35.drive_to("Кара Балта")

vehicles = (car_1, tesla_1, bus35)
for one_vehicle in vehicles:
    one_vehicle.drive_to("Кара Балта")