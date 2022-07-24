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
                
                if player__ == player_:
                    count += 1
                else:
                    player_ = player__
                    count = 1
            if count == match:
                # if player_ == ' ' or player_ == player:
                # print(f'PROB = 1.0', end='')
                res.append(val)
            # print()
    return res

def getMovesProb(vals, player, match=3):
    h, w = np.array(vals).shape

    res = []
    res_ver = getWinProb(vals, wn.getVerticalVals(vals, match=match), player, match=3)
    res_hor = getWinProb(vals, wn.getHorizontalVals(vals, match=match), player, match=3)
    res_dup = getWinProb(vals, wn.getDiagonalVals(vals, 'up', match=match), player, match=3)
    res_ddo = getWinProb(vals, wn.getDiagonalVals(vals, 'down', match=match), player, match=3)
    res.extend(res_ver)
    res.extend(res_hor)
    res.extend(res_dup)
    res.extend(res_ddo)
    print(f'res_ver: {res_ver}')
    print(f'res_hor: {res_hor}')
    print(f'res_dup: {res_dup}')
    print(f'res_ddo: {res_ddo}')

    probs = np.zeros((h, w))
    for rs in res:
        players = [player for player, (x, y) in rs]
        for r in rs:
            player_, (x, y) = r
            player_on_board = vals[y][x]
            if player_on_board == ' ':
                probs[y][x] += 1 +  players.count(player)

    return probs

def getNexMove(vals, player, match=3):
    h, w = np.array(vals).shape

    probs_me = getMovesProb(vals, player, match=match)
    print(f'probs_me:')
    print(probs_me)

    probs_op = getMovesProb(vals, 'X' if player == 'O' else 'O', match=match)
    print(f'probs_op:')
    print(probs_op)

    probs = probs_me + probs_op
    print(f'probs:')
    print(probs)

    prob_max = probs.max()
    moves = []
    for y in range(h):
        for x in range(w):
            if probs[y][x] == prob_max:
                moves.append((x, y))
    
    print(f'moves: {moves}')
    move = random.choice(moves)
    print(f'next_move: {move}')
    return move
