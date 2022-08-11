from typing import Callable, Union, Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field, InitVar
from itertools import count


def my_func(a: int, b: str) -> str:
    return str(a) + b


weird_dict = Dict[
    Union[int,  str],
    Union[
        List[int],
        Tuple[int, int],
        Callable[[int, str], str]
    ]
]

my_dict: weird_dict = {
    1: [1, 2, 3, 4, 5],
    'Oleg': (1, 'a'),  # type: ignore
    2: my_func
}


# def group_by_author(self, author_name: str) -> list[Book] | None:
#     for author in self.authors:
#         if author_name != author.name:
#             return author.books
#     return None


class Person:
    species = 'Human'

    __slots__ = 'first_name', 'last_name', 'age', 'address'

    def __init__(self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.age == other.age


# person = Person('Oleg', 'Bondar', 31, 'Zhmerynka')
# person_2 = Person('Alex', 'Shcherbinin', 31, 'Cherkasy')

# print(person)
#
# print(person == person_2)


@dataclass
class Address:
    street: str
    city: str
    region: str
    zip_code: int
    apartment: str | None = None


# @dataclass(frozen=True)
# @dataclass(order=True)
# @dataclass(kw_only=True)
# @dataclass(slots=True)
@dataclass
class PersonData:
    first_name: str = field(compare=False)
    last_name: str = field(compare=False)
    age: int
    address: Address = field(repr=False, compare=False)
    active: bool = True
    hobbies: list[str] = field(default_factory=list)
    id_: int = field(default_factory=count(1).__next__, init=False)
    # full_name: str | None = None
    #
    # def __post_init__(self):
    #     self.full_name = f'{self.first_name} {self.last_name}'
    #
    # def say_hello(self):
    #     return f'Hello {self.full_name}'


address = Address(
    'Shevchenka St',
    'Zhmerynka',
    'Vinnytska region',
    10000,
)
person_2 = PersonData('Alex', 'Bondar', 32, address)
person = PersonData('Oleg', 'Bondar', 31, address)
person_3 = PersonData('Yurii', 'Bondar', 31, address)


print(person)
print(person == person_2)
person.hobbies.append('Books')

# person.age = 20

print(person)
print(person_2)
print(person_3)
# print(person.full_name)
# person.full_name = 'Hello'
# print(person.say_hello())
# person.first_name = 'Alex'
print(person.__dict__)


@dataclass
class C:
    i: int
    j: int = None
    # database: InitVar[str] = None

    def __post_init__(self):
        if self.j is None and database is not None:
            self.j = database


c = C(10)

print(c)
