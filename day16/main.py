from flask import Flask, render_template, request
from DBcm import UseDatabase
app = Flask(__name__)

dbconfig = {
	'host':'127.0.0.1',
	'user':'root',
	'password':'password',
	'database': 'weaUserEmails',
}

@app.route('/')
@app.route('/main')
def mainPage():
	return render_template('home.html')
@app.route('/admin')
def adminPage():
	return render_template('admin.html')
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