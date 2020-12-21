from math import radians,cos,sin,acos


def distance_diff_kms(origin_lat,origin_long,dest_lat,dest_long):
    distance_diff = (6371 * acos(cos(radians(origin_lat))* cos(radians(dest_lat))* cos(radians(dest_long) - radians(origin_long))+ sin(radians(origin_lat))* sin(radians(dest_lat))))
    return distance_diff




print(distance_diff_kms(45.78,36.7,45.5,36.7))