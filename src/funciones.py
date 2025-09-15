def calcular_puntaje(stats):
    puntos = 3 * stats['innovacion'] + 1 * stats['presentacion']
 if stats['errores_graves']:
    puntos = puntos - 1
    return puntos
def mejor_equipo_de_ronda(ronda):
    puntajes = {} #diccionario vacio
    for equipo, stats in ronda.items():
        puntuacion = calcular_puntaje(stats)
        puntajes[equipo] = puntuacion
    
