# PROYECTO II - ANÁLISIS DE VIDEOJUEGOS
El programa tiene como objetivo analizar un conjunto de datos de ventas de videojuegos almacenados en el archivo ventas_videojuegos.json y mostrar distintos informes. 
Se pueden realizar distintos informes se incluyen las ventas totales por región, los videojuegos más vendidos, el análisis por género, el promedio de ventas por plataforma y el filtrado de juegos por rango de años.
Para llevarlo a cabo, el programa se estructura en varias funciones que trabajan de manera conjunta:

- La función LeerDatosVentas se encarga de leer el archivo ventas_videojuegos.json y devolver su contenido en forma de una lista de diccionarios, donde cada diccionario representa un videojuego. Además, gestiona posibles errores como la ausencia del archivo o un formato JSON incorrecto.
- La función CalcularVentasTotales recibe la lista de videojuegos y calcula las ventas totales por región (Norteamérica, Europa, Japón, Otros) y las ventas globales.
- La función TopVentasPorRegion recibe la lista de videojuegos, una región concreta y un número n, y devuelve los n videojuegos más vendidos en dicha región ordenados de mayor a menor.
- La función AnalizarPorGenero agrupa los videojuegos por género y calcula para cada uno el número total de juegos y las ventas acumuladas por región y a nivel global.
- La función CalcularVentasPromedioPorPlataforma calcula el promedio de ventas globales de los videojuegos para cada plataforma disponible.
- La función FiltrarPorRangoAnios permite filtrar los videojuegos según un rango de años indicado por el usuario.
- La función GenerarReporteCompleto utiliza todas las funciones anteriores para generar un informe detallado por pantalla que resume los principales resultados del análisis.
- La función main actúa como menú principal del programa, permitiendo al usuario interactuar con el sistema y elegir qué tipo de análisis desea realizar.

Reparto de tareas:
LeerDatosVentas() – Rubén
CalcularVentasTotales() – Jesús
TopVentasPorRegion() – Eliana
AnalizarPorGenero() – Rubén
CalcularVentasPromedioPorPlataforma() – Jesús
FiltrarPorRangoAnios() – Eliana
GenerarReporteCompleto() – Rubén y Jesús
main() y menú principal – Todo el grupo
