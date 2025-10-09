from time import sleep


class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return [self.name, self.id]


class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self, time):
        print(f"{self.name} сейчас будет менеджить проект...")
        for i in range(1, time + 1):
            print(f"\rЧто-то менеджит {i}", end=" ")
            sleep(1)
        print("Закончил(а) =)")

    def get_info(self):
        return super().get_info() + [self.department]


class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self, time):
        print(f"{self.name} сейчас будет пилить проект...")
        for i in range(1, time + 1):
            print(f"\rЧто-то пилит {i}", end=" ")
            sleep(1)
        print("Закончил(а) =)")

    def get_info(self):
        return super().get_info() + [self.specialization]


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def get_info_team(self):
        for el in self.employee_list:
            print(el.get_info())

    def get_info(self):
        return super().get_info() + [self.department, self.specialization]

    def perform_maintenance(self, time):
        return super().perform_maintenance(time)

    def manage_project(self, time):
        return super().manage_project(time)


emp1 = Employee("Витя", "2278")
emp2 = Employee("Иван", "64")
emp3 = Employee("Валя", "52")

man1 = Manager("Митя", "2278", "bul")
man2 = Manager("Диван", "64", "bul")
man3 = Manager("Валера", "52", "prod")

tech1 = Technician("Туня", "111", "it")
tech2 = Technician("Работник века", "1234", "kiib")

techlead1 = TechManager("Груня", "1113", "it", "prod")

print(emp1.get_info())
print(man1.get_info())
print(tech1.get_info())
print(techlead1.get_info())

techlead1.add_employee(emp1)
techlead1.add_employee(emp2)
techlead1.add_employee(man3)
techlead1.add_employee(tech1)

man1.manage_project(5)
tech1.perform_maintenance(10)
techlead1.manage_project(6)
techlead1.perform_maintenance(7)

techlead1.get_info()
techlead1.get_info_team()
