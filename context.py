import os
from decimal import Decimal, localcontext

# with open('.gitignore') as file:
#     for line in file:
#         print(line)
#
#
# file_object = open('.gitignore')
#
# try:
#     text = file_object.read()
#     print(text)
# finally:
#     file_object.close()


# with os.scandir('.') as items:
#     for item in items:
#         print(item.name, '->', item.stat().st_size, 'bytes')

# with localcontext() as context:
#     context.prec = 100
#     print(Decimal('1') / Decimal('13'))


class HelloWorldContextManager:

    def __enter__(self):
        print('Enter')
        return 'Hello world'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')
        print(exc_type, exc_val, exc_tb)


# with HelloWorldContextManager() as hello:
#     print(hello)


class MyFile:

    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# with MyFile('.gitignore') as file:
#     for line in file:
#         print(line)

# my_file = MyFile('.gitignore')

# print(my_file)
# print(my_file.file)
import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        self.end = 0
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(self.end - self.start)


# timer = Timer()
#
# with timer:
#     time.sleep(1)
#     time.sleep(1.5)


from contextlib import contextmanager


@contextmanager
def my_file(name, mode='r'):
    try:
        file = open(name, mode)
        yield file
    finally:
        file.close()


with my_file('.gitignore') as f:
    for line in f:
        print(line)


