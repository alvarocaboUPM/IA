from typing_extensions import Self
from lib import EstacionHandler
from geopy.distance import geodesic
import requests, json
from geopy.geocoders import Nominatim
from geopy.location import Location

GMAPS_KEY="AIzaSyAfODIWKl1TgUsvhJSF7JzMrEyhkznqKOw"
GMAPS_URL="https://maps.googleapis.com/maps/api/distancematrix/json?"

class Estacion:
    # Constructor de la clase estación
    def __init__(self, stnumber, stname, lat=0.0, long=0.0):
        self.name = stname
        self.number: int = stnumber
        self.lat = lat
        self.long = long
        
    # Busca latitud y longitud para cada estacion
    def writeCoords(self, file):
        #Defines
        sm =";"; cityname="Athens";wrstring = str(self.number) + sm + self.name
        keywords = ["station", "metro", "subway", "μετρό", "σταθμός", "underground"]
        locator= Nominatim(user_agent="telmove@gmx.com")
        i=0; querytext=None
        #Execution
        datfile = open(file, "a")
        coordenadas: Location = None
        while (coordenadas == None and i< len(keywords)):
            querytext = self.name + " " + keywords[i] + ", " +cityname
            coordenadas=locator.geocode(querytext)
            i=i+1
        
        if(coordenadas!=None):
            #Setting de la Estación
            print(querytext)
            self.lat = coordenadas.latitude
            self.long = coordenadas.longitude
        else:
            self.lat = 0.0
            self.long = 0.0
        wrstring = wrstring + sm + str(self.lat) + sm + str(self.long) + "\n"
        #Escribo en el csv
        print(wrstring)
        datfile.write(wrstring)
        datfile.close()

    #Prints formated station
    def toString(self):
        print(f"{self.name} | {self.number} | [{str(self.lat)}, {str(self.long)}]")

    # Devuelve la distancia en metros con otra estacion
    def calcDistance(self, other: Self):
        here = (self.lat, self.long)
        there = (other.lat, other.long)
        return geodesic(here, there) * 1000.0

    def calcTime(self, other:Self):
        here = (self.lat, self.long)
        there = (other.lat, other.long)
        r= requests.get(GMAPS_URL + 'origins = ' + here+
                              '&destinations = ' + there +
                              '&key = ' +GMAPS_KEY)
        out= r.json()
        print(json.dumps(out))

        time = out['duration']['value']
        print(time)
        distance = out['distance']['value']
        print(distance)


    #Calcula la linea de metro de la estacion actual
    def getLinea(self)->int: 
        return int(float(self.number) // 100) #Redondeo hacia abajo (floor)

    # Devuelve las estaciones adyacentes en una lista
    def calcAdjacents(self):
        list = []

        linea= Estacion.getLinea(self)

        # Casos especiales 319 y 321 por falta de 320
        if self.number == 319:
            list.append(EstacionHandler.metromap[318])
            list.append(EstacionHandler.metromap[321])
        elif self.number == 321:
            list.append(EstacionHandler.metromap[319])
            list.append(EstacionHandler.metromap[322])

        # Casos especiales 312 y 314 por falta de 313
        elif self.number == 312:
            list.append(EstacionHandler.metromap[311])
            list.append(EstacionHandler.metromap[314])
        elif self.number == 314:
            list.append(EstacionHandler.metromap[312])
            list.append(EstacionHandler.metromap[315])
            list.append(EstacionHandler.metromap[119])

        # Transbordo verde azul
        elif self.number == 218:
            list.append(EstacionHandler.metromap[315])
            list.append(EstacionHandler.metromap[217])
            list.append(EstacionHandler.metromap[219])
        elif self.number == 315:
            list.append(EstacionHandler.metromap[314])
            list.append(EstacionHandler.metromap[218])
            list.append(EstacionHandler.metromap[316])

        # Transbordo rojo verde
        elif self.number == 119:
            list.append(EstacionHandler.metromap[118])
            list.append(EstacionHandler.metromap[120])
            list.append(EstacionHandler.metromap[314])

        # Transbordo rojo azul
        elif self.number == 217:
            list.append(EstacionHandler.metromap[120])
            list.append(EstacionHandler.metromap[216])
            list.append(EstacionHandler.metromap[218])
        elif self.number == 120:
            list.append(EstacionHandler.metromap[217])
            list.append(EstacionHandler.metromap[119])
            list.append(EstacionHandler.metromap[121])

        # Princios y fines de Linea
        elif int(self.number) % 100 == 27:
            list.append(EstacionHandler.metromap[linea * 100 + 26])
        elif int(self.number) % 100 == 10:
            list.append(EstacionHandler.metromap[linea * 100 + 11])

        # Demas estaciones
        else:
            list.append(EstacionHandler.metromap[self.number + 1])
            list.append(EstacionHandler.metromap[self.number - 1])

        return list