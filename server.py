from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
  if not session.get('logged_in'):
    return render_template('login.html')
  else:
    return "Ya Logged in"

@app.route('/login', methods=['POST'])
def do_admin_login():
  if request.form['password'] == 'password' and request.form['username'] == 'admin':
    return redirect(url_for('/hello'))
  else:
    flash('wrong password!')
    return home()

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