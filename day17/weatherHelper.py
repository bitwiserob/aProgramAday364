import requests
import time


class weatherHandler():
    
    def __init__(self, city):
        self.city = city
        self.urlStencil = 'http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid=4be652987aa8129403b8d090deef289b&'
        self.format = 'metric'

    def get_weather(self):
        finalURL = self.urlStencil.format(self.city, self.format)
        data = requests.get(finalURL).json()
        self.format_data(data)

    def format_data(self, data):
        formatted_temp = 'Current temp is: {}'.format(data['main']['temp'])
        formatted_weather = 'Weather is {}'.format(data['weather'][0]['main'])
        formatted_minMax = 'Expected high is: {}\nExpected low is: {}'.format(data['main']['temp_max'], data['main']['temp_min'])
        formatted_time = 'Time:{}'.format(time.strftime("%I:%M:%S"))
        self.set_data(formatted_temp, formatted_weather, formatted_minMax, formatted_time)

    def set_data(self, formatted_temp, formatted_weather, formatted_minMax, formatted_time):
        self.formatted_temp = formatted_temp 
        self.formatted_weather = formatted_weather
        self.formatted_minMax = formatted_minMax
        self.formatted_time = formatted_time
    
    def return_data(self):
        weatherData = {'CurrentTemp':self.formatted_temp,'CurrentWeather':self.formatted_weather,
        'MinMaxTemp':self.formatted_minMax,'CurrentTime':self.formatted_time}
        return weatherData