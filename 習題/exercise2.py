import random
import numpy as np

# 定義城市的數量和每對城市之間的距離矩陣
num_cities = 5
distances = np.array([
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 10],
    [20, 25, 30, 0, 5],
    [25, 30, 10, 5, 0]
])

# 產生初始解（隨機城市順序）
def generate_initial_solution():
    return random.sample(range(num_cities), num_cities)

# 計算路徑的總距離
def calculate_distance(path):
    total_distance = 0
    for i in range(num_cities - 1):
        total_distance += distances[path[i]][path[i+1]]
    total_distance += distances[path[-1]][path[0]]  # 回到起始城市
    return total_distance

# 交換兩個城市的位置
def swap_cities(solution, idx1, idx2):
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]

# 爬山演算法求解 TSP
def hill_climbing(max_iterations):
    current_solution = generate_initial_solution()
    current_distance = calculate_distance(current_solution)

    for _ in range(max_iterations):
        next_solution = current_solution.copy()
        idx1, idx2 = random.sample(range(num_cities), 2)
        swap_cities(next_solution, idx1, idx2)
        next_distance = calculate_distance(next_solution)

        if next_distance < current_distance:
            current_solution = next_solution
            current_distance = next_distance

    return current_solution, current_distance

if __name__ == "__main__":
    max_iterations = 1000
    best_solution, best_distance = hill_climbing(max_iterations)
    print("Best path:", best_solution)
    print("Best distance:", best_distance)
