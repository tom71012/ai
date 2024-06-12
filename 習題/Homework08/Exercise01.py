import gymnasium as gym

# 初始化 Cart Pole 環境
env = gym.make("CartPole-v1", render_mode="human")

# 重置環境並獲取初始觀察
observation, info = env.reset(seed=42)
score = 0

# 開始執行策略
for _ in range(1000):
    # 顯示環境
    env.render()

    # 根據竿子傾斜的方向選擇動作
    if observation[2] < 0:  # 竿子向左傾斜
        action = 0  # 向左推動小車
    else:
        action = 1  # 向右推動小車

    # 執行動作並獲取相應的回饋
    observation, reward, terminated, truncated, info = env.step(action)
    score += reward

    # 如果遊戲結束，重置環境
    if terminated or truncated:
        observation, info = env.reset()
        print('done, score=', score)
        score = 0

# 關閉環境
env.close()
