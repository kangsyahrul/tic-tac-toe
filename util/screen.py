import os
import cv2
import numpy as np

from model.point import Point


def clearScreen():
    os.system('cls||clear')


def drawPointer(img, point, padding, box):
    box_px, box_py = box
    x1, x2 = padding + point.x * (box_px), padding + (point.x + 1) * box_px
    y1, y2 = padding + point.y * (box_py), padding + (point.y + 1) * box_py
    return cv2.rectangle(img, (x1, y1), (x2, y2), (0, 125, 0), -1)


def drawValues(img, point, padding, box, board, vals):
    board_w, board_h = board
    box_px, box_py = box
    for y in range(board_h):
        for x in range(board_w):
            val = vals[y][x]
            x1, x2 = padding + x * (box_px) + padding, padding + (x + 1) * box_px - padding
            y1, y2 = padding + y * (box_py) + padding, padding + (y + 1) * box_py - padding
            xc, yc = (x1 + x2)//2, (y1 + y2)//2

            if val == 'X':
                # Draw X
                img = cv2.line(img, (x1, y1), (x2, y2), (125, 0, 0), 4, cv2.LINE_AA)
                img = cv2.line(img, (x1, y2), (x2, y1), (125, 0, 0), 4, cv2.LINE_AA)

            elif val == 'O':
                # Draw O
                img = cv2.circle(img, (xc, yc), ((x2-x1)+(y2-y1))//4, (0, 0, 125), 4)
    
    return img


def drawGameOver(img, point, padding, box, area):
    box_px, box_py = box
    x1, x2 = padding + point.x * (box_px), padding + (point.x + 1) * box_px
    y1, y2 = padding + point.y * (box_py), padding + (point.y + 1) * box_py

    x1, y1 = area[0][1]
    x2, y2 = area[-1][1]
    
    x1, x2 = padding + x1 * box_px + box_px//2, padding + x2 * box_px + box_px//2
    y1, y2 = padding + y1 * box_py + box_py//2, padding + y2 * box_py + box_py//2

    return cv2.line(img, (x1, y1), (x2, y2), (0, 125, 125), 32, cv2.LINE_AA)


def getBackground(BOARD, WINDOW, PADDING):
    BOARD_W, BOARD_H = BOARD
    WINDOW_W, WINDOW_H = WINDOW

    # Create background
    background = np.zeros((WINDOW_H, WINDOW_W, 3), dtype=np.int8)

    # Draw line
    dx = (WINDOW_W - 2 * PADDING) // BOARD_W
    dy = (WINDOW_H - 2 * PADDING) // BOARD_H

    for i in range(BOARD_W + 1):
        x = PADDING + i * dx
        y1, y2 = PADDING, WINDOW_H - PADDING
        background = cv2.line(background, (x, y1), (x, y2), (255, 255, 255), 4, cv2.LINE_AA)

    for i in range(BOARD_H + 1):
        y = PADDING + i * dy
        x1, x2 = PADDING, WINDOW_H - PADDING
        background = cv2.line(background, (x1, y), (x2, y), (255, 255, 255), 4, cv2.LINE_AA)

    return background
