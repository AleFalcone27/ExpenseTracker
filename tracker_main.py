# Importamos bibliotecas
import dearpygui.dearpygui as dpg
from datetime import date

def main():
    
    # Creamos contexto para poder acceder a la libreria 
    dpg.create_context() 

    # Funcion para formatear la linea para caragarla de correctamente en el CVS 
    def line_to_csv(archivo:str,col_1:str, col_2:str ,col_3:str ,col4:str):

        with open(archivo,"a+") as registro:
                registro.write(str(col_1) + "," + col_2 + "," + col_3 + "," + col4 + "\n")

    # Archivo en el cual queremos operar
    archivo = "gastos1.xlsx"

    # Categorias para el combo de nuestro programa (se pueden añadir nuevas)
    categorias_combo = ["Comida","Regalos","Compra Super","Ingresos","Facultad","Pc"]

    # Esta funcion sera llamada al presionar el boton save en nuestro programa
    def load():
        
        # Campturamos los valores ingresados por el usuario
        precio_ingresado = dpg.get_value(precio)
        categoria_ingresada = dpg.get_value(categoria)
        comentario_ingresado = dpg.get_value(comentario)

        # Escribimos la linea en nuestro csv
        line_to_csv(archivo,"fecha",categoria_ingresada,precio_ingresado,comentario_ingresado) 

    # Nombre de nuestra ventana
    with dpg.window(tag="Primary Window"): 
        dpg.add_text("Vamos a ver si ahora llegas a fin de mes")

        # Creamos los elementos de nuestro programa
        precio = dpg.add_input_text(label="PRECIO",tag=1); # Cramos input del precio
        categoria = dpg.add_combo(categorias_combo, tag=2, label="CATEGORIAS"); # Creamos categoria del gasto
        comentario = dpg.add_input_text(label="COMENTARIO", tag=3) # Creamos input del comentario
        dpg.add_button(label="Save", callback= load,) # Al presionar el boton llamamos a la funcion encargada de guardar los datos en el archivo csv
        
    # Damos el nombre y dimensiones a la ventana
    dpg.create_viewport(title='Expenses Tracer ', width = 600, height = 300) 
    dpg.setup_dearpygui() 
    dpg.show_viewport() # Mostramos la ventana grafica
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui() # Comienza el bucle de renderizado
    dpg.destroy_context() # Destruimos el contexto

main()