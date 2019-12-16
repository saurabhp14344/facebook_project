import scrapy


class spider_fb(scrapy.Spider):
    name = 'profile'
    start_urls = ['https://www.facebook.com/IamSRK/']

    def parse(self, response):
        links = response.xpath("//a[@class='_2yau']/@href").getall()
        print(links)