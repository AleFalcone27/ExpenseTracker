import dearpygui as dpg
import tracker_main



def button_callback():
    precio_ingresado = dpg.get_value(tracker_main.precio)
    print("PRECIO: " + precio_ingresado)
    
    dpg.set_value(tracker_main.precio, "PRECIO"); #seteamos el valor a PRECIO para preparar la siguiente carga
    
    categoria_elegida = dpg.get_value(tracker_main.categoria) # obtenemos la categoria

    dpg.set_value(tracker_main.categoria, "CATEGORIA") #seteamos el valor a CATEGORIAS para preparar la siguiente carga
    
    cargar(categoria_elegida,precio_ingresado)
