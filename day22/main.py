from flask import Flask, render_template, request
from database_helper import UseDatabase
from email_helper import EmailHandler
from weather_helper import WeatherHandler
import genHTML


app = Flask(__name__)

DB_config = {
    'host': '127.0.0.1',
    'user': 'draxnol',
    'password': '',
    'database': 'weather',
}
email_config = {
    'senderlogin': '',
    'password': ''
}
emailer = EmailHandler(email_config['senderlogin'], email_config['password'])
print(emailer.login())
weather = WeatherHandler()


@app.route('/')
@app.route('/main')
def main_page():
    return render_template('home.html')


@app.route('/admin')
def admin_page():
    return render_template('admin.html')


@app.route('/getweather')
def get_weather():
    with UseDatabase(DB_config) as cursor:
        _SQL = "select user_city from users"
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        print(contents)
        for city in contents:
            cur_city = city[0]

            weather.set_city(str(cur_city))
            weather.get_weather()
            weather_data = weather.return_data()
            _SQL = "INSERT INTO weather (city,weather,temp,temp_min,temp_max,time) VALUES ('{}', '{}',{},{},{},'{}')".format(
                cur_city, weather_data['CurrentWeather'], weather_data[
                    'CurrentTemp'], weather_data['MinTemp'], weather_data['MaxTemp'],
                weather_data['CurrentTime'])
            print(_SQL)
            cursor.execute(_SQL)
    return render_template('getweather.html')


@app.route('/send_emails')
def send_emails():
    with UseDatabase(DB_config) as cursor:
        _SQL = """select user_email,user_city from users"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        for data in contents:
            print('email is: ' + data[0])
            emailer.set_recipient(data[0])
            print('city is: ' + data[1])
            _SQL_weather = """ select * from weather where city = '{}'""".format(data[
                                                                                 1])
            cursor.execute(_SQL_weather)
            city_weather = cursor.fetchall()
            for i in city_weather:
                print(i)
            city_info = {'city': city_weather[0][0], 'city_temp': city_weather[0][1], 'city_forecast': city_weather[
                0][2], 'city_min': city_weather[0][3], 'city_max': city_weather[0][4], 'city_time': city_weather[0][5]}

            msg = genHTML.generateHTML(city_info)
            emailer.generate_email('weather', msg)
            emailer.send_mail()
        emailer.quit()
    return render_template('send_emails.html')


@app.route('/register', methods=['POST'])
def register_page():
    with UseDatabase(DB_config) as cursor:
        _SQL = """insert into users
        (user_email,user_city)
        values
        (%s,%s)"""
        cursor.execute(
            _SQL, (request.form['user_email'], request.form['city']))
    return render_template('register.html')


app.run(debug=True)
