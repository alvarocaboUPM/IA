import sys
import io
from dotenv import dotenv_values
import folium 
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtGui
from PyQt5.uic.properties import QtWidgets

from lib import EstacionHandler
from lib.Estacion import Estacion

fileE = dotenv_values(".env")["FILE_ESTACIONES"]
fileM = dotenv_values(".env")["FILE_MATRIX"]
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Athens Metro')
        self.window_width, self.window_height = 800, 400
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowIcon(QtGui.QIcon('Utils/logobw.png'))

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        #Lineas
        lines= pd.read_csv(filepath_or_buffer='Utils/colors.csv', 
                            sep=';')

        #cityCoords= [50.4547,30.5238] #CAMBIAR POR LAS DE ATENAS
        cityCoords=[37.97945, 23.71622]

        #Actualiza el listado de estaciones
        EstacionHandler.read(fileE)
        
        mapWidget = folium.Map(location=cityCoords, zoom_start=10, control_scale=True)
        
        st: Estacion
        for st in EstacionHandler.estaciones:
            print(st.toString())
            l=st.getLinea(st)
            iColor: str = lines["COLOR"][l-1]

            #Añade el icono del marcador
            folium.Marker(location=[st.lat, st.long], 
                          popup=st.name,
                          icon=folium.Icon(color=iColor)).add_to(mapWidget)
            
        # save map data to data object
        data = io.BytesIO()
        mapWidget.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


# Funcion principal
if __name__ == '__main__':
    import graphics

app = QApplication(sys.argv)

myApp = MyApp()
myApp.show()
try:
	sys.exit(app.exec_())
except SystemExit:
	print('Se ha cerrado correctamente')
