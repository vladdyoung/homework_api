from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


def test_rectangle_create():
    rectangle = Rectangle(10, 5)
    assert isinstance(rectangle, Rectangle), 'Rectangle is not created'


def test_rectangle_area_create():
    rectangle = Rectangle(10, 12)
    assert hasattr(rectangle, 'area'), 'Area of rectangle is not created'


def test_rectangle_perimeter_create():
    rectangle = Rectangle(10, 12)
    assert hasattr(rectangle, 'perimeter'), 'Perimeter of rectangle is not created'


def test_rectangle_name_is_present():
    rectangle = Rectangle(10, 5)
    assert hasattr(rectangle, 'name') and rectangle.name == 'Rectangle', 'Unknown figure'


def test_add_square_area():
    rectangle = Rectangle(10, 12)
    square = Square(10)
    assert rectangle is not None and rectangle.add_figure(square) == rectangle.area + square.area, \
        'Square area not added'


def test_add_rectangle_area():
    rectangle = Rectangle(5, 6)
    assert rectangle is not None and rectangle.add_figure(rectangle) == rectangle.area + rectangle.area, \
        'Rectangle area not added'


def test_add_circle_area():
    rectangle = Rectangle(5, 6)
    circle = Circle(2)
    assert rectangle is not None and rectangle.add_figure(circle) == rectangle.area + circle.area, \
        'Circle area not added'


def test_add_triangle_area():
    rectangle = Rectangle(5, 6)
    triangle = Triangle(14, 15, 5)
    assert rectangle is not None and triangle is not None and \
           rectangle.add_figure(triangle) == rectangle.area + triangle.area, 'Triangle area not added'
