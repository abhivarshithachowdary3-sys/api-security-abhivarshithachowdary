import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env
API_KEY = os.getenv("API_KEY")  # Securely fetched, not hardcoded

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["weather"][0]["description"]
    elif response.status_code == 429:
        return "Rate limit exceeded. Please wait a minute before trying again."
    else:
        return f"Error: Unable to fetch weather (status {response.status_code})"
