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
            try:
                fila["Poblacion"] = int(fila["Poblacion"])
                fila["Superficie"] = int(fila["Superficie"])
            except ValueError:
                print(f"⚠️ Error en datos de: {fila}")
                continue

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
            return continente
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
            poblacion = int(input("Ingrese población: "))

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
    
def buscar_pais(paises):
    if not paises:
        print("Todavia no se ingresaron paises, pero puede hacerlo en la opcion numero 1 del menu")
        return
    pais_buscado = validar_pais_vacio()
    if pais_buscado == None:
        print("Volviendo al menu principal")
        return
    encontrado = False
    print("="*8,"LISTA DE PAISES RELACIONADOS A SU BUSQUEDA", "="*8)
    for pais in paises:
        if pais_buscado.lower() in pais["Pais"].lower():
            print(f'Pais: {pais["Pais"]} | Poblacion: {pais["Poblacion"]} | Superficie: {pais["Superficie"]} | Continente: {pais["Continente"]}')
            encontrado = True
    if not encontrado:
        print("no se encontro ningun pais igual o similar a lo que busca")
        return

def filtrar_paises(paises):
    if not paises:
        print("Todavia no se ingresaron paises, pero puede hacerlo en la opcion numero 1 del menu")
        return
    while True:
        print("="*8,"FILTROS DISPONIBLES","="*8)
        print("""
1. Filtrar por continente
2. Filtrar por rango de poblacion
3. Filtrar por rango de superficie
4. Volver al menu principal""")
        opcion = input("ingrese su opcion:")
        match opcion:
            case "1":
                continente = validar_continente()
                if continente == None:
                    continue
                encontrado = False
                print("=")
                for pais in paises:
                    if continente in pais["Continente"]:
                        print(f'Pais: {pais["Pais"]} | Poblacion: {pais["Poblacion"]} | Superficie: {pais["Superficie"]} | Continente: {pais["Continente"]}')
                        encontrado = True
                if not encontrado:
                    print("No hay paises cargados en ese continente")
                    continue
            case "2":
                print("Ingrese el rango minimo de poblacion")
                poblacion_minima = validar_poblacion()
                if poblacion_minima == None:
                    continue
                while True:
                    print("Ingrese el rango maximo de poblacion")
                    poblacion_maxima = validar_poblacion()
                    if poblacion_maxima == None:
                        break
                    if poblacion_maxima <= poblacion_minima:
                        print("El rango de poblacion maximo no puede ser menor o igual al rango minimo")
                    break
                if poblacion_maxima == None:
                    continue
                encontrado = False
                print("="*8, "PAISES DENTRO DEL RANGO INGRESADO", "="*8)
                print("")
                for pais in paises:
                    if poblacion_minima <= pais["Poblacion"] and pais["Poblacion"] <= poblacion_maxima:
                        print(f'Pais: {pais["Pais"]} | Poblacion: {pais["Poblacion"]} | Superficie: {pais["Superficie"]} | Continente: {pais["Continente"]}')
                        encontrado = True
                print("")
                if not encontrado:
                    print("no se encontraron paises en ese rango de poblacion")
                    continue 
            case "3":
                print("Ingrese la superficie minima de busqueda")
                superficie_minima = validar_superficie()
                if superficie_minima == None:
                    continue
                while True:
                    print("Ingrese el rango maximo de superficie")
                    superficie_maxima = validar_superficie()
                    if superficie_maxima == None:
                        break
                    if superficie_maxima <= poblacion_minima:
                        print("El rango de superficie maximo no puede ser menor o igual al rango minimo")
                    break
                if superficie_maxima == None:
                    continue
                encontrado = False
                print("="*8, "PAISES DENTRO DEL RANGO INGRESADO", "="*8)
                print("")
                for pais in paises:
                    if poblacion_minima <= pais["Superficie"] and pais["Superficie"] <= poblacion_maxima:
                        print(f'Pais: {pais["Pais"]} | Poblacion: {pais["Poblacion"]} | Superficie: {pais["Superficie"]} | Continente: {pais["Continente"]}')
                        encontrado = True
                print("")
                if not encontrado:
                    print("no se encontraron paises en ese rango de superficie")
                    continue 
            case "4":
                print("Volviendo al menu principal")
                return
            case _:
                print("Ingrese una opcion del menu 'FILTROS DISPONIBLES' por favor")
        
