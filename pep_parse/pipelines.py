from collections import Counter
from datetime import datetime as dt
from pathlib import Path

from itemadapter import ItemAdapter

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.counter = Counter()
        filename = (self.results_dir / "status_summary_"
                    f"{dt.now().strftime(DATETIME_FORMAT)}.csv")
        self.file = open(filename, "w", encoding='utf-8')
        self.file.write('Статус,Количество\n')

    def close_spider(self, spider):
        for status, st_count in self.counter.items():
            self.file.write(f"{status},{st_count!s}\n")
        self.file.write(f"Total,{self.counter.total()}\n")
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        status = adapter["status"]
        self.counter.update({f"{status}": 1})
        return item
