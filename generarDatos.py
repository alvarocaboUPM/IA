# MODULO GENERADOR DE DATOS

from lib import EstacionHandler
import os
from dotenv import dotenv_values


if __name__ == '__main__':
    fileE = dotenv_values(".env")["FILE_ESTACIONES"]
    fileM = dotenv_values(".env")["FILE_MATRIX"]

    print("Generando datos en archivo "+fileE+"... ")
    EstacionHandler.read(fileE)
    EstacionHandler.matrix(fileM)
    print("Datos generados correctamente \n")
