from lib import Estacion



class EstacionHandler:
    estaciones= []
    lineas={1:[], 2:[], 3:[],4:[]}
    metromap: Estacion= {}

    @staticmethod
    def populate(file,test: bool):

        # Trunca el fichero de texto
        if(test):
            datfile = open(file, "w")
            datfile.write("")
            datfile.close()

        # AQUI VAN LOS NOMBRES Y NUMEROS DE LAS ESTACIONES

        # LINEA 1 VERDE (24 estaciones)
        EstacionHandler.estaciones.append(Estacion.Estacion(101, "Piraeus"))
        EstacionHandler.estaciones.append(Estacion.Estacion(102, "Neo Faliro"))
        EstacionHandler.estaciones.append(Estacion.Estacion(103, "Moschato"))
        EstacionHandler.estaciones.append(Estacion.Estacion(104, "Kallithea"))
        EstacionHandler.estaciones.append(Estacion.Estacion(105, "Tavros"))
        EstacionHandler.estaciones.append(Estacion.Estacion(106, "Petralona"))
        EstacionHandler.estaciones.append(Estacion.Estacion(107, "Thissio"))
        EstacionHandler.estaciones.append(Estacion.Estacion(108, "Monastiraki"))
        EstacionHandler.estaciones.append(Estacion.Estacion(109, "Omonia"))
        EstacionHandler.estaciones.append(Estacion.Estacion(110, "Victoria"))
        EstacionHandler.estaciones.append(Estacion.Estacion(111, "Attiki"))
        EstacionHandler.estaciones.append(Estacion.Estacion(112, "Aghios Nikolaos"))
        EstacionHandler.estaciones.append(Estacion.Estacion(113, "Kato Patissia"))
        EstacionHandler.estaciones.append(Estacion.Estacion(114, "Aghios Eleftherios"))
        EstacionHandler.estaciones.append(Estacion.Estacion(115, "Ano Patissia"))
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
        EstacionHandler.estaciones.append(Estacion.Estacion(201, "Aghios Antonios"))
        EstacionHandler.estaciones.append(Estacion.Estacion(202, "Sepolia"))
        EstacionHandler.estaciones.append(Estacion.Estacion(203, "Attiki"))
        EstacionHandler.estaciones.append(Estacion.Estacion(204, "Larissa Station"))
        EstacionHandler.estaciones.append(Estacion.Estacion(205, "Metaxourghio"))
        EstacionHandler.estaciones.append(Estacion.Estacion(206, "Omonia"))
        EstacionHandler.estaciones.append(Estacion.Estacion(207, "Panepistimio"))
        EstacionHandler.estaciones.append(Estacion.Estacion(208, "Syntagma"))
        EstacionHandler.estaciones.append(Estacion.Estacion(209, "Akropoli"))
        EstacionHandler.estaciones.append(Estacion.Estacion(210, "Sygrou-Fix"))
        EstacionHandler.estaciones.append(Estacion.Estacion(211, "Neos Kosmos"))
        EstacionHandler.estaciones.append(Estacion.Estacion(212, "Aghios Ioannis"))
        EstacionHandler.estaciones.append(Estacion.Estacion(213, "Dafni"))
        EstacionHandler.estaciones.append(Estacion.Estacion(214, "Aghios Dimitrios"))

        # LINEA 3 AZUL (20 estaciones)
        EstacionHandler.estaciones.append(Estacion.Estacion(301, "Egaleo"))
        EstacionHandler.estaciones.append(Estacion.Estacion(302, "Eleonas"))
        EstacionHandler.estaciones.append(Estacion.Estacion(303, "Kerameikos"))
        EstacionHandler.estaciones.append(Estacion.Estacion(304, "Monastiraki"))
        EstacionHandler.estaciones.append(Estacion.Estacion(305, "Syntagma"))
        EstacionHandler.estaciones.append(Estacion.Estacion(306, "Evangelismos"))
        EstacionHandler.estaciones.append(Estacion.Estacion(307, "Megaro Moussikis"))
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
        EstacionHandler.estaciones.append(Estacion.Estacion(318, "Paiania-Kantza"))
        EstacionHandler.estaciones.append(Estacion.Estacion(319, "Koropi"))
        EstacionHandler.estaciones.append(Estacion.Estacion(320, "Airport"))

        # Escribir en el fichero de texto
        stat: Estacion
        for stat in EstacionHandler.estaciones:
            stat.writeCoords(file)

    # Lee las estaciones desde archivo
    @staticmethod
    def read(file):
        datfile = open(file, "r")
        statlines = datfile.readlines()
        for curline in statlines:
            split = curline.split(';')
            num = split[0]
            nam = split[1]
            latit = split[2]
            longit = split[3]
            stat = Estacion.Estacion((num), nam,float(latit), float(longit))
            EstacionHandler.lineas[stat.getLinea()].append(stat)
            EstacionHandler.estaciones.append(stat)
            EstacionHandler.metromap[int(num)] = stat

