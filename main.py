from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/request')
def request():
  
@app.route('/view')
def view():
  

@app.route('/')
def index():
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
