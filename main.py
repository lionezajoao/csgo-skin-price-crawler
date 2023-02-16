from src.crawler import Crawler

if __name__ == "__main__":
    skin_name = 'aquecimento de aço'
    crawler = Crawler(skin_name)

    list(map(lambda data:print(data, '\n'), crawler.get_skin_data()))