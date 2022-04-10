import math
from src.Figure import Figure


class Circle(Figure):
    def __new__(cls, radius):
        if radius > 0:
            obj = super().__new__(cls)
            obj.area = math.pi * (radius ** 2)
            obj.perimeter = 2 * math.pi * radius
            return obj
        else:
            try:
                raise Exception
            except Exception as ex:
                return

    def __init__(self, radius):
        self.name = 'Circle'
        self.radius = radius
