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
    gs = chess_engine.game_state()
    load_images()
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
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
