# MODULO GENERADOR DE DATOS

from pprint import pprint
from lib import EstacionHandler
import os
from dotenv import dotenv_values

if __name__ == '__main__':
    fileE = dotenv_values(".env")["FILE_ESTACIONES"]
    fileM = dotenv_values(".env")["FILE_MATRIX"]

    print("Generando datos en archivo "+fileE+"... ")
    #EstacionHandler.populate(fileE)
    EstacionHandler.read(fileE)
    EstacionHandler.matrix(fileM)

    for st in EstacionHandler.estaciones:
        print(st.name)
        pprint(st.calcAdjacents(
            EstacionHandler.metromap,
            EstacionHandler.trasbordos))
        print("\n")
    print("Datos generados correctamente \n")
