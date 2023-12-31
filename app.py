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
    # US time zones 
    "US/Pacific", "US/Mountain", "US/Central", "US/Eastern", "US/Hawaii",
    
    # Oceania time zones
    "Pacific/Auckland", "Australia/Melbourne", "Australia/Sydney", "Australia/Darwin", "Australia/Perth",

    # Asia time zones
    "Asia/Seoul", "Asia/Shanghai", "Asia/Jerusalem", 
    "Asia/Singapore", "Asia/Bangkok", "Asia/Tokyo",

    # Europe time zones
    "Europe/Berlin", "Europe/Moscow", "Europe/Rome", "Europe/Kiev",
    "Europe/Zurich", "Europe/Madrid", "Europe/Lisbon", "Europe/Paris", "Europe/London",

    # Corrected GMT time zones
    "Etc/GMT", "Etc/GMT+1", "Etc/GMT+2", "Etc/GMT+3", "Etc/GMT+4", "Etc/GMT+5", 
    "Etc/GMT+6", "Etc/GMT+7", "Etc/GMT+8", "Etc/GMT+9", "Etc/GMT+10", 
    "Etc/GMT+11", "Etc/GMT+12",
    "Etc/GMT-1", "Etc/GMT-2", "Etc/GMT-3", "Etc/GMT-4", "Etc/GMT-5", 
    "Etc/GMT-6", "Etc/GMT-7", "Etc/GMT-8", "Etc/GMT-9", "Etc/GMT-10", 
    "Etc/GMT-11", "Etc/GMT-12"
    ]

    time_zones_data = {}
    for tz in time_zones:
        now = datetime.datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        tz_id = tz  # Just use the time zone as it is
        time_zones_data[tz_id] = now
    return time_zones_data
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
