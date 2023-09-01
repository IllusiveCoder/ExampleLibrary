import requests

'''Description: This program fetches weather forecasts for a 
specified location using a weather API and presents the data to 
the user.'''

# Function to fetch weather forecast
def get_weather_forecast(api_key, location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
        description = data["weather"][0]["description"]
        return f"Weather in {location}: {description}, Temperature: {temperature:.2f}°C"
    else:
        return "Unable to fetch weather data."

# Example usage
api_key = "YOUR_API_KEY"
location = "New York"
forecast = get_weather_forecast(api_key, location)
print(forecast)
