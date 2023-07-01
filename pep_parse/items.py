import scrapy


class PepParseItem(scrapy.Item):
    """Scrapy item class for Python PEPs parser.

    Args:
        Item (Item): build-in base scrapy class for an item
    """
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
