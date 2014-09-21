from django.shortcuts import render
import geocoder
from .models import FoodFacility
from math import radians, cos, sin, asin, sqrt

food_facilities = FoodFacility.objects.all()

def index(request):
    context = {}
    if request.method == 'POST':
        address = request.POST['address']
        g = geocoder.google(address)
        nearby_foodtrucks = calculate_distance(g.lat, g.lng)
        if nearby_foodtrucks and len(nearby_foodtrucks) > 5:
            nearby_foodtrucks = nearby_foodtrucks[:5]
            
        context['foodtrucks'] = nearby_foodtrucks

    return render(request, 'foodtrucks/index.html', context)

def calculate_distance(in_lat, in_lng):
    """
    Calculate distance between entered address
    and each of the addresses in the database
    """
    #distance = {}
    nearby_foodtrucks = []
    for facility in food_facilities:
        lat, lng = facility.Latitude, \
            facility.Longitude
        dist_in_km = haversine(in_lng, in_lat, lng, lat)
        if dist_in_km <= 1:
            if facility not in nearby_foodtrucks:
                nearby_foodtrucks.append(facility)
        
        #distance[facility.locationid] = dist_in_km

    return nearby_foodtrucks

def haversine(lon1, lat1, lon2, lat2):
    """
    Copied from stack overflow: http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    # 6367 km is the radius of the Earth
    km = 6367 * c
    return km
