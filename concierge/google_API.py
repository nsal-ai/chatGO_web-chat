
import requests
from urllib.parse import urlencode
from urllib.parse import urlparse, parse_qsl
import json
import time


GOOGLE_API_KEY = "AIzaSyAuo5bAWOvBReyGLAVc_JbC8k6eMZ6ut3I"

# Geocoding API
# Places API

class GoogleMapsClient(object):
    lat = None
    lng = None
    data_type = 'json'
    location_query = None
    api_key = None

    def __init__(self, api_key=None, address_or_postal_code=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if api_key == None:
            raise Exception('API key required')
        self.api_key = api_key
        self.location_query = address_or_postal_code
        if self.location_query != None:
            self.extract_lat_lng()

    def extract_lat_lng(self, location=None):
        loc_query = self.location_query
        if location != None:
            loc_query = location
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        params = {"address": self.location_query, "key": self.api_key}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        
        if r.status_code not in range(200, 299): 
            return {}
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        lat, lng = latlng.get("lat"), latlng.get("lng")
        self.lat = lat
        self.lng = lng
        return lat, lng




client = GoogleMapsClient(api_key=GOOGLE_API_KEY, address_or_postal_code=str(input("enter your location")))
print(client.lat, client.lng)

#print(client.search('thai', radius=100))




#print(client.detail(place_id='ChIJ1XGIYT8FdkgRl_7t9uh8rGs')['result']['name']) # place id needs to be extracted GoogleMapsClient
#print(client.detail(place_id='ChIJG6soKcwEdkgRN5Q-HvqfMbc'))




class GooglePlaces(object):
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey
 
    def search_places_by_coordinate(self, location, radius, types):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'types': types,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return places
 
    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details
if __name__ == '__main__':
    api = GooglePlaces("AIzaSyAuo5bAWOvBReyGLAVc_JbC8k6eMZ6ut3I")
    places = api.search_places_by_coordinate(f"{client.lat} ,{client.lng}", "50", "restaurant")
    fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']
    for place in places:
        details = api.get_place_details(place['place_id'], fields)
        try:
            website = details['result']['website']
        except KeyError:
            website = ""
 
        try:
            name = details['result']['name']
        except KeyError:
            name = ""
 
        try:
            address = details['result']['formatted_address']
        except KeyError:
            address = ""
 
        try:
            phone_number = details['result']['international_phone_number']
        except KeyError:
            phone_number = ""
 
        try:
            reviews = details['result']['reviews']
        except KeyError:
            reviews = []
        print("===================PLACE===================")
        print("Name:", name)
        print("Website:", website)
        print("Address:", address)
        print("Phone Number", phone_number)
        print("==================REVIEWS==================")
        for review in reviews:
            author_name = review['author_name']
            rating = review['rating']
            text = review['text']
            time = review['relative_time_description']
            profile_photo = review['profile_photo_url']
            print("Author Name:", author_name)
            print("Rating:", rating)
            print("Text:", text)
            print("Time:", time)
            print("Profile photo:", profile_photo)
            print("-----------------------------------------")









