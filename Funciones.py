import csv
def crear_archivo(): #Se encarga de crear un archivo paises.CSV en caso de no encontrarlo
    try:
        with open("paises.csv", mode="r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        print("El archivo no existe, se va a crear...")
        with open("paises.csv", mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Pais", "Poblacion","Superficie","Continente"])
#Intenta abrir el archivo y en caso de que no exista lo crea
def cargar_datos(): # mete todos los datos del CSV en una lista de diccionarios
    paises = []

    with open("paises.csv", mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            try:
                fila["Poblacion"] = int(fila["Poblacion"])
                fila["Superficie"] = int(fila["Superficie"])
            except ValueError:
                print(f"Error en datos de: {fila}")
                continue

            paises.append(fila)

    return paises

def guardar_datos(paises): # es la encargada de almacenar en el archivo los cambios realizados
    #1. Abre el archivo y sus encabezados o campos
    with open("paises.csv", mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["Pais", "Poblacion","Superficie","Continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
    #2 Escribe lo que se encuentre dentro de la lista de diccionarios
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
        print("Ingrese el continente:")
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
            print("\nEntrada inválida. Debe ingresar un número.")
            intentos += 1
            # Por si el usuario ingresa letras o caracteres especiales

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
        elif pais.isdigit():
            print("El nombre del País no puede contener numeros")
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
                intento = 0  
            else:
                print("volviendo al menu principal")
                return

    # Procesamos la carga de datos en la lista 'paises'
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
            "Poblacion": poblacion,
            "Superficie": superficie,
            "Continente": continente
        }
        paises.append(nuevo_pais)
        print(f"¡{pais} preparado para guardar!")

    # Al terminar el bucle, guardamos toda la lista actualizada de forma limpia en el CSV
    guardar_datos(paises)
    print("\n¡Todos los países se han guardado correctamente en el archivo!")
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
        print("="*9,"FILTROS DISPONIBLES","="*9)
        print("="*40)
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
                print("="*40)
                for pais in paises:
                    if continente in pais["Continente"]:
                        print(f'Pais: {pais["Pais"]} | Poblacion: {pais["Poblacion"]} | Superficie: {pais["Superficie"]} | Continente: {pais["Continente"]}')
                        encontrado = True
                print("="*40)
                if not encontrado:
                    print("No hay paises cargados en ese continente")
                    continue
            case "2":
                print("--- FILTRO POR POBLACIÓN ---")
                print("Ingrese el rango mínimo de población")
                poblacion_minima = validar_poblacion()
                if poblacion_minima == None:
                    continue
                
                intentos = 0
                rango_valido = False
                
                while intentos < 3:
                    print("Ingrese el rango máximo de población")
                    poblacion_maxima = validar_poblacion()
                    
                    if poblacion_maxima == None:
                        # Si canceló dentro de validar_poblacion, salimos del filtro
                        break
                    
                    if poblacion_maxima <= poblacion_minima:
                        print(" El rango de población máximo no puede ser menor o igual al rango mínimo.")
                        intentos += 1
                    else:
                        rango_valido = True
                        break
                        
                    if intentos == 3:
                        if desea_continuar() == "si":
                            intentos = 0
                        else:
                            break 
                
                if not rango_valido:
                    continue 
                
                encontrado = False
                print("\n" + "="*8, "PAISES DENTRO DEL RANGO INGRESADO", "="*8)
                for pais in paises:
                    if poblacion_minima <= pais["Poblacion"] and pais["Poblacion"] <= poblacion_maxima:
                        print(f'Pais: {pais["Pais"]} | Poblacion: {pais["Poblacion"]} | Superficie: {pais["Superficie"]} | Continente: {pais["Continente"]}')
                        encontrado = True
                if not encontrado:
                    print("No se encontraron países en ese rango de población")
                print("="*40 + "\n")
            
            case "3":
                print("--- FILTRO POR SUPERFICIE ---")
                print("Ingrese la superficie mínima de búsqueda")
                superficie_minima = validar_superficie()
                if superficie_minima == None:
                    continue
                
                intentos = 0
                rango_valido = False
                
                while intentos < 3:
                    print("Ingrese el rango máximo de superficie")
                    superficie_maxima = validar_superficie()
                    
                    if superficie_maxima == None:
                        break
                    
                    if superficie_maxima <= superficie_minima:
                        print("El rango de superficie máximo no puede ser menor o igual al rango mínimo.")
                        intentos += 1
                    else:
                        rango_valido = True
                        break
                        
                    if intentos == 3:
                        if desea_continuar() == "si":
                            intentos = 0
                        else:
                            break 
                
                if not rango_valido:
                    continue 
                
                encontrado = False
                print("\n" + "="*8, "PAISES DENTRO DEL RANGO INGRESADO", "="*8)
                for pais in paises:
                    if superficie_minima <= pais["Superficie"] and pais["Superficie"] <= superficie_maxima:
                        print(f'Pais: {pais["Pais"]} | Poblacion: {pais["Poblacion"]} | Superficie: {pais["Superficie"]} | Continente: {pais["Continente"]}')
                        encontrado = True
                if not encontrado:
                    print("No se encontraron países en ese rango de superficie")
                print("="*40 + "\n")
            case "4":
                print("Volviendo al menu principal")
                return
            case _:
                print("Ingrese una opcion del menu 'FILTROS DISPONIBLES' por favor")
        
def ordenar_paises(paises):
    if not paises:
        print("Todavía no se ingresaron países, pero puede hacerlo en la opción número 1 del menú")
        return

    print("="*8, "OPCIONES DE ORDENAMIENTO", "="*8)
    print("""
1. Ordenar por Nombre
2. Ordenar por Población
3. Ordenar por Superficie
4. Volver al menú principal""")
    
    opcion = input("Ingrese su opción: ").strip()
    
    if opcion == "4":
        print("Volviendo al menú principal")
        return
    elif opcion not in ("1", "2", "3"):
        print("Opción inválida. Volviendo al menú principal.")
        return

    print("""
Como desea ordenar:
1. Ascendente (Menor a Mayor / A-Z)
2. Descendente (Mayor a Menor / Z-A)""")
    
    sentido = input("Ingrese su opción: ").strip()
    if sentido == "1":
        reversa = False
    elif sentido == "2":
        reversa = True
    else:
        print("Opción inválida. Se ordenará de forma ascendente por defecto.")
        reversa = False

    # Definimos la clave de ordenamiento según la opción
    match opcion:
        case "1":
            # Pasamos a .lower() para que no priorice mayúsculas sobre minúsculas en el orden alfabético
            paises_ordenados = sorted(paises, key=lambda x: x["Pais"].lower(), reverse=reversa)
            criterio = "Nombre"
        case "2":
            paises_ordenados = sorted(paises, key=lambda x: x["Poblacion"], reverse=reversa)
            criterio = "Población"
        case "3":
            paises_ordenados = sorted(paises, key=lambda x: x["Superficie"], reverse=reversa)
            criterio = "Superficie"

    print("\n" + "="*8, f"LISTA ORDENADA POR {criterio.upper()}", "="*8)
    for pais in paises_ordenados:
        print(f'País: {pais["Pais"]} | Población: {pais["Poblacion"]} | Superficie: {pais["Superficie"]} | Continente: {pais["Continente"]}')
    print("="*40)

def mostrar_estadisticas(paises):
    if not paises:
        print("Todavía no se ingresaron países, pero puede hacerlo en la opción número 1 del menú")
        return

    cantidad = len(paises)
    
    # 1. Cálculos de Población
    poblacion_total = sum(p["Poblacion"] for p in paises)
    poblacion_promedio = poblacion_total / cantidad
    pais_mas_poblado = max(paises, key=lambda x: x["Poblacion"])
    pais_menos_poblado = min(paises, key=lambda x: x["Poblacion"])

    # 2. Cálculos de Superficie
    superficie_total = sum(p["Superficie"] for p in paises)
    superficie_promedio = superficie_total / cantidad
    pais_mayor_superficie = max(paises, key=lambda x: x["Superficie"])
    pais_menor_superficie = min(paises, key=lambda x: x["Superficie"])

    # 3. Conteo de países por continente
    conteo_continentes={}
    for p in paises:
        continente = p["Continente"].strip().title()
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1

    # 4. Mostrar reportes en pantalla
    print("="*12, "ESTADÍSTICAS GENERALES", "="*12)
    print(f"Cantidad de países registrados: {cantidad}")
    print("-"*46)
    print(f"Población Total: {poblacion_total} hab.")
    print(f"Población Promedio: {poblacion_promedio:.2f} hab. por país")
    print(f"País más poblado: {pais_mas_poblado['Pais']} ({pais_mas_poblado['Poblacion']} hab.)")
    print(f"País menos poblado: {pais_menos_poblado['Pais']} ({pais_menos_poblado['Poblacion']} hab.)")
    print("-"*46)
    print(f"Superficie Total: {superficie_total} km²")
    print(f"Superficie Promedio: {superficie_promedio:.2f} km² por país")
    print(f"País con mayor superficie: {pais_mayor_superficie['Pais']} ({pais_mayor_superficie['Superficie']} km²)")
    print(f"País con menor superficie: {pais_menor_superficie['Pais']} ({pais_menor_superficie['Superficie']} km²)")
    print("="*46)

    print("Cantidad de países por continente:")
    for continente, cantidad_cont in conteo_continentes.items():
        print(f" - {continente}: {cantidad_cont}")
    print("="*46)