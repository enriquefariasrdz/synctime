from flask import Flask, render_template
import time
import pytz
import os

def get_current_time():
    current_time = time.time()
    current_time_obj = pytz.utc.localize(time.gmtime(current_time))
    return current_time_obj.strftime("%H:%M:%S")

def get_city_data():
    current_city = "New York"
    city_timezone = "America/New_York"

    cities = [
        {"name": current_city, "timezone": city_timezone},
        {"name": "London", "timezone": "Europe/London"},
        {"name": "Berlin", "timezone": "Europe/Berlin"},
        {"name": "Sydney", "timezone": "Australia/Sydney"},
        {"name": "Tokyo", "timezone": "Asia/Tokyo"}
    ]

    for city in cities:
        time_obj = pytz.utc.localize(pytz.timezone(city["timezone"])).normalize()
        city_time = time_obj.strftime("%H:%M:%S")
        city[current_city] = city_time
    return cities

app = Flask(__name__)

@app.route('/')
def index():
    current_time = get_current_time()
    cities = get_city_data()
    return render_template('index.html', current_time=current_time, cities=cities)

if __name__ == '__main__':
    app.run(debug=True)
