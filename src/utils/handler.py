import urllib
from unicodedata import normalize

def handle_skin_name_to_url(skin_name: str) -> str:
    return urllib.parse.quote(skin_name)

# Normalizing unicode characters
def normalize_data(data:str) -> str:
    return normalize('NFKD', data)