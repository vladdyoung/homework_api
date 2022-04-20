from src.Figure import Figure


class Rectangle(Figure):
    def __new__(cls, *sides):
        if len(sides) == 2:
            if sides[0] > 0 and sides[1] > 0:
                obj = super().__new__(cls)
                return obj
            else:
                raise Exception('Input two positive number')
        else:
            raise Exception('Input two sides of rectangle')

    def __init__(self, side1, side2):
        if self.__class__ == Figure:
            raise Exception('Cannot instantiate abstract base class')
        self.name = 'Rectangle'
        self.side1 = side1
        self.side2 = side2
        self.sides = [self.side1, self.side2]
        self.__area = None
        self.__perimeter = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.sides[0] * self.sides[1]
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = (self.sides[0] + self.sides[1]) * 2
        return self.__perimeter
