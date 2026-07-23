from flask import Flask, render_template, jsonify
from services.timezone_service import get_city_times
 
app = Flask(__name__)
 
@app.route("/")
def index():
return render_template("index.html")
 
@app.route("/api/times")
def times():
return jsonify(get_city_times())
 
if __name__ == "__main__":
app.run(debug=True)
