import logging
from typing import Iterator
import requests
import os
from dotenv import load_dotenv

from logger import NAME

logger = logging.getLogger(NAME)
logger.setLevel(logging.INFO)

load_dotenv()


def get_bus_arrival(stop_id: int):
    """Send GET request to LTA Bus Arrival API and return the arrival timings of all buses in that bus stop as of request time."""
    json_data = None
    
    url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"

    payload = {"BusStopCode": stop_id}

    headers = {"AccountKey": os.getenv("LTA_ACCOUNT_KEY"), "acccept": "application/json"}

    try:
        response = requests.request("GET", url, headers=headers, params=payload)
        json_data = response.json()
    except requests.exceptions.JSONDecodeError as e:
        logger.error(e)
        logger.debug(response.content)
        
    return json_data


def format_response():
    """TODO: Format response to human readable form"""

    response = get_bus_arrival(45451)

    bus_services = response["Services"]
    for s in bus_services:
        print(s["ServiceNo"])
        bus_timings: Iterator = filter(lambda x: "NextBus" in x, s)
        for timing in bus_timings:
            print(timing, s[timing])


if __name__ == "__main__":
    get_bus_arrival(stop_id=45451)
    format_response()
