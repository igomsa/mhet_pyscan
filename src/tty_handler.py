#!/usr/bin/env python3
'''
UART communication on Raspberry Pi using Pyhton
http://www.electronicwings.com
'''

import serial
from time import sleep
from openpyxl import Workbook


def leer_tty(puerto):
    ser = serial.Serial (puerto, 9600) #Abre el puerto con baud rate necesario
    recibido = ser.read()              #Lee el puerto serial
    #print (recibido)                   #Immprime el dato recibido
    sleep(0.03)
    bytes = ser.inWaiting()            #Revisa si hay algún byte en el buffer.
    recibido += ser.read(bytes)
    ser.write(recibido)                #Trasmite los datos seriales de vuelta.
    recibido = int(recibido)
    print ("\nCódigo artículo: " + str(recibido))                   #Immprime el dato recibido
    return recibido                    #Retorna dato recibido

###################### Matching number function. Here we need to run in local file or external.
