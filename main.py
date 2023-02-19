from src.utils.config import *
from src.crawler import Crawler

if __name__ == "__main__":
    skin_name = 'ak-47'
    crawler = Crawler(skin_name)

    list(map(lambda data:logging.info(f"\n{data}\n"), crawler.get_skin_data()))