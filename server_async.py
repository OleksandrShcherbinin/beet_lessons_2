import asyncio


PORT = 5001
SERVER = 'localhost'

ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'exit'
BYTES_CAPACITY = 4096


class Client:
    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.__reader: asyncio.StreamReader = reader
        self.__writer: asyncio.StreamWriter = writer
        self.__ip: str = writer.get_extra_info('peername')[0]
        self.__port: int = writer.get_extra_info('peername')[1]
        self.nickname: str = str(writer.get_extra_info('peername'))

    def __str__(self):
        return f"{self.nickname} {self.ip}:{self.port}"

    @property
    def reader(self):
        return self.__reader

    @property
    def writer(self):
        return self.__writer

    @property
    def ip(self):
        return self.__ip

    @property
    def port(self):
        return self.__port

    async def get_message(self):
        return str((await self.reader.read(BYTES_CAPACITY)).decode(FORMAT))


class Server:
    def __init__(self, ip: str, port: int, loop: asyncio.AbstractEventLoop):
        self.__ip: str = ip
        self.__port: int = port
        self.__loop: asyncio.AbstractEventLoop = loop
        self.__clients: dict[asyncio.Task, Client] = {}
        print(f"Server Initialized with {self.ip}:{self.port}")

    @property
    def ip(self):
        return self.__ip

    @property
    def port(self):
        return self.__port

    @property
    def loop(self):
        return self.__loop

    @property
    def clients(self):
        return self.__clients

    def start_server(self):
        try:
            self.server = asyncio.start_server(
                self.accept_client, self.ip, self.port
            )
            self.loop.run_until_complete(self.server)
            self.loop.run_forever()
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print("Keyboard Interrupt Detected. Shutting down!")

        self.shutdown_server()

    def accept_client(
            self,
            client_reader: asyncio.StreamReader,
            client_writer: asyncio.StreamWriter
    ):
        client = Client(client_reader, client_writer)
        task = asyncio.Task(self.incoming_client_message_cb(client))
        self.clients[task] = client

        client_ip = client_writer.get_extra_info('peername')[0]
        client_port = client_writer.get_extra_info('peername')[1]
        print(f"New Connection: {client_ip}:{client_port}")

        task.add_done_callback(self.disconnect_client)

    async def incoming_client_message_cb(self, client: Client):
        while True:
            client_message = await client.get_message()

            if DISCONNECT_MESSAGE in client_message:
                break
            else:
                self.broadcast_message(
                    f"{client.nickname}: {client_message}".encode(FORMAT))

            print(f"{client_message}")

            await client.writer.drain()

        print("Client Disconnected!")

    def broadcast_message(self, message: bytes, exclusion_list: list = []):
        for client in self.clients.values():
            if client not in exclusion_list:
                client.writer.write(message)

    def disconnect_client(self, task: asyncio.Task):
        client = self.clients[task]

        self.broadcast_message(
            f"{client.nickname} has left!".encode(FORMAT), [client])

        del self.clients[task]
        client.writer.write(DISCONNECT_MESSAGE.encode(FORMAT))
        client.writer.close()
        print("End Connection")

    def shutdown_server(self):
        print("Shutting down server!")
        for client in self.clients.values():
            client.writer.write(DISCONNECT_MESSAGE.encode(FORMAT))
        self.loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server = Server(SERVER, PORT, loop)
    server.start_server()
