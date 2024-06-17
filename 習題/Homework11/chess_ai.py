class Chess:
    def __init__(self):
        self.grid = [['' for _ in range(8)] for _ in range(8)]
        self.move_history = []
        self.setup_board()

    def setup_board(self):
        # Initialize some pieces on the board
        self.grid[1][0] = 'b_pawn'
        self.grid[1][1] = 'b_pawn'
        self.grid[0][0] = 'b_rook'
        self.grid[6][0] = 'w_pawn'
        self.grid[6][1] = 'w_pawn'
        self.grid[7][0] = 'w_rook'

    def move(self, fromX, fromY, toX, toY):
        if 0 <= toX < 8 and 0 <= toY < 8:
            piece = self.grid[fromX][fromY]
            self.grid[fromX][fromY] = ''
            self.grid[toX][toY] = piece
            self.move_history.append((fromX, fromY, toX, toY, piece))
        else:
            raise ValueError("Move out of board boundaries")

    def undo(self):
        if self.move_history:
            fromX, fromY, toX, toY, piece = self.move_history.pop()
            self.grid[toX][toY] = ''
            self.grid[fromX][fromY] = piece

    def get_steps(self, x, y):
        steps = []
        potential_steps = [{'x': x+1, 'y': y}, {'x': x, 'y': y+1}]
        for step in potential_steps:
            if 0 <= step['x'] < 8 and 0 <= step['y'] < 8:
                steps.append(step)
        return steps

class ChessAI:
    def __init__(self, chess):
        self.chess = chess

    def AI(self):
        result = self.minimax(4, 'b', -float('inf'), float('inf'))
        if result['fromX'] is not None and result['fromY'] is not None:
            self.chess.move(result['fromX'], result['fromY'], result['toX'], result['toY'])
            print(f"AI moved from ({result['fromX']}, {result['fromY']}) to ({result['toX']}, {result['toY']})")

    def minimax(self, depth, turn, alpha, beta):
        best_move = {
            'fromX': None,
            'fromY': None,
            'toX': None,
            'toY': None,
            'score': -float('inf') if turn == 'b' else float('inf')
        }

        for x in range(8):
            for y in range(8):
                steps = self.chess.get_steps(x, y)
                for pos in steps:
                    self.chess.move(x, y, pos['x'], pos['y'])

                    if depth > 0:
                        score = self.minimax(depth - 1, 'w' if turn == 'b' else 'b', alpha, beta)['score']
                    else:
                        score = self.evaluation(self.chess.grid)

                    self.chess.undo()

                    if turn == 'b' and score > best_move['score']:
                        best_move.update({'fromX': x, 'fromY': y, 'toX': pos['x'], 'toY': pos['y'], 'score': score})
                        alpha = max(alpha, best_move['score'])

                    if turn == 'w' and score < best_move['score']:
                        best_move.update({'fromX': x, 'fromY': y, 'toX': pos['x'], 'toY': pos['y'], 'score': score})
                        beta = min(beta, best_move['score'])

                    if alpha >= beta:
                        break

        return best_move

    def evaluation(self, grid):
        points = 0
        for row in grid:
            for piece in row:
                if piece:
                    points += self.get_piece_value(piece)
        return points

    def get_piece_value(self, piece):
        piece_values = {
            'b_pawn': 10, 'b_knight': 30, 'b_bishop': 30,
            'b_rook': 50, 'b_queen': 300, 'b_king': 1000,
            'w_pawn': -10, 'w_knight': -30, 'w_bishop': -30,
            'w_rook': -50, 'w_queen': -300, 'w_king': -1000
        }
        return piece_values.get(piece, 0)

# 创建 Chess 类的实例
chess = Chess()

# 创建 ChessAI 类的实例，并传入 chess 物件
chess_ai = ChessAI(chess)

# 使用 AI 方法选择并执行最佳移动
chess_ai.AI()
