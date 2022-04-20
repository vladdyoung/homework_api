import math
from src.Figure import Figure


class Triangle(Figure):
    def __new__(cls, *sides):
        if len(sides) == 3 and (sides[0] > 2 and sides[1] > 2 and sides[2] > 2):
            if type(sides[0]) == int and type(sides[1]) == int and type(sides[2]) == int:
                obj = super().__new__(cls)
                return obj
            else:
                raise Exception('Input number')
        else:
            raise Exception('Input tree sides of triangle')

    def __init__(self, side1, side2, side3):
        if self.__class__ == Figure:
            raise Exception('Cannot instantiate abstract base class')
        self.name = 'Triangle'
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.sides = [self.side1, self.side2, self.side3]
        self.__area = None
        self.__perimeter = None

    @property
    def area(self):
        if self.__area is None:
            self.p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
            self.__area = math.sqrt(self.p * (self.p - self.sides[0]) * (self.p - self.sides[1]) * (self.p - self.sides[2]))
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = self.sides[0] + self.sides[1] + self.sides[2]
        return self.__perimeter
