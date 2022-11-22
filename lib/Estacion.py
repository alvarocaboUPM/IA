from typing_extensions import Self
from lib import EstacionHandler
from geopy.distance import geodesic

file="lib/data.csv"


class Estacion:
    # Constructor de la clase estación
    def __init__(self, stnumber, stname, lat, long):
        self.name = stname
        self.number = stnumber
        self.lat = lat
        self.long = long
        
    # Busca latitud y longitud para cada estacion
    def writeCoords(self):
        sm =";"
        datfile = open(file, "a") 
        wrstring = str(self.number) + sm + self.name
        querytext = self.name + " Estacion, Kyiv"
        curLoc = EstacionHandler.locator.geocode(querytext)
        wrstring = wrstring + sm + str(curLoc.latitude) + sm + str(curLoc.longitude) + "\n"
        self.lat = curLoc.latitude
        self.long = curLoc.longitude
        print(wrstring)
        datfile.write(wrstring)
        datfile.close()

    def print(self) -> None:
        print(f"{self.name} | {self.number} | [{str(self.lat)}, {str(self.long)}]")

    # Devuelve la distancia en metros con otra estacion
    def calcDistance(self, other: Self):
        here = (self.lat, self.long)
        there = (other.lat, other.long)
        return geodesic(here, there) * 1000.0

    # Devuelve las estaciones adyacentes en una lista
    def calcAdjacents(self):
        list = []

        # Calcula la linea de metro de la estacion actual
        stline = self.number // 100 #Redondeo hacia abajo (floor)

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

        # Extremos
        elif self.number % 100 == 27:
            list.append(EstacionHandler.metromap[stline * 100 + 26])
        elif self.number % 100 == 10:
            list.append(EstacionHandler.metromap[stline * 100 + 11])

        # Demas estaciones
        else:
            list.append(EstacionHandler.metromap[self.number + 1])
            list.append(EstacionHandler.metromap[self.number - 1])

        return list

