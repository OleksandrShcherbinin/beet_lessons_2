from abc import ABC, abstractmethod


class MyClass(object):
    pass


class Engine:
    def __init__(self, cylinders, capacity, fuel_type):
        self.cylinders = cylinders
        self.capacity = capacity
        self.fuel_type = fuel_type

    def start(self):
        print('Engine starts')

    def stop(self):
        print('Engine stops')


class Car:

    NUMBER_OF_WHEELS = 4

    def __init__(
            self,
            color: str,
            model: str,
            price: int,
            # engine: Engine
    ):
        self.color = color
        self.model = model
        self.price = price
        self.engine = None

    def attach_engine(self, engine):
        self.engine = engine

    def go(self):
        print(f'{self.model} goes!!!')
        self.engine = Engine(4, 2, 'Gasoline')

    def stop(self):
        print(f'{self.model} stopped')


class Employee(ABC):

    @abstractmethod
    def work(self):
        pass


class CarDriver(Employee):

    def work(self):
        print(f'{self.__class__.__name__} drives')


class Waiter(Employee):

    def work(self):
        print(f'{self.__class__.__name__} serves food and drinks')


###########################################################
# MULTIPLE INHERITANCE


# class Square:
#     def __init__(self, length):
#         self.length = length
#
#     def area(self):
#         return self.length ** 2
#
#     def perimeter(self):
#         return self.length * 4


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# class Cube(Square):
#     # def surface_area(self):
#     #     return self.area() * 6
#
#     def volume(self):
#         surface = self.area()
#         return surface * self.length
#
#     def perimeter(self):
#         print('No perimeter')


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


class Pyramid(Triangle, Square):
    def __init__(self, base, height):
        self.base = base
        self.height = height


class A:
    def __init__(self):
        print('A')
        super().__init__()


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class C:
    def __init__(self):
        print('C')
        super().__init__()


class Forward(B, C):
    def __init__(self):
        print('Forward')
        super().__init__()


class Back(C, B):
    def __init__(self):
        print('Back')
        super().__init__()


class Pyramid2(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs['height'] = slant_height
        kwargs['length'] = base
        super().__init__(base=base, **kwargs)


class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)

        return surface_area


class Cube(SurfaceAreaMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [
            Square,
            Square,
            Square,
            Square,
            Square,
            Square
        ]

    def volume(self):
        surface = self.area()
        return surface * self.length

    def perimeter(self):
        print('No perimeter')


class Pyramid3(Square, Triangle, SurfaceAreaMixin):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        self.height = slant_height
        self.length = base
        self.width = base

        self.surfaces = [
            Square,
            Triangle,
            Triangle,
            Triangle,
            Triangle
        ]


def main():
    # c = MyClass()
    # print(dir(c))
    #
    # o = object()
    #
    # print(dir(o))
    # engine = Engine(8, 4, 'Diesel')
    #
    # car = Car('Red', 'BMW', 50000, engine)
    #
    # car.engine.start()
    # print(car.engine.fuel_type)
    # car.go()
    # car.stop()
    # car.engine.stop()
    #
    # engine.start()
    #
    # driver = CarDriver()
    # driver.work()
    #
    # waiter = Waiter()
    # waiter.work()
    #
    # employee = Employee()
    # employee.work()
    #
    # square = Square(20)
    # print(square.perimeter())
    # print(square.area())
    # print(square.__class__.__bases__)
    # cube = Cube(20)
    # volume = cube.volume()
    # print(volume)
    # cube.perimeter()
    # perimeter = super(Cube, cube).perimeter()
    # print(perimeter)
    # pyramid = Pyramid(20, 12)
    # print(pyramid.__class__.__bases__)
    # print(Pyramid.mro())
    # print(Pyramid.__mro__)
    #
    # forward = Forward()
    # print('-' * 80)
    # backward = Back()
    cube = Cube(10)
    print(cube.surface_area())
    pyramid = Pyramid3(10, 10)
    print((pyramid.surface_area()))


if __name__ == '__main__':
    main()
