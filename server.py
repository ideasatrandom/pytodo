from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('hello.html')

@app.route("/example")
def example():
  return render_template('example.html')

if __name__ == "__main__":
  app.run()