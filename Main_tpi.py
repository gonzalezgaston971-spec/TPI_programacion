from Funciones import *
#Llamamos todas las funciones existentes en el archivo de funciones a la rama principal
import csv
crear_archivo()
#creamos el archivo en el caso de que no exista
paises = cargar_datos()
#en caso de que el csv tenga datos los pasamos a una lista
while True:
    opcion = menu_principal()
    #Aqui se imprime un menu simple dentro de un bucle para que se cierre cuado el usuario lo desee
    match opcion:
        case "1" | "uno":
            agregar_pais(paises)
        case "2" | "dos":
            actualizar_poblacion_superficie(paises)
        case "3" | "tres":
            buscar_pais(paises)
        case "4" | "cuatro":
            filtrar_paises(paises)
        case "5" | "cinco":
            pass
        case "6" | "seis":
            pass
        case "7" | "siete":
            print("Cerrando menu, Esperamos fuera de su agrado")
            print("¡Adios!")
            break
        case _:
            print("\nPor favor ingrese una de las opciones dadas en el 'MENU'")