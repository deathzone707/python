from flask import Flask, redirect, url_for
import requests as re

#ip = input('Input 1 IP: ')
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
	n = 0
	while n <= len(ipinfo(ip)):
		return ipinfo(ip)[n]
		n += 1

def ipinfo(ip):
	r = re.get(f'http://ipinfo.io/{ip}?token=d3de8a5e2d4c60')
	return [x.strip(' ') for x in r.text.split('\n')[1:len(ip)-1]]

if __name__ == "__main__":
	app.run(debug=True)