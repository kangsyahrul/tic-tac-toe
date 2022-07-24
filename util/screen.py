import os
import numpy as np

from model.point import Point


def clearScreen():
    os.system('cls||clear')


def drawVerticalEdge(size, padding):
    w, h = size
    padding_x, padding_y = padding

    for a in range((w) * (padding_x * 2) * 2 + 1):
        if a % (padding_x + 1) * 2 == 0:
            print('+', end='')
        else:
            print('-', end='')


def colored(color, text):
    r, g, b = color
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)


def drawBoard(point: Point, vals, padding=(2, 1), area=[]):
    h, w = np.array(vals).shape
    padding_x, padding_y = padding

    i = 0
    for y in range((h * 2 + 1) + (h * 2) * (padding_y - 1)):
        for x in range((w * 2 + 1) + (w * 2) * (padding_x - 1)):
            if y % (padding_y * 2) == padding_y:
                if x % (padding_x * 2) == padding_x:
                    # Value
                    a, b = i % w, i // w
                    if point.x == a and point.y == b:
                        # Hightlight this cell
                        val = vals[b][a]
                        text = '_' if val == ' ' else val
                        color = (255, 0, 0) # Red: filled up cell

                        if text == '_':
                            color = (0, 255, 0) # Green: pointer

                        for v, pt in area:
                            if a == pt[0] and b == pt[1]:
                                color = (255, 255, 0) # Yellow: pointer

                        print(colored(color, text), end='')

                    else:
                        color = (255, 255, 255)
                        for v, pt in area:
                            if a == pt[0] and b == pt[1]:
                                color = (255, 255, 0) # Yellow: pointer

                        text = vals[b][a] 
                        print(colored(color, text), end='')

                    i += 1

                elif x % (padding_x * 2) == 0:
                    print('+', end='')
                
                else:
                    print(' ', end='')
            
            elif y % (padding_y * 2) == 0:
                if x % (padding_x * 2) == 0:
                    print('+', end='')
                
                else:
                    print('-', end='')
            
            else:
                if x % (padding_x * 2) == 0:
                    print('+', end='')

                else:
                    print(' ', end='')
                
        print()

