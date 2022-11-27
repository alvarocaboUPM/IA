from queue import PriorityQueue
from dotenv import dotenv_values
import pandas as pd
from lib import EstacionHandler, Estacion
class Astar():
    #Camino inicial vacío
    path = [Estacion]

    #Constructor con punto de incio y fin
    def __init__(self, start, end):
        self.start :Estacion = EstacionHandler.metromap[start]
        self.end : Estacion= EstacionHandler.metromap[end]
        self.h = pd.read_csv(dotenv_values(".env")["FILE_MATRIX"],sep=';')
    
    def routing(self):
        #INIT
        steps=0
        #OPEN -> Nodos no visitados
        openQ= PriorityQueue() 
        openQ.put((0, steps, self.start)) 
        #CLOSE -> Nodos visitados
        closeQ= {self.start}
        cost= {Estacion:float}
        finalCost = {}
        #END INIT

        #1. Llenar el Open
        st : Estacion
        adj: Estacion

        for st in EstacionHandler.metromap.values():
            cost[st] = float("inf")
            finalCost[st] = float("inf")
            
        cost[self.start] = 0
        finalCost[self.start] = 0+self.h[self.start.name][self.end.name]
        
        while not openQ.empty():
            n = openQ.get()[2] #Obtenemos y eliminamos el actual de open
            closeQ.remove(n) #Lo sacamos de los visitados

            if n == self.end:
                res = [n]
                while n in closeQ:
                    n = closeQ[n]
                    res.append(n)
                return list(reversed(res))
            
            for adj in n.calcAdjacents(EstacionHandler.metromap):
                print(adj.name)
                tmp = self.h[st.name][adj.name]
                if(tmp < cost[adj]):
                    closeQ[adj] = n
                    cost[adj] = tmp
                    if adj not in closeQ:
                        steps +=1
                        openQ.put(finalCost[adj], steps, adj)
                        closeQ.add(adj)
            if n != self.start:
                print("CUlo")
                pass
                # curr.make_closed() # grafico: marcar st como visitado

        return None