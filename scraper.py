import json
from abc import ABC, abstractmethod

from requests import Session
from bs4 import BeautifulSoup


class Scraper(ABC):

    @abstractmethod
    def scrape(self):
        """ Implement your scrape logic here. """


class GoodReadsScraperException(Exception):
    pass


class GoodReadsScraper(Scraper):
    DOMAIN = 'https://www.goodreads.com/book/show/'
    TIMEOUT = 10
    FILE_NAME = 'book.json'

    def __init__(self, list_url: list[str]):
        self.url_list = self._validate_urls(list_url)
        self.data_list = []

    def scrape(self):
        for url in self.url_list:
            response_string = self._get_response(url)

            data = self._parse_html(response_string)
            self.data_list.append(data)

        self._json_file_write()

    def _validate_urls(self, url_list: list[str]) -> list[str]:
        if not all(url.startswith(self.DOMAIN) for url in url_list):
            raise GoodReadsScraperException('Not valid urls')

        return url_list

    def _get_response(self, url) -> str:
        with Session() as session:
            response = session.get(url, timeout=self.TIMEOUT)

            assert response.status_code == 200, 'Bad response'

        return response.text

    @staticmethod
    def _parse_html(response_string: str) -> dict[str, ...]:
        soup = BeautifulSoup(response_string, 'html.parser')

        title = soup.select('#bookTitle')
        author = soup.select('#bookAuthors span div a span')
        rating = soup.select('span[itemprop="ratingValue"]')
        text = soup.select('#description span')
        img_url = soup.select('#coverImage')
        reviews = [review.text.strip() for review
                   in soup.select('.reviewText span span')]

        return {
            'title': title[0].text.strip(),
            'author': author[0].text.strip(),
            'rating': float(rating[0].text.strip()),
            'text': text[1].text,
            'img_url': img_url[0]['src'],
            'reviews': reviews
        }

    def _json_file_write(self, indent=4):
        with open(self.FILE_NAME, 'w') as file:
            json.dump(self.data_list, file, indent=indent)


def main():

    urls = [
        'https://www.goodreads.com/book/show/1.Harry_Potter_and_the_Half_Blood_Prince',
    ]

    scraper = GoodReadsScraper(urls)
    scraper.scrape()


if __name__ == '__main__':
    main()
