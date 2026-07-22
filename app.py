from flask import Flask, render_template
from datetime import datetime
import pytz
import os

def get_current_time():
    # Gets the current time in UTC and formats it
    current_time_obj = datetime.now(pytz.utc)
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

    # Get the current time in UTC first
    utc_now = datetime.now(pytz.utc)

    for city in cities:
        # Convert UTC time to the target city's timezone
        target_tz = pytz.timezone(city["timezone"])
        city_time_obj = utc_now.astimezone(target_tz)
        
        # Format the time and assign it to the city dictionary
        city["time"] = city_time_obj.strftime("%H:%M:%S")
        
    return cities

app = Flask(__name__)

@app.route('/')
def index():
    current_time = get_current_time()
    cities = get_city_data()
    return render_template('index.html', current_time=current_time, cities=cities)

if __name__ == '__main__':
    app.run(debug=True)