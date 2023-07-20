import requests


city = 'Омск'

url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

weather_data = requests.get(url).json()
temperature = round(weather_data['main']['temp'])

print(f'В городе {city} сейчас {temperature} градусов цельсия.')