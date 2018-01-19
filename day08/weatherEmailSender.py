import smtplib
import requests
import time
from bs4 import BeautifulSoup
import urllib.request
import sys
gmailPassword = sys.argv[1]
gmailAddress = sys.argv[0]
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
senderEmail = ''
urlStencil = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4be652987aa8129403b8d090deef289b&'
city = 'toronto'
x = 0
global weatherString


def login(email, password):
    smtpObj.ehlo()
    print(smtpObj.login(email, password))


def genSubject():
    return 'Time:{}'.format(time.strftime("%I:%M:%S\n"))


def createEmail(weather, comic):
    print(weather)
    x = 'Current weather:\n{} {}'.format(weather, comic)
    print(x)
    return x
    


def getComic():
    httpVar = 'http:'
    url = 'http://explosm.net/comics/latest/'
    soup = BeautifulSoup(urllib.request.urlopen(url), 'html5lib')
    imgSrc = soup.find(id='main-comic')['src']
    imgSrc = '{}' + imgSrc
    imgSrc = imgSrc.format(httpVar)
    imgUrlSrc = "<img src='{}' alt='Logo' title='Logo' style='display:block' width='200' height='87' />'".format(imgSrc)
    return imgUrlSrc



    
def getWeather(url, city):
    finalURL = url.format(city)
    data = requests.get(finalURL).json()
    formatData(data)


def formatData(data):
    formatted_temp = 'Current temp is: {}\n'.format(data['main']['temp'])
    formatted_weather = 'Weather is {}\n'.format(data['weather'][0]['main'])
    formattedMinMax = 'Expected high is: {}\nExpected low is: {}\n'.format(data['main']['temp_max'], data['main']['temp_min'])
    formattedTime = 'Time:{}'.format(time.strftime("%I:%M:%S\n"))
    createWeatherString(formatted_temp, formatted_weather, formattedMinMax, formattedTime)


def createWeatherString(formatted_temp, formatted_weather, formattedMinMax, formattedTime):
    global weatherString
    weatherString = formatted_temp + formatted_weather + formattedMinMax + formattedTime
    


def setEmailInfo():
    subject = genSubject()
    email = createEmail(weatherString, getComic())
    sendEmail(gmailAddress, subject, email)


def sendEmail(recipient, subject, email):
    formattedEmail = "Subject: {}.\n{}".format(subject, email)
    sendmailStatus = smtpObj.sendmail(senderEmail, recipient, formattedEmail)
    print(sendmailStatus)

getWeather(urlStencil, city)
login(gmailAddress, gmailPassword)
setEmailInfo()
smtpObj.quit()
