from geopy.geocoders import Nominatim
from geopy.location import Location
from lib import EstacionHandler, Astar
from pprint import pprint

if __name__ == '__main__':
    EstacionHandler.read()
    algoritmo : Astar = Astar(110,113)
    
    print(algoritmo.routing())
    
    
    
    
