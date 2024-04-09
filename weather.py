import sys
import requests
from datetime import date, datetime
from prettytable import PrettyTable



def get_current_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def print_day(today):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[today.weekday()]


today = date.today()
d2 = today.strftime("%B %d, %Y")
day_text= print_day(today)
api_key = '0f9da0e0a6c6e2c3032d8a3a06c0dbe0'
city = sys.argv[1]

current_weather_data = get_current_weather(api_key, city)
current_temp = current_weather_data['main']['temp']
low_temp = current_weather_data['main']['temp_min']
high_temp = current_weather_data['main']['temp_max']
weather_id = current_weather_data['weather'][0]['description']



print(f"""
Today is {day_text}, {d2}
""")

current = PrettyTable()

current.title = 'Current Weather'

current.field_names = ["City", "Current Temp", "Low", "High", "Weather"]
current.add_row([city,f"{current_temp} °C",f"{low_temp} °C",f"{high_temp} °C",weather_id])
print(current)