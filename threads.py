# git reset --hard origin/<branch>
import threading
from time import sleep
from concurrent.futures import ThreadPoolExecutor


# def say_hello_to1(name: str):
#     print('Function1 started!')
#     print(f'Hello {name}')
#     sleep(5)
#     print('Function1 finished!')
#
#
# def say_hello_to2(name: str):
#     print('Function2 started!')
#     print(f'Hello {name}')
#     sleep(5)
#     print('Function2 finished!')
#
#
# def say_hello_to3(name: str):
#     print('Function3 started!')
#     print(f'Hello {name}')
#     sleep(5)
#     print('Function3 finished!')
#
#
# if __name__ == '__main__':
#     print('Main Start')
#     thread1 = threading.Thread(target=say_hello_to1, args=('Lev',))
#     thread1.start()
#     thread2 = threading.Thread(target=say_hello_to2, args=('Oleg',))
#     thread2.start()
#     thread3 = threading.Thread(target=say_hello_to3, args=('Yurii',))
#     thread3.start()
#     thread1.join()
#     thread2.join()
#     thread3.join()
#     print('Main Finished')


# def say_hello_to(name: str):
#     print('Function started!')
#     print(f'Hello {name}')
#     sleep(5)
#     print('Function finished!')
#
#
# if __name__ == '__main__':
#     print('Main Start')
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         # executor.map(say_hello_to, ['Mykola', 'Lev', 'Tetiana', 'Vlad', 'Oleg'])
#         for name in ('Mykola', 'Lev', 'Tetiana', 'Vlad', 'Oleg'):
#             executor.submit(say_hello_to, name)
#     print('Main Finished')


class BackAccount:

    def __init__(self):
        self.balance = 100
        self.lock = threading.Lock()

    def update(self, transaction: str, amount: int):
        print(transaction, 'processing....')
        with self.lock:
            balance_copy = self.balance
            if transaction == 'deposit':
                balance_copy += amount
            if transaction == 'withdraw':
                balance_copy -= amount
            sleep(1)
            self.balance = balance_copy

        print(transaction, 'finished...')


account = BackAccount()
print('Starting balance', account.balance)

with ThreadPoolExecutor(max_workers=2) as executor:
    for transaction, amount in [('deposit', 50), ('withdraw', 150)]:
        executor.submit(account.update, transaction, amount)


print(f'Finished operation, account balance {account.balance}')

lock = threading.Lock()
print(lock)
lock.acquire()
print(lock)
lock.release()
print(lock)

lock = threading.RLock()
print(lock)
lock.acquire()
lock.acquire()
print(lock)
lock.release()
lock.release()
print(lock)