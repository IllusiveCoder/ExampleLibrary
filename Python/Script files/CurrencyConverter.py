import requests

def convert_currency(amount, from_currency, to_currency):
    api_key = "YOUR_API_KEY"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    data = response.json()
    converted_amount = data["conversion_result"]
    return converted_amount

# Usage example
amount = 100
from_currency = "USD"
to_currency = "EUR"
result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")