import requests
from geopy.geocoders import Nominatim

base_weather_url = "https://api.open-meteo.com/v1/forecast?hourly=temperature_2m&"
base_currency_url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"

city = input("Enter a city: ")

geolocator = Nominatim(user_agent="my-app")
location = geolocator.geocode(city)

if location:
    latitude = location.latitude
    longitude = location.longitude

    weather_url = f"{base_weather_url}latitude={latitude}&longitude={longitude}"
    weather_response = requests.get(weather_url).json()

    currency_response = requests.get(base_currency_url).json()

    print("Weather Data:")
    print(weather_response)

    print("\nCurrency Data:")
    print(currency_response)
else:
    print("Unable to determine the coordinates for the specified city.")






# currency_api_url = "https://currency-api.bank.ltd/"
# currency_api_access_key = "<YOUR_CURRENCY_API_ACCESS_KEY>"

# weather_api_url = "https://api.open-meteo.com/v1/forecast"
# weather_api_access_key = "<YOUR_WEATHER_API_ACCESS_KEY>"

# def get_currency(city):
#     # Make a request to the currency API
#     response = requests.get(f"{currency_api_url}rates?base=USD&symbols={city}&access_key={currency_api_access_key}")
#     data = response.json()

#     # Extract the exchange rate
#     exchange_rate = data["rates"][city]

#     return exchange_rate

# def get_weather(city):
#     # Make a request to the weather API
#     response = requests.get(f"{weather_api_url}?city={city}&key={weather_api_access_key}")
#     data = response.json()

#     # Extract the relevant weather information
#     if "current" in data and "temperature" in data["current"] and "weather" in data["current"]:
#         temperature = data["current"]["temperature"]
#         weather_conditions = data["current"]["weather"][0]["description"]
#         return temperature, weather_conditions
#     else:
#         return None, None


# def main():
#     city = input("Enter the city: ")

#     # Get the weather information
#     temperature, weather_conditions = get_weather(city)
#     print(f"The temperature in {city} is {temperature}°C with {weather_conditions}.")

#     # Get the currency information
#     exchange_rate = get_currency(city)
#     print(f"The exchange rate for {city} is 1 USD = {exchange_rate} {city}.")

# if __name__ == "__main__":
#     main()


# def main():
#     pygame.init()
#     # Create an instance on your controller object
#     # Call your mainloop

#     ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######


# # https://codefather.tech/blog/if-name-main-python/
# if __name__ == "__main__":
#     main()

