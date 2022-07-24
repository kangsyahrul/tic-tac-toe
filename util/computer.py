import math
import random
import numpy as np
import util.winner as wn


def getWinProb(vals, values, player, match=3):
    h, w = np.array(vals).shape
    res = []
    for value in values:
        for idx_start in range(0, w - match + 1):
            val = value[idx_start:idx_start + match]
            # print(f'value: {val} ', end='')
            player_, count = None, 0
            for player__, point in val:
                if player__ == ' ':
                    player__ = player
                
                if player_ == player__:
                    count += 1
                else:
                    player_ = player__
                    count = 1
            # print(f'count = {count} ', end='')
            if count >= match:
                # if player_ == ' ' or player_ == player:
                # print(f'PROB = 1.0', end='')
                res.append(val)
            # print()
    return res

def getMovesProb(vals, player, match=3):
    h, w = np.array(vals).shape

    res = []
    res_ver = getWinProb(vals, wn.getVerticalVals(vals, match=match), player, match=match)
    res_hor = getWinProb(vals, wn.getHorizontalVals(vals, match=match), player, match=match)
    res_dup = getWinProb(vals, wn.getDiagonalVals(vals, 'up', match=match), player, match=match)
    res_ddo = getWinProb(vals, wn.getDiagonalVals(vals, 'down', match=match), player, match=match)
    res.extend(res_ver)
    res.extend(res_hor)
    res.extend(res_dup)
    res.extend(res_ddo)
    # print(f'res_ver:')
    # for r in res_ver: print(f'\t{r}')
    # print(f'res_hor:')
    # for r in res_hor: print(f'\t{r}')
    # print(f'res_dup:')
    # for r in res_dup: print(f'\t{r}')
    # print(f'res_ddo:')
    # for r in res_ddo: print(f'\t{r}')

    probs = np.zeros((h, w))
    for rs in res:
        players = [player for player, (x, y) in rs]
        for r in rs:
            player_, (x, y) = r
            player_on_board = vals[y][x]
            if player_on_board == ' ':
                ct = players.count(player)
                probs[y][x] += 0.5 + players.count(player) ** 2

    return probs

def normalize(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def getNexMove(vals, player, match=3):
    h, w = np.array(vals).shape
    np.set_printoptions(precision=3)

    probs_me = getMovesProb(vals, player, match=match)
    # probs_me = normalize(probs_me)
    # print(f'probs_me:')
    # print(probs_me)

    probs_op = getMovesProb(vals, 'X' if player == 'O' else 'O', match=match)
    # probs_op = normalize(probs_op)
    # print(f'probs_op:')r
    # print(probs_op)

    probs = probs_me * 1.0 + probs_op * 1.0
    probs = normalize(probs)
    # print(f'probs:')
    # print(probs)

    prob_max = probs.max()
    moves = []
    for y in range(h):
        for x in range(w):
            if probs[y][x] == prob_max:
                moves.append((x, y))
    
    if len(moves) > 0:
        move = random.choice(moves)
    else:
        move = x, y = random.randint(0, w - 1), random.randint(0, h - 1)
    # print(f'moves: {moves}')
    # print(f'next_move: {move}')
    return move
