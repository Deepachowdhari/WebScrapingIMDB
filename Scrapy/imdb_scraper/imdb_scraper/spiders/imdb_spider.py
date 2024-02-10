import scrapy


class ImdbSpiderSpider(scrapy.Spider):
    name = "imdb_spider"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        for movie in response.css('.lister-list tr'):
            yield {
                'title': movie.css('.titleColumn a::text').get(),
                'year': movie.css('.titleColumn span.secondaryInfo::text').get(),
                'rating': movie.css('.imdbRating strong::text').get()
            }
