from geopy.geocoders import Nominatim
from lib import Estacion

file="lib/data.csv"

class EstacionHandler:
    locator = Nominatim(user_agent="telmove@gmx.com")
    estaciones: Estacion = []
    metromap = {}

    @staticmethod
    def populate():

        # Trunca el fichero de texto
        datfile = open(file, "w")
        datfile.write("")
        datfile.close()

        # AQUI VAN LOS NOMBRES Y NUMEROS DE LAS ESTACIONES

        # LINEA 1 ROJA (18 estaciones)
        EstacionHandler.estaciones.append(Estacion(110, "Akademmistechko"))
        EstacionHandler.estaciones.append(Estacion(111, "Zhytomyrska"))

        # LINEA 2 AZUL (18 estaciones)
        EstacionHandler.estaciones.append(Estacion(210, "Heroiv Dnipra"))

        # LINEA 3 VERDE (16 estaciones)
        EstacionHandler.estaciones.append(Estacion(310, "Syrets"))

        # Escribir en el fichero de texto
        for stat in EstacionHandler.estaciones:
            stat.writeCoords()

    # Lee las estaciones desde archivo
    @staticmethod
    def read():
        datfile = open(file, "r")
        statlines = datfile.readlines()
        for curline in statlines:
            split = curline.split(';')
            num = split[0]
            nam = split[1]
            latit = split[2]
            longit = split[3]
            stat = Estacion.Estacion((num), nam,float(latit), float(longit))
            EstacionHandler.estaciones.append(stat)
            EstacionHandler.metromap[num] = stat


