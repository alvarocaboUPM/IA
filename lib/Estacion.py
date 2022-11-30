from dotenv import dotenv_values
import pandas

from typing_extensions import Self

from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from geopy.location import Location

from lib.EstacionHandler import EstacionHandler

class Estacion:
    # Constructor de la clase estación
    def __init__(self, stnumber, stname, lat=0.0, long=0.0):
        self.name: str = stname
        self.number: int = stnumber
        self.lat = lat
        self.long = long
        self.trasbordo:int = -1
        self.line = Estacion.getLinea(self)

    # def __eq__(self, __o) -> bool:
    #     if isinstance(__o, Estacion):
    #         return self.number==__o.number and self.name==__o.name
    
    # Busca latitud y longitud para cada estacion
    def writeCoords(self, file):
        #Defines
        sm =";"; cityname="Athens";wrstring = str(self.number) + sm + self.name
        keywords = ["station", "metro", "subway", "μετρό", "σταθμός", "underground"]
        locator= Nominatim(user_agent="telmove@gmx.com")
        i=0; querytext=None
        #Execution
        datfile = open(file, "a")
        jsonfile = open("data/json/"+str(self.line)+".json","a")

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
        
        
        json = "["+str(self.long)+","+str(self.lat)+"],\n"
        if(self.firstOrLast()==1):
            print("ULTIMA")
            json = "["+str(self.long)+","+str(self.lat)+"]\n"
        wrstring += sm + str(self.lat) + sm + str(self.long)+"\n"
        #Escribo en el csv
        
        datfile.write(wrstring)
        
        jsonfile.write(json)
        datfile.close()
        jsonfile.close()

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

    def firstOrLast(self:Self)-> int:
        if(int(self.number) % 100 ==1):
            return 0
        try:
            if(EstacionHandler.estaciones[EstacionHandler.estaciones.index(self) + 1].line != self.line ):
                return 1
        except IndexError:
            return 1
        return -1

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

