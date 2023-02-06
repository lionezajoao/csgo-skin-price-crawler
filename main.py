import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://neshastore.com/?q=case%20hardened&r=95&pag=1"

    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    # skin card class name: card-internal
    divs = soup.find_all(class_='card-internal')

    for div in divs:
        print(div.prettify(), '\n\n\n')