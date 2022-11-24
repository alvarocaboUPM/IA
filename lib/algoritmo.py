from queue import PriorityQueue
from lib import EstacionHandler, Estacion

'''
diccionario de arrays que tiene como key el nombre de la estación y como value el array de los vecinos de dicha estación
calculamos el tiempo total como la suma de los caminos entre nodos vecinos y al final le sumamos el total de paradas realizadas por el metro*20s
nuestra función recibe como parámetros de entrada el st de inicio y del final del trayecto
'''

''' def reconstruct_path(anterior, curr, draw):
		while curr in anterior:
        	curr = anterior[curr]
        	curr.make_path()
        	draw() 
'''

class Algoritmo():
    #Empty path
    path: Estacion = []
    #Constructor con punto de incio y fin
    def __init__(self, start, end):
        self.start = EstacionHandler.metromap[start]
        self.end = EstacionHandler.metromap[end]
        self.map = EstacionHandler.metromap

    def best_route(self):
        #INIT
        pasos = 0
        openQ = PriorityQueue()
        openQ.put((0, pasos, self.start)) 
        anterior = {}
        g_n = {}
        #ENDINIT
        st : Estacion
        for st in self.map:
            g_n[st] = float("inf")
        #g_n = {spot: float("inf") for row in grid for spot in row}
        g_n[self.start] = 0
        #f_n = {spot: float("inf") for row in grid for spot in row}
        f_n = {}
        for st in self.map:
            f_n[st] = float("inf")
        # poner nuestra estimación
        f_n[self.start] = self.h(self.start, self.end)
        closeQ = {self.start}

        while not openQ.empty():
            curr = openQ.get()[2]
            closeQ.remove(curr)

            if curr == self.end:
                res = [curr]
                while curr in anterior:
                    curr = anterior[curr]
                    res.append(curr)

                return list(reversed(res))

            for vecino in self.map[curr]:
                # función de ruben y vinh que devuelve el tiempo entre estaciones vecinas
                temp_g_n = g_n[curr] + Estacion.calcTime(curr, vecino)
                if temp_g_n < g_n[vecino]:
                    anterior[vecino] = curr
                    g_n[vecino] = temp_g_n
                    f_n[vecino] = temp_g_n + self.h(vecino, self.end)
                    if vecino not in closeQ:
                        pasos += 1
                        openQ.put((f_n[vecino], pasos, vecino))
                        closeQ.add(vecino)
                        # vecino.make_open() # grafico: marcar st como abierto

            if curr != self.start:
                pass
                # curr.make_closed() # grafico: marcar st como visitado

        return None

