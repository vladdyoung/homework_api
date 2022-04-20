import math
from src.Figure import Figure


class Circle(Figure):
    def __new__(cls, radius):
        if radius > 0:
            obj = super().__new__(cls)
            return obj
        else:
            raise Exception('Input positive number')

    def __init__(self, radius):
        if self.__class__ == Figure:
            raise Exception('Cannot instantiate abstract base class')
        self.name = 'Circle'
        self.radius = radius
        self.__area = None
        self.__perimeter = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = math.pi * (self.radius ** 2)
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = 2 * math.pi * self.radius
        return self.__perimeter
