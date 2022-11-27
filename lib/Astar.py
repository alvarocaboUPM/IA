from queue import PriorityQueue
from lib import EstacionHandler, Estacion
class Astar():
    #Camino inicial vacío
    path = [Estacion]

    #Constructor con punto de incio y fin
    def __init__(self, start, end):
        self.start = EstacionHandler.metromap[start]
        self.end = EstacionHandler.metromap[end]

    def routing(self):
        #INIT
        steps=0
        #OPEN -> Nodos no visitados
        openQ= PriorityQueue() 
        #CLOSE -> Nodos visitados
        closeL= {Estacion}
        cost= {}
        #END INIT

        #1. Llenar el Open
        st : Estacion
        for st in EstacionHandler.metromap.values():
