def desea_continuar():
    print("Tuvo demasiados errores consecutivos.")
    while True:
        try:
            desea_continuar = input("¿Desea continuar con la carga de datos?(si/no)").lower().strip()
            if not desea_continuar in ("si","no"):
                raise ValueError("solo puede ingresar si o no")
            break
        except ValueError as e:
            print("ERROR",e)
        return desea_continuar
    
def validar_continente():
    error = 0
    while error < 3:
        try:
            continente=input("Ingrese aqui el continente del pais: ").strip().capitalize()
            if continente == "":
                error += 1
                raise ValueError("El nombre del continente no puede estar vacio")
            return continente
        except ValueError as e:
            print("ERROR:",e)
            if error == 3:
                    continuar = desea_continuar()
                    if continuar == "si":
                        error = 0
                    else:
                        return 
    
def validar_superficie():
    error = 0
    while error < 3:
        try:
            superficie = int(input("Ingrese aqui la superficie del pais en km2: "))
            if superficie < 1:
                raise ValueError("la superficie no puede ser menor a 1")
            return superficie
        except ValueError as e:
            print("ERROR:",e)
            if error == 3:
                    continuar = desea_continuar()
                    if continuar == "si":
                        error = 0
                    else:
                        return 
def validar_poblacion():
    error = 0
    while error < 3:
        try:
            poblacion = int(input("ingrese la poblacion del pais: "))
            if poblacion < 0:
                raise ValueError("No puede ingresar numeros menores a 0")
            return poblacion 
        except ValueError as e:
            print("ERROR:",e)
            if error == 3:
                    continuar = desea_continuar()
                    if continuar == "si":
                        error = 0
                    else:
                        return 

def validar_pais_vacio():
    error = 0
    while error < 3:
        try:
            pais=input("Ingrese aqui su pais: ").strip().capitalize()
            if pais == "":
                error += 1
                raise ValueError("El nombre del pais no puede estar vacio")
            return pais
        except ValueError as e:
            print("ERROR:",e)
            if error == 3:
                    continuar = desea_continuar()
                    if continuar == "si":
                        error = 0
                    else:
                        return 
                        
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
