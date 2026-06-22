# Sistema de Gestión de Países (CSV)

## Descripción del programa

Este programa permite gestionar información de países utilizando un archivo **CSV (`paises.csv`)** como almacenamiento persistente.

Al iniciar, el sistema verifica si el archivo existe. En caso contrario, lo crea automáticamente con los encabezados correspondientes para su correcto funcionamiento.

El sistema permite agregar, modificar, buscar, filtrar, ordenar y obtener estadísticas sobre los países cargados.

---

## Funcionalidades principales

### 1. Agregar países

Permite ingresar uno o varios países al sistema.

* Se solicita:

  * Nombre del país
  * Población
  * Superficie
  * Continente
* Validaciones:

  * No se permiten campos vacíos
  * No se permiten números en nombres
  * No se permiten duplicados
  * Datos numéricos obligatorios donde corresponda
* En caso de errores repetidos:

  * Se permite cancelar la operación
* Los datos se guardan en el archivo CSV

---

### 2. Actualizar población y superficie

Permite modificar datos de un país existente.

* Requisitos:

  * Debe haber países cargados
  * El país debe existir
* Se actualizan:

  * Población
  * Superficie
* Se puede cancelar la operación ante errores
* Los cambios se guardan automáticamente

---

### 3. Buscar un país

Permite buscar un país por nombre o parte del nombre.

* Muestra:

  * Coincidencias exactas o parciales
  * Todos los datos del país
* Si no hay resultados:

  * Se informa al usuario

---

### 4. Filtrar países

Permite visualizar países según distintos criterios.

Opciones disponibles:

* Por continente
* Por rango de población
* Por rango de superficie

Características:

* Menú persistente hasta que el usuario decida salir
* Validación de rangos (mínimo < máximo)
* Manejo de errores con opción de continuar o cancelar

---

### 5. Ordenar países

Permite ordenar los países según distintos criterios:

* Por nombre
* Por población
* Por superficie

Modos:

* Ascendente
* Descendente

---

### 6. Mostrar estadísticas

Genera un resumen general de los países cargados:

* Cantidad total de países
* Población:

  * Total
  * Promedio
  * País más poblado
  * País menos poblado
* Superficie:

  * Total
  * Promedio
  * País con mayor superficie
  * País con menor superficie
* Cantidad de países por continente

---

### 7. Salir

Finaliza la ejecución del programa.

---

## Instrucciones de uso

1. Ejecutar el programa principal.
2. Seleccionar una opción del menú.
3. Ingresar los datos solicitados.
4. Seguir las validaciones indicadas por el sistema.
5. Utilizar la opción 7 para salir del programa.

---

## Ejemplos de uso

### Ejemplo 1: Agregar país

```id="39nc7l"
Ingrese la cantidad de paises a cargar: 1
Ingrese el nombre del país: Argentina
Ingrese población: 45000000
Ingrese superficie (km2): 2780400
Ingrese el continente: 2
```

Salida:

```id="wcxksl"
¡Argentina preparado para guardar!
¡Todos los países se han guardado correctamente!
```

---

### Ejemplo 2: Buscar país

```id="6vzv9q"
Ingrese el nombre del país: Argen
```

Salida:

```id="y2vn6y"
Pais: Argentina | Poblacion: 45000000 | Superficie: 2780400 | Continente: America del Sur
```

---

### Ejemplo 3: Filtro por población

```id="gqg930"
Ingrese población mínima: 1000000
Ingrese población máxima: 50000000
```

---

## Estructura del archivo CSV

El archivo `paises.csv` contiene las siguientes columnas:

* Pais
* Poblacion
* Superficie
* Continente

---

## Integrantes del proyecto

* Integrante 1: Gaston 
* Integrante 2: Santiago

Nota:
Las funcionalidades de:

* Agregar paises
* actualizar poblacion y superficie
* filtrar paises

fueron desarrolladas principalmente por el primer integrante.

Las funcionalidades de:

* Ordenar países
* Mostrar estadísticas
* buscar paises

fueron desarrolladas principalmente por el segundo integrante.

a lo largo del codigo hubo una participacion activa de ambos ya sea en la correccion de codigo y la creacion del mismo

---

## Consideraciones

* El programa utiliza manejo de errores para evitar datos inválidos.
* Se permite cancelar operaciones ante múltiples errores.
* Se trabaja con listas de diccionarios para manejar los datos en memoria.
* El archivo CSV se actualiza automáticamente tras cada modificación.

---

## Tecnologías utilizadas

* Python
* Módulo `csv`
* Estructuras de datos (listas y diccionarios)

---

## Estado del proyecto

Funcional y completo
Validaciones implementadas
Persistencia de datos en CSV

---

Link De Demostracion: https://youtu.be/81lU6jj7y_w




