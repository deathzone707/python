from flask import Flask, redirect, url_for, render_template
from os import environ
import requests as re
import json

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

@app.route('/ip/<ip>')
def ip(ip):
	return render_template('ipinfo.html', ipinformation=ipinfo(ip))

def ipinfo(ip):
	token = environ['IPINFOTOKEN']
	r = re.get(f'http://ipinfo.io/{ip}?token={token}')
	r = json.loads(r.text)
	return r

if __name__ == "__main__":
	app.run()