from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError('Please implement method perimeter')

    @abstractmethod
    def draw(self):
        pass


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def draw(self):
        print(f'Draw {self.__class__.__name__}')


class Square:
    def __init__(self, length):
        self.length = length

    def perimeter(self):
        return self.length * 4

    def draw(self):
        print(f'Draw {self.__class__.__name__}')


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def draw(self):
        print(f'Draw {self.__class__.__name__}')


rect = Rectangle(10, 20)
square = Square(10)
triangle = Triangle(10, 20, 10)

geom_list = [rect, square, triangle]

for figure in geom_list:
    print(figure.perimeter())


class GraphicEditor:

    def draw(self, figure):
        figure.draw()


editor = GraphicEditor()

editor.draw(square)
editor.draw(triangle)
editor.draw(rect)


class PointSingelton:
    count = 0
    instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, cls):
            cls.instance = super().__new__(cls)
            cls.count += 1
        else:
            print('Instance already created')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = PointSingelton(1, 1)
p2 = PointSingelton(1, 10)
p3 = PointSingelton(10, 15)
