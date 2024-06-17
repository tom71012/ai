import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
SQ_SIZE = HEIGHT // 8
FPS = 60

# Colors
LIGHT_COLOR = (240, 217, 181)
DARK_COLOR = (181, 136, 99)

# Define constants for piece types
EMPTY = 'empty'
PAWN = 'pawn'
KNIGHT = 'knight'
BISHOP = 'bishop'
ROOK = 'rook'
QUEEN = 'queen'
KING = 'king'

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess AI with pygame')

# Sample chess grid representation (initial state)
# 'b_' prefix for black pieces, 'w_' prefix for white pieces
chess_grid = [
    ['b_rook', 'b_knight', 'b_bishop', 'b_queen', 'b_king', 'b_bishop', 'b_knight', 'b_rook'],
    ['b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn'],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    ['w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn'],
    ['w_rook', 'w_knight', 'w_bishop', 'w_queen', 'w_king', 'w_bishop', 'w_knight', 'w_rook']
]

# Load images
pieces_images = {
    'b_pawn': pygame.image.load('images/b_pawn.png'),
    'b_knight': pygame.image.load('images/b_knight.png'),
    'b_bishop': pygame.image.load('images/b_bishop.png'),
    'b_rook': pygame.image.load('images/b_rook.png'),
    'b_queen': pygame.image.load('images/b_queen.png'),
    'b_king': pygame.image.load('images/b_king.png'),
    'w_pawn': pygame.image.load('images/w_pawn.png'),
    'w_knight': pygame.image.load('images/w_knight.png'),
    'w_bishop': pygame.image.load('images/w_bishop.png'),
    'w_rook': pygame.image.load('images/w_rook.png'),
    'w_queen': pygame.image.load('images/w_queen.png'),
    'w_king': pygame.image.load('images/w_king.png'),
    'empty': pygame.Surface((SQ_SIZE, SQ_SIZE))  # Placeholder for empty square
}

# Resize images to fit the square size
for piece, image in pieces_images.items():
    pieces_images[piece] = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))

# Function to draw the chess board
def draw_board(screen):
    colors = [LIGHT_COLOR, DARK_COLOR]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Function to draw pieces on the board
def draw_pieces(screen, chess_grid):
    for row in range(8):
        for col in range(8):
            piece = chess_grid[row][col]
            if piece != EMPTY:
                screen.blit(pieces_images[piece], pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Function to move a piece on the chess board
def move_piece(from_x, from_y, to_x, to_y):
    piece = chess_grid[from_x][from_y]
    if is_valid_move(from_x, from_y, to_x, to_y):
        chess_grid[to_x][to_y] = piece
        chess_grid[from_x][from_y] = EMPTY
        return True
    else:
        return False

# Function to check if a move is valid
def is_valid_move(from_x, from_y, to_x, to_y):
    # Implement your validation logic here
    # For simplicity, assume all moves are valid for now
    return True

# Function to run the AI using minimax algorithm
def run_ai(depth, turn):
    best_move = minimax(depth, turn)
    move_piece(best_move['fromX'], best_move['fromY'], best_move['toX'], best_move['toY'])

# Minimax algorithm
def minimax(depth, turn):
    best_score = float('-inf') if turn == 'b' else float('inf')
    best_move = {}

    for x in range(8):
        for y in range(8):
            if chess_grid[x][y].startswith(turn):
                for to_x in range(8):
                    for to_y in range(8):
                        if move_piece(x, y, to_x, to_y):
                            score = evaluation(chess_grid)
                            if (turn == 'b' and score > best_score) or (turn == 'w' and score < best_score):
                                best_score = score
                                best_move = {'fromX': x, 'fromY': y, 'toX': to_x, 'toY': to_y}
                            # Undo the move for next iteration
                            chess_grid[x][y] = chess_grid[to_x][to_y]
                            chess_grid[to_x][to_y] = EMPTY

    return best_move

# Evaluation function (basic material count)
def evaluation(grid):
    points = 0
    for row in range(8):
        for col in range(8):
            piece = grid[row][col]
            if piece == 'b_pawn':
                points += 10
            elif piece == 'b_knight' or piece == 'b_bishop':
                points += 30
            elif piece == 'b_rook':
                points += 50
            elif piece == 'b_queen':
                points += 300
            elif piece == 'b_king':
                points += 1000
            elif piece == 'w_pawn':
                points -= 10
            elif piece == 'w_knight' or piece == 'w_bishop':
                points -= 30
            elif piece == 'w_rook':
                points -= 50
            elif piece == 'w_queen':
                points -= 300
            elif piece == 'w_king':
                points -= 1000

    return points

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True
    turn = 'w'  # Start with white's turn

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turn == 'w':
                    # Human player's turn (for example, click to move)
                    mouse_pos = pygame.mouse.get_pos()
                    from_x, from_y = mouse_pos[1] // SQ_SIZE, mouse_pos[0] // SQ_SIZE
                    print(f"Selected position: {from_x}, {from_y}")
                    # Implement your mouse click handling to select and move pieces
                else:
                    # AI's turn (run AI to make a move)
                    run_ai(depth=3, turn='b')  # Example: depth 3 for AI search
                    turn = 'w'  # After AI move, switch turn back to human

        screen.fill((0, 0, 0))
        draw_board(screen)
        draw_pieces(screen, chess_grid)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
