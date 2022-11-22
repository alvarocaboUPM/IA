import sys
import io
import folium 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.uic.properties import QtWidgets

from lib import EstacionHandler

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Athens metro helper')
        self.window_width, self.window_height = 800, 400
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        EstacionHandler.read()
        #print("Numero de Estaciones -> "+str(len(EstacionHandler.estaciones)))

        cityCoords= [50.4547,30.5238] #CAMBIAR POR LAS DE ATENAS

        mapWidget = folium.Map(location=cityCoords, zoom_start=10, control_scale=True)
        for st in EstacionHandler.estaciones:
            st.print()
            folium.Marker(location=[st.lat, st.long], fill_color="#e61b1b").add_to(mapWidget)

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
	print('Closing Window...')
