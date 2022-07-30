import unittest
from unittest.mock import patch, call

from scraper import GoodReadsScraperException, GoodReadsScraper


class TestGoodReadsScraper(unittest.TestCase):

    def setUp(self) -> None:
        self.url_list = [
            'https://www.goodreads.com/book/show/1.Harry_Potter_and_the_Half_Blood_Prince',
            'https://www.goodreads.com/book/show/1.Harry_Potter_and_the_Half_Blood_Prince',
        ]
        self.bad_url_list = [
            'https://www.goodeads.com/book/show/1.Harry_Potter_and_the_Half_Blood_Prince',
        ]

    def test_urls_validation(self):
        with self.assertRaises(GoodReadsScraperException):
            GoodReadsScraper(self.bad_url_list)

    @patch('scraper.GoodReadsScraper._json_file_write')
    @patch('scraper.GoodReadsScraper._parse_html')
    @patch('scraper.GoodReadsScraper._get_response')
    def test_scrape_success(self, mock_response, mock_parse, mock_json):
        mock_response.return_value = 'Oleg'
        mock_parse.return_value = {
            'title': 'Title',
            'author': 'Author',
            'rating': 5.0,
            'text': 'Text',
            'img_url': 'img_url',
            'reviews': ['reviews']
        }

        GoodReadsScraper(self.url_list).scrape()

        mock_response.assert_has_calls(
            [call(self.url_list[0]),
             call(self.url_list[1])]
        )
        mock_parse.assert_has_calls([call('Oleg'), call('Oleg')])
        self.assertEqual(mock_parse.call_count, 2)
        mock_json.assert_called_once()
