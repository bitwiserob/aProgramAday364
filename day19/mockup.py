import psycopg2
from flask import Flask, render_template, request
conn = psycopg2.connect(host="localhost",database="users", user="postgres", password="")
cur = conn.cursor()

app = Flask(__name__)



@app.route('/')
@app.route('/home')
def entry_page() -> 'html':
    return render_template('home.html')



@app.route('/store')
def store_page():
	cur.execute("SELECT name,cost,quantity FROM items")
	row = cur.fetchall()
	return render_template('store.html', itemname=row[0][0],itemcost=row[0][1],quantity=row[0][2])



app.run(debug=True)
