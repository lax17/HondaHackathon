from utils import *
from constants import *
import requests


def CarBasedShopping(current_lat,current_long,product_name,product_price=None):
    CARBASEDSHOPPINGSUGGEST = "Company Name {} {:0.2f} koilmeter away from your for product {} with product description as {} for price {} rupees"
    payload = {"current_lat":float(current_lat),"current_long":float(current_long),"product_name":product_name}
    if product_price:
        payload["product_price"] = product_price
    response = requests.request("GET",PRODUCTLIST_URL, headers=PRODUCTLISTAPIHEADER, data=json.dumps(payload))
    response = json.loads(response.text)
    try:
        for res in response["result"]:
            CARBASEDSHOPPINGSUGGEST = CARBASEDSHOPPINGSUGGEST.format(res["Company_Name"],res["distance_diff"],res["productname"],res["productdescription"],res["productprice"])
        prepare_voice_output(CARBASEDSHOPPINGSUGGEST)
    except Exception as e:
        print(e)
        prepare_voice_output(response["result"])



CarBasedShopping(current_lat=45.78,current_long=36.7,product_name="Dress")