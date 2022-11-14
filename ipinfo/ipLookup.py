from flask import Flask, redirect, url_for
from os import environ
import requests as re

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello! This is the main page. <h1>WELCOME HUMAN</h1>"

@app.route("/<name>")
def user(name):
	return f"This is the name page. {name}"

@app.route('/ip/<ip>')
def ip(ip):
	return ipinfo(ip)

def ipinfo(ip):
	token = environ['IPINFOTOKEN']
	r = re.get(f'http://ipinfo.io/{ip}?token={token}')
	return [x for x in r.text.split('\n')[1:len(ip)-1]]

if __name__ == "__main__":
	app.run()