from random import randint
from time import perf_counter


def timer(function):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = function(*args, **kwargs)
        print(f'{function.__name__} took {perf_counter() - t1} seconds')
        return result
    return wrapper


# O(n^2)
@timer
def selection_sort(array):
    for i in range(len(array) - 1):

        min_value = array[i]
        min_value_index = i

        for j in range(i + 1, len(array)):
            if min_value > array[j]:
                min_value = array[j]
                min_value_index = j

        if min_value_index != i:
            temporary = array[i]
            array[i] = array[min_value_index]
            array[min_value_index] = temporary


items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
selection_sort(items)
print('Selection sort', items)
random_array = [randint(1, 1000) for _ in range(1000)]
#
selection_sort(random_array)


# O(n^2)
@timer
def bubble_sort(array):

    for i in range(len(array) - 1):
        already_sorted = True

        for j in range(len(array) - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break


items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
bubble_sort(items)
print('Bubble sort', items)
random_array = [randint(1, 1000) for _ in range(1000)]
#
bubble_sort(random_array)


# O(n^2)
@timer
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break


items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
insertion_sort(items)
print('Insertion sort', items)
random_array = [randint(1, 1000) for _ in range(1000)]

insertion_sort(random_array)


# O(n)
def merge_sorted_list(left, right):
    i = 0
    j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:] + right[j:]

    return merged


# O(n log n)
def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge_sorted_list(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:])
    )


items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
merged = merge_sort(items)
print('Merged sort', merged)
random_array = [randint(1, 1000) for _ in range(1000)]

t1 = perf_counter()
merge_sort(random_array)
print(perf_counter() - t1)


# # O(n log n)
def quick_sort(array):
    if len(array) > 1:
        pivot = array[randint(0, len(array) - 1)]

        low_values = [value for value in array if value < pivot]

        equal_values = [value for value in array if value == pivot]

        high_values = [value for value in array if value > pivot]

        array = quick_sort(low_values) + equal_values + quick_sort(high_values)

    return array


items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
quick = quick_sort(items)
print('Quick sort', quick)
random_array = [randint(1, 1000000) for _ in range(1000000)]

t1 = perf_counter()
quick_sort(random_array)
print(perf_counter() - t1)
