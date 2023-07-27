from flask import Flask, render_template, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    time_zones_data = get_time_zones()
    return render_template('clock.html', time_zones = time_zones_data)

@app.route('/time')
def time():
    time_zones_data = get_time_zones()
    return jsonify(time_zones_data)

def get_time_zones():
    time_zones = [
        "US/Pacific", "US/Mountain", "US/Central", "US/Eastern",
        "Pacific/Auckland", "Australia/Melbourne", "Australia/Sydney", "Australia/Darwin", "Australia/Perth",
        "Asia/Seoul", "Asia/Shanghai", "Asia/Beijing", "Asia/Jerusalem", "Asia/Singapore", "Asia/Bangkok", "Asia/Tokyo", "Pacific/Fiji",
        "Europe/Berlin", "Europe/Moscow", "Europe/Rome", "Europe/Kiev", "Europe/Zurich", "Europe/Madrid", "Europe/Lisbon", "Europe/Paris", "Europe/London"        
    ]
    time_zones_data = {}
    for tz in time_zones:
        now = datetime.datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        tz_id = tz.replace("/", "-")  # Replace "/" with "-" to create a valid CSS ID
        time_zones_data[tz_id] = now
    return time_zones_data
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
