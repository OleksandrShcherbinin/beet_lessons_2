from decimal import Decimal
from unittest import TestCase
from unittest.mock import patch

from warehouse import Product, WareHouse, WareHouseException, MeasurementUnit
from cart import Cart, CartException


class CartTestCase(TestCase):

    def setUp(self) -> None:
        self.beer = Product('Beer', 24, Decimal('25.55'))
        self.wine = Product('Wine', 1, Decimal('555.99'))
        self.beef = Product('Beef', 3000, Decimal('0.39'), MeasurementUnit.GRAMS)
        self.pork = Product('Pork', 5000, Decimal('0.149'), MeasurementUnit.GRAMS)
        self.soda = Product('Soda', 24, Decimal('20.99'))
        self.products = {self.beer, self.wine, self.beef, self.pork}
        self.warehouse = WareHouse()
        self.cart = Cart(self.warehouse)

    def test_add_product_success(self):
        with self.warehouse as stock:
            stock.add(*self.products)
            self.cart.add(self.beer, 11)

        product_in_cart = self.cart._products.get(self.beer.sku)
        self.assertEqual(product_in_cart.name, self.beer.name)
        self.assertEqual(product_in_cart.quantity, 11)
        # check beer quantity on stock after add to cart
        self.assertEqual(self.beer.quantity, 13)

    def test_add_locked_fail(self):
        with self.assertRaises(WareHouseException) as context:
            self.cart.add(self.wine)

        self.assertEqual(context.exception.args[0], 'WareHouse locked!')

    def test_remove_from_cart_success(self):
        with self.warehouse as stock:
            stock.add(*self.products)
            self.cart.add(self.beer, 12)
            self.cart.remove(self.beer, 2)

        product_in_cart = self.cart._products.get(self.beer.sku)
        self.assertEqual(product_in_cart.name, self.beer.name)
        self.assertEqual(product_in_cart.quantity, 10)
        # check beer quantity on stock after add to cart
        self.assertEqual(self.beer.quantity, 14)

    def test_remove_locked_fail(self):
        with self.assertRaises(WareHouseException) as context:
            self.cart.remove(self.wine)

        self.assertEqual(context.exception.args[0], 'WareHouse locked!')

    def test_resupply_not_in_stock_product(self):
        with self.assertRaises(CartException) as context:
            with self.warehouse as stock:
                stock.add(*self.products)
                self.cart.add(self.beer, 12)
                self.cart.remove(self.soda, 12)

        self.assertEqual(
            context.exception.args[0],
            'No such product in the cart'
        )

    def test_remove_too_many_items_fail(self):
        with self.assertRaises(CartException) as context:
            with self.warehouse as stock:
                stock.add(*self.products)
                self.cart.add(self.beer, 12)
                self.cart.remove(self.beer, 13)

        self.assertEqual(
            context.exception.args[0],
            'There are only 12 pieces inside cart'
        )

    @patch('builtins.print')
    def test_sell_success(self, mock_print):
        with self.warehouse as stock:
            stock.add(*self.products)
            self.cart.add(self.beer, 12)
            self.cart.add(self.wine)
            self.cart.sell()

        self.assertEqual(self.cart.income, Decimal('862.59'))
        self.assertFalse(len(self.cart._products))
        mock_print.assert_called_once()

    def test_sell_fail_because_of_empty_cart(self):
        with self.assertRaises(CartException) as context:
            with self.warehouse as stock:
                stock.add(*self.products)
                self.cart.sell()

        self.assertEqual(
            context.exception.args[0],
            'Cart is empty, there is nothing to sell'
        )

    def test_sell_fail_because_of_empty_cart_after_removed_products(self):
        with self.assertRaises(CartException) as context:
            with self.warehouse as stock:
                stock.add(*self.products)
                self.cart.add(self.beer, 12)
                self.cart.remove(self.beer, 12)
                self.cart.sell()

        self.assertEqual(
            context.exception.args[0],
            'Cart is empty, there is nothing to sell'
        )
