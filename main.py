from flask import Flask, session, redirect, url_for, escape, request

from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///data.db', echo=True)

app = Flask(__name__)

@app.route('/request')
def request():
  
@app.route('/view')
def view():
  

@app.route('/')
def index():
  if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('
    

@app.route('/login', methods=['POST'])
def login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('Incorrect Credentials')
    return home()
    

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return index()

app.secret_key = 'key'
