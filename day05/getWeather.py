import tkinter as tk
import requests
import time
from tkinter import ttk
from tkinter import scrolledtext

def setData():
    urlStencil = 'http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid=4be652987aa8129403b8d090deef289b&'
    formats = ('metric','imperial')
    city = cityEntryBoxString.get()
    formatSelection=radioSelection.get()
    x = int(formatSelection)
    getWeather(urlStencil, formats[x], city)
    

def outDataToGui(formatted_temp, formatted_weather, formattedMinMax, formattedTime):
    scr.insert(tk.END, formatted_temp)
    scr.insert(tk.END, formatted_weather)
    scr.insert(tk.END, formattedMinMax)
    scr.insert(tk.END, formattedTime)
    scr.insert(tk.END,'------------------------------')

def formatData(data):
    formatted_temp = 'Current temp is: {}\n'.format(data['main']['temp'])
    formatted_weather = 'Weather is {}\n'.format(data['weather'][0]['main'])
    formattedMinMax = 'Expected high is: {}\nExpected low is: {}\n'.format(data['main']['temp_max'],data['main']['temp_min'])
    formattedTime = 'Time:{}'.format(time.strftime("%I:%M:%S\n"))
    outDataToGui(formatted_temp, formatted_weather, formattedMinMax, formattedTime)
    


def getWeather(url, formats, city):
    finalURL =  url.format(city, formats)
    data = requests.get(finalURL).json()
    formatData(data)
    
    
    


window = tk.Tk()
window.title('Get Weather')
# Labels
cityName = ttk.Label(window,text='Enter City Name')
# Buttons
submit = ttk.Button(window, text='submit', command=setData)
# entry boxes
cityEntryBoxString = tk.StringVar()
cityBox = ttk.Entry(window, width=12,textvariable=cityEntryBoxString)
#Scrolled textBox
scrol_w = 30
scrol_h = 15 
scr = scrolledtext.ScrolledText(window, width=scrol_w, height=scrol_h, wrap=tk.WORD,)
#radio button
radioSelection = tk.IntVar()
radioButtonParagraph = tk.Radiobutton(window, text='celsius', variable=radioSelection, value='0')
radioButtonParagraph.select()
radioButtonBodyTag = tk.Radiobutton(window, text='fahrenheit', variable=radioSelection, value='1')
radioButtonBodyTag.deselect()
#UI
cityName.grid(column=0,row=0)
cityBox.grid(column=1,row=0)
submit.grid(column=2,row=0)
radioButtonParagraph.grid(column=0, row=1, stick=tk.W)
radioButtonBodyTag.grid(column=1, row=1, stick=tk.W)
scr.grid(column=0,columnspan=4,row=2)
window.mainloop()
