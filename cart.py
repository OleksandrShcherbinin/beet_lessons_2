from uuid import uuid4

from warehouse import Product, WareHouse, WareHouseException


class CartException(Exception):
    pass


class Cart:
    def __init__(self, warehouse: WareHouse):
        self._warehouse = warehouse
        self._products: dict[uuid4, Product] = {}
        self.__income = 0

    @property
    def check(self) -> str:
        check = '\n'.join(
            {f'name: {p.name}, quantity: {p.quantity}, '
             f'price: {p.price}, amount={p.quantity * p.price}'
             for p in self._products.values()}
        )
        self.income = sum(p.price * p.quantity for p in self._products.values())
        return f'{check}\nTotal: {self.income}'

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        self.__income = value

    def add(self, product: Product, quantity: int = 1) -> None:
        self._raise_if_locked()

        self._warehouse.remove(product, quantity)

        self._products[product.sku] = Product(
            name=product.name,
            measurement=product.measurement,
            price=product.price,
            quantity=quantity,
            sku=product.sku
        )

    def remove(self, product: Product, quantity: int = 1) -> None:
        self._raise_if_locked()

        product = self._products.get(product.sku)

        if not product:
            raise CartException('No such product in the cart')

        if (pieces := product.quantity) >= quantity:
            product.quantity -= quantity

        if pieces < quantity:
            raise CartException(f'There are only {pieces} pieces inside cart')

        self._move_back_to_warehouse(product, quantity)

    def sell(self) -> None:
        if not self._products or all(p.quantity == 0 for p in self._products.values()):
            raise CartException('Cart is empty, there is nothing to sell')

        print(self.check)
        self._products.clear()

    def _raise_if_locked(self):
        if self._warehouse.locked:
            raise WareHouseException('WareHouse locked!')

    def _move_back_to_warehouse(self, product: Product, quantity: int) -> None:
        self._warehouse.resupply(product, quantity)

    def __str__(self) -> str:
        return 'Amount of money products stored=' \
               f'{sum(p.quantity * p.price for p in self._products.values())}, ' \
               f'Number of positions={len(self._products)}'
