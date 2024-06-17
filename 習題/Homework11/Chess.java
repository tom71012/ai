function AI () {
    var result = minimax(4, 'b');
    chess.move(result.fromX, result.fromY, result.toX, result.toY);
}

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

function evaluation (grid) {
    var points = 0;
    for (var x = 0; x < 8; x++) {
        for (var y = 0; y < 8; y++) {
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


