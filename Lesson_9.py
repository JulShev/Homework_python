from dataclasses import dataclass


# создаем класс данных, в котором хранятся данные работников
@dataclass
class Employees:
    index: int
    profession: str
    name: str
    rate: int
    department: str


class Person:
    department = 'department name'
    _index = 0  # Индекс будет увеличиваться по мере создания новых работников

    def __init__(self, first_name, profession, salary):
        self.first_name = first_name
        self.profession = profession
        self.profession = salary

        # Создаем переменную, в которой будет храниться информация о работнике с класса Employees
        # Данные работника структурированы в классе Employees
        # Необходимо создать его экземпляр, чтобы можно было с ним работать, здесь мы это реализовываем с помощью переменной info (она и является экземпляром)
        # Теперь можно обращаться через person.info ко всем значениям класса Employees
        self.info = Employees(index=self._index, profession=profession, name=first_name, rate=salary, department=self.department)
        Person._index += 1  # Увеличиваем индекс на 1 после создания работника

    # создаем статикметод, который выводит имя работника
    @staticmethod
    def name(name: str):
        print(name)

    # создаем классметод, который создает работника от его почасовой оплаты и кол-ва часов в день

    @classmethod
    def from_per_hour_salary(cls, first_name: str, profession: str, earn_per_hour: (float, int), hours_in_day: int):
        if isinstance(earn_per_hour, (float, int)) and isinstance(hours_in_day, int):
            return cls(first_name, profession, 20 * earn_per_hour * hours_in_day)


# Создаем метакласс
C = type("CLASS", (Person,), {"department": " "})


person3 = Person.from_per_hour_salary('Tony', 'teamlead', 500, 8)
print(person3.info.rate)
