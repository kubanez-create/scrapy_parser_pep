import scrapy


class PepParseItem(scrapy.Item):
    def __init__(self):
        super().__init__()
        self.fields["Номер"] = scrapy.Field()
        self.fields["Название"] = scrapy.Field()
        self.fields["Статус"] = scrapy.Field()
