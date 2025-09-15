def calcular_puntaje(stats):
    innovacion = 3
    presentacion = 1
    puntos = innovacion * stats['innovacion'] + presentacion * stats['presentacion']
    if stats['errores_graves']:
     puntos = puntos - 1
    return puntos

def mejor_equipo_de_ronda(ronda):
    puntajes = {} #diccionario vacio
    for equipo, stats in ronda.items():
        puntuacion = calcular_puntaje(stats)
        puntajes[equipo] = puntuacion
    
