# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ProductItem(scrapy.Item):
    """  """
    name = scrapy.Field()
    image_url = scrapy.Field()
    rating = scrapy.Field()
    no_of_reviews = scrapy.Field()
    current_price = scrapy.Field()
    original_price = scrapy.Field()
    discount = scrapy.Field()
    condition = scrapy.Field()
    specifications = scrapy.Field()
    description = scrapy.Field()
    features = scrapy.Field()

class MobilePhoneSpecifications(scrapy.Item):
    """ Struct for Mobile Phone Specifications """
    screen_size = scrapy.Field()
    front_camera = scrapy.Field()
    back_camera = scrapy.Field()
    display_type = scrapy.Field()
    network_connectivity = scrapy.Field()
    battery_capacity = scrapy.Field()
    sim_card_size = scrapy.Field()
    storage_rom = scrapy.Field()
    memory_ram = scrapy.Field()
    processor_brand = scrapy.Field()
    processor_model = scrapy.Field()
    processor_speed = scrapy.Field()
    operating_system = scrapy.Field()