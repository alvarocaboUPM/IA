from geopy.geocoders import Nominatim
from geopy.location import Location
from lib import EstacionHandler, Estacion
from pprint import pprint

FILE="lib/data.csv"
if __name__ == '__main__':
    EstacionHandler.read(FILE)

    map = EstacionHandler.coolmap
    pprint(list(map.items()))
    
    
