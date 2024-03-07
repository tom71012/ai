class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # 檢查給定的顏色是否可以分配給v
    def is_safe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # 在圖上使用回溯法來著色
    def graph_colouring_util(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, colour, c):
                colour[v] = c
                if self.graph_colouring_util(m, colour, v + 1):
                    return True
                colour[v] = 0

    # 主函數來求解圖著色問題
    def graph_colouring(self, m):
        colour = [0] * self.V
        if not self.graph_colouring_util(m, colour, 0):
            print("無法著色")
            return False

        print("可以著色:")
        for c in colour:
            print(c, end=" ")
        return True

# 範例圖
g = Graph(4)
g.graph = [[0, 1, 1, 1],
           [1, 0, 1, 0],
           [1, 1, 0, 1],
           [1, 0, 1, 0]]

'''g = Graph(7)
g.graph =[[0, 1, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 1, 1],
          [0, 0, 1, 0, 1, 0, 0],
          [0, 0, 0, 0, 1, 0, 0]]'''


m = 3  # 可用的顏色數量
g.graph_colouring(m)
