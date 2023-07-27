import requests
from bs4 import BeautifulSoup

def get_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all("span", class_="text")
    return [quote.get_text() for quote in quotes]

# Usage example
quotes = get_quotes()
for i, quote in enumerate(quotes, 1):
    print(f"{i}. {quote}")