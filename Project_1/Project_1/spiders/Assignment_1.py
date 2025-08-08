import scrapy
from ..items import MyBooksItem

class BooksSpider(scrapy.Spider):
    name = "books_scrap"
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            item = MyBooksItem()

            item['title'] = book.css('h3 a::attr(title)').get()
            item['price'] = book.css('p.price_color::text').get()

            # Fix for availability to handle extra whitespace/newlines
            availability_list = book.css('p.availability::text').getall()
            item['availability'] = ''.join(availability_list).strip()

            item['rating'] = book.css('p.star-rating::attr(class)').re_first('star-rating (\w+)')

            yield item

        # Pagination - follow next page if available
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
