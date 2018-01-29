from weatherHelper import WeatherHandler
from lxml.html import builder as E 
import lxml as lxml

def get_city(city):
	_weather_stuff = WeatherHandler(city)
	_weather_stuff.get_weather()
	html = E.HTML(
		E.HEAD(
			E.TITLE("Weather for:{}".format(_weather_stuff.city))
			),
		E.BODY(
			E.H1("Weather for:{}".format(_weather_stuff.city)),
			E.P("{}".format(_weather_stuff.formatted_temp)),
			E.P("{}".format(_weather_stuff.formatted_weather)),
			E.P("{}".format(_weather_stuff.formatted_minMax)),
			E.P("{}".format(_weather_stuff.formatted_time))
			)
	)
	byteString = lxml.html.tostring(html)
	string = byteString.decode('utf-8')
	return string
