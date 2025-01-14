"""
This is the main file for the pygame project for the Programming 1 Lecture class (Fall 2024)

Contributors (add your name to this list if you haven't):

Gavin Conley


"""
import pygame

pygame.init()

resolution = (640, 480)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
running = True


# Setup 5x5 game board
EMPTY = 0
CROSS = 1
RING = 2

board = [[EMPTY] * 5] * 5


# Initially fill it all with 0 (empty spaces)
for i in range(5):
    for j in range(5):
        board[i][j] = 0

# Game's main loop
while running:

    # Go through pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()