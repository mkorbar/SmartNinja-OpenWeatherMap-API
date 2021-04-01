import requests
from flask import Flask, render_template
from datetime import datetime
import os
import secrets

app = Flask(__name__)


@app.route("/")
def index():
    town = "Postojna,Slovenia"
    api_key = os.getenv("OPEN_WEATHER_MAP_API_KEY")
    units = "metric"

    api_url = "https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units={2}".format(town, api_key, units)
    data = requests.get(url=api_url)
    json_data = data.json()
    sr = datetime.utcfromtimestamp(json_data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', weather_data=json_data, sunrise=sr)


if __name__ == '__main__':
    app.run(debug=True)

