list_numbers = [1, 2, 3, 4, 5]
set_numbers = {1, 2, 3, 4, 5}
# index = 0
#
#
# while index < len(list_numbers):
#     print(list_numbers[index])
#     index += 1

# for i in list_numbers:
#     print(i)


# print(dir(list_numbers))
# print(dir(set_numbers))
#
# iterator = iter(set_numbers)
#
# print(next(iterator))


def for_loop(iterable):
    iterator = iter(iterable)
    next_element_exists = True

    while next_element_exists:
        try:
            from_iterator = next(iterator)
            print(from_iterator)
        except StopIteration:
            next_element_exists = False


# for_loop(set_numbers)


class InfiniteIterator:
    def __init__(self, initial_number):
        self._number = initial_number

    def __iter__(self):
        return self

    def __next__(self):
        self._number = self._number ** 2
        return self._number


iterator = InfiniteIterator(2)
#
# for i in iterator:
#     print(i)


# for i in range(1, 10, 2):
#     print(i)


class FloatIterator:
    def __init__(self, start=0.0, stop=0.0, step=0.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value

        else:
            raise StopIteration


float_iter = FloatIterator(1, 10, 0.5)

# for i in float_iter:
#     print(i)
#
# for i in float_iter:
#     print(i)


class FibonacciIterator:

    ZERO = 0
    ONE = 1
    COUNTER = 0

    def __init__(self, position):
        self.position = position
        self.previous = self.ONE
        self.before_previous = self.ZERO
        self.value = 0

    def __iter__(self):
        if self.position < 0:
            raise ValueError('Only positive number')

        return self

    def __next__(self):
        if self.COUNTER == self.position:
            raise StopIteration

        self.COUNTER += 1

        if self.position == 0 or self.COUNTER == 1:
            return self.ZERO

        if self.position == 1 or self.COUNTER == 2:
            return self.ONE

        self.value = self.before_previous + self.previous
        self.before_previous = self.previous
        self.previous = self.value

        return self.value


import sys


fibonacci = FibonacciIterator(100000)

# for i in fibonacci:
#     print(i, end=',')


# compr = [i * 2 for i in range(100000)]

# print('SIZE', sys.getsizeof(fibonacci))
# print('SIZE', sys.getsizeof(compr))

###############################################################################
# Generators


def infinite():
    num = 0
    while True:
        yield num
        num += 1
        yield 'Second yield'

        yield 'Third'


inf = infinite()



# for i in inf:
#
#     print(i)


def limited(limit: int):
    num = 0
    while num <= limit:
        yield num
        num += 1


lim = limited(10)

# for i in lim:
#     print(i)
#
# for i in lim:
#     print(i)


def restartable():
    num = 0
    while True:
        value = (yield num)
        if value == 'restart':
            num = 0
        if value == 'stop':
            break
        else:
            num += 1


restart = restartable()

for i in restart:
    print(i)
    if i == 10:
        restart.send('')
        # restart.throw(Exception('Error'))


squares = [num ** 2 for num in range(100000)]

squares_gen = (num ** 2 for num in range(100))

# print(sys.getsizeof(squares))
#
# print(sys.getsizeof(squares_gen))

import cProfile
#
# for i in squares_gen:
#     print(i)


# cProfile.run('sum([num ** 2 for num in range(100000)])')
#
# cProfile.run('sum((num ** 2 for num in range(100000)))')

file_name = 'Gross-domestic-product-March-2022-quarter-visualisation-csv.csv'

lines = (line for line in open(file_name))

list_rows = (row.strip().split(',') for row in lines)

columns = next(list_rows)

industries_dict = (dict(zip(columns, data)) for data in list_rows)

GDP = (
    float(industry['Amount'])
    for industry in industries_dict
    if industry['Description'] == 'Mining'
)

total = sum(GDP)



# print('Agriculture GDP sum', total)

