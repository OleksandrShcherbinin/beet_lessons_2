import unittest
# ARRANGE
# ACT
# ASSERT

assert sum([1, 2, 3]) == 6, 'Should be 6'


def test_sum():
    assert sum([1, 2, 3]) == 6, 'Should be 6'


def test_sum_tuple():
    assert sum((1, 2, 3)) == 6, 'Should be 6'


# test_sum()
# test_sum_tuple()


def my_sum(*args):
    total = 0
    for num in args:
        total += num

    return total


class TestMySum(unittest.TestCase):

    def test_my_sum_success(self):
        data = [5, 6, 1]

        result = my_sum(*data)

        self.assertEqual(result, 12)

#
# if __name__ == '__main__':
#     unittest.main()
