import csv
def crear_archivo():
    try:
        with open("paises.csv", mode="r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        print("El archivo no existe, se va a crear...")
        with open("paises.csv", mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Pais", "Poblacion","Superficie","Continente"])

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
        continente = input("Ingrese el continente: ").strip().capitalize()

        if continente == "":
            print(" No puede estar vacío")
            intentos += 1
        else:
            return continente

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

def validar_pais_carga(paises):
    intentos = 0

    while intentos < 3:
        pais = input("Ingrese el nombre del país: ").strip().title()

        if pais == "":
            print("El nombre no puede estar vacío")
            intentos += 1

        else:
            existe = False
            for p in paises:
                if p["Pais"].lower() == pais.lower():
                    existe = True
                    break

            if existe:
                print("El país ya existe")
                intentos += 1
            else:
                return pais
        if intentos == 3:
            continuar = desea_continuar()

            if continuar == "si":
                intentos = 0
            else:
                return None 
            
def validar_pais_vacio():      
    intentos = 0
    while intentos < 3:
        pais = input("Ingrese el nombre del país: ").strip().title()
        if pais == "":
            print("El nombre no puede estar vacío")
            intentos += 1
        else:
            return pais
        if intentos == 3:
            continuar = desea_continuar()
            if continuar == "si":
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
    intento = 0
    while intento < 3:
        try:
            cantidad_a_cargar = int(input("Ingrese la cantidad de paises a cargar: "))
            if cantidad_a_cargar < 1:
                print("no puede ingresar un numero menor a 1 para la cantidad de paises")
                intento += 1
                continue
            break
        except ValueError:
            print("Solo se permiten numeros")
            intento += 1
        if intento == 3:
            continuar = desea_continuar()
            if continuar == "si":
                intento == 0
            else:
                print("volviendo al menu principal")
                return

    with open("paises.csv", mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for _ in range(cantidad_a_cargar):
            pais = validar_pais_carga(paises)
            if pais == None:
                print("Volviendo al menu principal")
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

def actualizar_poblacion_superficie(paises):
    if not paises:
        print("Todavia no se ingresaron paises, pero puede hacerlo en la opcion numero 1 del menu")
        return
    pais_buscado = validar_pais_vacio()
    if pais_buscado == None:
        print("volviendo al menu principal")
        return
    existe = False
    for p in paises:
        if p["Pais"].title() == pais_buscado.title():
            existe = True
            poblacion_nueva = validar_poblacion()
            if poblacion_nueva == None:
                print("Volviendo al menu principal")
                return
            superficie_nueva = validar_superficie()
            if superficie_nueva == None:
                print("Volviendo al menu principal")
                return
            p["Poblacion"] = poblacion_nueva
            p["Superficie"] = superficie_nueva
            guardar_datos(paises)
            print("¡Pais actualizado correctamente!")
            return 
    if not existe:
        print("no se encontro el pais que buscaba")
        return