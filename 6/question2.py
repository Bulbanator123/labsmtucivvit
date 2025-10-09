class Vehicle():
    def __init__(self, make, model):
        # конструктор
        self.make = make
        self.model = model

    def get_info(self):
        # возвращаем массив с информацией о траспорте
        return [self.make, self.model]


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        # конструктор
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        # возвращаем массив с информацией об автомобиле
        return super().get_info() + [self.fuel_type]


veh1 = Vehicle("boeng", "777")
car1 = Car("Lada", "Niva", "95")
print(veh1.get_info())
print(car1.get_info())
