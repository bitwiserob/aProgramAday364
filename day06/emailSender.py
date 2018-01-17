import smtplib
from tkinter import ttk
from tkinter import scrolledtext
import tkinter as tk
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
senderEmail = ''


def login(email, password):
    smtpObj.ehlo()
    print(smtpObj.login(email, password))


def submitAction():
    recipient = recipientBox.get()
    subject = subjectBox.get()
    email = scr.get(1.0, tk.END)
    sendEmail(recipient, subject, email)


def sendEmail(recipient, subject, email):
    formattedEmail = "Subject: {}.\n{}".format(subject, email)
    sendmailStatus = smtpObj.sendmail(senderEmail, recipient, formattedEmail)
    print(sendmailStatus)


def loginAction():
    global senderEmail
    senderEmail = BoxEmail.get()
    password = BoxPassword.get()
    frameLogin.grid_forget()
    frameSendEmail.grid(column=0, row=0)
    login(senderEmail, password)


def on_closing():
    smtpObj.quit()
    root.destroy()

    
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
frameLogin = tk.Frame(root)
frameSendEmail = tk.Frame(root)

# #Login Frame
startButton = ttk.Button(frameLogin, text='submit', command=loginAction)
startButton.grid(column=1, row=3, columnspan=3)
labelEmail = ttk.Label(frameLogin, text='Email:')
labelPassword = ttk.Label(frameLogin, text='Password:')
BoxStringEmail = tk.StringVar()
BoxStringPassword = tk.StringVar()
BoxEmail = ttk.Entry(frameLogin, width=24, textvariable=BoxStringEmail)
BoxPassword = ttk.Entry(frameLogin, width=24, show="*", textvariable=BoxStringPassword)

labelEmail.grid(column=0, row=1)
labelPassword.grid(column=0, row=2)
BoxEmail.grid(column=1, row=1)
BoxPassword.grid(column=1, row=2)
# #Email Frame
# Labels
labelText = ttk.Label(frameSendEmail, text='Recipient:')
labelText2 = ttk.Label(frameSendEmail, text='Subject:')
labelBox = ttk.Label(frameSendEmail, text='Enter Email:')

# Button
submitButton = ttk.Button(frameSendEmail, text='submit', command=submitAction)
# Text Box
recipientBoxString = tk.StringVar()
recipientBox = ttk.Entry(frameSendEmail, width=26, textvariable=recipientBoxString)
subjectBoxString = tk.StringVar()
subjectBox = ttk.Entry(frameSendEmail, width=26, textvariable=subjectBoxString)

# Scrolled TextBox
scrol_w = 30
scrol_h = 15 
scr = scrolledtext.ScrolledText(frameSendEmail, width=scrol_w, height=scrol_h, wrap=tk.WORD,)
labelText.grid(column=0, row=0, sticky=tk.W)
labelText2.grid(column=0, row=1, sticky=tk.W)
recipientBox.grid(column=1, row=0, columnspan=2, sticky=tk.W)
subjectBox.grid(column=1, row=1, columnspan=2, sticky=tk.W)
labelBox.grid(column=0, row=2, sticky=tk.W)
submitButton.grid(column=0, row=4, sticky=tk.W)
scr.grid(column=0, columnspan=4, row=3)

# #

frameLogin.grid(column=0, row=0)
root.mainloop()
