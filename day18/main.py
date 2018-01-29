from flask import Flask, render_template, request
from database_helper import UseDatabase
from email_helper import EmailHandler
import genHTML
app = Flask(__name__)

DB_config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'password',
    'database': 'weauser_emails',
}
email_config = {
    'senderlogin':'senderlogin',
    'password':'password'
}
emailer = EmailHandler(email_config['senderlogin'], email_config['password'])
print(emailer.login())


@app.route('/')
@app.route('/main')
def main_page():
    return render_template('home.html')


@app.route('/admin')
def admin_page():
    return render_template('admin.html')


@app.route('/send_emails')
def send_emails():
    with UseDatabase(DB_config) as cursor:
        _SQL = """select email,name,city from emailTable"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        for data in contents:
            print('email is: ' + data[0])
            emailer.set_recipient(data[0])
            print('name is: ' + data[1])
            print('city is: ' + data[2])
            msg = genHTML.get_city(data[2])
            emailer.generate_email('weather', msg)
            emailer.send_mail()
        emailer.quit()
    return render_template('send_emails.html')


@app.route('/register', methods=['POST'])
def register_page():
    with UseDatabase(DB_config) as cursor:
        _SQL = """insert into emailTable
        (email,name,city)
        values
        (%s, %s, %s)"""
        cursor.execute(_SQL, (request.form['user_email'], request.form['name'], request.form['city']))
    return render_template('register.html')


app.run(debug=True)
