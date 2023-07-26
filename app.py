from flask import Flask, json
from datetime import datetime
import pytz

app = Flask(__name__)

time_zones = {
    "PST": "US/Pacific",
    "MST": "US/Mountain",
    "CST": "US/Central",
    "EST": "US/Eastern",
    "UTC": "UTC"
}

@app.route("/time")
def time():
    response = {}
    for tz_short, tz in time_zones.items():
        now = datetime.now(pytz.timezone(tz))
        response[tz_short] = now.strftime("%Y-%m-%d %I:%M:%S %p")
    return json.dumps(response)
