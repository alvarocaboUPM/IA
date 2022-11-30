# MODULO GENERADOR DE DATOS

from pprint import pprint
from lib import EstacionHandler, Astar
import os, sys
from dotenv import dotenv_values

if __name__ == '__main__':
    print("Generando datos")
    EstacionHandler.populate()
    #EstacionHandler.read()
    print("Datos generados correctamente \n")
