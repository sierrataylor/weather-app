from flask import Flask, render_template, request
import requests
import configparser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/weather", methods=["GET", "POST"])
def render_weather_page():
    zip_code = request.form['zipCode'] 
    api = get_api()
    data = get_weather_results(zip_code, api)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"] 
    return render_template("weather.html", location=location, temp=temp, weather=weather, feels_like=feels_like)
    
def get_api():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config['openweathermap']['api']

def get_weather_results(zip_code, api):
    url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api)
    r = requests.get(url)
    return r.json()
    
if __name__ == "__main__":
	app.run(debug=True)