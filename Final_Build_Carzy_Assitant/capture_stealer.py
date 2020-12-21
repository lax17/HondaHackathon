from datetime import datetime
import requests
from constants import *
from utils import reverseGeocode
import json
from utils import *


def capture_stealer(origin, destination):
    try:
        CAPTURESTEALER = "Please Find the nearest toll {} and connect and file complaint"
        params = {'from': {'address': '{}'.format(origin)}, 'to': {'address': '{}'.format(destination)},
                  'vehicleType': '2AxlesAuto'}
        headers = {'Content-type': 'application/json', 'x-api-key': Tolls_Key}
        response = requests.post(Tolls_URL, json=params, headers=headers)
        response = json.loads(response.text)
        a = response.get('summary').get('route')[0].get('location')
        coordinates = tuple(a.values())
        address = reverseGeocode(coordinates)
    except Exception as e:
        address = None
        print(e)
    if address is not None:
        CAPTURESTEALER = CAPTURESTEALER.format(address)
        prepare_voice_output(CAPTURESTEALER)

capture_stealer("mulund","kalyan")



