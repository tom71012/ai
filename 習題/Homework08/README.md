## 參考ChatGPT並理解

1. **環境初始化**：
   ```
   env = gym.make("CartPole-v1", render_mode="human")
   ```
   - 碼使用 Gymnasium 庫來創建一個 Cart Pole 的環境，並將渲染模式設置為 "human"，以便在窗口中顯示環境。

2. **重置環境並獲取初始觀察**：
   ```
   observation, info = env.reset(seed=42)
   ```
   - 調用環境的 `reset` 方法來初始化環境並獲取初始觀察。`seed=42` 參數設置了隨機種子，以確保重現性。

3. **執行策略**：
   ```
   for _ in range(1000):
       env.render()
       if observation[2] < 0:
           action = 0
       else:
           action = 1
       observation, reward, terminated, truncated, info = env.step(action)
       score += reward
       if terminated or truncated:
           observation, info = env.reset()
           print('done, score=', score)
           score = 0
   ```
   - 在這個迴圈中，我們執行了 1000 個步驟。
   - `env.render()` 用於顯示環境，使我們可以在窗口中看到小車和竿子的位置。
   - 根據觀察中的竿子角度，我們選擇了要採取的動作。如果竿子向左傾斜，我們選擇向左推動小車（`action = 0`），否則我們選擇向右推動小車（`action = 1`）。
   - 使用選擇的動作來執行一步並獲取相應的回饋（reward）。
   - 如果遊戲結束（terminated）或者步驟被截斷（truncated），我們重置環境並打印出該輪的得分。

4. **關閉環境**：
   ```
   env.close()
   ```
   - 最後使用 `close()` 方法關閉環境，釋放相關資源。
