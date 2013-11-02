# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PopcornItem(Item):
    # define the fields for your item here like:
    title = Field()
    url = Field()
    year = Field()
    genre = Field()
    date = Field()
    country = Field()
    language = Field()
    length = Field()
    rating = Field()
    users = Field()
    storyline = Field()
    filmingLocation = Field()