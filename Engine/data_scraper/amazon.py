from ..utils.utils import  (
    get_url,
    get_image_url,
    validate_url

)


class AmazonScraper():
    def __init__(self, url):
        self.url = url

    def extract_product_listings(self):
        """Extract product listings """
        if validate_url(self.url):
            response = get_url(self.url)



    