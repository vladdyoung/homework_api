from src.Figure import Figure


class Square(Figure):
    def __new__(cls, sides):
        if sides > 0:
            obj = super().__new__(cls)
            obj.area = sides ** 2
            obj.perimeter = sides * 4
            return obj
        else:
            try:
                raise Exception
            except Exception as ex:
                return

    def __init__(self, sides):
        self.name = 'Square'
        self.sides = sides
