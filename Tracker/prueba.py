
from openpyxl import Workbook, load_workbook
from  tracker_main import *
from datetime import now

def cargar():
    heading = ["fecha","categoria","precio","comentario"]

    bandera = True

    fecha = now.year



    # cargamos el archivo 
    wb = load_workbook("gastos.xlsx")

    # agarra la pestaña activa 
    ws = wb.active

    # Los headers se van a escribir solo la primera vez que corra el codigo
    while bandera == True:
        ws.append(heading)
        bandera = False;

    # cargamos en el archivo el nuevo gasto
    ws.append([fecha,categoria,precio,comentario])


    # Save the file
    wb.save("gastos.xlsx")



    

