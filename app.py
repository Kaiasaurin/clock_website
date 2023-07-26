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
    time_zones = ["US/Pacific", "US/Mountain", "US/Central", "US/Eastern", "UTC"]
    time_zones_data = {}
    for tz in time_zones:
        now = datetime.datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        time_zones_data[tz] = now
    return time_zones_data
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
