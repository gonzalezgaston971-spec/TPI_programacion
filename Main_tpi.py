import csv
from Funciones import *
#Llamamos todas las funciones existentes en el archivo de funciones a la rama principal

while True:
    opcion = menu_principal()
    match opcion:
        case "1" | "uno":
            pass
        case "2" | "dos":
            pass
        case "3" | "tres":
            pass
        case "4" | "cuatro":
            pass
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