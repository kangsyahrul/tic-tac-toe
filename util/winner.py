import sys
import numpy as np


def getHorizontalVals(vals, match=3):
    h, w = np.array(vals).shape
    res = []
    for y in range(h):
        array = []
        for x in range(w):
            array.append((vals[y][x], (x, y)))
        if len(array) >= match:
            res.append(array)
    return res


def getVerticalVals(vals, match=3):
    h, w = np.array(vals).shape
    res = []
    for x in range(w):
        array = []
        for y in range(h):
            array.append((vals[y][x], (x, y)))
        if len(array) >= match:
            res.append(array)
    return res


def getDiagonalVals(vals, mode, match=3):
    h, w = np.array(vals).shape
    res = []

    assert mode in ['up', 'down']

    # Diagonal UP
    if mode == 'up':
        for a in range(h * 2 - 1):
            array = []
            x = 0
            for y in range(a, -1, -1):
                if 0 <= x < w and 0 <= y < h:
                    array.append((vals[y][x], (x, y)))
                x += 1
            if len(array) >= match:
                res.append(array)

    # Diagonal Down
    if mode == 'down':
        res = []
        for a in range(-h, h):
            array = []
            x = 0
            for y in range(a, h, 1):
                if 0 <= x < w and 0 <= y < h:
                    array.append((vals[y][x], (x, y)))
                x += 1
            if len(array) >= match:
                res.append(array)
    
    return res


def checkWinner(vals, match=3):
    '''Return the winner: X, O, or None'''
    h, w = np.array(vals).shape

    arrays = []
    arrays.append(('horizontal', getHorizontalVals(vals, match=match)))
    arrays.append(('vertical', getVerticalVals(vals, match=match)))
    arrays.append(('diagonal up', getDiagonalVals(vals, 'up', match=match)))
    arrays.append(('diagonal down', getDiagonalVals(vals, 'down', match=match)))

    # Check if game
    for kind, array in arrays:
        for vals in array:
            (winner, point), count = vals[0], 1
            area = [(winner, point)]
            for val, point in vals[1:]:
                if winner == val and winner != ' ':
                    count += 1
                    area.append((winner, point))

                else:
                    winner = val
                    count = 1
                    area = [(winner, point)]
                
                if count >= match:
                    return winner, area

    return None, []
