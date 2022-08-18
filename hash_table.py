a = 'Hello' * 1000

print(hash(a))
print(hash(a))
print(hash(a))
print(hash(12342342442))

print(hash(322818021289917443))
print(hash(3.14))


class Person:

    def __hash__(self):
        return 1


print(hash(None))
print(hash(hash))
print(hash(Person))
print(hash(Person()))

print(id('Hello'))

print(hash('Hello'))


def simple_hash_func(text):
    return sum(ord(symbol) for symbol in text)


print('*' * 80)
print(simple_hash_func('hello'))
print(simple_hash_func('hello'))


def simple_hash_func(key):
    return sum(ord(symbol) for symbol in str(key))


print('*' * 80)
print(simple_hash_func(3.14))
print(simple_hash_func(True))
print(simple_hash_func('hello'))

print(simple_hash_func('Hello'))
print(simple_hash_func('elloH'))

print(simple_hash_func('3.14'))
print(simple_hash_func(3.14))


def simple_hash_func(key):
    return sum(ord(symbol) for symbol in repr(key))


print('*' * 80)
print(repr('3.14'))
print(repr(3.14))
print(simple_hash_func('3.14'))
print(simple_hash_func(3.14))

print(simple_hash_func('Hello'))
print(simple_hash_func('eloHl'))

from time import time


time_stamp = time()


def simple_hash_func(key):
    return sum(
        time_stamp * index * ord(symbol)
        for index, symbol in enumerate(repr(key), start=1)
    )


print('*' * 80)
print(simple_hash_func('Hello' * 1000))
print(simple_hash_func('eloHl'))

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Pair:
    key: Any
    value: Any


BLANK = object()


class HashTable:

    def __init__(self, capacity):
        self._pairs = capacity * [BLANK]

    def __len__(self):
        return len(self._pairs)

    def __setitem__(self, key, value):
        self._pairs[self._index(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self._pairs[self._index(key)]
        if pair is BLANK:
            raise KeyError(key)

        return pair.value

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)

    def __iter__(self):
        yield from self.pairs

    def _index(self, key):
        return hash(key) % len(self)

    @property
    def pairs(self):
        return {pair for pair in self._pairs}


print('*' * 80)
table = HashTable(3)

# print(len(table))

table['Oleg'] = 'Senior Python developer'
table['Yurii'] = 'Team lead'
table['Tetiana'] = 'Data scientist'

print(table['Oleg'])
print(table['Tetiana'])
print(table['Yurii'])

print('Lev' in table)

print(table.get('Yurii'))

for i in table:
    print(i)

print(table.pairs)
