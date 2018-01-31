import requests
import time


class WeatherHandler():
    
    def __init__(self, city=''):
        self.city = city
        self.url_stencil = 'http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid=4be652987aa8129403b8d090deef289b&'
        self.format = 'metric'

    def set_city(self,city):
        self.city = city

    def get_weather(self):
        finalURL = self.url_stencil.format(self.city, self.format)
        data = requests.get(finalURL).json()
        self.format_data(data)

    def format_data(self, data):
        formatted_temp = int(data['main']['temp'])
        formatted_weather = data['weather'][0]['main']
        formatted_min =  int(data['main']['temp_min'])
        formatted_max = int(data['main']['temp_max'])
        formatted_time = time.strftime("%I:%M:%S")
        self.set_data(formatted_temp, formatted_weather, formatted_min,formatted_max, formatted_time)

    def set_data(self, formatted_temp, formatted_weather, formatted_min,formatted_max, formatted_time):
        self.formatted_temp = formatted_temp 
        self.formatted_weather = formatted_weather
        self.formatted_time = formatted_time
        self.formatted_max = formatted_max
        self.formatted_min = formatted_min
    def return_data(self):
        weather_data = {'CurrentTemp':self.formatted_temp,'CurrentWeather':self.formatted_weather,
        'MinTemp':self.formatted_min,'CurrentTime':self.formatted_time,'MaxTemp':self.formatted_max}
        return weather_data