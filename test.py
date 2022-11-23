from geopy.geocoders import Nominatim
from geopy.location import Location
from lib import EstacionHandler, Estacion

if __name__ == '__main__':
    EstacionHandler.read()

    sm =";"; cityname="Athens"
    keywords = ["station", "metro", "subway", "μετρό", "σταθμός", "underground"]
    coordenadas: Location = None

    st: Estacion
    for st in EstacionHandler.estaciones:
        i=0
        while (coordenadas == None and i< len(keywords)):
            querytext = st.name + " " + keywords[i] + "," +cityname
            coordenadas= Nominatim(user_agent="telmove@gmx.com").geocode(querytext)
            i=i+1
        
        if(coordenadas == None):
            print("NINGUNO")
        else:
            print(coordenadas)
        
    """
    EstacionHandler.read()
    map = EstacionHandler.metromap
    st: Estacion = map[318]
    
    """