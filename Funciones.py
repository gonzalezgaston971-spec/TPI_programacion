
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


def normalizar_texto():
    pass