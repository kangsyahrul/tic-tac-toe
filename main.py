import sys
import cv2
import random
import numpy as np
import util.screen as sc
import util.winner as wn
import util.computer as comp

from time import sleep
from model.point import Point


# GAME SETTINGS
BOARD_W, BOARD_H = BOARD_SIZE = (3, 3)  # board size
GAME_MATCH = 3      # number of tic tac toe

# SCREEN SETTINGS
PADDING = 24
BOX_PX, BOX_PY = BOX = (96, 96)
WINDOW_W = BOX_PX * BOARD_W + PADDING * 2
WINDOW_H = BOX_PY * BOARD_H + PADDING * 2


# Variables
vals = []
point = Point(0, 0)


def isGameOver(vals):
    # Check if there is a winner
    winner, area = wn.checkWinner(vals, match=GAME_MATCH)
    if winner is not None:
        return True, winner, area
    
    # Check if all array is filled up
    for row in vals:
        if ' ' in row:
            return False, None, []
    
    return True, None, []
    

def computerNextMove(vals):
    x, y = comp.getNexMove(vals, 'O', match=GAME_MATCH)
    if vals[y][x] != ' ':
        while True:
            x, y = random.randint(0, BOARD_SIZE[0] - 1), random.randint(0, BOARD_SIZE[1] - 1)
            if vals[y][x] == ' ':
                break
    vals[y][x] = 'O'
    return vals


def isComputer(vals):
    count = 0
    for row in vals:
        for col in row:
            if col != ' ':
                count += 1
    
    return count % 2 == 1


def restartGame():
    w, h = BOARD_SIZE
    vals = []
    for y in range(h):
        val = []
        for x in range(w):
            val.append(' ')
        vals.append(val)
    
    point = Point(0, 0)

    return point, vals


def welcomeScreen():
    sc.clearScreen()
    print('Welcome to TIC TAC TOE Game')
    gameStart()


def gameStart():
    global point, vals
    point, vals = restartGame()
    main()


def main():
    global BOARD_SIZE, BOARD_W, BOARD_H, WINDOW_W, WINDOW_H, PADDING, BOX, BOX_PX, BOX_PY, vals

    # Get background
    background = sc.getBackground(BOARD_SIZE, (WINDOW_W, WINDOW_H), PADDING)

    # Restart game
    point, vals = restartGame()
    is_game_over = False
    while True:
        img = background.copy()

        # Draw pointer
        img = sc.drawPointer(img, point, PADDING, BOX)

        # Draw values
        img = sc.drawValues(img, point, PADDING, BOX, BOARD_SIZE, vals)

        # Check if game over
        is_game_over, winner, area = isGameOver(vals)
        if is_game_over:
            print('Game Over')
            img = sc.drawGameOver(img, point, PADDING, BOX, area)
        
        cv2.imshow('Board', img)

        key = cv2.waitKey(0)
        if key == ord('q'):
            break

        if key == ord('x'):
            if vals[point.y][point.x] == ' ':
                vals[point.y][point.x] = 'X'

            # Check if game over
            is_game_over, winner, area = isGameOver(vals)
            if not is_game_over:
                # Computer turn
                if isComputer(vals):
                    vals = computerNextMove(vals)
        
        # Restart
        if key == ord('r'):
            point, vals = restartGame()
            is_game_over = False

        # Arrow: left
        if key == 81 and not is_game_over:
            if point.x > 0:
                point.x -= 1

        # Arrow: up
        if key == 82 and not is_game_over:
            if point.y > 0:
                point.y -= 1

        # Arrow: right
        if key == 83 and not is_game_over:
            if point.x < BOARD_W - 1:
                point.x += 1

        # Arrow: bottom
        if key == 84 and not is_game_over:
            if point.y < BOARD_H - 1:
                point.y += 1
        

if __name__ == '__main__':
    welcomeScreen()
