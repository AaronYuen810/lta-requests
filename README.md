# Description
Side project that involves creating a simple Flask application that makes GET request to LTA DataMall's Bus Arrival API. How this app work involves supplying a bus stop code of interest, and the API will return a JSON response containing the bus arrival timings of all buses servicing that bus stop as of the request time.

# Pre-requisite
- LTA DataMall API Tokan: Generate from https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html and populate in `.env` file. An example .env template file is provided with `.env.template`


# Setup
1. Create virtual env
```
python -m venv .venv
```
2. Install dependnecies
```
# activate venv
source .venv/bin/activate # mac / unix
.venv/Scripts/activate # windows

# install packages
pip install -r requirements.txt
```

# Interfacing with the app
1. Initialize flask app
```
flask run
```
2. Retrieve bus arrival timings for a specific bus stop by supplying its bus stop code. 
If unsure of your bus stop code, do a quick search in https://busrouter.sg/.
```
127.0.0.1:5000/bus_arrival/<bus_stop_id>
```

3. Example: Fetching bus arrivals for Bukit Gombak Stn (43579) 
```
127.0.0.1:5000/bus_arrival/43579
```

Sample Response:
```
>>> {
  "BusStopCode": "43579",
  "Services": [
    {
      "NextBus": {
        "DestinationCode": "43009",
        "EstimatedArrival": "2024-07-14T15:03:09+08:00",
        "Feature": "WAB",
        "Latitude": "1.3627118333333332",
        "Load": "SEA",
        "Longitude": "103.75145066666667",
        "OriginCode": "43009",
        "Type": "SD",
        "VisitNumber": "1"
      },
      "NextBus2": {
        "DestinationCode": "43009",
        "EstimatedArrival": "2024-07-14T15:17:59+08:00",
        "Feature": "WAB",
        "Latitude": "0.0",
        "Load": "SEA",
        "Longitude": "0.0",
        "OriginCode": "43009",
        "Type": "SD",
        "VisitNumber": "1"
      },
      "NextBus3": {
        "DestinationCode": "43009",
        "EstimatedArrival": "2024-07-14T15:26:59+08:00",
        "Feature": "WAB",
        "Latitude": "0.0",
        "Load": "SEA",
        "Longitude": "0.0",
        "OriginCode": "43009",
        "Type": "SD",
        "VisitNumber": "1"
      },
      "Operator": "TTS",
      "ServiceNo": "945"
    },
    {
      "NextBus": {
        "DestinationCode": "43009",
        "EstimatedArrival": "2024-07-14T15:10:50+08:00",
        "Feature": "WAB",
        "Latitude": "1.3771815",
        "Load": "SEA",
        "Longitude": "103.75168116666667",
        "OriginCode": "44009",
        "Type": "DD",
        "VisitNumber": "1"
      },
      "NextBus2": {
        "DestinationCode": "43009",
        "EstimatedArrival": "2024-07-14T15:21:55+08:00",
        "Feature": "WAB",
        "Latitude": "0.0",
        "Load": "SEA",
        "Longitude": "0.0",
        "OriginCode": "44009",
        "Type": "DD",
        "VisitNumber": "1"
      },
      "NextBus3": {
        "DestinationCode": "43009",
        "EstimatedArrival": "2024-07-14T15:33:55+08:00",
        "Feature": "WAB",
        "Latitude": "0.0",
        "Load": "SEA",
        "Longitude": "0.0",
        "OriginCode": "44009",
        "Type": "DD",
        "VisitNumber": "1"
      },
      "Operator": "SMRT",
      "ServiceNo": "991"
    }
  ],
  "request_time": "Sun, 14 Jul 2024 06:56:13 GMT"
}
```
