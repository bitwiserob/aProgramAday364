'''
Created on Jan 20, 2018

@author: Robert
'''
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
        formattedMinMax = 'Expected high is: {}\nExpected low is: {}'.format(data['main']['temp_max'], data['main']['temp_min'])
        formattedTime = 'Time:{}'.format(time.strftime("%I:%M:%S"))
        self.set_data(formatted_temp, formatted_weather, formattedMinMax, formattedTime)

    def set_data(self, formatted_temp, formatted_weather, formattedMinMax, formattedTime):
        self.formatted_temp = formatted_temp 
        self.formatted_weather = formatted_weather
        self.formattedMinMax = formattedMinMax
        self.formattedTime = formattedTime
