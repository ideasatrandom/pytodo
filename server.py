from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, url_for,abort
import os

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
  if not session.get('logged_in'):
    return render_template('login.html')
  else:
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
  if request.form['password'] == 'password' and request.form['username'] == 'admin':
    session['logged_in'] = True
    return home()
  else:
    return "Wrong Password"

@app.route("/logout")
def logout():
  session['logged_in'] = False
  return home()

@app.route("/hello")
def hello():
  return render_template('hello.html')

@app.route("/example")
def example():
  return render_template('example.html')

if __name__ == "__main__":
  app.run()