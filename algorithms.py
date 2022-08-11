from time import sleep, time
# O(1)
my_list = range(1, 65)


def get_length(list_):
    return len(list_)


# print(get_length(my_list))

# O(n)
# t1 = time()
for i in my_list:
    print(i)
#     # sleep(1)
# for i in my_list:
#     print(i)
#
# for i in my_list:
#     print(i)
#
#
# t2 = time()
# print(t2 - t1)
# O(n2)
# for i in range(10):
#     for j in range(10):
#         print(i + j)
#
#
# # O(n2)
# for i in range(10):
#     for j in range(i, 10):
#         print(j)


# O (log n)
def binary_search(list_, item_find):
    low = 0
    high = len(list_) - 1
    step_counter = 0

    while low <= high:
        step_counter += 1
        middle = int((low + high) / 2)

        match = list_[middle]

        if match == item_find:
            print('Index', match)
            print('Steps', step_counter)
            return middle
        if match > item_find:
            high = middle - 1
        else:
            low = middle + 1

    return None

# log 2 64 = 8
binary_search(my_list, 64)

# O(2n)
# O(n!)

