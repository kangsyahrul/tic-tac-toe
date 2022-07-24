import util.screen as sc
import util.computer as comp

vals = [
    ['X', ' ', ' ', ' ', ' '], 

    ['X', ' ', ' ', ' ', ' '], 
    
    ['X', ' ', 'O', ' ', ' '],
    
    [' ', 'O', 'O', ' ', ' '],
    
    [' ', ' ', ' ', ' ', ' '],
    
    [' ', ' ', ' ', ' ', ' '],
]
sc.clearScreen()
# comp.getNexMove(vals, 'X', match=4)
comp.getNexMove(vals, 'O', match=4)