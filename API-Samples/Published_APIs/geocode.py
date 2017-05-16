import json
import requests

def getGeocodeLocation(inputString):
           
    google_api_key = "Paste your google API Key here"

    url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    querystring = {"address":"{}".format(inputString),"key":"{}".format(google_api_key)}
    
    response = requests.request("GET", url, params=querystring)
    responseDict = json.loads(response.text)
    
    latitude = responseDict['results'][0]['geometry']['location']['lat']
    longitude = responseDict['results'][0]['geometry']['location']['lng']

    
    return (latitude,longitude)

