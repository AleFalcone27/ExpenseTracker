import dearpygui.dearpygui as dpg

# generamos las categorias 
categorias = ["Comida","Regalos","Compra Super","Ingresos"]; 

# generamos tuplas para discriminar los gatos por categorias
comida = []
regalos = []
compra_super = []
ingresos = []

# cargamos los montos ingresados en cada una de las caracteristicas 
def cargar(categoria_elegida,precio_ingresado):

    # Hacerlo con excel 
    
    if(categoria_elegida == "Regalos"):
        print("REGALOS")
        regalos.append(precio_ingresado) 
        
    elif(categoria_elegida == "Comida" ):
        print("COMIDA")
        comida.append(precio_ingresado)
        
    elif(categoria_elegida == "Compra Super"):
        print("Compra super")
        compra_super.append(precio_ingresado)
        
    elif(categoria_elegida == "Ingresos"):
        print("ingresos")
        
        ingresos.append(precio_ingresado)
        

def button_callback():
    
    precio_ingresado = dpg.get_value(precio)
    
    print("PRECIO: " + precio_ingresado)
    
    dpg.set_value(precio, "PRECIO"); #seteamos el valor a PRECIO para preparar la siguiente carga
    
    categoria_elegida = dpg.get_value(categoria) # obtenemos la categoria

    dpg.set_value(categoria, "CATEGORIA") #seteamos el valor a CATEGORIAS para preparar la siguiente carga
    
    cargar(categoria_elegida,precio_ingresado)

        


dpg.create_context() #creamos el contexto para acceder los comandos de la libreria



with dpg.window(label="aa"):
    dpg.add_text("VAMOS A TRAKEAR TUS GASTOS MENSUALES")
    dpg.add_button(label="INGRESAR", callback= button_callback, tag="boton") # boton para cargar los datos 
    
    precio = dpg.add_input_text(tag=1); # input del precio
    
    categoria = dpg.add_combo(categorias, tag=2); # categoria del gasto
    dpg.set_value(categoria, "CATEGORIA")

    
    
    
    
    
# crea la ventana grafica
dpg.create_viewport(title='NLAFM', width=1200, height=600) # nombre de ka ventana , ancho , alto

dpg.setup_dearpygui()

dpg.show_viewport() # mostramos la ventana grafica

dpg.start_dearpygui() # arranca el bucle de renderizado


print(comida)
print(regalos)
print(compra_super)
print(ingresos)



dpg.destroy_context() #Destruimos el contexto

