// 點擊「run AI」時會執行此函式
// 如果有啟用 enable AI 每次點擊棋盤下棋後，也會自動執行此函式
function AI(game, depth) {
    var startTime = Date.now()
    var result = alphabeta(game.clone(), depth, -Infinity, Infinity)
    game.place(result.x, result.y)
    console.log(`depth: ${depth} cost: ${Date.now() - startTime}ms`)
}


function alphabeta(game, depth, alpha, beta) {
    
    // 紀錄目前找到最佳的策略下法以及棋分數
    var best = {
        x: undefined,
        y: undefined,
        score: game.turn === 'w' ? -Infinity: Infinity
    }

    for (var x = 0; x < 8; x++) {
        for (var y = 0; y < 8; y++) {
            if (game.place(x, y)) {

                if (depth > 1) {
                    var score = alphabeta(game, depth - 1, alpha, beta).score
                } else {
                    var score = evaluation(game.grid)
                }

                if (game.turn === 'b' && score > best.score) {
                    best.x = x
                    best.y = y
                    alpha = best.score = score
                }
                if (game.turn === 'w' && score < best.score) {
                    best.x = x
                    best.y = y
                    beta = best.score = score
                }
                game.undo()
                
                // 剪枝
                if (alpha > beta) return best
            }
        }
    }

    if (best.x === undefined) {
        best.score = evaluation(game.grid)
    }

    return best
}

// 評估函式
function evaluation(grid) {
    var score = 0
    for (var x = 0; x < 8; x++) {
        for (var y = 0; y < 8; y++) {
            var i = 1
            if (x === 0 || x === 7) i *= 10
            if (y === 0 || y === 7) i *= 10
            if (x === 1 || y === 1 || x === 6 || y === 6) i *= -1
            if (grid[y][x] === 'w') score += i
            if (grid[y][x] === 'b') score -= i
        }
    }
    return score
}

