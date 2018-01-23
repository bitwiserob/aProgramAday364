from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def entry_page() -> 'html':
	return render_template(
		'index.html')
def logUserInfo(req:'request',uEmail:str,uName:str,comment:str) -> None:
	dbconfig = {'host':'127.0.0.1',
				'user':'dreambriefDB',
				'password':'password',
				'database':'emailLog',}
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()
	_SQL = """insert into log 
			   (email,username,usercomment)
			   values
			   (%s,%s,%s)"""
	cursor.execute(_SQL,(uEmail,uName,comment,))
	conn.commit()
	cursor.close()
	conn.close()

	# with open ('userInfo.log', 'a') as log:
	# 	print(uEmail+,uName,comment,file=log, sep='|')

@app.route('/results', methods=['POST'])
def process_signup() -> 'html':
	userComment =  str(request.form['comments'])
	userEmail = str(request.form['UserEmail'])
	userName = str(request.form["UserName"])
	logUserInfo(request,userEmail,userName,userComment)
	return render_template(
		'results.html',the_username=userName,the_useremail=userEmail)


app.run(debug=True)
