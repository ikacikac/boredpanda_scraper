# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Compose


class BoredpandaScraperItem(Item):
    title = Field()  # Storing article title
    content = Field()  # Storing article textual content.
    votes = Field()  # Storing article up votes.
    images = Field()  # Will be populated with image file system paths when downloaded.
    image_urls = Field()  # Storing all article images urls for later download.
    date_created = Field()  # Storing UTC date when item was scraped
    url = Field()  # URL of a page.


class BoredpandaScraperItemLoader(ItemLoader):
    # Content is a list of strings. Those should be
    # concatenated and exported as a string.
    content_in = Compose(lambda x: '\n'.join(x))
    content_out = TakeFirst()

    # Votes gets scraped as a one item list
    # and should be exported as str. Same for url.
    votes_out = TakeFirst()

    url_out = TakeFirst()

    title_in = MapCompose(lambda x: x.strip())
    title_out = TakeFirst()

    date_created_out = TakeFirst()

