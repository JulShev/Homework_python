import time
class Auto:
    # создаем переменную для расчета возраста
    count_age = 0

    def __init__(self, brand, mark, age, color="", weight=0):
        self.brand = brand
        self.mark = mark
        self.age = age
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def birthday(self):
        # при вызове метода возраст увеличивается на 1
        self.count_age += 1
        print(self.count_age)

    def stop(self):
            print("stop")

# создаем наследуемый класс от Auto
class Truck(Auto):
    def __init__(self, brand, mark, age, color="", weight=0, max_load=50):
        super().__init__(brand, mark, age, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        print("move")

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)
# создаем второй наследуемый класс от Auto
class Car(Auto):
    def __init__(self, brand, mark, age, color="", weight=0, max_speed=100):
        super().__init__(brand, mark, age, color, weight)
        self.max_speed = max_speed

    def move(self):
        print("move")
        print("max speed is < max_speed")
# создаем 2 объекта класса Truck
truck = Truck("Brand", "Mark",5)
truck2 = Truck("Brand2", "Mark2", 1)
# вызываем метогды move и load у созданных объектов
truck.move()
truck.load()

# создаем 2 объекта класса Car
car = Car("Brand_car", "Mark_car", 3)
car2 = Car("Brand2_car", "Mark2_car", 10)
# вызываем метогды move и birthday у созданных объектов
car.move()
car2.birthday()