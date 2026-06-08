import csv
def crear_archivo():
    try:
        with open("paises.csv", mode="r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        print("El archivo no existe, se va a crear...")
        with open("paises.csv", mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Pais", "Poblacion","superficie","Continente"])

def cargar_datos():
    paises = []

    with open("paises.csv", mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            paises.append(fila)

    return paises

def guardar_datos(paises):
    with open("paises.csv", mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["Pais", "Poblacion","Superficie","Continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(paises)

def desea_continuar():
    print("Tuvo demasiados errores consecutivos.")
    while True:
        try:
            continuar = input("¿Desea continuar con la carga de datos?(si/no): ").lower().strip()
            if not continuar in ("si","no"):
                raise ValueError("solo puede ingresar si o no")
            return continuar
        except ValueError as e:
            print("ERROR",e)


def validar_continente():
    intentos = 0
    
    while intentos < 3:
        print("""
        1. America del Norte
        2. America del Sur
        3. America Central
        4. Asia
        5. Africa
        6. Antartida
        7. Europa
        8. Oceania
        """)
        continente = input("Ingrese el continente: ").strip()
        
        if continente == "":
            print("No puede estar vacío.")
            intentos += 1
        elif continente.isdigit():
            # El input es un string, así que evaluamos strings ("1", "2") en lugar de enteros (1, 2)
            match continente:
                case "1":
                    return "America del Norte"
                case "2":
                    return "America del Sur"
                case "3":
                    return "America Central"
                case "4":
                    return "Asia"
                case "5":
                    return "Africa"
                case "6":
                    return "Antartida"
                case "7":
                    return "Europa"
                case "8":
                    return "Oceania"
                case _:
                    # Caso default por si ingresan un número que no está en la lista (ej: "8")
                    print("Opción inválida. Ingrese un número del 1 al 7.")
                    intentos += 1
        else:
            # Por si el usuario ingresa letras o caracteres especiales
            print("Entrada inválida. Debe ingresar un número.")
            intentos += 1

        if intentos == 3:
            if desea_continuar() == "si":
                intentos = 0
            else:
                return None


def validar_superficie():
    intentos = 0

    while intentos < 3:
        try:
            superficie = int(input("Ingrese superficie (km2): "))

            if superficie < 1:
                print("Debe ser mayor a 0")
                intentos += 1
                continue

            return superficie

        except ValueError:
            print("Solo números enteros")
            intentos += 1

        if intentos == 3:
            if desea_continuar() == "si":
                intentos = 0
            else:
                return None
            
def validar_poblacion():
    intentos = 0

    while intentos < 3:
        try:
            poblacion = int(input("Ingrese la población del país: "))

            if poblacion < 0:
                print(" No se permiten números negativos")
                intentos += 1
                continue

            return poblacion

        except ValueError:
            print(" Solo se permiten números enteros")
            intentos += 1

        if intentos == 3:
            continuar = desea_continuar().lower()

            if continuar == "si":
                intentos = 0
            elif continuar == "no":
                return None

def validar_pais(paises):
    intentos = 0
    while intentos < 3:
        pais = input("Ingrese país: ").strip().title()
        if pais == "":
            print("No puede estar vacío")
            intentos += 1
            continue
        existe = False
        for p in paises:
            if p["Pais"].lower() == pais.lower():
                existe = True
                break
        if existe:
            print("País ya existe")
            intentos += 1
        else:
            return pais

        if intentos == 3:
            if desea_continuar() == "si":
                intentos = 0
            else:
                return None 
                        
def menu_principal():
    print("""

================ MENU =================

1. Agregar paises
2. Actualizar poblacion y superficie
3. Buscar un pais
4. Filtrar paises
5. Ordenar paises
6. Mostrar estadisticas 
7. Salir \n""")
    print("="*40)
    opcion = input("\nIngrese su opcion aqui por favor: ").strip().lower()
    print("")
    print("="*40)
    return opcion

def agregar_pais(paises):

    with open("paises.csv", mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        pais = validar_pais(paises)
        if pais == None:
            return
        poblacion = validar_poblacion()
        if poblacion == None:
            return
        superficie = validar_superficie()
        if superficie == None:
            return
        continente = validar_continente()
        if continente == None:
            return
        nuevo_pais = {
            "Pais": pais,
            "Poblacion":poblacion,
            "Superficie":superficie,
            "Continente":continente
        }
        paises.append(nuevo_pais)

        escritor.writerow([pais, poblacion, superficie, continente ])
        print("¡País agregado correctamente!")
    return paises
