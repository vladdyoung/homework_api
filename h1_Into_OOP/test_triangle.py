from h1_Into_OOP.src.Triangle import Triangle
from h1_Into_OOP.src.Square import Square
from h1_Into_OOP.src.Rectangle import Rectangle
from h1_Into_OOP.src.Circle import Circle


def test_triangle_create():
    triangle = Triangle(10, 12, 13)
    assert isinstance(triangle, Triangle), 'Triangle is not created'


def test_triangle_area_create():
    triangle = Triangle(10, 12, 3)
    assert hasattr(triangle, 'area'), 'Area of triangle is not created'


def test_triangle_perimeter_create():
    triangle = Triangle(10, 12, 3)
    assert hasattr(triangle, 'perimeter'), 'Perimeter of triangle is not created'


def test_triangle_name_is_present():
    triangle = Triangle(10, 12, 12)
    assert hasattr(triangle, 'name') and triangle.name == 'Triangle', 'Unknown figure'


def test_add_square_area():
    triangle = Triangle(14, 15, 5)
    square = Square(10)
    assert triangle is not None and triangle.add_figure(square) == triangle.area + square.area, 'Square area not added'


def test_add_rectangle_area():
    triangle = Triangle(14, 15, 5)
    rectangle = Rectangle(5, 6)
    assert triangle is not None and triangle.add_figure(rectangle) == triangle.area + rectangle.area, \
        'Rectangle area not added'


def test_add_circle_area():
    triangle = Triangle(14, 15, 5)
    circle = Circle(2)
    assert triangle is not None and triangle.add_figure(circle) == triangle.area + circle.area, 'Circle area not added'


def test_add_triangle_area():
    triangle = Triangle(14, 15, 5)
    assert triangle is not None and triangle.add_figure(triangle) == triangle.area + triangle.area, \
        'Triangle area not added'
