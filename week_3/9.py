"""
:(
"""
correct = ["1", "2", "3", "4"]
#list_of_square_coords = ["0:2, 0:2","2:4, 2:4","0:2, 2:4","2:4, 0:2"]
import numpy as np
#line1, line2, line3, line4 = list(input()), list(input()), list(input()), list(input())
#matrix = [line1, line2, line3, line4]
matrix = np.array([['0', '0', '0', '0'], ['0', '0', '2', '0'], ['0', '1', '0', '0'], ['3', '2', '0', '4']])
def fix(line):
    if line.count("0") == 1:
        missing = list(set(correct).difference(line))
        index = line.index("0")
        line[index] = missing[0]
    return(line)
        
def solve_sudoku(matrix):
    if not any("0" in sublist for sublist in matrix):
        return(matrix)
    for i in range(4): #verticals
        line = matrix[:, i].tolist()
        matrix[:, i] = fix(line)
    for i in range(4): #horizontals
        line = matrix[i, :].tolist()
        matrix[i, :] = fix(line)
    #squares
    line = matrix[0:2, 0:2].tolist()
    matrix[0:2, 0:2] = fix(line)
    line = matrix[2:4, 2:4].tolist()
    matrix[2:4, 2:4] = fix(line)
    line = matrix[0:2,2:4].tolist()
    matrix[0:2, 2:4] = fix(line)
    line = matrix[2:4, 0:2].tolist()
    matrix[2:4, 0:2] = fix(line)
    line = []
    print(matrix)
    solve_sudoku(matrix)

solve_sudoku(matrix)
#print(fix(["1", "2", "0", "4"]))