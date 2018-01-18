import random as randGen
import urllib.request
import tkinter as tk
import io
from tkinter import ttk
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import ImageTk, Image

httpVar = 'http:'
comicNum = randGen.randrange(1, 4000)
webUrl = "http://explosm.net/comics/{}/"
finalUrl = webUrl.format(comicNum)
print(finalUrl)
soup = BeautifulSoup(urllib.request.urlopen(finalUrl), 'html5lib')

imgSrc = soup.find(id='main-comic')['src']
imgSrc = '{}' + imgSrc
imgSrc = imgSrc.format(httpVar)
print(imgSrc)

page = urlopen(imgSrc)

root = tk.Tk()
frameMenu = tk.Frame(root)
frameComic = tk.Frame(root)

picture = io.BytesIO(page.read())
pil_img = Image.open(picture)
tk_img = ImageTk.PhotoImage(pil_img)

labelText = ttk.Label(frameMenu, text='Comic:')
label = tk.Label(frameComic, image=tk_img)

#randomButton = ttk.Button(frameMenu,text='random Comic', command=getComic)
#randomButton.grid(row=2,column=0)
label.grid(row=0, column=0)
labelText.grid(row=0, column=0)
frameMenu.grid(column=0,row=0)
frameComic.grid(column=1,row=0)
root.mainloop()