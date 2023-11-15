# Example 3: Web scraping to extract quotes from a website

import requests
from bs4 import BeautifulSoup

# Function to get quotes from a website
def get_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("span", class_="text")
    return [quote.get_text() for quote in quotes]

# Usage
quotes = get_quotes()

# Output the quotes
print("Quotes:")
for i, quote in enumerate(quotes, 1):
    print(f"{i}. {quote}")
