import tkinter as tk
import urllib.parse
import urllib.request
from tkinter import ttk
from tkinter import scrolledtext
url = "http://pastebin.com/api/api_post.php"
Values = {'api_option' : 'paste',
              'api_dev_key' : '',
              'api_paste_code' : '',
              'api_paste_private' : '0',
              'api_paste_name' : 'paste',
              'api_paste_expire_date' : '10M',
              'api_paste_format' : 'python',
              'api_user_key' : 'User Key Here',
              'api_paste_name' : 'paste',
              'api_paste_code' : ''}

    
def submitAction():
    apiCode = apiCodeBoxString.get()
    pasteName = pasteNameBox.get()
    pasteContent = scr.get(1.0, tk.END)
    setValues(apiCode, pasteContent, pasteName)
    sendPaste()


def setValues(apiKey, pasteContent, pasteName):
    global Values
    Values['api_dev_key'] = apiKey
    Values['api_paste_code'] = pasteContent
    Values['api_paste_name'] = pasteName
    return Values


def sendPaste():
    data = urllib.parse.urlencode(Values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    pasteURLBox.insert(tk.END, the_page)


# |================GUI=================| #
window = tk.Tk()
window.title('Paste to pastebin')
# Labels
labelText = ttk.Label(window, text='Enter api code:')
labelBox = ttk.Label(window, text='Enter Paste:')
labelPasteName = ttk.Label(window, text='Enter PasteName:')
labelUrl = ttk.Label(window, text='URL')
# Button
submitButton = ttk.Button(window, text='submit', command=submitAction)
# Text Box
apiCodeBoxString = tk.StringVar()
apiCodeBox = ttk.Entry(window, width=26, textvariable=apiCodeBoxString)

pasteURL = tk.StringVar()
pasteURLBox = ttk.Entry(window, width=20, textvariable=pasteURL)

pasteName = tk.StringVar()
pasteNameBox = ttk.Entry(window, width=26, textvariable=pasteName)

# Scrolled TextBox
scrol_w = 30
scrol_h = 15 
scr = scrolledtext.ScrolledText(window, width=scrol_w, height=scrol_h, wrap=tk.WORD,)

# Adding Widgets to ui
labelText.grid(column=0, row=0, sticky=tk.W)
apiCodeBox.grid(column=1, row=0, columnspan=2, sticky=tk.W)
labelPasteName.grid(column=0, row=1, sticky=tk.W)
pasteNameBox.grid(column=1, row=1, columnspan=2, sticky=tk.W)
labelBox.grid(column=0, row=2, sticky=tk.W)
submitButton.grid(column=0, row=4, sticky=tk.W)
pasteURLBox.grid(column=2, row=4)
labelUrl.grid(column=1, row=4)
scr.grid(column=0, columnspan=4, row=3)

window.mainloop()
