from dotenv import dotenv_values
import pandas

from typing_extensions import Self

from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from geopy.location import Location



class Estacion:
    # Constructor de la clase estación
    def __init__(self, stnumber, stname, lat=0.0, long=0.0):
        self.name: str = stname
        self.number: int = stnumber
        self.lat = lat
        self.long = long
        self.trasbordo:int = -1
        self.line = Estacion.getLinea(self)
    
    @staticmethod
    # Busca latitud y longitud para cada estacion
    def writeCoords(self, file):
        #Defines
        sm =";"; cityname="Athens";wrstring = str(self.number) + sm + self.name
        keywords = ["station", "metro", "subway", "μετρό", "σταθμός", "underground"]
        locator= Nominatim(user_agent="telmove@gmx.com")
        i=0; querytext=None
        #Execution
        datfile = open(file, "a")

        #Utilizamos la API de geopy para rellenar las coordenadas
        if(self.lat == 0.0 and self.long == 0.0):
            coordenadas: Location = None
            while (coordenadas == None and i< len(keywords)):
                querytext = self.name + " " + keywords[i] + ", " +cityname
                coordenadas=locator.geocode(querytext)
                i=i+1
            
            if(coordenadas!=None):
                #Setting de la Estación
                self.lat = coordenadas.latitude
                self.long = coordenadas.longitude

        wrstring += sm + str(self.lat) + sm + str(self.long)+"\n"
        #Escribo en el csv
        print(wrstring)
        datfile.write(wrstring)
        datfile.close()

    #Prints formated station
    def toString(self):
        return f"{self.name} | {self.number} | [{str(self.lat)}, {str(self.long)}] | Linea {self.line}"

    # Devuelve la distancia en metros con otra estacion
    def calcDistance(self, other: Self):
        here = (self.lat, self.long)
        there = (other.lat, other.long)
        return geodesic(here, there).km

    @staticmethod
    #Calcula la linea de metro de la estacion actual
    def getLinea(self: Self)->int:
        return int(float(self.number) // 100) #Redondeo hacia abajo (floor)

    # Devuelve las estaciones adyacentes en una lista
    def calcAdjacents(self, map, ok =0):
        list=[]
        
        #Principio linea
        if(int(self.number) % 100 !=1):
            list.append(map[int(self.number) - 1])
        #Fin de linea
        if(map.get(int(self.number) + 1) is not None):
            list.append(map[int(self.number) + 1])
        
        #Trasbordos
        if(self.trasbordo != -1 and ok <1):
            list +=(Estacion.calcAdjacents(map[int(self.trasbordo)],map,1))
        return list