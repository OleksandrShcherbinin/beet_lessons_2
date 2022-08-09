from abc import ABC, abstractmethod
from enum import Enum
from typing import Iterable


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size


class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args: Specification):
        self.args = args

    def is_satisfied(self, item: Product):
        return all(map(
            lambda specification: specification.is_satisfied(item), self.args
        ))


class OrSpecification(Specification):
    def __init__(self, *args: Specification):
        self.args = args

    def is_satisfied(self, item: Product):
        return any(map(
            lambda specification: specification.is_satisfied(item), self.args
        ))


class Filter(ABC):
    @abstractmethod
    def filter(self, items, specification):
        pass


class ProductFilter(Filter):
    def filter(self, items: Iterable[Product], specification: Specification):
        for item in items:
            if specification.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('apple', Color.GREEN, Size.SMALL)
    tree = Product('tree', Color.GREEN, Size.LARGE)
    house = Product('house', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    product_filter = ProductFilter()
    print('Green products:')
    green = ColorSpecification(Color.GREEN)
    for product in product_filter.filter(products, green):
        print(f'{product.name} is GREEN')

    print('Large size products:')
    large = SizeSpecification(Size.LARGE)
    for product in product_filter.filter(products, large):
        print(f'{product.name} is LARGE')

    print('Large blue items')
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for product in product_filter.filter(products, large_blue):
        print(f'{product.name} is LARGE and BLUE')

    large_and_blue = large & ColorSpecification(Color.BLUE)
    for product in product_filter.filter(products, large_and_blue):
        print(f'{product.name} is LARGE and BLUE with __and__ overload')

    large_or_green = OrSpecification(large, ColorSpecification(Color.GREEN))
    for product in product_filter.filter(products, large_or_green):
        print(f'{product.name} is LARGE or GREEN')

    large_or_green = large | ColorSpecification(Color.GREEN)
    for product in product_filter.filter(products, large_or_green):
        print(f'{product.name} is LARGE or BLUE with __or__ overload')
