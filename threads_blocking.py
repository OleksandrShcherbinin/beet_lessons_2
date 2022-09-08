import threading
from time import sleep


def fibonacci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


def say_hello_1(name):
    print('Function1 started')
    print(f'Hello {name}')
    fibonacci(20)
    # sleep(3)
    print('Function1 finished')


def say_hello_2(name):
    print('Function2 started')
    print(f'Hello {name}')
    # sleep(3)
    fibonacci(20)
    print('Function2 finished')


if __name__ == '__main__':
    print('Main start')
    # t1 = threading.Thread(target=say_hello_1, args=('Lev',))
    # t1.start()
    # t2 = threading.Thread(target=say_hello_2, args=('Oleg',))
    # t2.start()
    # t1.join()
    # t2.join()
    say_hello_1('Lev')
    say_hello_1('Oleg')
    print('Main finished')
