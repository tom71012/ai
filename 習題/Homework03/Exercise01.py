import scipy.optimize as opt

# 目標函數係數（我們要最大化 3x + 2y + 5z，所以在 linprog 中傳入 -3, -2, -5）
c = [-3, -2, -5]

# 不等式約束條件的左邊係數
A = [
    [1, 1, 0],   # x + y <= 10
    [2, 0, 1],   # 2x + z <= 9
    [0, 1, 2]    # y + 2z <= 11
]

# 不等式約束條件的右邊值
b = [10, 9, 11]

# 變數的邊界 (x >= 0, y >= 0, z >= 0)
x_bounds = (0, None)
y_bounds = (0, None)
z_bounds = (0, None)
bounds = [x_bounds, y_bounds, z_bounds]

# 使用 linprog 函數解決線性規劃問題
result = opt.linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# 輸出結果
if result.success:
    print("最佳解：")
    print(f"x = {result.x[0]}")
    print(f"y = {result.x[1]}")
    print(f"z = {result.x[2]}")
    print(f"最大值 = {-result.fun}")
else:
    print("無法找到最佳解")
