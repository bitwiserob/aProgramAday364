import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter import scrolledtext
ipAddress = '127.0.0.1'
# |=============Functions==============| #

def startPing():
    ipAddress = ipAddressBox.get()
    ping(ipAddress)

def ping(ipAddress):
    out_bytes = subprocess.check_output(['ping',ipAddress])
    out_text = out_bytes.decode('utf-8')
    scr.insert(tk.END, out_text)
    scr.insert(tk.END, '----------------------------')
# |================GUI=================| #

window = tk.Tk()
window.title('ping')
# Labels
ipAddressLabel = ttk.Label(window,text='Enter ip address:')
# Buttons
startButton = ttk.Button(window, text='start', command=startPing)
# entry boxes
ipEntryBoxString = tk.StringVar()
ipAddressBox = ttk.Entry(window, width=12,textvariable=ipEntryBoxString)
#Scrolled textBox
scrol_w = 30
scrol_h = 15 
scr = scrolledtext.ScrolledText(window, width=scrol_w, height=scrol_h, wrap=tk.WORD,)
#UI
ipAddressLabel.grid(column=0,row=0)
ipAddressBox.grid(column=1,row=0)
startButton.grid(column=2,row=0)
scr.grid(column=0,columnspan=4,row=1)
window.mainloop()