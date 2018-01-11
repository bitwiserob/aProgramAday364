import tkinter as tk
from tkinter import ttk
outData = ''
startNum = 0
win = tk.Tk()
win.title('outPut to file')
#|======================================|#
instruct = ttk.Label(win, text='Enter some text to copy to file')
instruct.grid(column=0,row=0)

def copyToFile():
    outData = textIn.get()
    action.configure(text='copied')
    outputToFile(outData)

def outputToFile(data):
    global startNum
    filename = 'file000{}.txt'.format(startNum)
    startNum += 1
    file = open(filename,'w')
    file.writelines(data)
    file.close()
    
    

action = ttk.Button(win, text='copy', command=copyToFile)
action.grid(column=1,row=0)

textIn = tk.StringVar()
textEntered = ttk.Entry(win,width=30,textvariable=textIn)
textEntered.grid(column=2,row=0)
#|======================================|#


win.mainloop()