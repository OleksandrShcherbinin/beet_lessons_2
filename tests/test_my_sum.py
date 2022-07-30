from unittest import TestCase
from fractions import Fraction

from python_test import my_sum


class TestMySum(TestCase):

    def test_my_sum_success(self):
        data = [5, 6, 1]

        result = my_sum(*data)

        self.assertEqual(result, 12)

    def test_my_sum_tuple_success(self):
        data = (5, 6, 1)

        result = my_sum(*data)

        self.assertEqual(result, 12)

    def test_my_sum_fraction_success(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 4)]

        result = my_sum(*data)

        self.assertEqual(result, 1)

    def test_float_success(self):
        data = [0.5, 0.5, 0.5]

        result = my_sum(*data)

        self.assertEqual(result, 1.5)

    def test_bad_type(self):
        data = ['apple', 'banana']

        with self.assertRaises(TypeError):
            my_sum(*data)
