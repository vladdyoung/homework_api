from h1_Into_OOP.src.Figure import Figure


class Square(Figure):
    def __new__(cls, sides):
        if sides > 0:
            obj = super().__new__(cls)
            return obj
        else:
            raise ValueError('Input positive number')

    def __init__(self, sides):
        if self.__class__ == Figure:
            raise Exception('Cannot instantiate abstract base class')
        self.name = 'Square'
        self.sides = sides
        self.__area = None
        self.__perimeter = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.sides ** 2
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = self.sides * 4
        return self.__perimeter
