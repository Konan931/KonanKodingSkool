import math
from teach_goio import area_rectangle, area_circle, area_triangle, area_square, area_ellipse, parse_and_convert_classname


def test_area_rectangle():
    assert area_rectangle(3, 4) == 12.0


def test_area_circle():
    assert math.isclose(area_circle(2), math.pi * 4)


def test_area_triangle():
    assert area_triangle(6, 4) == 12.0


def test_area_square():
    assert area_square(5) == 25.0


def test_area_ellipse():
    assert math.isclose(area_ellipse(3, 2), math.pi * 6)


def test_parse_binary_tag():
    conv = parse_and_convert_classname('#h/10001001')
    assert conv['dec'] == 137
    assert conv['hex'] == hex(137)
