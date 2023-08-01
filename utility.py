#Prend en entrée un tableau de sudoku, un nombre, et un emplacement de case
#Retourne Vrai si le nombre d'entrée peut être placé à cet emplacement en toute légalité
#Retourne Faux dans le cas contraire
def is_valid(grid, n, row, col):
    for i in range(9):
        if grid[i][col] == n or grid[row][i] == n:  #Vérification de la ligne et de la colonne
            return False
    rowsq, colsq = 3 * (row//3) , 3 * (col//3)
    for i in range(rowsq, rowsq+3):                 #Vérification du carré 3x3
        for j in range(colsq, colsq+3):
            if grid[i][j] == n:
                return False
    return True

#Retourne un tuple représentant le numéro de ligne et de colonne de la première case vide de la grille d'entrée.
#Retourne Faux si il n'y a plus de cases vides
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i,j
    return False

def solve(grid):
    empty_cell = find_empty(grid)
    if not empty_cell:
        return grid
    row, col = empty_cell

    for n in range(1,10):
        if is_valid(grid,n,row,col):
            grid[row][col] = n

            if solve(grid):
                return grid

            grid[row][col] = 0
    return False

def display_solved(grid):
    BOLD = '\033[1m'
    RESET = '\033[0m'
    BG_RED = '\033[41m'
    solved_grid = solve(grid)
    for i in range(9):
        print()
        if i in (3,6):
            print()
        for j in range(9):
            print(str(solved_grid[i][j]), end='')
            if j in (2,5):
                print(" ", end='')


