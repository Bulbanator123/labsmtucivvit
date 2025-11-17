class Vehicle():
    def __init__(self, make, model):
        # конструктор
        self.make = make
        self.model = model

    def get_info(self):
        # возвращаем массив с информацией о траспорте
        return f"Транспорт с маркой {self.make}, модель {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        # конструктор
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        # возвращаем массив с информацией об автомобиле
        return "машина" + super().get_info()[9:] + f" может ехать на {self.fuel_type} топливе"


veh1 = Vehicle("boeng", "777")
car1 = Car("Lada", "Niva", "95")
print(veh1.get_info())
print(car1.get_info())
