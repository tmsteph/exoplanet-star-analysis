# pip install flask-bootstrap
import sqlite3
from flask import Flask
from flask import render_template  



app = Flask(__name__)



@app.route('/test')
def hello():
	return 'Hello World!!!!'

@app.route('/')
def home():
	return render_template('index.html')	

if __name__ == "__main__":
        app.run(debug = True)
