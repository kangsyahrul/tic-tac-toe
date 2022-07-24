import util.computer as comp

vals = [
    ['X', 'O', 'X'], 
    [' ', 'O', ' '], 
    ['O', 'X', ' '],
]
comp.getNexMove(vals, 'X', match=3)
# comp.getNexMove(vals, 'O', match=3)