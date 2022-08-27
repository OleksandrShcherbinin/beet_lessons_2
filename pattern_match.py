from dataclasses import dataclass
from typing import Literal


def greet(name):
    match name:
        case 'Oleg':
            print(f'Very glad to see you {name.upper()}')
        case 'Tetiana':
            print(f'You are very nice {name}')
        case _:
            print(f'Hello {name.upper()}')


# greet('Oleg')
# greet('Tetiana')
# greet('Yurii')


def command_split(command):
    match command.split():
        case ['make']:
            print('Make')
        case ['make', command]:
            print(f'Make {command}')
        case ['restart']:
            print('Restarting')
        case ['rm', *files]:
            print(f'Removing {files}')
        case _:
            print('No such command')


command_split('make')
command_split('make script')
command_split('restart')
command_split('rm file1.py file2.py file3.py')


def match_command(command):
    match command.split():
        case ['north'] | ['go', 'north']:
            print('Go north')
        case ['get', obj] | ['pick', obj] | ['pick', 'up', obj] | ['pick', obj, 'up']:
            print(f'Picking {obj}')


match_command('north')
match_command('go north')

match_command('get sword')
match_command('pick axe')
match_command('pick up bow')
match_command('pick bow up')


def match_subpattern(command):
    match command.split():
        case ['go', ('north' | 'south' | 'west' | 'east') as direction]:
            print(f'Go {direction}')
        case _:
            print('Russian warship go fuck yourself')


match_subpattern('go west')


@dataclass
class Click:
    position: tuple[int, int]
    button: Literal['left', 'right']


@dataclass
class KeyPress:
    key_name: str


@dataclass
class Quit:
    pass


def match_event(event):
    match event:
        case Click(position=(x, y), button='left'):
            print(f'Left button clicked position x={x}, y={y}')
        case Click(position=(x, y), button='right'):
            print(f'Right button clicked position x={x}, y={y}')
        case KeyPress(key_name=key_name):
            print(f'Pressed {key_name}')
        case other_event:
            print(f'Other event {other_event}')


match_event(Click((100, 101), 'left'))
match_event(Click((0, 0), 'right'))
match_event(KeyPress('Enter'))
match_event('Hello')


def sum_list(numbers):
    match numbers:
        case []:
            return 0
        case [int(first) | float(first), *rest]:
            return first + sum_list(rest)
        case _:
            print('Only numbers')


# my_list = [1, 2, 3, 4, 5, 'Oleg']
#
# print(sum_list(my_list))


def pattern_sort(list_):
    match list_:
        case [] | [_]:
            return list_
        case [x, y] if x <= y:
            return list_
        case [x, y]:
            return [y, x]
        case [x, y, z] if x <= y <= z:
            return list_
        case [x, y, z] if x >= y >= z:
            return [z, y, x]
        case [pivot, *rest]:
            low = pattern_sort([x for x in rest if x <= pivot])
            high = pattern_sort([x for x in rest if pivot < x])
            return low + [pivot] + high


unsorted = [4, 2, 1]

print(pattern_sort(unsorted))

