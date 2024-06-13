import numpy as np

# TwoOpt crea una vecindad basada en el operador two-opt de forma determinista
# Todas las permutaciones que se pueden obtener con two-opt están en la vecindad
def TwoOpt(perm):
    n = perm.shape[0]
    n_neighbors = int(n * (n - 1) / 2 - n)  # Convertir a entero
    neighbors = np.zeros((n_neighbors, n))  # Guardaremos todos los vecinos en neighbors
    ind = 0
    for i in range(n - 1):
        for j in range(i + 2, n):  # Las posiciones a elegir para el two-opt no deben ser consecutivas
            if not (i == 0 and j == n - 1):  # Las posiciones no deben ser primera y última (son circularmente consecutivas)
                neighbors[ind, :] = perm
                aux = perm[i:j + 1].copy()
                neighbors[ind, i:j + 1] = aux[::-1]  # Se invierte el camino entre posiciones elegidas
                ind = ind + 1
    return neighbors

# Swap crea una vecindad basada en el operador de intercambio entre posiciones
# Todas las permutaciones que se pueden obtener como un swap entre la primera posición
# y cualquiera de las restantes están en la vecindad
def Swap(perm):
    n = perm.shape[0]
    n_neighbors = n - 1  # Número de vecinos
    neighbors = np.zeros((n_neighbors, n))  # Guardaremos todos los vecinos en neighbors
    ind = 0
    for i in range(1, n):
        neighbors[ind, :] = perm
        neighbors[ind, i] = perm[0]
        neighbors[ind, 0] = perm[i]
        ind = ind + 1
    return neighbors

# Complement crea una vecindad basada en el operador de complemento entre posiciones
# en la cual cada valor i en la permutación es sustituido por el valor (n-i) excepto para i=n,
# que permanece igual
# Cada permutación tiene un único vecino
def Complement(perm):
    n = perm.shape[0]
    n_neighbors = 1  # Número de vecinos
    neighbors = np.zeros((n_neighbors, n))  # Guardaremos todos los vecinos en neighbors
    pos_n = np.where(perm == n)
    neighbors[0, :] = (n - perm)  # Se sustituye por el complemento
    neighbors[0, pos_n] = n  # Se mantiene el valor de n igual
    return neighbors

# Decrease crea una vecindad basada en obtener una nueva solución restando un valor "v" a cada posición
# y crear una solución vecina por cada valor de v en (1,...,n-1). Cuando la resta da valor cero, se pasa
# a n
# Ej: permutacion original: 5 3 4 2 1:
# permutaciones vecinas: (4 2 3 1 5),(3,1,2,5,4),(2,5,1,4,3),(1,4,5,3,2)
def Decrease(perm):
    n = perm.shape[0]
    n_neighbors = n - 1  # Número de vecinos
    neighbors = np.zeros((n_neighbors, n))  # Guardaremos todos los vecinos en neighbors
    auxperm = perm.copy()
    for i in range(n - 1):
        auxperm = auxperm - 1
        pos_0 = np.where(auxperm == 0)
        auxperm[pos_0] = n
        neighbors[i, :] = auxperm
    return neighbors

n = 6
perm = np.random.permutation(n) + 1
print("Permutación original:", perm)
neighbors1 = TwoOpt(perm)
neighbors2 = Swap(perm)
neighbors3 = Complement(perm)
neighbors4 = Decrease(perm)

print("Vecinos generados por TwoOpt:\n", neighbors1)
print("Vecinos generados por Swap:\n", neighbors2)
print("Vecinos generados por Complement:\n", neighbors3)
print("Vecinos generados por Decrease:\n", neighbors4)
