import socket
import asyncio
from aioconsole import ainput


PORT = 5001
SERVER = "localhost"
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'exit'


async def start_cli(username, writer):
    while True:
        client_message = await ainput()
        writer.write(f'{username}: {client_message}'.encode(FORMAT))

        await writer.drain()

        if client_message == DISCONNECT_MESSAGE:
            print('Bye-bye')
            break


async def receive_messages(reader):
    while True:
        server_message = str((await reader.read(4096)).decode(FORMAT))
        print(server_message)
        if DISCONNECT_MESSAGE in server_message:
            break


async def main():
    reader, writer = await asyncio.open_connection(
        SERVER,
        PORT,
        family=socket.AF_INET
    )
    username = input('Введіть ваш нікнейм: ')

    await asyncio.gather(
        receive_messages(reader),
        start_cli(username, writer),
    )


if __name__ == '__main__':
    asyncio.run(main())
