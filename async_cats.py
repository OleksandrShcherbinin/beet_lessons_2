# import requests
# from time import time
#
#
# def get_file(url):
#     response = requests.get(url, allow_redirects=True)
#     return response
#
#
# def write_file(response):
#     filename = response.url.split('/')[-1]
#     with open(f'images/{filename}', 'wb') as file:
#         file.write(response.content)
#
#
# def main():
#     url = 'https://loremflickr.com/320/240'
#     start = time()
#     for _ in range(10):
#         response = get_file(url)
#         write_file(response)
#
#     end_time = time()
#
#     print(f'Getting images finished in {end_time - start:.2f} seconds')
#
#
# if __name__ == '__main__':
#     main()
###############################################################################
import asyncio
import aiohttp
import ssl
import certifi
from time import time


def write_file(data):
    filename = int(time() * 1000)
    with open(f'images/{filename}.jpg', 'wb') as file:
        file.write(data)


async def get_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()

        write_file(data)


async def main():
    url = 'https://loremflickr.com/320/240'

    tasks = []

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=conn) as session:
        for _ in range(10):
            task = asyncio.create_task(get_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time()

    asyncio.run(main())

    end_time = time()
    print(f'Getting images finished in {end_time - start:.2f} seconds')