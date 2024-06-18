## 參考ChatGPT
這段程式碼實現了使用爬山演算法（Hill Climbing Algorithm）來解決旅行推銷員問題（TSP）。

### 1. 定義城市數量和距離矩陣
```python
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
```
- **功能**：設置城市的數量（`num_cities`）為5，並定義一個5x5的距離矩陣（`distances`），其中每個元素表示兩個城市之間的距離。

### 2. 產生初始解（隨機城市順序）
```python
# 產生初始解（隨機城市順序）
def generate_initial_solution():
    return random.sample(range(num_cities), num_cities)
```
- **功能**：生成一個隨機的城市順序作為初始解。使用`random.sample`從`0`到`num_cities-1`中隨機選取不重複的數字。

### 3. 計算路徑的總距離
```python
# 計算路徑的總距離
def calculate_distance(path):
    total_distance = 0
    for i in range(num_cities - 1):
        total_distance += distances[path[i]][path[i+1]]
    total_distance += distances[path[-1]][path[0]]  # 回到起始城市
    return total_distance
```
- **功能**：計算給定路徑的總距離。遍歷路徑上的每對相鄰城市，累加他們之間的距離，最後加上回到起始城市的距離。

### 4. 交換兩個城市的位置
```python
# 交換兩個城市的位置
def swap_cities(solution, idx1, idx2):
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
```
- **功能**：交換路徑中兩個城市的位置，用於產生鄰域解。

### 5. 爬山演算法求解 TSP
```python
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
```
- **功能**：實現爬山演算法來求解TSP。
  - `current_solution`：生成初始解。
  - `current_distance`：計算初始解的總距離。
  - **迴圈（`for _ in range(max_iterations)`）**：
    - 隨機選擇兩個城市，交換他們的位置來生成新解。
    - 計算新解的總距離。
    - 如果新解的總距離小於當前解的總距離，則更新當前解和距離。
  - 返回最優解和對應的最小距離。

### 6. 主程式執行
```python
if __name__ == "__main__":
    max_iterations = 1000
    best_solution, best_distance = hill_climbing(max_iterations)
    print("Best path:", best_solution)
    print("Best distance:", best_distance)
```
- **功能**：設定最大迭代次數為1000，調用`hill_climbing`函式求解TSP，並打印最優路徑和最小距離。

### 總結
這段程式碼利用爬山演算法來求解TSP。主要步驟包括生成初始解、計算路徑總距離、交換城市位置以生成鄰域解，並在迭代過程中不斷更新最優解。最終，返回並打印最優路徑及其距離。
