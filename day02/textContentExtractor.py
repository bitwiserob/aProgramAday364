import tkinter as tk
import urllib.request
from lxml.html import fromstring
from tkinter import ttk
from tkinter import scrolledtext

# |============Declarations============| #

webURL = 'http://httpbin.org/html'


# |=============Functions==============| #
def setURL():
    webURL = urlBoxString.get()
    radSel = radioSelection.get()
    openURL(webURL,radSel)


def openURL(webURL,radSel):
    content = urllib.request.urlopen(webURL).read()
    doc = fromstring(content)
    if radSel == 1:
        for selectedTag in doc.cssselect('p'):
            scr.insert(tk.END,selectedTag.text_content())
    elif radSel == 2:
        for selectedTag in doc.cssselect('body'):
            scr.insert(tk.END,selectedTag.text_content())
    elif radSel == 3:
        for selectedTag in doc.cssselect('head'):
            scr.insert(tk.END,selectedTag.text_content())
     
     

# |================GUI=================| #
window = tk.Tk()
window.title('get text content')
# Labels
labelText = ttk.Label(window, text='Enter URL:')
labelTags = ttk.Label(window, text='select tags')
# Button
startButton = ttk.Button(window, text='start', command=setURL)
# Text Box
urlBoxString = tk.StringVar()
urlBox = ttk.Entry(window, width=12, textvariable=urlBoxString)
# Radio stuff
radioSelection = tk.IntVar()

radioButtonParagraph = tk.Radiobutton(window, text='Paragraph', variable=radioSelection, value='1')
radioButtonParagraph.select()

radioButtonBodyTag = tk.Radiobutton(window, text='Body', variable=radioSelection, value='2')
radioButtonBodyTag.deselect()

radioButtonHeadTag = tk.Radiobutton(window, text='Head', variable=radioSelection, value='3')
radioButtonHeadTag.deselect()
# Scrolled TextBox
scrol_w = 30
scrol_h = 15 
scr = scrolledtext.ScrolledText(window, width=scrol_w, height=scrol_h, wrap=tk.WORD,)

# Adding Widgets to ui
labelText.grid(column=0, row=0)
urlBox.grid(column=1, row=0)
startButton.grid(column=2, row=0)
labelTags.grid(column=0, row=1)
radioButtonParagraph.grid(column=1, row=1, stick=tk.W)
radioButtonBodyTag.grid(column=2, row=1, stick=tk.W)
radioButtonHeadTag.grid(column=3, row=1, stick=tk.W)
scr.grid(column=0, columnspan=4)



window.mainloop()
