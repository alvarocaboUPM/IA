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
        self.h.drop_duplicates()
        
    
    def routing(self):
        #INIT
        print("Calculando camino desde {init} hasta {fin}".format(init=self.start.name,
         fin=self.end.name))
        steps=0
        #OPEN -> Nodos no visitados
        openQ= PriorityQueue() 
        openQ.put((0, steps, self.start)) 
        #CLOSE -> Nodos visitados
        closeQ= {self.start}
        came_from = {}
        cost= {} #h_n
        finalCost = {}  #f_n
        #END INIT

        #1. Llenar el Open
        st : Estacion
        adj: Estacion
        

        for st in EstacionHandler.metromap.values():
            cost[st] = float("inf")
            finalCost[st] = float("inf")
            
        cost[self.start] = 0
        finalCost[self.start] = 0+self.h.loc[self.start.name][self.end.name]
        
        while not openQ.empty():
            n:Estacion
            aux = openQ.get()
            n = aux[2] #Obtenemos y eliminamos el actual de open
            print("#{} Buscando en n: {} - {}".format(aux[1],n.name, n.number))
            closeQ.remove(n) #Lo sacamos de los visitados

            if n.number==self.end.number:
                res = [n.name]
                while n in came_from:
                    n = came_from[n]
                    res.append(n.name)
                return list(reversed(res))
            
            for adj in n.calcAdjacents(EstacionHandler.metromap):
                tmp = cost[n]+1

                if(tmp < cost[adj]):
                    came_from[adj]= n
                    cost[adj] = tmp
                    finalCost[adj] = tmp
                    if adj not in closeQ:
                        print(" -> Adding to open and close ->"+ adj.name)
                        steps +=1
                        openQ.put((finalCost[adj], steps, adj))
                        closeQ.add(adj)

            if n != self.start:
                pass
                # curr.make_closed() # grafico: marcar st como visitado

        return None