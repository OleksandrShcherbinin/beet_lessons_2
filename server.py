import json
import socket
import threading

PORT = 8001
SERVER = socket.gethostbyname(socket.gethostname())

ADDRESS = (SERVER, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'exit'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDRESS)


def handle_client(connection, address):
    print(f'NEW CONNECTION - {address}')
    connected = True
    while connected:
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(FORMAT)
            message = json.loads(message)
            print('My encryption key', message.get('key'))
            if message.get('message') == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{address}] - {message["message"]}')

            connection.send(f'Message received from {address}'.encode(FORMAT))
        else:
            print(f'ACTIVE CONNECTIONS {threading.active_count() - 2}')
            connected = False

    connection.close()


def start():
    server.listen()
    print(f'SERVER LISTEN ON: {SERVER}')
    while True:
        connection, address = server.accept()
        thread = threading.Thread(
            target=handle_client, args=(connection, address)
        )
        thread.start()
        print(f'ACTIVE CONNECTIONS {threading.active_count() - 1}')


print('Server started')
start()
