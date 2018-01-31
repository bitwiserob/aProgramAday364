import psycopg2
from weather_helper import WeatherHandler

conn = psycopg2.connect(host="localhost",database="weather", user="draxnol", password="")
cur = conn.cursor()

weather = WeatherHandler()

cities = ['toronto','new york','moscow']

for city in cities:
	weather.set_city(city)
	weather.get_weather()
	weather_data = weather.return_data()
	_SQL = "INSERT INTO weather (city,weather,temp,temp_min,temp_max,time) VALUES('{}','{}',{},{},{},'{}')".format(
		city,weather_data['CurrentWeather'],weather_data['CurrentTemp'],weather_data['MinTemp'],weather_data['MaxTemp'],
		weather_data['CurrentTime'])
	cur.execute(_SQL)
conn.commit()
cur.close()
conn.close()