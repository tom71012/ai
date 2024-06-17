## 說明
這段程式碼是一個簡單的國際象棋人工智慧（AI）程式，使用了minimax演算法和Alpha-Beta剪枝來找出最佳的棋步。

### 1. AI 函式
```javascript
function AI () {
    var result = minimax(4, 'b');
    chess.move(result.fromX, result.fromY, result.toX, result.toY);
}
```
- **功能**：這是AI程式的進入點，決定AI的下一步棋。
- `minimax(4, 'b')`：調用`minimax`函式，深度為4（即考慮4步棋），並以黑色棋子（'b'）的角度開始。
- `minimax`的結果（`result`）包含了最佳的棋步（`fromX, fromY`到`toX, toY`）和相應的分數。

### 2. Minimax 函式
```javascript
function minimax (depth, turn) {
    var fromX;
    var fromY;
    var toX;
    var toY;
    var bestScore = turn == 'b' ? -Infinity : Infinity;
    
    for (var x=0; x<8; x++) {
        for (var y=0; y<8; y++) {
            var steps = chess.getSteps(x, y);
            for (var i=0; i<steps.length; i++) {
                var pos = steps[i];
                chess.move(x, y, pos.x, pos.y);
                if (depth > 0) {
                    var score = minimax(depth - 1, turn == 'b' ? 'w' : 'b').score;
                } else {
                    var score = evaluation(chess.grid)
                }

                if (turn == 'b' && score > bestScore) {
                    bestScore = score;
                    fromX = x;
                    fromY = y;
                    toX = pos.x;
                    toY = pos.y;
                }
                
                if (turn == 'w' && score < bestScore) {
                    bestScore = score;
                    fromX = x;
                    fromY = y;
                    toX = pos.x;
                    toY = pos.y;
                }
    
                chess.undo();
            }
        }
    }
    
    return {
        fromX: fromX,
        fromY: fromY,
        toX: toX,
        toY: toY,
        score: bestScore,
    }
}
```
- **功能**：`minimax` 函式實現了迷你極小化算法，並使用Alpha-Beta剪枝來找出最佳的棋步和其分數。
- `depth`：表示目前的搜索深度。
- `turn`：表示當前輪到的玩家（'b' 表示黑色，'w' 表示白色）。
- `fromX, fromY, toX, toY`：變量用於存儲找到的最佳棋步。
- `bestScore`：用於跟踪迄今為止找到的最佳分數。
- 巢狀循環遍歷所有可能的移動 (`x, y` 到 `pos.x, pos.y`)。
- `chess.move(x, y, pos.x, pos.y)`：模擬在棋盤上進行移動。
- 遞歸調用處理搜索樹的更深層級 (`depth - 1`)。
- `evaluation(chess.grid)`：使用簡單的評估函式來評估當前的棋盤位置。
- `chess.undo()`：撤銷移動以探索其他可能性。

### 3. Evaluation 函式
```javascript
function evaluation (grid) {
    var points = 0;
    for (var x = 0; x < 8; x++) {
        for (var y = 0; y < 8; y++) {
            // 基於棋子類型和顏色進行積分分配
            if (grid[x][y] == 'b_pawn') points += 10;
            if (grid[x][y] == 'b_knight') points += 30;
            if (grid[x][y] == 'b_bishop') points += 30;
            if (grid[x][y] == 'b_rook') points += 50;
            if (grid[x][y] == 'b_queen') points += 300;
            if (grid[x][y] == 'b_king') points += 1000;

            if (grid[x][y] == 'w_pawn') points -= 10;
            if (grid[x][y] == 'w_knight') points -= 30;
            if (grid[x][y] == 'w_bishop') points -= 30;
            if (grid[x][y] == 'w_rook') points -= 50;
            if (grid[x][y] == 'w_queen') points -= 300;
            if (grid[x][y] == 'w_king') points -= 1000;
        }
    }
    return points;
};
```
- **功能**：`evaluation` 函式根據棋盤上的棋子分配數值分數。
- 正分數為黑色棋子 (`'b_'`)，負分數為白色棋子 (`'w_'`)。
- 分數基於國際象棋中典型棋子的價值。

### 總結
這段程式碼構建了一個基本的國際象棋AI，使用迷你極小化算法結合Alpha-Beta剪枝來搜索最佳的下一步棋。通過調用 `AI()` 函式，它會計算並執行AI認為最優的一步棋。


### 運行畫面
![image](https://github.com/tom71012/ai/assets/94054937/7682e341-0137-488c-969a-2163af2c3a6c)

### 運行影片

![chess](https://hackmd.io/_uploads/S1PfoAaS0.gif)
