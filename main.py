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

        cityCoords=[37.97945, 23.71622]

        #Actualiza el listado de estaciones
        EstacionHandler.read()

        mapWidget = folium.Map(location=cityCoords, zoom_start=10, control_scale=True)
        
        st: Estacion
        for st in EstacionHandler.estaciones:
            iColor: str = lines["COLOR"][st.line-1]
            #Añade el icono del marcador
            folium.Marker(location=[st.lat, st.long], 
                          popup=st.name,
                          icon=folium.Icon(color=iColor)).add_to(mapWidget)

        for i in range(1,4):
            iColor: str = lines["COLOR"][i-1]
            style={'fillColor': iColor, 'color': iColor}
            folium.GeoJson("data/json/{i}.json".format(i=i), style_function=lambda x:style).add_to(mapWidget)

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
