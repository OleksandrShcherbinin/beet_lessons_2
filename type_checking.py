# dynamic typing
if False:
    var = 1 + "two"  # This line never runs, so no TypeError is raised
else:
    var = 1 + 2

print(var)

# String thing;
# thing = "Hello";

from datetime import datetime
from zoneinfo import ZoneInfo


def greet_period(hour):
    if 6 <= hour <= 10:
        return 'Good morning'
    if 10 < hour <= 18:
        return 'Good day'
    if 18 < hour <= 22:
        return 'Good evening'
    else:
        return 'Good night'


def greet_person(name, time_based=True):
    time_hour = datetime.now(ZoneInfo('Europe/Kiev')).time().hour
    greeting = greet_period(time_hour)
    if not time_based:
        return f'Hello {name.title()}'
    return f'{greeting} {name}'


print(greet_person('Alex'))


def greet_period_typed(hour: int) -> str:
    if 6 <= hour <= 10:
        return 'Good morning'
    if 10 < hour <= 18:
        return 'Good day'
    if 18 < hour <= 22:
        return 'Good evening'
    else:
        return 'Good night'


def greet_person_typed(name: str, time_based: bool = True) -> str:
    time_hour = datetime.now(ZoneInfo('Europe/Kiev')).time().hour
    greeting = greet_period_typed(time_hour)
    if not time_based:
        return f'Hello {name.title()}'
    return f'{greeting} {name}'


print(greet_person('Alex'))


print(greet_person_typed('Alex', time_based=False))

print(greet_person_typed('Alex', time_based='No'))

# Переваги перевірки типів:
# 1. Виявлення помилок на етапі написання коду
# 2. Краща документація коду
# 3. Коаща робота IDE та лінтерів


# Недоліки:
# 1. Більше часу на написання коду
# 2. Повільніше виконання коду дуже трошки

# час на завантаження модулю
# python -m timeit "import typing"

# ANNOTATIONS from python 3.0
import math


def circle_area(radius: float) -> float:
    return (math.pi * radius) ** 2


print(circle_area.__annotations__)


import math
# reveal_type(math.pi)
#
# radius = 1
# circle_area = (math.pi * radius) ** 2
# reveal_locals()
# mypy type_checking.py

pi: float = 3.14


def circumference(radius: float) -> float:
    return 2 * pi * radius


print(__annotations__)


def nive_title(text, width=80, fill_char='-'):
    # type: (str, int, str) -> str
    return f' {text.title()} '.center(width, fill_char)


print(nive_title("type comments work", width=40))


def nice_title(
    text,           # type: str
    width=80,       # type: int
    fill_char='-',  # type: str
):                  # type: (...) -> str
    return f' {text.title()} '.center(width, fill_char)


print(nice_title("type comments work", width=40))
