###############################################################################
import asyncio
import json
from time import time
from asyncio.queues import Queue

import httpx
import uvloop
from bs4 import BeautifulSoup


notebooks_list = []


def write_json_file(data):
    with open('notebooks.json', 'w') as file:
        json.dump(data, file, indent=4)


def process(html_string: str, url: str):
    soup = BeautifulSoup(html_string, 'html.parser')
    notebooks = soup.select('.goods-tile__inner')

    for notebook in notebooks:
        name = notebook.select('.goods-tile__title')
        price = notebook.select('.goods-tile__price-value')
        old_price = notebook.select('.goods-tile__price--old')
        img_urls = notebook.select('.goods-tile__picture img')
        reviews = notebook.select('.goods-tile__reviews-link')
        promo = notebook.select('.goods-tile__label')
        availability = notebook.select('.goods-tile__availability')
        rating = notebook.select('.goods-tile__stars svg')

        old_price = ''.join([num for num in old_price[0].text.replace('\xa0', '').strip()
                             if num and num.isdigit()]) if old_price else None

        notebook = {
            'name': name[0].text.strip(),
            'price': int(price[0].text.replace('\xa0', '').strip()),
            'reviews': reviews[0].text.strip() if reviews else None,
            'promo': promo[0].text.strip() if promo else None,
            'old_price': int(old_price) if old_price else None,
            'rating': rating[0].get('aria-label'),
            'availability': availability[0].text.strip() if availability else None,
            'images': [img.get('src') for img in img_urls]
        }

        notebooks_list.append(notebook)

    print('Parsed', url)


async def worker(queue, number, session):
    while True:
        if queue.qsize() == 0:
            break

        url = await queue.get()

        if url == 'https://rozetka.com.ua/ua/notebooks/c80004/page=1/':
            url = 'https://rozetka.com.ua/ua/notebooks/c80004/'

        print(f'[Request in worker number {number}], queue size={queue.qsize()}, {url}')
        try:
            response = await session.get(url, timeout=10)

            print(response.status_code)
            assert response.status_code == 200
            process(response.text, url)

        except (httpx.ConnectError, httpx.ConnectTimeout, AssertionError) as error:
            print(error)
            await queue.put(url)

        except Exception as error:
            print(error)


async def main():
    queue = Queue()
    domain = 'https://rozetka.com.ua/ua/notebooks/c80004/page={page}/'
    last_page = 67
    workers = 40

    for page in range(1, last_page + 1):
        queue.put_nowait(domain.format(page=page))

    session = httpx.AsyncClient()
    tasks = []

    for worker_number in range(workers):
        task = asyncio.create_task(worker(queue, worker_number, session))
        tasks.append(task)

    await asyncio.gather(*tasks)

    write_json_file(notebooks_list)


if __name__ == '__main__':
    uvloop.install()

    start = time()

    asyncio.run(main())

    end_time = time()
    print(f'Scrapping finished in {end_time - start:.2f} seconds')
