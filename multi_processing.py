import os
import multiprocessing

from dataclasses import dataclass
from time import time, sleep
from pprint import pprint
from concurrent.futures import ProcessPoolExecutor

from threads_blocking import fibonacci


@dataclass(frozen=True)
class Student:
    name: str
    age: int
    level: str


students = [
    Student('Oleg', 31, 'Junior'),
    Student('Vlad', 16, 'Trainee'),
    Student('Yurii', 36, 'Junior'),
    Student('Tetiana', 24, 'Junior'),
    Student('Olga', 27, 'Junior'),
    Student('Serhii', 25, 'Junior'),
    Student('Vlad', 44, 'Junior'),
    Student('Vadim', 24, 'Junior'),
    Student('Dmytro', 31, 'Junior'),
    Student('Mykola', 22, 'Junior'),
    Student('Lev', 24, 'Junior'),
]


def transform(student: Student):
    print(f'Processing record {student.name}, process_id:{os.getpid()}')
    fibonacci(35)
    result = {'name': student.name, 'year_born': 2022 - student.age}

    print(f'Finished processing record {student.name}, process_id:{os.getpid()}')
    return result


if __name__ == '__main__':

    t1 = time()

    # pool = multiprocessing.Pool()
    #
    # result = pool.map(transform, students)
    with ProcessPoolExecutor() as executor:
        # result = executor.map(transform, students)
        for student in students:
            result = executor.submit(transform, student)
            print(result)
    # pprint(list(result))

    print(f'Time spent to transform {time() - t1:.2f}')
