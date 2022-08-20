class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]

        return total

    # def pay(self, payment_type, security_code):
    #     if payment_type == 'debit':
    #         print('Debit payment')
    #         print(f'Verified security code {security_code}')
    #         self.status = 'paid'
    #     elif payment_type == 'credit':
    #         print('Credit card payment')
    #         print(f'Verified security code {security_code}')
    #     else:
    #         raise Exception('Unknown payment type')


# order = Order()
# order.add_item('apple', 10, 5)
# order.add_item('banana', 5, 25)
# order.add_item('kiwi', 2, 105)

# print(order.total_price())
# order.pay('debit', '134134134')
# order.pay('credit', 'credit134134134')

""" Single responsibility. """


# class PaymentProcessor:
#     def pay_credit(self, order, security_code):
#         print('Credit card payment')
#         print(f'Verified security code {security_code}')
#         order.status = 'paid'
#
#     def pay_debit(self, order, security_code):
#         print('Debit payment')
#         print(f'Verified security code {security_code}')
#         order.status = 'paid'

    # def pay_paypal(self):
    #     ...


# order = Order()
# order.add_item('apple', 10, 5)
# order.add_item('banana', 5, 25)
# order.add_item('kiwi', 2, 105)
#
# processor = PaymentProcessor()
# processor.pay_credit(order, 'credit_code')

""" Open-Closed Principle. """
from abc import ABC, abstractmethod


# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order, security_code):
#         pass


# class DebitPaymentProcessor(PaymentProcessor):
#
#     def pay(self, order, security_code):
#         print('Debit card payment')
#         print(f'Verified security code {security_code}')
#         order.status = 'paid'
#
#
# class CreditPaymentProcessor(PaymentProcessor):
#
#     def pay(self, order, security_code):
#         print('Credit card payment')
#         print(f'Verified security code {security_code}')
#         order.status = 'paid'
#
#
# class PaypalPaymentProcessor(PaymentProcessor):
#
#     def pay(self, order, security_code):
#         print('Paypal payment')
#         print(f'Verified security code {security_code}')
#         order.status = 'paid'


# order = Order()
# order.add_item('apple', 10, 5)
# order.add_item('banana', 5, 25)
# order.add_item('kiwi', 2, 105)

# debit = DebitPaymentProcessor()
# credit = CreditPaymentProcessor()
# paypal = PaypalPaymentProcessor()
#
# debit.pay(order, 'debit')
# credit.pay(order, 'credit')
# paypal.pay(order, 'paypal')

""" Liskov substitution principle. """

#
# class PaypalPaymentProcessor(PaymentProcessor):
#
#     def pay(self, order, email):
#         print('Paypal payment')
#         print(f'Verified email {email}')
#         order.status = 'paid'
#
#
# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order):
#         pass
#
#
# class DebitPaymentProcessor(PaymentProcessor):
#
#     def __init__(self, security_code):
#         self.security_code = security_code
#
#     def pay(self, order):
#         print('Debit card payment')
#         print(f'Verified security code {self.security_code}')
#         order.status = 'paid'
#
#
# class CreditPaymentProcessor(PaymentProcessor):
#     def __init__(self, security_code):
#         self.security_code = security_code
#
#     def pay(self, order):
#         print('Credit card payment')
#         print(f'Verified security code {self.security_code}')
#         order.status = 'paid'
#
#
# class PaypalPaymentProcessor(PaymentProcessor):
#
#     def __init__(self, email):
#         self.email = email
#
#     def pay(self, order):
#         print('Paypal payment')
#         print(f'Verified email {self.email}')
#         order.status = 'paid'
#
#
# order = Order()
# order.add_item('apple', 10, 5)
# order.add_item('banana', 5, 25)
# order.add_item('kiwi', 2, 105)
#
# debit = DebitPaymentProcessor('debit')
# credit = CreditPaymentProcessor('credit')
# paypal = PaypalPaymentProcessor('paypal')
#
# debit.pay(order)
# credit.pay(order)
# paypal.pay(order)
#
#
# """ Interface segregation. """
#
#
# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order):
#         pass
#
#     @abstractmethod
#     def auth_sms(self, code):
#         pass
#
#
# class DebitPaymentProcessor(PaymentProcessor):
#
#     def __init__(self, security_code):
#         self.security_code = security_code
#         self.verified = False
#
#     def pay(self, order):
#         if not self.verified:
#             raise Exception('Not verified!')
#         print('Debit card payment')
#         print(f'Verified security code {self.security_code}')
#         order.status = 'paid'
#
#     def auth_sms(self, code):
#         self.verified = True
#         print(f'Verified sma {code}')
#
#
# class CreditPaymentProcessor(PaymentProcessor):
#     def __init__(self, security_code):
#         self.security_code = security_code
#
#     def pay(self, order):
#         print('Credit card payment')
#         print(f'Verified security code {self.security_code}')
#         order.status = 'paid'
#
#     def auth_sms(self, code):
#         raise Exception('No needed')
#
#
# class PaypalPaymentProcessor(PaymentProcessor):
#
#     def __init__(self, email):
#         self.email = email
#         self.verified = False
#
#     def pay(self, order):
#         if not self.verified:
#             raise Exception('Not verified!')
#         print('Paypal payment')
#         print(f'Verified email {self.email}')
#         order.status = 'paid'
#
#     def auth_sms(self, code):
#         self.verified = True
#         print(f'Verified sma {code}')


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class PaymentProcessorSMS(PaymentProcessor):

    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessorSMS):

    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def pay(self, order):
        if not self.verified:
            raise Exception('Not verified!')
        print('Debit card payment')
        print(f'Verified security code {self.security_code}')
        order.status = 'paid'

    def auth_sms(self, code):
        self.verified = True
        print(f'Verified sms {code}')


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print('Credit card payment')
        print(f'Verified security code {self.security_code}')
        order.status = 'paid'


class PaypalPaymentProcessor(PaymentProcessorSMS):

    def __init__(self, email):
        self.email = email
        self.verified = False

    def pay(self, order):
        if not self.verified:
            raise Exception('Not verified!')
        print('Paypal payment')
        print(f'Verified email {self.email}')
        order.status = 'paid'

    def auth_sms(self, code):
        self.verified = True
        print(f'Verified sms {code}')


order = Order()
order.add_item('apple', 10, 5)
order.add_item('banana', 5, 25)
order.add_item('kiwi', 2, 105)

debit = DebitPaymentProcessor('debit')
debit.auth_sms('code')
debit.pay(order)

credit = CreditPaymentProcessor('credit')
credit.pay(order)

paypal = PaypalPaymentProcessor('test@email.com')
paypal.auth_sms('code_paypal')
paypal.pay(order)


class Printer(ABC):
    def print(self):
        pass


class Scaner(ABC):
    def scan(self):
        pass


class Xerox(ABC):
    def copy(self):
        pass


class MultiFunctionalMachine(Printer, Scaner, Xerox):
    pass


class ScanerXerox(Scaner, Xerox):
    pass


""" Dependency inversion. """


# class PrivatBankConverter:
#     def convert(self, from_currency, to_currency, amount):
#         print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
#         return amount * 1.2
#
#
# class Application:
#     def start(self):
#         converter = PrivatBankConverter()
#         converter.convert('EUR', 'USD', 100)
#
#
# app = Application()
#
# app.start()


class CurrencyConverter(ABC):
    def convert(
            self,
            from_currency: str,
            to_currency: str, amount: int
    ) -> float:
        pass


class PrivatBankConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class MonoBankConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.3} {to_currency}')
        return amount * 1.3


class Application:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


# converter = MonoBankConverter()
converter = PrivatBankConverter()
choice = {
    'mono': MonoBankConverter,
    'privat': PrivatBankConverter,
}
converter = input('Виберіть спосіб конвертації: ')
real_converter = choice.get(converter)

app = Application(real_converter())

app.start()
