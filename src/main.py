#!/usr/bin/env python3

from tty_handler import *
from edit_table import *
from drive_handler import *
#import tty_handler

puerto = "/dev/ttyUSB0"

# Lectura "base de datos"
id_drive = 'your id'
ruta_descarga = 'your_path'

# Escritura "base de datos"
ruta_archivo = 'your_path'
id_folder = 'your id'

if __name__ == "__main__":
    while True:
        # Se extrae código de barras
        print('\n\n\nInicia escaneo')
        codigo = leer_tty(puerto)

        # Se descarga la base datos para actualizarla.
        bajar_archivo_por_id(id_drive,ruta_descarga)

        # Se comprara código de barras con base_dateos
        #print('\nInicia búsqueda de código')
        valor = buscar_codigo(codigo)
        try:
            print("Nombre del artículo: " + valor)
        except:
            print("Código no encontrado")
            print('\nFin del escaneo')
            continue

        # Se llena la hoja de asistencia
        print('\nInicia adición de valor en hoja de asistencia')
        asistencia(valor)
        print('\nFin del escaneo')


        ## Se sube la hoja de asisstencia al servidor
        subir_archivo(ruta_archivo,id_folder)
