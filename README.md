# Proyecto GPS IA

## Autores

- [Álvaro Cabo](https://github.com/alvarocabo)

## Set Up

- Requirements:
  - Python/Python3
  - Pip

### Start Up

1. Situarse con la consola en la carpeta madre (GPS/)
2. Crear un entorno virtual  

```shell
   python3 -m venv venv/
   
   source venv/bin/activate
```

3. Instalar librerías necesarias:

```shell
   pip install -r Utils/requirements.txt
```

- Si no funciona el script puedes instalarlos individualmente

```shell
    pip install folium PyQt5 geopy
```

1. Instalar el motor gráfico

```shell
   pip install pyqtwebengine
```

### Running project

```shell
   python main.py
```