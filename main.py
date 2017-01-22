# Author: Patrick Shinn
# version: 1/6/16
from flask import Flask, render_template
from apixu_API.apixu_client import ApixuClient
import calendar
import datetime
import os



# setting up flask
app = Flask(__name__)

# setting up how web pages will work


@app.route('/')
def index():
    weather = get_weather()
    forecast = get_forecast()
    return render_template("index.html", current_temp=weather['temp'], current_weather=weather['description'],
                           wind_speed=weather['wind_speed'], icon=weather["icon"],
                           date0=forecast[0]['day'], high0=forecast[0]['high'], icon0=forecast[0]['icon'],
                           low0=forecast[0]['low'], condition0=forecast[0]['condition'],
                           date1=forecast[1]['day'], high1=forecast[1]['high'], icon1=forecast[1]['icon'],
                           low1=forecast[1]['low'], condition1=forecast[1]['condition'],
                           date2=forecast[2]['day'], high2=forecast[2]['high'], icon2=forecast[2]['icon'],
                           low2=forecast[2]['low'], condition2=forecast[2]['condition'],
                           date3=forecast[3]['day'], high3=forecast[3]['high'], icon3=forecast[3]['icon'],
                           low3=forecast[3]['low'], condition3=forecast[3]['condition'],
                           date4=forecast[4]['day'], high4=forecast[4]['high'], icon4=forecast[4]['icon'],
                           low4=forecast[4]['low'], condition4=forecast[4]['condition']
                           )


# +++++++++++++++++ utility functions +++++++++++++++++

# api key and client for the weather API
pwd = os.path.dirname(os.path.realpath(__file__))
api_key = open(pwd + "/secrets/Apixu.key", "r")
api_key = api_key.readline()
weather_client = ApixuClient(api_key=api_key)

json_file = weather_client.getForecastWeather(q="25701", days=5)


# current weather
def get_weather():
    now = json_file['current']
    weather = dict()
    weather["temp"] = now['temp_f']
    weather["description"] = now['condition']['text']
    weather["wind_speed"] = now['wind_mph']
    weather["wind_direction"] = now['wind_dir']
    weather["pressure"] = now['pressure_in']
    weather["icon"] = now['condition']['icon']
    return weather


# processing of forecast
def get_forecast():
    weather_list = [[], [], [], [], []] # will be the returned list of forecasts
    raw_forecast = json_file['forecast']['forecastday']  # the data is organized by day & time via the index!

    counter = 0
    for day in raw_forecast:
        # getting the day of the week
        date = datetime.date.weekday(datetime.datetime.now())
        date = (date + counter) % 7
        date = calendar.day_name[date]

        # building the weather dictionary
        weather = dict()
        weather["day"] = date
        weather["high"] = day['day']['maxtemp_f']
        weather["low"] = day['day']['mintemp_f']
        weather["precipitation"] = day['day']['totalprecip_in']
        weather["condition"] = day['day']['condition']['text']
        weather["icon"] = day['day']['condition']['icon']
        weather["city"] = json_file['location']['name']
        weather["state"] = json_file['location']['region']

        # appending to weather_list
        weather_list[counter] = weather
        counter += 1
    return weather_list


# get the google calendar info
# todo learn the google calendar api
def get_calendar():
    return None

# +++++++++++++++++ utility functions end +++++++++++++++++

# runs the program
if __name__ == '__main__':
    app.run(debug=True)
