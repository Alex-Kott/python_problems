from math import sqrt
from typing import Union


class Point:
    x: float
    y: float

    def __init__(self, x: Union[float, int], y: Union[float, int]):
        self.x = float(x)
        self.y = float(y)


class Triangle:
    a: Point
    b: Point
    c: Point

    def __init__(self, a: Point, b: Point, c: Point) -> None:
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self) -> float:
        ab_length = calc_length(self.a, self.b)
        bc_length = calc_length(self.b, self.c)
        ca_length = calc_length(self.c, self.a)

        perimeter = ab_length + bc_length + ca_length

        return perimeter


def calc_length(a: Point, b: Point) -> float:
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def main() -> None:
    input_data = input("Input coords (x1, y1, x2, y2, x3, y3):")
    x1, y1, x2, y2, x3, y3 = input_data.split(" ")
    a = Point(x1, y1)
    b = Point(x2, y2)
    c = Point(x3, y3)

    triangle = Triangle(a, b, c)
    triangle_perimeter = triangle.calc_perimeter()

    print(triangle_perimeter)


if __name__ == "__main__":
    main()
