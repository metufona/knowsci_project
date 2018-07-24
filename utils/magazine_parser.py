import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0'}
DOMAIN = "http://synergy-journal.ru/"

url = "http://synergy-journal.ru/archive/10"


def parse_articles():
    articles = [x for x in bs.find_all("div", "r") if x["data-record-type"] == "374"]
    #[x.find("a")["href"] for x in bs.find_all("div", "r") if x["data-record-type"] == "374"]


if __name__ == "__main__":
    main()