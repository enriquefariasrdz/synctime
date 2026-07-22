import asyncio
import uvicorn

app = Flask(__name__)

CITIES = [
    {"name": "New York", "timezone": "America/New_York"},
    {"name": "London", "timezone": "Europe/London"},
    {"name": "Berlin", "timezone": "Europe/Berlin"},
    {"name": "Sydney", "timezone": "Australia/Sydney"},
    {"name": "Tokyo", "timezone": "Asia/Tokyo"}
]

@app.route('/')
def index():
    current_time = tzlocal().now().strftime("%I:%M %p")
    cities_data = []
    for city in CITIES:
        time_obj = tzutc().localize(pytz.timezone(city['timezone'])).normalize()
        city_time = time_obj.strftime("%I:%M %p")
        cities_data.append({"name": city['name'], "time": city_time})
    return render_template('index.html', current_time=current_time,
cities=cities_data)

if __name__ == '__main__':
    app.run(debug=True)

async def main():
    await uvicorn.run("global_clock:app", host="0.0.0.0", port=8000,
log_level="info")
