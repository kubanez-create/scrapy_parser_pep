from collections import Counter
from datetime import datetime as dt

from itemadapter import ItemAdapter


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = Counter()
        filename = ("results/status_summary_"
                    f"{dt.now().strftime('%Y-%m-%d_%H-%M-%S')}")
        self.file = open(filename, "w", encoding='utf-8')
        self.file.write('Статус,Количество\n')

    def close_spider(self, spider):
        for status, st_count in self.counter.items():
            self.file.write(f"{status},{st_count!s}\n")
        self.file.write(f"Total,{self.counter.total()}\n")
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        status = adapter["Статус"]
        self.counter.update({f"{status}": 1})
        return item
