'''
Created on Jan 20, 2018

@author: Robert
'''
from weatherHelper import weatherHandler
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
@app.route('/weaApp')
def entry_page() -> 'html':
    return render_template('weaApp.html')


@app.route('/results', methods=['POST'])
def results() -> 'html':
    city = request.form['name']
    weaGet = weatherHandler(city)
    weaGet.getWeather()

    return render_template(
    	'results.html', curCity=city,curTemp=weaGet.formatted_temp, curWeather=weaGet.formatted_weather,curMinMax=weaGet.formattedMinMax,curTime=weaGet.formattedTime)


app.run(debug=True)
