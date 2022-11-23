import pandas as pd
import numpy as np
from lib import EstacionHandler, Estacion

if __name__ == '__main__':
    df= pd.read_csv(
                        filepath_or_buffer='Utils/colors.csv', 
                        sep=';',
                        )

    EstacionHandler.read()
    st: Estacion
    for st in EstacionHandler.estaciones:
        
        print(st.getLinea())
