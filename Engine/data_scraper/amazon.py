from ..utils.utils import  (
    get_url,
    get_image_url,
    validate_url
)
from bs4 import BeautifulSoup
from lxml import etree

class AmazonScraper():
    def __init__(self, url):
        self.url = url

    def extract_product_listings(self):
        """Extract product listings """
        page_text = get_url(self.url)




    