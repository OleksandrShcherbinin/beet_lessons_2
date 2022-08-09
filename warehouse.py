from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from uuid import uuid4


class MeasurementUnit(Enum):
    PIECE = 1
    GRAMS = 2
    LITRES = 2


@dataclass
class Product:
    name: str
    quantity: int
    price: Decimal
    measurement: MeasurementUnit = MeasurementUnit.PIECE
    sku: str = field(default_factory=uuid4)

    def __hash__(self) -> int:
        return hash(self.sku)


class WareHouseException(Exception):
    pass


class WareHouse:
    """ WareHouse works unlocked only with context manager. """

    def __init__(self):
        self._products: dict[uuid4, Product] = {}
        self.__locked = True

    @property
    def locked(self) -> bool:
        return self.__locked

    @locked.setter
    def locked(self, value: bool):
        self.__locked = value

    @property
    def total_amount(self) -> Decimal:
        return Decimal(sum(p.quantity * p.price for p in self._products.values()))

    def add(self, *products: Product) -> None:
        self._raise_if_locked()
        for product in products:
            in_stock = self._products.get(product.sku)
            if not in_stock:
                self._products[product.sku] = product
            else:
                in_stock.quantity += product.quantity

    def resupply(self, product: Product, quantity: int) -> None:
        self._raise_if_locked()

        product = self._products.get(product.sku)

        self._raise_if_not_product(product)

        product.quantity += quantity

    def remove(self, product: Product, quantity: int = 1) -> None:
        self._raise_if_locked()

        product = self._products.get(product.sku)

        self._raise_if_not_product(product)

        if (pieces := product.quantity) >= quantity:
            product.quantity -= quantity
        else:
            raise WareHouseException(f'There are only {pieces} left on stock')

    def _raise_if_locked(self):
        if self.locked:
            raise WareHouseException('WareHouse locked!')

    @staticmethod
    def _raise_if_not_product(product):
        if not product:
            raise WareHouseException(
                'Please add this product into warehouse first'
            )

    def __enter__(self):
        self.locked = False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.locked = True

    def __str__(self):
        return 'Amount of money products stored=' \
               f'{sum(p.quantity * p.price for p in self._products.values())}' \
               f', Number of positions={len(self._products)}'
