import requests
from bs4 import BeautifulSoup

'''The Web Scraping program extracts specific 
information from a website using web scraping techniques
with BeautifulSoup and requests. It fetches quotes from 
the "quotes.toscrape.com" website and prints them to 
the console. The BeautifulSoup library helps parse the 
HTML content, and requests are made to retrieve the data.'''

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