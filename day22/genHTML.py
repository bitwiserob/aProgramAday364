from lxml.html import builder as E 
import lxml as lxml

def generateHTML(city_info):
	html = E.HTML(
		E.HEAD(
			E.TITLE("Weather for:{}".format(city_info['city']))
			),
		E.BODY(
			E.H1("Weather for:{}".format(city_info['city'])),
			E.P("{}".format(city_info['city_temp'])),
			E.P("{}".format(city_info['city_forecast'])),
			E.P("{}".format(city_info['city_min'])),
			E.P("{}".format(city_info['city_max'])),
			E.P("{}".format(city_info['city_time']))
			)
	)
	byteString = lxml.html.tostring(html)
	string = byteString.decode('utf-8')
	return string
