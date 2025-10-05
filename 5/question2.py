class Circle():
    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


r20 = Circle(50)
print(r20.get_radius())
r20.set_radius(20)
print(r20.get_radius())
