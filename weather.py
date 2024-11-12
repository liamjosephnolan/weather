
#!/usr/bin/python3
import sys
import requests
from datetime import date
from prettytable import PrettyTable

def get_current_weather(latitude, longitude):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&daily=temperature_2m_max,temperature_2m_min&timezone=auto'
    print(url)
    response = requests.get(url)  # Get response from Open Meteo API
    data = response.json()  # Convert the response to JSON
    return data['current_weather']

def convert_city_coords(city):  # Function to convert city name to coordinates
    url = f'https://geocode.xyz/{city}?json=1'
    response = requests.get(url)
    data = response.json()
    latitude = data['latt']
    longitude = data['longt']
    return latitude, longitude

def print_day(today):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[today.weekday()]


def get_weather_description(weather_code):
# Dictionary mapping weather codes to descriptions
    weather_descriptions = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Slight or moderate thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
    }

# Get the weather description based on the code
    return weather_descriptions.get(weather_code, "Unknown weather condition")

# Get city from command-line arguments
city = sys.argv[1]

# Convert city name to latitude and longitude
latitude, longitude = convert_city_coords(city)

# Fetch current weather data
current_weather_data = get_current_weather(latitude, longitude)

# Get today's date and weekday
today = date.today()
d2 = today.strftime("%B %d, %Y")
day_text = print_day(today)

# Parse weather data from Open Meteo's response
current_temp = current_weather_data['temperature']
windspeed = current_weather_data['windspeed']
weather_code = current_weather_data.get('weathercode', "N/A")  # Weather codes vary in interpretation
is_day = "Day" if current_weather_data['is_day'] else "Night"

# Print the weather display
print(f"""
     ------------------------------------------
         Today is {day_text}, {d2} 
     ------------------------------------------
              /
     _    _  /
    (o)--(o)
   /.______.\ 
   \________/
  ./        \.
 ( .        , )
  \ \_\\//_/ /
   ~~  ~~  ~~
 """)

# Create and print the weather table
current = PrettyTable()
current.title = 'Current Weather'
current.field_names = ["City", "Current Temp", "Wind Speed", "Current Weather", "Time of Day"]
current.add_row([city, f"{current_temp} °C", f"{windspeed} km/h", get_weather_description(weather_code), is_day])
print(current)
