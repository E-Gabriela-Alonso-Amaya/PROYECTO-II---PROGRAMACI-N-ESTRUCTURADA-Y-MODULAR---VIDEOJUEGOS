"""
Proyecto: Análisis de Ventas de Videojuegos
Jesús González Lechuga
Rubén Córdoba Gallego
Eliana Gabriela Alonso Amaya
"""

import json
import os


def LeerDatosVentas():
    """
    Lee el fichero ventas_videojuegos.json y devuelve una lista de diccionarios.
    Maneja errores de archivo no encontrado o JSON incorrecto.
    """
    if not os.path.exists("ventas_videojuegos.json"):
        print("Error: El archivo ventas_videojuegos.json no existe.")
        return []

    try:
        with open("ventas_videojuegos.json", "r", encoding="utf-8") as f:
            datos = json.load(f)
            return datos.get("videojuegos", [])
    except json.JSONDecodeError:
        print("Error: El archivo JSON está mal formado.")
        return []


def CalcularVentasTotales(datos):
    """
    Calcula las ventas totales por región.
    """
    totales = {"na": 0, "eu": 0, "jp": 0, "otros": 0, "global": 0}

    for juego in datos:
        totales["na"] += juego.get("ventas_na", 0)
        totales["eu"] += juego.get("ventas_eu", 0)
        totales["jp"] += juego.get("ventas_jp", 0)
        totales["otros"] += juego.get("ventas_otros", 0)
        totales["global"] += juego.get("ventas_global", 0)

    return totales


def TopVentasPorRegion(datos, region, n=5):
    """
    Devuelve los n videojuegos más vendidos en una región.
    """
    clave = f"ventas_{region}" if region != "global" else "ventas_global"
    ranking = []

    for juego in datos:
        ranking.append((juego.get("nombre", "Desconocido"), juego.get(clave, 0)))

    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking[:n]


def AnalizarPorGenero(datos):
    """
    Analiza ventas agrupadas por género.
    """
    generos = {}

    for juego in datos:
        genero = juego.get("genero", "Desconocido")

        if genero not in generos:
            generos[genero] = {
                "cantidad_juegos": 0,
                "ventas_global": 0,
                "ventas_na": 0,
                "ventas_eu": 0,
                "ventas_jp": 0
            }

        generos[genero]["cantidad_juegos"] += 1
        generos[genero]["ventas_global"] += juego.get("ventas_global", 0)
        generos[genero]["ventas_na"] += juego.get("ventas_na", 0)
        generos[genero]["ventas_eu"] += juego.get("ventas_eu", 0)
        generos[genero]["ventas_jp"] += juego.get("ventas_jp", 0)

    return generos


def CalcularVentasPromedioPorPlataforma(datos):
    """
    Calcula el promedio de ventas globales por plataforma.
    """
    plataformas = {}

    for juego in datos:
        plat = juego.get("plataforma", "Desconocida")
        if plat not in plataformas:
            plataformas[plat] = {"ventas": 0, "cantidad": 0}

        plataformas[plat]["ventas"] += juego.get("ventas_global", 0)
        plataformas[plat]["cantidad"] += 1

    promedios = {}
    for plat, info in plataformas.items():
        promedios[plat] = info["ventas"] / info["cantidad"]

    return promedios


def FiltrarPorRangoAnios(datos, anio_inicio, anio_fin):
    """
    Filtra videojuegos por rango de años.
    """
    return [
        juego for juego in datos
        if anio_inicio <= juego.get("anio", 0) <= anio_fin
    ]


def GenerarReporteCompleto(datos):
    """
    Genera un reporte completo por pantalla.
    """
    print("\n" + "=" * 60)
    print("REPORTE COMPLETO DE VENTAS DE VIDEOJUEGOS")
    print("=" * 60)

    print(f"Total de juegos analizados: {len(datos)}\n")

    totales = CalcularVentasTotales(datos)
    print("VENTAS TOTALES POR REGIÓN (millones)")
    for region, total in totales.items():
        print(f"  {region.upper():<7}: {total:.2f}")

    print("\nTOP 5 POR REGIÓN")
    for region in ["na", "eu", "jp", "otros", "global"]:
        print(f"\n Región {region.upper()}:")
        for nombre, ventas in TopVentasPorRegion(datos, region):
            print(f"   {nombre:<30} {ventas:.2f}")

    print("\nANÁLISIS POR GÉNERO")
    generos = AnalizarPorGenero(datos)
    for genero, info in generos.items():
        print(f"\n {genero}")
        print(f"   Juegos: {info['cantidad_juegos']}")
        print(f"   Ventas Globales: {info['ventas_global']:.2f}")

    print("\nVENTAS PROMEDIO POR PLATAFORMA")
    promedios = CalcularVentasPromedioPorPlataforma(datos)
    for plat, promedio in sorted(promedios.items(), key=lambda x: x[1], reverse=True):
        print(f"  {plat:<10}: {promedio:.2f}")

    anios = [juego.get("anio", 0) for juego in datos]
    if anios:
        print(f"\nRango temporal: {min(anios)} - {max(anios)}")

    print("=" * 60)


def main():
    """
    Menú principal del programa.
    """
    datos = LeerDatosVentas()

    if not datos:
        return

    while True:
        print("""
MENÚ PRINCIPAL
1. Ver reporte completo
2. Top ventas por región
3. Filtrar por rango de años
4. Salir
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            GenerarReporteCompleto(datos)
        elif opcion == "2":
            region = input("Región (na, eu, jp, otros, global): ")
            top = TopVentasPorRegion(datos, region)
            for nombre, ventas in top:
                print(f"{nombre:<30} {ventas:.2f}")
        elif opcion == "3":
            inicio = int(input("Año inicio: "))
            fin = int(input("Año fin: "))
            filtrados = FiltrarPorRangoAnios(datos, inicio, fin)
            print(f"Juegos encontrados: {len(filtrados)}")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
