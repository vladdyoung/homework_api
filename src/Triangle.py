import math
from src.Figure import Figure


class Triangle(Figure):
    def __new__(cls, *sides):
        if len(sides) == 3 and (sides[0] > 2 and sides[1] > 2 and sides[2] > 2):
            if type(sides[0]) == int and type(sides[1]) == int and type(sides[2]) == int:
                obj = super().__new__(cls)
                p = (sides[0] + sides[1] + sides[2]) / 2
                obj.area = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
                obj.perimeter = sides[0] + sides[1] + sides[2]
                return obj
            else:
                return
        else:
            try:
                raise Exception
            except Exception as ex:
                return

    def __init__(self, side1, side2, side3):
        self.name = 'Triangle'
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.sides = [self.side1, self.side2, self.side3]
