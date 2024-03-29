from flask import Flask, render_template, request
import requests
app = Flask(__name__)

ipstack_json = requests.get('http://api.ipstack.com/check?access_key=3ea5ee126f84aa3900d32b15efc32b79&format=1').json()
ip = ipstack_json['ip'] 
params = {
    'access_key': '3a152a1afe50c56cf61fef12cd96ea2f',
    'query': ip,
    'units': 'f'
}
def call_weather_api():
    api_result = requests.get('http://api.weatherstack.com/current', params)
    return api_result

def get_wind_level():
    json_response = call_weather_api().json()
    wind_speed = json_response['current']['wind_speed']
    wind_level = ''
    if(0 <= wind_speed <= 15):
        wind_level = 'Little to no wind'
    elif(16 <= wind_speed <= 20 ):
        wind_level = 'Breezy'
    elif(21 <= wind_speed <= 30):
        wind_level = 'Windy'
    elif(31 <= wind_speed <= 40):
        wind_level = 'Very windy'
    elif(41 <= wind_speed < 73):
        wind_level = 'Dangerously high winds'
    else:
        wind_level = 'Hurricane-force winds!'
    return wind_level

@app.route("/")
def weather():
    json_response = call_weather_api().json() 

    name = json_response['location']['name']
    region = json_response['location']['region'] 
    location = f'{name}, {region}'
    temp = json_response['current']['temperature']
    weather_descriptions = json_response['current']['weather_descriptions'][0] 
    wind_level = get_wind_level()
    humidity = json_response['current']['humidity']
    feels_like = json_response['current']['feelslike']
    img_src = json_response['current']['weather_icons'][0]

    return render_template(
        'weather.html',
        location=location,
        temp=temp,
        feels_like=feels_like,
        weather_descriptions=weather_descriptions,
        wind_level=wind_level,
        humidity=humidity,
        img_src=img_src
        )

 
if __name__ == "__main__":
	app.run(debug=True)