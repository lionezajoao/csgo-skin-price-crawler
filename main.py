import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://neshastore.com/?q=case%20hardened&r=95&pag=1"

    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    print(soup.prettify())