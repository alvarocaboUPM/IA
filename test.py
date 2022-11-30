import pandas as pd
from dotenv import dotenv_values
from geopy.geocoders import Nominatim
from geopy.location import Location
from lib import EstacionHandler, Astar
from pprint import pprint

from lib.Estacion import Estacion

if __name__ == '__main__':
    EstacionHandler.read()

    # h= pd.read_csv(dotenv_values(".env")["FILE_MATRIX"],sep=';')
    # h.drop_duplicates
    # n = EstacionHandler.metromap[110]
    # print(n.name)
    # l = n.calcAdjacents(EstacionHandler.metromap)

    # for adj in l:
    #             print(adj.name)
    #             tmp = h.loc[n.name][adj.name]

    #             print(str(tmp))
                
    algoritmo : Astar = Astar(112,315)
    print(algoritmo.routing())
    
    
    
    
