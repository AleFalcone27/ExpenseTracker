import dearpygui.dearpygui as dpg
from datetime import date
from openpyxl import Workbook, load_workbook

dpg.create_context() # Creamos contexto para poder acceder a la libreria 

dpg.create_viewport(title='Custom Title', width=600, height=300) # Damos el nombre y medidas a la ventana

# Generamos las categorias
categorias = ["Comida","Regalos","Compra Super","Ingresos"]

# Seteamos la bandera en True
bandera = True;

# Obtenemos la fecha
fecha = date.today()


# Realizamos la carga de datos en el excel
def cargar(fecha,categoria_ingresada,precio_ingresado,comentario_ingresado):
    heading = ["fecha","categoria","precio","comentario"]

    bandera = True

    # Cargamos el archivo 
    wb = load_workbook("gastos.xlsx")

    # Agarramos la pestaña activa 
    ws = wb.active

    # Los headers se van a escribir solo la primera vez que corra el codigo
    while bandera == True:
        ws.append(heading)
        bandera = False;

    # cargamos en el archivo el nuevo gasto
    ws.append([fecha,categoria_ingresada,precio_ingresado,comentario_ingresado])

    # Save the file
    wb.save("gastos.xlsx")

    
def save():
    precio_ingresado = dpg.get_value(precio)
    categoria_ingresada = dpg.get_value(categoria)
    comentario_ingresado = dpg.get_value(comentario)

    print(precio_ingresado)
    print(categoria_ingresada)
    print(comentario_ingresado)
    
    cargar(fecha,categoria_ingresada,precio_ingresado,comentario_ingresado)


with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save", callback= save,)
    
    precio = dpg.add_input_text(label="PRECIO",tag=1); # Cramos input del precio
    
    categoria = dpg.add_combo(categorias, tag=2, label="CATEGORIAS"); # Creamos categoria del gasto
    
    comentario = dpg.add_input_text(label="COMENTARIO", tag=3) # Creamos input del comentario
    
    








dpg.setup_dearpygui() 
dpg.show_viewport() # Mostramos la ventana grafica
dpg.start_dearpygui() # Comienza el bucle de renderizado

dpg.destroy_context() # Destruimos el contexto

