# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IkmanCarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    make  = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    condition = scrapy.Field()
    price = scrapy.Field()
    mileage = scrapy.Field()
    gear = scrapy.Field()
    fuel_type = scrapy.Field()
    engine_capability = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    scraped_date = scrapy.Field()
    store = scrapy.Field()
    pass

class IkmanVanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    make  = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    condition = scrapy.Field()
    price = scrapy.Field()
    mileage = scrapy.Field()
    gear = scrapy.Field()
    fuel_type = scrapy.Field()
    engine_capability = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    scraped_date = scrapy.Field()
    store = scrapy.Field()
    pass

class RiyaCarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    make  = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()
    mileage = scrapy.Field()
    gear = scrapy.Field()
    fuel_type = scrapy.Field()
    engine_capability = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    scraped_date = scrapy.Field()
    store = scrapy.Field()
    
    pass

class RiyaBikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    make  = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()
    mileage = scrapy.Field()
    start_type = scrapy.Field()
    gear = scrapy.Field()
    fuel_type = scrapy.Field()
    engine_capability = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    scraped_date = scrapy.Field()
    store = scrapy.Field()
    
    pass
    

