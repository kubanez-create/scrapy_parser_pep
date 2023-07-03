import csv
from collections import Counter
from datetime import datetime as dt
from pathlib import Path

from itemadapter import ItemAdapter

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S"


class PepParsePipeline:
    """Pipeline class for Python PEP parser."""

    def __init__(self):
        self.results_dir = BASE_DIR / "results"
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        """Create counter instance and file to write into.

        Args:
            spider (spider): spider class
        """
        self.counter = Counter()
        self.filename = (
            self.results_dir / "status_summary_"
            f"{dt.now().strftime(DATETIME_FORMAT)}.csv"
        )

    def close_spider(self, spider):
        """Write collected statistics into the file and close it.

        Args:
            spider (spider): spider class
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            fieldnames = ["Статус", "Количество"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(
                (
                    {"Статус": key, "Количество": val}
                    for key, val in self.counter.items()
                )
            )
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"Total,{self.counter.total()}\n")

    def process_item(self, item, spider):
        """Count each item's status.

        Args:
            item (Item): custom scrapy item class
            spider (spider): spider class

        Returns:
            Item: custom scrapy item class
        """
        adapter = ItemAdapter(item)
        status = adapter["status"]
        self.counter.update({f"{status}": 1})
        return item
