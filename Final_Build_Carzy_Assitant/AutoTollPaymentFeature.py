import requests
import json
from CarShoppingServer.utils import distance_diff_kms
from utils import *
from constants import *
# https://tollguru.com/developers/docs/#tolls-object

Amount = 12000

SAID = True


def AutoTollPayment(origin,destination):
    try:
        global Amount
        global SAID
        TOLL_DEDUCTION = "{} rupees has been deducted from your Account for toll payment purpose"
        NEAREST_TOLL_DEDUCT = "we are {:0.2f} km away from toll will will Like if i proceed with the payment"
        ROUTEDETAILS = "From {origin} location to {destination} location we have {toll} Number of tolls and it will take {duration} time to reach"
        params = {'from':{'address': '{}'.format(origin)},'to':{'address':'{}'.format(destination)},'vehicleType': '2AxlesAuto'}
        headers = {'Content-type': 'application/json','x-api-key': Tolls_Key}
        response = requests.post(Tolls_URL, json=params, headers=headers)
        response = json.loads(response.text)
        ROUTEDETAILS = ROUTEDETAILS.format(origin=origin,destination=destination,toll=len(response["routes"][0]["tolls"]),duration=response["routes"][0]["summary"]["duration"]["text"].replace("h","hours"))
        distance_diff = distance_diff_kms(response["summary"]["route"][0]["location"]['lat'],response["summary"]["route"][0]["location"]['lng'],response["routes"][0]["tolls"][0]['lat'],response["routes"][0]["tolls"][0]['lng'])
        if distance_diff <=1.5:
            prepare_voice_output(NEAREST_TOLL_DEDUCT.format(distance_diff))
            if "yes" in prepare_input_from_voice():
                Amount = Amount - response["routes"][0]["tolls"][0]['oneWay']
                print(Amount)
                prepare_voice_output(TOLL_DEDUCTION.format(response["routes"][0]["tolls"][0]['oneWay']))
            else:
                pass
        if SAID == True:
            prepare_voice_output(ROUTEDETAILS)
            SAID = None
    except Exception as e:
        prepare_voice_output(WRONGLOCATIONEXCEPTION)



AutoTollPayment("mulund","kalyan")

