from weatherHelper import weatherHandler
from lxml.html import builder as E 
import lxml as lxml

def getCity(city):
	weatherStuff = weatherHandler(city)
	weatherStuff.get_weather()
	html = E.HTML(
		E.HEAD(
			E.TITLE("Weather for:{}".format(weatherStuff.city))
			),
		E.BODY(
			E.H1("Weather for:{}".format(weatherStuff.city)),
			E.P("{}".format(weatherStuff.formatted_temp)),
			E.P("{}".format(weatherStuff.formatted_weather)),
			E.P("{}".format(weatherStuff.formatted_minMax)),
			E.P("{}".format(weatherStuff.formatted_time))
			)
	)
	byteString = lxml.html.tostring(html)
	string = byteString.decode('utf-8')
	return string
