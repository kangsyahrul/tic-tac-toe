import sys
import random
import keyboard
import util.screen as sc
import util.winner as wn

from time import sleep
from model.point import Point

# GAME SETTINGS
GAME_SIZE = (4, 7)  # board size
GAME_MATCH = 5       # number of tic tac toe


# Variables
vals = []
point = Point(0, 0)


def main():
    global vals, point

    # Clear screen
    sc.clearScreen()

    # Draw board
    sc.drawBoard(point, vals)
    sleep(0.2)

    # Read input
    key = keyboard.read_key()
    point, vals = keyboardAction(key, point, vals)

    # Check if game over
    is_game_over, winner, area = isGameOver(vals)
    if is_game_over:
        gameOver(winner, area)
        return

    # Computer turn
    if isComputer(vals):
        vals = computerNextMove(vals)
    
    # Check if game over
    is_game_over, winner, area = isGameOver(vals)
    if is_game_over:
        gameOver(winner, area)
        return

    main()


def gameOver(winner, area):
    global point, vals

    sc.clearScreen()
    sc.drawBoard(point, vals, area=area)
    print('GAME OVER!!!')
    print('Winner is : ', winner)
    print()
    print('Press "R" to restart the game')
    print('Press "Q" to quit the game')
    print()

    # Read input
    key = keyboard.read_key()
    print(f'Key: {key}')
    if key.lower() == 'r':
        point, vals = keyboardAction(key, point, vals)
        main()
    
    if key.lower() == 'q':
        return 

    else:
        gameOver(winner, area)


def gameStart():
    global point, vals

    point, vals = restartGame()
    main()


def welcomeScreen():
    sc.clearScreen()
    print('Welcome to TIC TAC TOE Game')
    print('Press "Enter" to start')
    # input_str = input()

    gameStart()


def keyboardAction(key, point, vals):
    # Vertical
    if key == 'up' and point.y > 0:
        point.y = point.y - 1
    if key == 'down' and point.y < GAME_SIZE[1] - 1:
        point.y = point.y + 1
    
    # Horizontal
    if key == 'left' and point.x > 0:
        point.x = point.x - 1
    if key == 'right' and point.x < GAME_SIZE[0] - 1:
        point.x = point.x + 1
    
    # X
    if str(key).lower() == 'x' and vals[point.y][point.x] == ' ':
        vals[point.y][point.x] = 'X'

    # Restart
    if str(key).lower() == 'r':
        point, vals = restartGame()
    
    return point, vals


def isGameOver(vals):
    # Check if there is a winner
    winner, area = wn.checkWinner(vals, match=GAME_MATCH)
    if winner is not None:
        print(f'Winner is: "{winner}"')
        return True, winner, area
    
    # Check if all array is filled up
    for row in vals:
        if ' ' in row:
            return False, None, []
    
    return True, None, []
    

def computerNextMove(vals):
    while True:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if vals[y][x] == ' ':
            vals[y][x] = 'O'
            break
    return vals


def isComputer(vals):
    count = 0
    for row in vals:
        for col in row:
            if col != ' ':
                count += 1
    
    return count % 2 == 1


def restartGame():
    w, h = GAME_SIZE
    vals = []
    for y in range(h):
        val = []
        for x in range(w):
            val.append(' ')
        vals.append(val)
    
    point = Point(0, 0)

    return point, vals


if __name__ == '__main__':
    welcomeScreen()
