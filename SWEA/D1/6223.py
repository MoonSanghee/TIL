class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return 3.14*(self.radius)**2

ar=Circle(2)
print("원의 면적: %.2f"%ar.area())