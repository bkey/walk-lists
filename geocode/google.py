import requests
from models.mailing_address_dim import MailingAddresDim

BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'


class GoogleGeocoder(object):
    """gets lat and long coordinates from address via google api"""
    def __init__(self, api_key):
        self.api_key = api_key

    def get_lat_long_for_address(self, address_string):
        parameters = {
            'key': self.api_key,
            'address': address_string
        }
        response = requests.get(BASE_URL, parameters)
        if response.status_code == 200:
            json_response = response.json()
            results = json_response['results']
            if results:
                first_result = results[0]
                if 'geometry' in first_result:
                    loc = first_result['geometry']['location']
                    return loc['lat'], loc['lng']

        return None, None