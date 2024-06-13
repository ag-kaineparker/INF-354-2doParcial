import numpy as np
import random


# Definición del grafo y las distancias entre nodos
grafo = {
    ('A', 'B'): 7, ('A', 'C'): 9, ('A', 'D'): 8, ('A', 'E'): 20,
    ('B', 'C'): 10, ('B', 'E'): 11, ('B', 'D'): 4,
    ('C', 'D'): 15, ('C', 'E'): 5,
    ('D', 'E'): 17
}

nodos = ['A', 'B', 'C', 'D', 'E']

# Función para calcular la longitud de una ruta
def calcular_longitud_ruta(ruta):
    longitud = 0
    for i in range(len(ruta) - 1):
        origen, destino = ruta[i], ruta[i+1]
        if (origen, destino) in grafo:
            longitud += grafo[(origen, destino)]
        elif (destino, origen) in grafo:
            longitud += grafo[(destino, origen)]
        else:
            raise ValueError(f"No se encontró la conexión entre {origen} y {destino} en el grafo.")
    return longitud

# Función para generar una población inicial aleatoria
def generar_poblacion_inicial(tamano_poblacion, nodos):
    poblacion = []
    for _ in range(tamano_poblacion):
        ruta = ['A'] + list(np.random.permutation([n for n in nodos if n != 'A']))
        poblacion.append(ruta)
    return poblacion



# Función de selección de padres por torneo

def seleccion_padres_torneo(poblacion, k):
    padres = []
    for _ in range(len(poblacion)):
        torneo = random.sample(poblacion, k)
        mejor_padre = min(torneo, key=lambda ruta: calcular_longitud_ruta(ruta))
        padres.append(mejor_padre)
    return padres

# Función de cruce de dos padres para generar un hijo
def cruzar_padres(padre1, padre2):
    punto_cruce = np.random.randint(1, len(padre1) - 1)
    hijo = padre1[:punto_cruce] + [nodo for nodo in padre2 if nodo not in padre1[:punto_cruce]]
    return hijo

# Función de mutación de una ruta
def mutar_ruta(ruta):
    idx1, idx2 = np.random.choice(range(1, len(ruta) - 1), 2, replace=False)  # Excluir el nodo A
    ruta[idx1], ruta[idx2] = ruta[idx2], ruta[idx1]
    return ruta

# Algoritmo genético para encontrar la ruta más corta
def algoritmo_genetico(num_generaciones, tamano_poblacion, k_torneo):
    poblacion = generar_poblacion_inicial(tamano_poblacion, nodos)
    
    for _ in range(num_generaciones):
        padres = seleccion_padres_torneo(poblacion, k_torneo)
        descendencia = []
        
        for i in range(0,len(padres), 2):
            hijo1 = cruzar_padres(padres[i], padres[i+1])
            hijo2 = cruzar_padres(padres[i+1], padres[i])
            
            if np.random.rand() < tasa_mutacion:
                hijo1 = mutar_ruta(hijo1)
                hijo2 = mutar_ruta(hijo2)
            
            descendencia.append(hijo1)
            descendencia.append(hijo2)
        
        poblacion = descendencia
    
    mejor_ruta = min(poblacion, key=lambda ruta: calcular_longitud_ruta(ruta))
    mejor_longitud = calcular_longitud_ruta(mejor_ruta)
    
    return mejor_ruta, mejor_longitud

# Parámetros del algoritmo genético
num_generaciones = 1000
tamano_poblacion = 50
k_torneo = 3
tasa_mutacion = 0.1

# Ejecutar el algoritmo genético
mejor_ruta, mejor_longitud = algoritmo_genetico(num_generaciones, tamano_poblacion, k_torneo)

# Resultados
print("Mejor Ruta:", mejor_ruta)
print("Longitud de la Ruta:", mejor_longitud)

