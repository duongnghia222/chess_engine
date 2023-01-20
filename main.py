import pygame
import chess_engine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = WIDTH // DIMENSION
MAX_FPS = 15
IMAGES = {}


def load_images():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bP',
              'wR', 'wN', 'wB', 'wQ', 'wK', 'wP']
    for p in pieces:
        IMAGES[p] = pygame.transform.scale(
            pygame.image.load("images/" + p + ".png"),
            (SQ_SIZE, SQ_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    gs = chess_engine.GameState()
    load_images()
    running = True
    selected_square = ()
    player_action = []
    valid_moves = gs.get_valid_moves()
    made_move = False
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z:
                    gs.undo_move()
                    made_move = True
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col, row = [pos[0] // SQ_SIZE, pos[1] // SQ_SIZE]
                if selected_square == (row, col):
                    player_action = []
                    selected_square = ()
                else:
                    selected_square = (row, col)
                    player_action.append(selected_square)
                if len(player_action) == 2:
                    move = chess_engine.Move(player_action[0], player_action[1], gs.board)
                    print(move.get_chess_notation())
                    if move in valid_moves:
                        gs.make_move(move)
                        made_move = True
                    selected_square = ()
                    player_action = []
        if made_move:
            valid_moves = gs.get_valid_moves()
            print(valid_moves)
            made_move = False
        clock.tick(MAX_FPS)
        pygame.display.flip()
        draw_game_state(screen, gs)


def draw_board(screen):
    colors = [pygame.Color("white"), pygame.Color('grey')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


if __name__ == "__main__":
    main()
