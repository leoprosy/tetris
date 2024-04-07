import numpy as np
import pygame
from blocks import Block
from time import sleep

board = np.full((20,10), 0, dtype=object)
blocks = []
WIDTH:int = 400
HEIGHT:int = 800
SIZE:int = int(WIDTH/10)

def new_block() -> object:
    return Block()

def fix_block(block:object) -> None:
    I, J = block.pos
    for i, y in enumerate(block.shape):
        for j, x in enumerate(y):
            if x == 1:
                board[i+I][j+J] = block.color

def clear_board() -> None:
    board[board != ""] = 0

def draw_block(screen, block:object, size:int) -> list:
    Y, X = block.pos
    for i, y in enumerate(block.shape):
        for j, x in enumerate(y):
            if i+Y<20 and 0<=j+X<10:
                if x == 1:
                    pygame.draw.rect(screen, block.color, (int((j+X)*size), int((i+Y)*size), size, size))

def display(screen, block:object, size:int) -> None:
    for row, col in np.ndindex(board.shape):
        if board[row][col] != 0:
            color:tuple = board[row][col]
            pygame.draw.rect(screen, color, (int(col*size), int(row*size), size, size))
    draw_block(screen, block, size)

def check_collision(block:object, my, mx) -> bool:
    Y, X = block.pos
    for i, y in enumerate(block.shape):
        for j, x in enumerate(y):
            if i+Y>20 or 0>j+X+mx>10:
                return False
            if x != 0 and (i+Y+my >= 20 or board[i+Y+my][j+X+mx] != 0):
                return False
    return True
            
def move_block(block:object, my:int, mx:int) -> object:
    if check_collision(block, my, mx):
        y, x = block.pos
        block.pos = (y+my, x+mx)
    else:
        y, x = block.pos
        if y == 0:
            return "lose"
        fix_block(block)
        return None
    return block

def rotate(block:object) -> object:
    return block

def main() -> None:
    pygame.init()
    start_ticks = pygame.time.get_ticks()
    last_time = 0
    pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill((0,0,0))

    block = new_block()

    while True:
        screen.fill((0,0,0))
        display(screen, block, SIZE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    block = move_block(block, 0, -1)
                if event.key == pygame.K_RIGHT:
                    block = move_block(block, 0, 1)
                if event.key == pygame.K_DOWN:
                    block = move_block(block, 1, 0)
        
        if ((pygame.time.get_ticks()-start_ticks) / 100) - last_time >= 5:
            block = move_block(block, 1, 0)
            last_time = (pygame.time.get_ticks()-start_ticks) / 100

        if not block:
            block = new_block()
        elif block == "lose":
            break

        pygame.display.flip()
        pygame.display.update()

if __name__ == "__main__":
    main()