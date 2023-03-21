from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


def test_square_create():
    circle = Circle(10)
    assert isinstance(circle, Circle), 'Circle is not created'


def test_square_area_create():
    circle = Circle(10)
    assert hasattr(circle, 'area'), 'Area of circle is not created'


def test_square_perimeter_create():
    circle = Circle(10)
    assert hasattr(circle, 'perimeter'), 'Perimeter of circle is not created'


def test_square_name_is_present():
    circle = Circle(10)
    assert hasattr(circle, 'name') and circle.name == 'Circle', 'Unknown figure'


def test_add_square_area():
    circle = Circle(10)
    square = Square(10)
    assert circle is not None and circle.add_figure(square) == circle.area + square.area, \
        'Square area not added'


def test_add_rectangle_area():
    circle = Circle(10)
    rectangle = Rectangle(5, 6)
    assert circle is not None and circle.add_figure(rectangle) == circle.area + rectangle.area, \
        'Rectangle area not added'


def test_add_circle_area():
    circle = Circle(2)
    assert circle is not None and circle.add_figure(circle) == circle.area + circle.area, 'Circle area not added'


def test_add_triangle_area():
    circle = Circle(2)
    triangle = Triangle(14, 15, 5)
    assert circle is not None and circle is not None \
           and circle.add_figure(triangle) == circle.area + triangle.area, 'Triangle area not added'
