from geocode import getGeocodeLocation
import json
import requests

import sys
import codecs
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "Paste here your foursquare client ID"
foursquare_client_secret = "Paste here your foursquare client secret"
oauth_token = "Paste here your foursquare oauth token or use the token below"
# "G5HSEVQPKDADDS13U3DLINR2LFKGRL0UDX0GOKMR0MDO5LEH"


def findARestaurant(mealType,location):
    #1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    #2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
    # HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    #3. Grab the first restaurant
    #4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
    #5. Grab the first image
    #6. If no image is available, insert default a image url
    #7. Return a dictionary containing the restaurant name, address, and image url
    #restAdress = responseDict['response']['venues'][0]['location']['address']

    # Geocode from Google    
    latitude, longitude = getGeocodeLocation(location)
	radius = 15000

    # Venues from Foursquare
    url = "https://api.foursquare.com/v2/venues/search"
    querystring = {"v":"20161016","ll":"{},{}".format(latitude, longitude),"query":"{}".format(mealType),"intent":"browse", "radius":"{}".format(radius),"client_id":"{}".format(foursquare_client_id), "client_secret":"{}".format(foursquare_client_secret) }

    response = requests.request("GET", url, params=querystring)
    responseDict = json.loads(response.text)
    
    # Getting data from first venue if it exists
    if responseDict['response']['venues']:
        restName = responseDict['response']['venues'][0]['name']
        restFullAdress = "".join(responseDict['response']['venues'][0]['location']['formattedAddress'])

        venueId = responseDict['response']['venues'][0]['id']

        # Getting photos from api
        url = 'https://api.foursquare.com/v2/venues/{}/photos?oauth_token={}&v=20150603'.format(venueId, oauth_token)
        imgResult = requests.request("GET", url, params="")        
        responseImg = json.loads(imgResult.text)
        
        # Getting the first image if it exists
        if responseImg['response']['photos']['items']:
            res = "300x300"
            prefix = responseImg['response']['photos']['items'][0]['prefix']
            suffix = responseImg['response']['photos']['items'][0]['suffix']
            imageLink = "{}{}{}".format(prefix,res,suffix)
        else: # Else use this image
            imageLink = "http://static5.uk.businessinsider.com/image/569535aadd089578468b45ec-1190-625/the-21-best-restaurants-for-a-power-lunch-in-new-york-city.jpg" 

        print("Name  : {}".format(restName))
        print("Adress: {}".format(restFullAdress))
        print("Photo : {}".format(imageLink))
        
        
        return {"" : restName, "" : restFullAdress, "" : imageLink}
    
    else:
        print("No restaurants found in this area")
        
        return "No restaurants found"
        

if (__name__ == '__main__'):
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")
