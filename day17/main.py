from flask import Flask, render_template, request
from DBcm import UseDatabase
from emailHelper import emailHandler
import genHTML
app = Flask(__name__)

dbconfig = {
	'host':'127.0.0.1',
	'user':'root',
	'password':'1131',
	'database': 'weaUserEmails',
}
emailconfig={
	'senderlogin':'senderlogin',
	'password':'password'
}
emailer = emailHandler(emailconfig['senderlogin'],emailconfig['password'])
print(emailer.login())


@app.route('/')
@app.route('/main')
def mainPage():
	return render_template('home.html')
@app.route('/admin')
def adminPage():
	return render_template('admin.html')
@app.route('/sendEmails')
def sendEmails():
	with UseDatabase(dbconfig) as cursor:
		_SQL = """select email,name,city from emailTable"""
		cursor.execute(_SQL)
		contents = cursor.fetchall()
		for i in contents:
			print('email is: ' + i[0])
			emailer.set_recipient(i[0])
			print('name is: ' + i[1])
			print('city is: ' + i[2])
			msg = genHTML.getCity(i[2])
			emailer.generate_email('weather',msg)
			emailer.send_mail()
		emailer.quit()
	return render_template('sendEmails.html')

@app.route('/register', methods=['POST'])
def registerPage():
	with UseDatabase(dbconfig) as cursor:
		_SQL = """insert into emailTable
		(email,name,city)
		values
		(%s, %s, %s)"""
		cursor.execute(_SQL,(request.form['userEmail'],request.form['name'],request.form['city']))
	return render_template('register.html')
app.run(debug=True)