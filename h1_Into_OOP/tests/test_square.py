from h1_Into_OOP.src.Triangle import Triangle
from h1_Into_OOP.src.Square import Square
from h1_Into_OOP.src.Rectangle import Rectangle
from h1_Into_OOP.src.Circle import Circle


def test_square_create():
    square = Square(10)
    assert isinstance(square, Square), 'Square is not created'


def test_square_area_create():
    square = Square(10)
    assert hasattr(square, 'area'), 'Area of square is not created'


def test_square_perimeter_create():
    square = Square(10)
    assert hasattr(square, 'perimeter'), 'Perimeter of square is not created'


def test_square_name_is_present():
    square = Square(10)
    assert hasattr(square, 'name') and square.name == 'Square', 'Unknown figure'


def test_add_square_area():
    square = Square(10)
    assert square is not None and square .add_figure(square) == square .area + square.area, 'Square area not added'


def test_add_rectangle_area():
    square = Square(10)
    rectangle = Rectangle(5, 6)
    assert square is not None and square.add_figure(rectangle) == square.area + rectangle.area, \
        'Rectangle area not added'


def test_add_circle_area():
    square = Square(10)
    circle = Circle(2)
    assert square is not None and square.add_figure(circle) == square.area + circle.area, 'Circle area not added'


def test_add_triangle_area():
    square = Square(10)
    triangle = Triangle(14, 15, 5)
    assert square is not None and triangle is not None \
           and square.add_figure(triangle) == square.area + triangle.area, 'Triangle area not added'
