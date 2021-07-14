from flask import Flask, render_template, request
import socket
import requests
#import configparser

app = Flask(__name__)

api = '3a152a1afe50c56cf61fef12cd96ea2f'
ip = requests.get('https://api.ipify.org').text
params = {
    'access_key': api,
    'query': ip,
    'units': 'f'
}

@app.route("/")
def weather():
    api_result = requests.get('http://api.weatherstack.com/current', params)
    json_response = api_result.json()
    print(json_response)
    print()
    location = str(json_response['location']['name'])
    print(json_response['location']['name']+','+json_response['location']['region'])
    return render_template('weather.html', location=location)

if __name__ == "__main__":
	app.run(debug=True)