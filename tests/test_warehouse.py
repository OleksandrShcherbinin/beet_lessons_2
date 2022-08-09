from decimal import Decimal
from unittest import TestCase

from warehouse import Product, WareHouse, WareHouseException, MeasurementUnit


class WareHouseTestCase(TestCase):

    def setUp(self) -> None:
        self.beer = Product('Beer', 24, Decimal('25.55'))
        self.wine = Product('Wine', 1, Decimal('555.99'))
        self.beef = Product('Beef', 3000, Decimal('0.39'), MeasurementUnit.GRAMS)
        self.pork = Product('Pork', 5000, Decimal('0.149'), MeasurementUnit.GRAMS)
        self.soda = Product('Soda', 24, Decimal('20.99'))
        self.products = {self.beer, self.wine, self.beef, self.pork}
        self.warehouse = WareHouse()

    def test_add_product_success(self):
        with self.warehouse as stock:
            stock.add(*self.products)

        self.assertTrue(self.warehouse._products)
        self.assertEqual(len(self.warehouse._products), 4)
        self.assertEqual(self.warehouse.total_amount, Decimal('3084.19'))

    def test_add_product_second_time_success(self):
        with self.warehouse as stock:
            stock.add(*self.products)
            stock.add(self.wine)

        wine = stock._products.get(self.wine.sku)
        self.assertTrue(self.warehouse._products)
        self.assertEqual(len(self.warehouse._products), 4)
        self.assertEqual(self.warehouse.total_amount, Decimal('3640.18'))
        self.assertEqual(wine.quantity, 2)

    def test_add_product_second_time_multiple_success(self):
        with self.warehouse as stock:
            stock.add(*self.products)
            beer = Product('Beer', 1, Decimal('25.55'), sku=self.beer.sku)
            stock.add(self.wine, beer)

        wine = stock._products.get(self.wine.sku)
        beer = stock._products.get(beer.sku)
        self.assertTrue(self.warehouse._products)
        self.assertEqual(len(self.warehouse._products), 4)
        self.assertEqual(self.warehouse.total_amount, Decimal('3665.73'))
        self.assertEqual(wine.quantity, 2)
        self.assertEqual(beer.quantity, 25)

    def test_add_locked_fail(self):
        with self.assertRaises(WareHouseException) as context:
            self.warehouse.add(*self.products)

        self.assertEqual(context.exception.args[0], 'WareHouse locked!')

    def test_resupply_success(self):
        with self.warehouse as stock:
            stock.add(*self.products)
            stock.resupply(self.wine, 12)
            # check total amount change
            self.assertEqual(self.warehouse.total_amount, Decimal('9756.07'))
            # check wine attributes after resupply
            wine = stock._products.get(self.wine.sku)
            self.assertEqual(wine.name, self.wine.name)
            self.assertEqual(wine.quantity, 13)
            self.assertEqual(wine.price, self.wine.price)
            self.assertEqual(wine.measurement, self.wine.measurement)

    def test_resupply_not_in_stock_product(self):
        with self.assertRaises(WareHouseException) as context:
            with self.warehouse as stock:
                stock.add(*self.products)
                stock.resupply(self.soda, 12)

        self.assertEqual(
            context.exception.args[0],
            'Please add this product into warehouse first'
        )

    def test_resupply_locked_fail(self):
        with self.assertRaises(WareHouseException) as context:
            with self.warehouse as stock:
                stock.add(*self.products)
            # try to resupply while locked
            stock.resupply(self.wine, 12)

        self.assertEqual(
            context.exception.args[0],
            'WareHouse locked!'
        )
        wine = stock._products.get(self.wine.sku)
        self.assertEqual(wine.name, self.wine.name)
        self.assertEqual(wine.quantity, 1)

    def test_remove_success(self):
        with self.warehouse as stock:
            stock.add(*self.products)
            stock.remove(self.beer)
            # check total amount reduce after one beer remove
            self.assertEqual(self.warehouse.total_amount, Decimal('3058.64'))
            # check stock beer quantity
            beer = stock._products.get(self.beer.sku)
            self.assertEqual(beer.name, self.beer.name)
            self.assertEqual(beer.quantity, 23)

    def test_remove_not_in_stock_product(self):
        with self.assertRaises(WareHouseException) as context:
            with self.warehouse as stock:
                stock.add(*self.products)
                stock.remove(self.soda)

        self.assertEqual(
            context.exception.args[0],
            'Please add this product into warehouse first'
        )

    def test_remove_not_enough_in_stock_fail(self):
        with self.assertRaises(WareHouseException) as context:
            with self.warehouse as stock:
                stock.add(*self.products)
                stock.remove(self.wine, 2)

        self.assertEqual(
            context.exception.args[0],
            f'There are only {self.wine.quantity} left on stock'
        )

    def test_remove_locked_fail(self):
        with self.assertRaises(WareHouseException) as context:
            with self.warehouse as stock:
                stock.add(*self.products)
            # try to remove while locked
            stock.remove(self.wine)

        self.assertEqual(
            context.exception.args[0],
            'WareHouse locked!'
        )
        wine = stock._products.get(self.wine.sku)
        self.assertEqual(wine.name, self.wine.name)
        self.assertEqual(wine.quantity, 1)
