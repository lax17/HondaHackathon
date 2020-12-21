Tolls_Key = '3dHq68mqt9LL3gPnGRFnrB7dmtgQ9Qq9'
Tolls_URL = 'https://dev.tollguru.com/v1/calc/here'
PRODUCTLIST_URL = "http://127.0.0.1:5000/productList"
PRODUCTLISTAPIHEADER = {
    'Content-Type': 'application/json'
}
VALUEERROR = "Sorry I did not hear your question, Please repeat again."
MeterIndicator_LowFuel_GAS = "The low fuel warning !!! also light will always turn on when starting up the engine to check the bulb, but should go out once the engine has turned over."
WRONGLOCATIONEXCEPTION = "Location you said as {} and {} Does Not exist on Map. Enter something else."

MeterIndicator_Engine_Failure_Status = "Your engine light is flashing, you can't keep driving the car. It's an emergency If you keep driving, you will likely cause irreversible damage"
tolls = {
    "status": "OK",
    "summary": {
        "route": [
            {
                "location": {
                    "lat": 19.17435,
                    "lng": 72.95063
                },
                "address": "Mulund West, Mumbai, MH, India"
            },
            {
                "location": {
                    "lat": 19.2395,
                    "lng": 73.12979
                },
                "address": "Kalyan, MH, India"
            }
        ],
        "rates": {
            "USD": 1,
            "CAD": 1.285101,
            "MXN": 20.15697,
            "INR": 73.633302,
            "AUD": 1.320885,
            "GBP": 0.748925,
            "EUR": 0.82058
        },
        "currency": "INR",
        "countries": [
            "IND"
        ],
        "departure_time": 1608533110,
        "fuelPrice": {
            "value": 70,
            "currency": "INR"
        },
        "fuelEfficiency": {
            "city": 23.4,
            "hwy": 30,
            "units": "mpg"
        },
        "vehicleType": "2AxlesAuto",
        "share": {
            "name": "mumbai,mh-kalyan,mh",
            "prefix": "mumbai%2Cmh-kalyan%2Cmh",
            "uuid": "f475d95a-0e51-41bf-8f4d-18dd10135c76"
        },
        "source": "HERE"
    },
    "routes": [
        {
            "summary": {
                "hasTolls": "true",
                "diffs": {
                    "cheapest": 0,
                    "fastest": 0
                },
                "url": "https://www.google.com/maps/?saddr=19.1743503,72.9506293&daddr=19.1907549,72.9630375+to:19.2094338,72.9737341+to:19.2114723,72.9758692+to:19.2677557,73.0807972+to:19.2696226,73.0831575+to:19.2395014,73.1297911&via=1,2,3,4,5",
                "distance": {
                    "text": "16.1 mi",
                    "metric": "25.9 km",
                    "value": 25888
                },
                "duration": {
                    "text": "1 h 3 min",
                    "value": 3822
                },
                "name": "AH47",
                "note": []
            },
            "costs": {
                "fuel": 161,
                "cash": 80
            },
            "tolls": [
                {
                    "id": 9232347,
                    "lat": 19.18525,
                    "lng": 72.95495,
                    "name": "Mulund LBS Marg",
                    "road": "LBS Rd",
                    "state": "Maharashtra",
                    "type": "barrier",
                    "currency": "INR",
                    "tagPrimary": [
                        "Tag transponder"
                    ],
                    "tagSecondary": "null",
                    "oneWay": 40,
                    "return": "null",
                    "monthly": 1320,
                    "height": "null",
                    "arrival": {
                        "distance": 1433,
                        "time": "2020-12-21T06:48:20+00:00"
                    },
                    "point": {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "type": "Point",
                            "coordinates": [
                                72.95495,
                                19.18525
                            ]
                        }
                    },
                    "nhai": "null"
                },
                {
                    "id": 9232351,
                    "lat": 19.25295,
                    "lng": 73.09875,
                    "name": "Kon Gaon",
                    "road": "Kalyan Rd",
                    "state": "Maharashtra",
                    "type": "barrier",
                    "currency": "INR",
                    "tagPrimary": [
                        "Tag transponder"
                    ],
                    "tagSecondary": "null",
                    "oneWay": 40,
                    "return": 60,
                    "monthly": 1320,
                    "height": "null",
                    "arrival": {
                        "distance": 21795,
                        "time": "2020-12-21T07:10:24+00:00"
                    },
                    "point": {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "type": "Point",
                            "coordinates": [
                                73.09875,
                                19.25295
                            ]
                        }
                    },
                    "nhai": "null"
                }
            ],
            "directions": [
                {
                    "position": {
                        "latitude": 19.1743503,
                        "longitude": 72.9506293
                    },
                    "maneuver": "forward",
                    "html_instructions": "Head <span class=\"heading\">northeast</span> on <span class=\"street\">P K Road</span>. <span class=\"distance-description\">Go for <span class=\"length\">0.2 mi</span>.</span>",
                    "distance": 242,
                    "duration": 33,
                    "note": []
                },
                {
                    "position": {
                        "latitude": 19.1759276,
                        "longitude": 72.9521906
                    },
                    "maneuver": "forward",
                    "html_instructions": "Continue on <span class=\"next-street\">Maharshi Azad Chowk</span>. <span class=\"distance-description\">Go for <span class=\"length\">351 ft</span>.</span>",
                    "distance": 107,
                    "duration": 11,
                    "note": []
                },
                {
                    "position": {
                        "latitude": 19.1766465,
                        "longitude": 72.9528558
                    },
                    "maneuver": "forward",
                    "html_instructions": "Continue on <span class=\"next-street\">P K Road</span>. <span class=\"distance-description\">Go for <span class=\"length\">0.5 mi</span>.</span>",
                    "distance": 857,
                    "duration": 111,
                    "note": []
                },
                {
                    "position": {
                        "latitude": 19.1839421,
                        "longitude": 72.9533923
                    },
                    "maneuver": "right",
                    "html_instructions": "Turn <span class=\"direction\">right</span> onto <span class=\"next-street\">Lal Bahadur Shastri Marg</span>. <span class=\"distance-description\">Go for <span class=\"length\">0.2 mi</span>.</span>",
                    "distance": 302,
                    "duration": 45,
                    "note": [
                        {
                            "type": "info",
                            "code": "tollRoad",
                            "text": "Toll road"
                        },
                        {
                            "type": "info",
                            "code": "tollBooth",
                            "text": "Stop for toll booth"
                        }
                    ]
                },
                {
                    "position": {
                        "latitude": 19.1854763,
                        "longitude": 72.9556131
                    },
                    "maneuver": "right",
                    "html_instructions": "Take the <span class=\"exit\">2nd exit</span> from Mulund Check Naka roundabout onto <span class=\"next-street\">L. B. S. Marg</span>. <span class=\"distance-description\">Go for <span class=\"length\">0.5 mi</span>.</span>",
                    "distance": 840,
                    "duration": 94,
                    "note": []
                },
                {
                    "position": {
                        "latitude": 19.1881049,
                        "longitude": 72.9628336
                    },
                    "maneuver": "bearLeft",
                    "html_instructions": "Keep <span class=\"direction\">left</span> toward <span class=\"sign\">Marathon Chowk</span>. <span class=\"distance-description\">Go for <span class=\"length\">256 ft</span>.</span>",
                    "distance": 78,
                    "duration": 11,
                    "note": []
                },
                {
                    "position": {
                        "latitude": 19.1885126,
                        "longitude": 72.9634345
                    },
                    "maneuver": "left",
                    "html_instructions": "Turn <span class=\"direction\">left</span> onto <span class=\"next-street\">Service Road</span>. <span class=\"distance-description\">Go for <span class=\"length\">0.2 mi</span>.</span>",
                    "distance": 254,
                    "duration": 16,
                    "note": [
                        {
                            "type": "info",
                            "code": "tollRoad",
                            "text": "Toll road"
                        }
                    ]
                },
                {
                    "position": {
                        "latitude": 19.1907549,
                        "longitude": 72.9630375
                    },
                    "maneuver": "forward",
                    "html_instructions": "Take ramp onto <span class=\"next-street\">Eastern Express Highway</span> <span class=\"number\">(NH-48)</span>. <span class=\"distance-description\">Go for <span class=\"length\">0.4 mi</span>.</span>",
                    "distance": 686,
                    "duration": 48,
                    "note": [
                        {
                            "type": "info",
                            "code": "tollRoad",
                            "text": "Toll road"
                        }
                    ]
                },
                {
                    "position": {
                        "latitude": 19.1968703,
                        "longitude": 72.962383
                    },
                    "maneuver": "bearRight",
                    "html_instructions": "Keep <span class=\"direction\">right</span> onto <span class=\"next-street\">Ghodbunder Road</span> <span class=\"number\">(NH-48)</span>. <span class=\"distance-description\">Go for <span class=\"length\">1.2 mi</span>.</span>",
                    "distance": 1856,
                    "duration": 160,
                    "note": [
                        {
                            "type": "info",
                            "code": "tollRoad",
                            "text": "Toll road"
                        }
                    ]
                },
                {
                    "position": {
                        "latitude": 19.2094338,
                        "longitude": 72.9737341
                    },
                    "maneuver": "bearRight",
                    "html_instructions": "Keep <span class=\"direction\">right</span> onto <span class=\"next-street\">Ghodbunder Road</span> <span class=\"number\">(NH-48)</span>. <span class=\"distance-description\">Go for <span class=\"length\">0.2 mi</span>.</span>",
                    "distance": 321,
                    "duration": 34,
                    "note": [
                        {
                            "type": "info",
                            "code": "tollRoad",
                            "text": "Toll road"
                        }
                    ]
                },
                {
                    "position": {
                        "latitude": 19.2114723,
                        "longitude": 72.9758692
                    },
                    "maneuver": "bearRight",
                    "html_instructions": "Keep <span class=\"direction\">right</span> onto <span class=\"next-street\">Eastern Express Highway</span> <span class=\"number\">(NH-48)</span> toward <span class=\"sign\"><span lang=\"en\">Nashik</span></span>. <span class=\"distance-description\">Go for <span class=\"length\">8.3 mi</span>.</span>",
                    "distance": 13427,
                    "duration": 746,
                    "note": [
                        {
                            "type": "info",
                            "code": "tollRoad",
                            "text": "Toll road"
                        },
                        {
                            "type": "info",
                            "code": "tollBooth",
                            "text": "Stop for toll booth"
                        }
                    ]
                },
                {
                    "position": {
                        "latitude": 19.2677557,
                        "longitude": 73.0807972
                    },
                    "maneuver": "left",
                    "html_instructions": "Turn <span class=\"direction\">left</span> onto <span class=\"next-street\">Mumbai Nashik Road</span> <span class=\"number\">(AH47)</span> toward <span class=\"sign\"><span lang=\"en\">Holiday Resort Malshej Ghat</span></span>. <span class=\"distance-description\">Go for <span class=\"length\">0.2 mi</span>.</span>",
                    "distance": 329,
                    "duration": 48,
                    "note": [
                        {
                            "type": "info",
                            "code": "tollRoad",
                            "text": "Toll road"
                        }
                    ]
                },
                {
                    "position": {
                        "latitude": 19.2696226,
                        "longitude": 73.0831575
                    },
                    "maneuver": "right",
                    "html_instructions": "Turn <span class=\"direction\">right</span> onto <span class=\"next-street\">Kalyan Bhiwandi Road</span> <span class=\"number\">(SH-35)</span> toward <span class=\"sign\"><span lang=\"en\">Holiday Resort Malshej Ghat</span></span>. <span class=\"distance-description\">Go for <span class=\"length\">3.1 mi</span>.</span>",
                    "distance": 4977,
                    "duration": 311,
                    "note": [
                        {
                            "type": "info",
                            "code": "tollRoad",
                            "text": "Toll road"
                        },
                        {
                            "type": "info",
                            "code": "tollBooth",
                            "text": "Stop for toll booth"
                        }
                    ]
                },
                {
                    "position": {
                        "latitude": 19.246738,
                        "longitude": 73.1200218
                    },
                    "maneuver": "right",
                    "html_instructions": "Take the <span class=\"exit\">2nd exit</span> from Durgamata Chowk roundabout onto <span class=\"next-street\">Agra Road</span> <span class=\"number\">(SH-35)</span> toward <span class=\"sign\"><span lang=\"en\">Kalyan City</span></span>. <span class=\"distance-description\">Go for <span class=\"length\">0.9 mi</span>.</span>",
                    "distance": 1518,
                    "duration": 165,
                    "note": []
                },
                {
                    "position": {
                        "latitude": 19.2400968,
                        "longitude": 73.1293237
                    },
                    "maneuver": "left",
                    "html_instructions": "Turn <span class=\"direction\">left</span> onto <span class=\"next-street\">Chhatrapati Shivaji Maharaj Chowk</span>. <span class=\"distance-description\">Go for <span class=\"length\">102 ft</span>.</span>",
                    "distance": 31,
                    "duration": 6,
                    "note": []
                },
                {
                    "position": {
                        "latitude": 19.2398608,
                        "longitude": 73.1293452
                    },
                    "maneuver": "left",
                    "html_instructions": "Turn <span class=\"direction\">left</span> onto <span class=\"next-street\">Bharatratna DR Babashaheb Ambedkar Marg</span> <span class=\"number\">(SH-35)</span>. <span class=\"distance-description\">Go for <span class=\"length\">207 ft</span>.</span>",
                    "distance": 63,
                    "duration": 5,
                    "note": []
                },
                {
                    "position": {
                        "latitude": 19.2395014,
                        "longitude": 73.1297911
                    },
                    "maneuver": "forward",
                    "html_instructions": "Arrive at <span class=\"street\">Bharatratna DR Babashaheb Ambedkar Marg</span> <span class=\"number\">(SH-35)</span>.",
                    "distance": 0,
                    "duration": 0,
                    "note": []
                }
            ],
            "polyline": "u~_tBmdg|Lk@k@qAiAkCqCq@o@c@c@aAw@i@i@kBeB_@YYMuCu@u@GsAAaHLwHa@k@AeAT{@p@e@HcABg@DqA\\SFW}@cAqCu@mAmCeDIAGGCICIBMFIKMKUI[G]MuBCqBQeC{@sGWsAWgA[q@a@m@yAyCaCuDi@aAg@s@QQWq@gAPaGf@uBR_@EMI}OtAuEb@cF\\}@@cCEsB]eBa@uBs@mBcAeBeAiCcCuTaV{CwCmGcH{C_DuCkC{EwEsDyDS[w@{@aC_CiEsEI_@OWa@}@Oi@UiBA}@R{ELeAJeBlA{MNyAPwBpAuMbA_MvBgVt@gJz@cJTgAhBkTT{CTmBFoB@aC]aEc@iCk@sBk@wAqAaCaAmAyI}IkBuBaC{Bu@y@kIaIeDgDaB_B_XqXkHmH{BkCuHwHy@s@gBmBaBwBsCuEuLgTwBkEUYsHqMCIuBmDcF_JcCaEs@iA}AwAkSeWcEuF_@a@yD}DoMyOcIkK}AmByIwLcKyMuIqKo@aAaCuEeQo_@mE{JaAoCe@wA[q@c@w@g@o@aE{DiB_CiA{AoFoIu@qAc@k@{BcEeA_CoC}EwI}NWo@Ua@mIaOaAiBoK{QcEoHqEyHs@qAmA_@eHwLKQ|@w@^UdF_ElC{Bl@a@xCcB`Ae@`H{D|AgAtD{DlBuB`GuH`DkElAuAtCeCn@m@nGyFzOcO~FkFjEwE|@gAXc@bAiBfAyBvBuDdAqBbAsBd@mAnAoCxA{Cf@_AtBeDvBsDfCoFnDuGPc@ZcATsAz@kPHsDBqCHWYyAYiD{BsRK]c@}CMGAIDODCD?DoDL{B\\}JVsJH}ANkA~@_BxLmOd@a@`@Qj@K`A@~EZ|Fh@z@NFIHCT@FD\\]h@y@"
        }
    ],
    "meta": {
        "userId": "laxmi17sarki@gmail.com",
        "customerId": "cus_Ibm3stclaQlmSj",
        "tx": 3,
        "type": "general",
        "client": "api",
        "source": "HERE"
    }
}

print(tolls["summary"]["route"][0]["location"])
print(tolls["routes"][0]["tolls"][0]['lat'])
# print(tolls["routes"][0]["summary"]["duration"]["text"])