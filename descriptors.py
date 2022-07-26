class Engine:
    def __init__(self, capacity: int, turbocharged: bool = False):
        self.capacity = capacity
        self.turbocharged = turbocharged

    def __str__(self):
        return f'{self.capacity}, {self.turbocharged}'


class Car:
    def __init__(self, model, color, engine):
        self.model = model
        self.color = color
        self.engine = engine

    @classmethod
    def corola(cls, color):
        engine = Engine(2000)
        return cls('Corola', color, engine)

    @classmethod
    def camry_red(cls):
        engine = Engine(2500)
        return cls('Corola', 'Red', engine)

    @classmethod
    def land_cruiser(cls, color):
        engine = Engine(3000, True)
        return cls('Land Cruiser', color, engine)

    def __str__(self):
        return f'{self.model}, {self.color}, {self.engine}'


engine_1 = Engine(2000)
engine_2 = Engine(3000)

car_1 = Car('Corola', 'Red', engine_1)
car_2 = Car('Camry', 'Red', engine_2)

car_3 = Car.camry_red()


class Book:
    num_books = 0

    def __init__(self, name):
        self.name_book = name
        Book.num_books += 1

    @classmethod
    def books_count(cls):
        return cls.num_books


b1 = Book('Hary Poter')
b2 = Book('Zapovit')

# print(Book.books_count())


class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        print('Get')
        return self._radius

    def set_radius(self, value):
        print('Set')
        self._radius = value

    def del_radius(self):
        print('Delete')
        del self._radius

    radius = property(
        fget=get_radius,
        fset=set_radius,
        fdel=del_radius,
        doc="Radius property"
    )


# circle = Circle(10)
#
# print(circle.radius)
# circle.radius = 20
# print(circle.radius)
#
# del circle.radius


class Circle2:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """ Radius """
        print('Get')
        return self._radius

    @radius.setter
    def radius(self, value):
        print('Set')
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2


# circle = Circle2(10)
# print(circle.radius)
#
# print(circle.diameter)
#
# circle.diameter = 50
#
# print(circle.radius)

import os
import hashlib


class User:
    def __init__(self, email):
        self.email = email
        self.__password = None

    @property
    def password(self):
        raise AttributeError('You can not see password.')

    @password.setter
    def password(self, value):
        salt = os.urandom(32)
        self.__password = hashlib.pbkdf2_hmac(
            'sha256', value.encode('utf-8'), salt, 10000
        )
        print(self.__password)


# user = User('test@email.com')
#
# user.password = 'qwerty'
# print(user._User__password)


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Employee(Person):

    @property
    def name(self):
        return super().name.upper()


e = Employee('Oleg')

# print(e.name)


class Coordinate:
    #
    # def __init__(self, name):
    #     self.name = name

    def __set_name__(self, owner, name):
        print()
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        print()
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if isinstance(value, int) or isinstance(value, float):
            setattr(instance, self.name, value)

        else:
            raise ValueError()


class Point3D:
    x = Coordinate()
    y = Coordinate()
    z = Coordinate()

    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return f'{self.__class__.__name__} x={self.x}, y={self.y}, z={self.z}'


point = Point3D()

point.x = 20
point.y = 12.0

print(point.__dict__)
print('*' * 20)
print(point.__class__.__dict__)

getattr(point, 'hello', None)

setattr(point, 'hello', 'Hello')

print(point.hello)

