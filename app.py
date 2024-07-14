"""
Simple web app that make get request to LTA DataMall's Bus Arrival API. 

This app will serve my bus arrival widget to inform me the optimal time for me to leave home for the bus stop, with minimal waiting.
"""

import logging
from flask import Flask, Response, jsonify, url_for
from datetime import datetime, timezone, timedelta

from lta import get_bus_arrival
from datetime import timezone

from logger import NAME

app = Flask(NAME)
app.logger.setLevel(logging.DEBUG)

SGT = timezone(timedelta(hours=8))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bus_arrival/<int:stop_id>")
def bus_arrival(stop_id: int) -> Response:

    json_data = get_bus_arrival(stop_id)
    # json_data["request_time"] = datetime.now(SGT)

    return jsonify(json_data)


with app.test_request_context():
    print(url_for("bus_arrival", stop_id=45451))

if __name__ == "__main__":
    app.run()
