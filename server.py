# lsof -i -P | grep -i "listen" for mac
# netstat -an on windows
# ipconfig
# ifconfig


import socket
import threading

PORT = 8001  # ПОРТ ЩО МИ ВІДКРИЄМО ДЛЯ РОБОТИ
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)

ADDRESS = (SERVER, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'exit'

# Створюємо сервер, додаємо сім'ю і тип серверу
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDRESS)


def handle_client(connection, address):
    # ця функція буде використовуватися для обробки зв'язку з сервером клієнту
    print(f'NEW CONNECTION - {address}')
    connected = True
    while connected:
        # recv кількість байтів що отримає клієнт
        # Але ми не можемо знати завчасно скільки отримаємо
        # message = connection.recv(HEADER)
        # тому варто створити хедер
        # раз ми не знаємо розмір повідомлення, що буде відправлено на сервер
        # то ми будемо спочатку відправляти такзваний хедер,
        # в якому ми будемо вказувати розмір повідомлення, а потім
        # будемо відправляти саме повідомлення
        # 11 "hello world"
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:  # later after client first try
            message_length = int(message_length)
            message = connection.recv(message_length).decode(FORMAT)
            # далі маємо потурбуватися щоб з'єднання було закрито
            if message == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{address}] - {message}')
            # У же після того як показав зв'язок з декількома клієнтами
            # зробимо так, що сервер теж щось відповідав
            connection.send(f'Message received from {address}'.encode(FORMAT))

    connection.close()


def start():
    server.listen()
    print(f'SERVER LISTEN ON: {SERVER}')
    while True:
        # connettion - це об'єкт сокет
        connection, address = server.accept()
        # handle_client(connection, address)  # спочатку запустити
        # в одному потоці
        thread = threading.Thread(
            target=handle_client, args=(connection, address)
        )
        thread.start()
        print(f'ACTIVE CONNECTIONS {threading.active_count() - 1}')


print('Server started')
start()
