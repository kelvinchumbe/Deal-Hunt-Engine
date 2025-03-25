import scrapy
import json

class AmazonMobilePhonesSpider(scrapy.Spider):
    name = "bookspider"
    start_url = None
    
    def __init__(self):
        with open("Deal-Hunt-Engine/Engine/productscraper/store_product_links.json") as file:
            data = json.load(file)
            self.start_url = data[0]["amazon"]["mobile_phones"]

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response):
        cards = response.xpath('//div[@data-component-type="s-search-result"]')
        card_urls = [card.xpath("./div/div/div/div/span/div/div/div[3]/div[1]/h2/a/@href").extract() for card in cards]
        

        for card in cards:
            pass
