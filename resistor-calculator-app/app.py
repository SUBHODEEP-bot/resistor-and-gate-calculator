﻿from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is your Resistor Calculator App hosted on Render!"
