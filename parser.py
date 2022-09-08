from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from queue import Queue

from requests import Session
from bs4 import BeautifulSoup


from rozetka_db import Image, Price, Product


class RozetkaScraper:
    LOCK = Lock()
    TIME = 10

    def __init__(self, domain_url: str, last_page: int):
        self._domain_url = domain_url
        self._last_page = last_page

    def scrape(self):
        qu = self._fill_queue()
        print('Started scrapping!!!')
        with ThreadPoolExecutor(max_workers=20) as executor:
            for i in range(self._last_page):
                executor.submit(self._scrape, qu)

    def _fill_queue(self):
        qu = Queue()
        for page in range(1, self._last_page + 1):
            qu.put(self._domain_url.format(page=page))

        return qu

    def _scrape(self, qu: Queue):
        while True:
            url = qu.get()
            print(qu.qsize(), url)
            try:
                response_string = self._get_response(url)
                self._process(response_string)
            except Exception as error:
                print('Error', error)
                qu.put(url)

            if qu.empty():
                break

    def _get_response(self, url: str) -> str:
        try:
            with Session() as session:
                response = session.get(url, timeout=self.TIME)
                print(response.status_code)
                assert response.status_code == 200, 'Bad response'
            return response.text

        except Exception as error:
            print(error)

    def _process(self, html_string: str):
        soup = BeautifulSoup(html_string, 'html.parser')
        notebooks = soup.select('.goods-tile__inner')

        with self.LOCK:
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

                price, _ = Price.get_or_create(
                    price=int(price[0].text.replace('\xa0', '').strip()),
                    old_price=int(old_price) if old_price else None
                )

                notebook = {
                    'name': name[0].text.strip(),
                    'reviews': reviews[0].text.strip() if reviews else None,
                    'promo': promo[0].text.strip() if promo else None,
                    'price': price,
                    'rating': rating[0].get('aria-label'),
                    'availability': availability[0].text.strip() if availability else None
                }
                product, _ = Product.get_or_create(**notebook)
                print(product)

                images = [img.get('src') for img in img_urls]
                if images:
                    for img in images:
                        if img:
                            Image.create(product=product, url=img)

        print('PAGE SCRAPPED!!!')


def main():
    domain = 'https://rozetka.com.ua/ua/notebooks/c80004/page={page}/'
    last_page = 67

    scraper = RozetkaScraper(domain, last_page)
    scraper.scrape()


if __name__ == '__main__':
    main()
