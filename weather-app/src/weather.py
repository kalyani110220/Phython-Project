import requests

API_KEY = "6c54fe77f3b2a49fae01125ff63a8f1a"
# <-- Put your OpenWeather API key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()


if data["cod"] == "404":
    print("City not found!")
else:
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    print(f"\nWeather in {city.capitalize()}:")
    print(f"Description: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
