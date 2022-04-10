from src.Figure import Figure


class Rectangle(Figure):
    def __new__(cls, *sides):
        if len(sides) == 2:
            if sides[0] > 0 and sides[1] > 0:
                obj = super().__new__(cls)
                obj.area = sides[0] * sides[1]
                obj.perimeter = (sides[0] + sides[1]) * 2
                return obj
            else:
                try:
                    raise Exception
                except Exception as ex:
                    return
        else:
            try:
                raise Exception
            except Exception as ex:
                return

    def __init__(self, side1, side2):
        self.name = 'Rectangle'
        self.side1 = side1
        self.side2 = side2
        self.sides = [self.side1, self.side2]

