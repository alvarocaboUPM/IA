from pprint import pprint

from dotenv import dotenv_values
from lib import Estacion

fileE = dotenv_values(".env")["FILE_ESTACIONES"]
fileM = dotenv_values(".env")["FILE_MATRIX"]

class EstacionHandler:
    estaciones = []
    metromap= {}
    coolmap={}
    trasbordos={}


    @staticmethod
    def populate():
        """Función que rellena un csv con los datos de posicion de todas las estaciones"""
        # Trunca el fichero de texto
        datfile = open(fileE, "w")
        datfile.write("ID;Estacion;Latitud;Longitud\n")
        datfile.close()

        # AQUI VAN LOS NOMBRES Y NUMEROS DE LAS ESTACIONES

        # LINEA 1 VERDE (24 estaciones)
        EstacionHandler.estaciones.append(Estacion.Estacion(101, "Piraeus"))
        EstacionHandler.estaciones.append(Estacion.Estacion(102, "Neo Faliro",37.96,23.68))
        EstacionHandler.estaciones.append(Estacion.Estacion(103, "Moschato"))
        EstacionHandler.estaciones.append(Estacion.Estacion(104, "Kallithea"))
        EstacionHandler.estaciones.append(Estacion.Estacion(105, "Tavros"))
        EstacionHandler.estaciones.append(Estacion.Estacion(106, "Petralona"))
        EstacionHandler.estaciones.append(Estacion.Estacion(107, "Thissio"))
        EstacionHandler.estaciones.append(Estacion.Estacion(108, "Monastiraki"))
        EstacionHandler.estaciones.append(Estacion.Estacion(109, "Omonia"))
        EstacionHandler.estaciones.append(Estacion.Estacion(110, "Victoria"))
        EstacionHandler.estaciones.append(Estacion.Estacion(111, "Attiki"))
        EstacionHandler.estaciones.append(Estacion.Estacion(112, "Aghios Nikolaos", 38.00751483506223, 23.72802727940956))
        EstacionHandler.estaciones.append(Estacion.Estacion(113, "Kato Patissia",38.011403374873, 23.729143078325432))
        EstacionHandler.estaciones.append(Estacion.Estacion(114, "Aghios Eleftherios", 38.02026171288618, 23.733005459223712))
        EstacionHandler.estaciones.append(Estacion.Estacion(115, "Ano Patissia", 38.023870693338594, 23.73595358730873))
        EstacionHandler.estaciones.append(Estacion.Estacion(116, "Perissos"))
        EstacionHandler.estaciones.append(Estacion.Estacion(117, "Pefkakia"))
        EstacionHandler.estaciones.append(Estacion.Estacion(118, "Nea Ionia"))
        EstacionHandler.estaciones.append(Estacion.Estacion(119, "Iraklio"))
        EstacionHandler.estaciones.append(Estacion.Estacion(120, "Irini"))
        EstacionHandler.estaciones.append(Estacion.Estacion(121, "Neratziotissa"))
        EstacionHandler.estaciones.append(Estacion.Estacion(122, "Maroussi"))
        EstacionHandler.estaciones.append(Estacion.Estacion(123, "KAT"))
        EstacionHandler.estaciones.append(Estacion.Estacion(124, "Kifissia"))

        # LINEA 2 ROJA (14 estaciones)
        EstacionHandler.estaciones.append(Estacion.Estacion(201, "Aghios Antonios", 38.00675407002947, 23.699491726643075))
        EstacionHandler.estaciones.append(Estacion.Estacion(202, "Sepolia"))
        EstacionHandler.estaciones.append(Estacion.Estacion(203, "Attiki"))
        EstacionHandler.estaciones.append(Estacion.Estacion(204, "Larissa Station"))
        EstacionHandler.estaciones.append(Estacion.Estacion(205, "Metaxourghio", 37.98624953252499, 23.720839210933928))
        EstacionHandler.estaciones.append(Estacion.Estacion(206, "Omonia"))
        EstacionHandler.estaciones.append(Estacion.Estacion(207, "Panepistimio"))
        EstacionHandler.estaciones.append(Estacion.Estacion(208, "Syntagma"))
        EstacionHandler.estaciones.append(Estacion.Estacion(209, "Akropoli"))
        EstacionHandler.estaciones.append(Estacion.Estacion(210, "Sygrou-Fix", 37.964338038418184, 23.726568290097944))
        EstacionHandler.estaciones.append(Estacion.Estacion(211, "Neos Kosmos"))
        EstacionHandler.estaciones.append(Estacion.Estacion(212, "Aghios Ioannis", 37.956629712245814, 23.734670183005026))
        EstacionHandler.estaciones.append(Estacion.Estacion(213, "Dafni"))
        EstacionHandler.estaciones.append(Estacion.Estacion(214, "Aghios Dimitrios", 37.940668890782966, 23.740780697774923))

        # LINEA 3 AZUL (20 estaciones)
        EstacionHandler.estaciones.append(Estacion.Estacion(301, "Egaleo"))
        EstacionHandler.estaciones.append(Estacion.Estacion(302, "Eleonas"))
        EstacionHandler.estaciones.append(Estacion.Estacion(303, "Kerameikos"))
        EstacionHandler.estaciones.append(Estacion.Estacion(304, "Monastiraki"))
        EstacionHandler.estaciones.append(Estacion.Estacion(305, "Syntagma"))
        EstacionHandler.estaciones.append(Estacion.Estacion(306, "Evangelismos"))
        EstacionHandler.estaciones.append(Estacion.Estacion(307, "Megaro Moussikis", 37.97934984463451, 23.75287849588745))
        EstacionHandler.estaciones.append(Estacion.Estacion(308, "Ambelokipi"))
        EstacionHandler.estaciones.append(Estacion.Estacion(309, "Panormou"))
        EstacionHandler.estaciones.append(Estacion.Estacion(310, "Katehaki"))
        EstacionHandler.estaciones.append(Estacion.Estacion(311, "Ethniki Amyna"))
        EstacionHandler.estaciones.append(Estacion.Estacion(312, "Holargos"))
        EstacionHandler.estaciones.append(Estacion.Estacion(313, "Nomismatokopio"))
        EstacionHandler.estaciones.append(Estacion.Estacion(314, "Aghia Paraskevi"))
        EstacionHandler.estaciones.append(Estacion.Estacion(315, "Halandri"))
        EstacionHandler.estaciones.append(Estacion.Estacion(316, "Doukissis Plakentias"))
        EstacionHandler.estaciones.append(Estacion.Estacion(317, "Pallini"))
        EstacionHandler.estaciones.append(Estacion.Estacion(318, "Paiania-Kantza", 37.9854072929238, 23.870406985250174))
        EstacionHandler.estaciones.append(Estacion.Estacion(319, "Koropi", 37.913286685491364, 23.89597172156))
        EstacionHandler.estaciones.append(Estacion.Estacion(320, "Airport"))

        # Escribir en el fichero de texto
        stat: Estacion
        for stat in EstacionHandler.estaciones:
            stat.writeCoords(stat,fileE)
        EstacionHandler.read()
        
    @staticmethod
    def read():
        """ Lee las estaciones desde archivo"""
        datfile = open(fileE, "r")
        statlines = datfile.readlines()
        statlines.pop(0)
        for curline in statlines:
            split = curline.split(';')
            num = split[0]
            nam = split[1]
            latit = split[2]
            longit = split[3]
            stat: Estacion = Estacion((num), nam, float(latit), float(longit))
            EstacionHandler.estaciones.append(stat)
            EstacionHandler.metromap[int(num)] = stat
            EstacionHandler.coolmap[int(num)] = stat.toString()
        EstacionHandler.matrix()

    @staticmethod      
    def matrix():
        """Crea la matriz de costes"""
        datfile = open(fileM, "w")
        st:Estacion ;st2: Estacion
        i= len(EstacionHandler.metromap.values())
        datfile.write(" ;")
        for st in EstacionHandler.metromap.values():
            if(i != 1):
                datfile.write(st.name+";")
            else:
                 datfile.write(st.name)
            i=i-1

        datfile.write("\n")  
        for st in EstacionHandler.metromap.values():
            append : str = ""
            for st2 in EstacionHandler.metromap.values():
                d= st.calcDistance(st2)
                append+=(str(d)+";")
                if(d==0 and st.line != st2.line):
                    st.trasbordo= st2.number
                    st2.trasbordo= st.number
                    EstacionHandler.trasbordos[st.name] = (st.number, st2.number)
            datfile.write(st.name+";"+append+"\n")
      