
import genHTML
from emailHelper import emailHander
from flask import Flask, render_template, request

app = Flask(__name__)
emailer = emailHander()


@app.route('/')
@app.route('/emaillogin')
def entry_page() -> 'html':
	return render_template('emailLogin.html')


@app.route('/sendMail', methods=['POST'])
def sendMail() -> 'html':
	email = request.form['email']
	password = request.form['password']
	emailer.set_user_email(email)
	emailer.set_user_password(password)
	print(emailer.login())
	return render_template('sendMail.html')

@app.route('/results', methods=['POST'])
def result():
	city = request.form['city']
	emails = request.form['emails']
	emails = emails.split(',')
	weather = genHTML.getCity(city)
	weather = '<!doctype html>{}'.format(weather)
	for i in emails:
		print(str(i)) 
		emailer.set_recipient(str(i))
		emailer.generate_email('Weather',weather)
		emailer.send_mail()
	emailer.quit()
	emails = ''.join(emails)
	return render_template('results.html',the_emails=emails)

app.run(debug=True)

