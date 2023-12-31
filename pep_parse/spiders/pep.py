import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    """Custom Spider class.

    Args:
        scrapy (spider): spider class
    """
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Parse start url, extract links to individual PEP and parse it also.

        Args:
            response (response): response instance

        Yields:
            item: item instance through a callback to parse_pep method
        """
        table = response.xpath(
            '//section[@id="numerical-index"]').css('tr')
        for row in table[1:]:
            item = PepParseItem()
            item['number'] = int(row.css('td a::text').get())
            item['name'] = row.xpath('td[3]/a/text()').get()

            yield response.follow(
                row.xpath('td/a/@href').get(),
                callback=self.parse_pep,
                cb_kwargs=dict(item=item))

    def parse_pep(self, response, item):
        """Parse individual PEP's summary.

        Args:
            response (response): response instance
            item (item): item instance

        Returns:
            item: item instance
        """
        item['status'] = response.xpath(
            '//dt[contains(., "Status")]/following-sibling::*/abbr/text()'
        ).get()
        return item
