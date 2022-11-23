# MODULO GENERADOR DE DATOS

from lib import EstacionHandler

FILE="test/test_data.csv"
if __name__ == '__main__':
    print("Generando datos... \n")
    EstacionHandler.populate(FILE, True)
    print("Datos generados correctamente \n")
