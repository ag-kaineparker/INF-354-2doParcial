import numpy as np
import math

def create_initial_solution(n):
    return np.random.permutation(n)

def calculate_distance(matrix, solution):
    return sum([matrix[solution[i-1], solution[i]] for i in range(len(solution))])

def generate_neighbor(solution):
    i, j = np.random.randint(0, len(solution), size=2)
    if i > j:
        i, j = j, i
    new_solution = solution.copy()
    new_solution[i:j+1] = new_solution[i:j+1][::-1]  # Two-opt move
    return new_solution

def simulated_annealing(distance_matrix, initial_temp, cooling_rate, stopping_temp, stopping_iter):
    current_solution = create_initial_solution(len(distance_matrix))
    current_cost = calculate_distance(distance_matrix, current_solution)
    best_solution = current_solution.copy()
    best_cost = current_cost

    print(f"Solución inicial: {current_solution}, Costo inicial: {current_cost}")

    temperature = initial_temp
    iter = 0

    while temperature > stopping_temp and iter < stopping_iter:
        candidate_solution = generate_neighbor(current_solution)
        candidate_cost = calculate_distance(distance_matrix, candidate_solution)

        acceptance_probability = np.exp((current_cost - candidate_cost) / temperature)
        if candidate_cost < current_cost or np.random.rand() < acceptance_probability:
            current_solution = candidate_solution
            current_cost = candidate_cost

        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
            print(f"Iteración {iter}: ¡Nueva mejor solución!: {best_solution} con costo: {best_cost}")

        temperature *= cooling_rate
        iter += 1

        if iter % 100 == 0:
            print(f"Iteración {iter}: Temperatura: {temperature}, Mejor costo actual: {best_cost}")

    return best_solution, best_cost

# Ejemplo de matriz de distancias entre ciudades (simétrica)
distance_matrix = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])

# Parámetros de Simulated Annealing
initial_temp = 1000
cooling_rate = 0.995
stopping_temp = 1e-3
stopping_iter = 1000

best_solution, best_cost = simulated_annealing(distance_matrix, initial_temp, cooling_rate, stopping_temp, stopping_iter)
print("Mejor solución:", best_solution)
print("Costo de la mejor solución:", best_cost)
