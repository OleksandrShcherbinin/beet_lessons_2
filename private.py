class Point:

    __SIZE = 5

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_coordinates(self):
        return self.__x, self.__y

    def set_coordinates(self, x, y):
        if self.__validate_coordinates(x) and self.__validate_coordinates(y):
            self.__x = x
            self.__y = y
        else:
            print('Attributes must be int or float')

    @staticmethod
    def __validate_coordinates(value):
        if isinstance(value, int) or isinstance(value, float):
            return True

        return False

    def __setattr__(self, key, value):
        if key == f'_Point__SIZE':
            raise AttributeError('You can not assign __SIZE')
        else:
            self.__dict__[key] = value

    def __getattribute__(self, item):
        if item == '_Point__SIZE':
            raise AttributeError('It is private')
        else:
            return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print('No such attribute')
        self.__dict__[item] = None
        return item

    def __delattr__(self, item):
        print(f'No such attribute {item}')

    def __del__(self):
        print('Object deleted')
        del self


class Line(Point):

    def get_line_points(self):
        return self.get_coordinates()

    def __len__(self):
        return 100


point = Point()
# print(dir(point))
# print(point.get_coordinates())
# print(point._Point__validate_coordinates(20))
# print(point._Point__x)
# point._Point__x = 10
# print(point._Point__SIZE)
# point._Point__SIZE = 10
#
point.hello = 'Hello'
#
# print(point.__dict__)

# line = Line(10, 20)
# print(line.get_line_points())

# print(point.good_buy)
#
# print(point.good_buy)
#
# del point.no_attribute
#
# del point
# print(point)

line = Line(10, 10)

print(len(line))
