'''
Created on Jan 22, 2018

@author: Robert
'''
from flask import Flask, render_template, request
from emailHelper import emailHandler

app = Flask(__name__)
emailer = emailHandler()

@app.route('/')
@app.route('/emailLogin.html')
def entry_page() -> 'html':
    print("*******")
    print(emailer.code)
    return render_template('emailLogin.html')


@app.route('/sendMail.html', methods=['POST'])
def sendMail() -> 'html':
	print(emailer.code)
	emailer.userEmail = request.form['email']
	emailer.password = request.form['password']
	return render_template('sendMail.html')
@app.route('/results', methods=['POST'])
def results() -> 'html':
	city = request.form['city']
	emails = request.form['emails']
	emails = emails.split(',')
	print(emailer.userEmail)
	print(emailer.password)
	emailer.createSMTPobject()


	return render_template('results.html',the_emails=emails)
app.run(debug=True)
