from colorama import init, Fore, Style
init()
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

#Retourne un tuple représentant le numéro de ligne et de colonne de la première case vide de la grille.
#Retourne Faux si il n'y a plus de cases vides
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i,j
    return False

#Prend un tableau de sudoku en entrée
#Retourne la grille complétée et résolue avec la méthode du backtracking
#Retourne Faux si aucune solution n'est possible
def solve(grid):
    empty_cell = find_empty(grid)
    if not empty_cell:
        return grid
    row, col = empty_cell

    for n in range(1,10):   #On essaie chaque nombre de 1 à 9 sur les cases vides
        if is_valid(grid,n,row,col):
            grid[row][col] = n

            if solve(grid):  #Etape suivante, appel récursif de la fonction
                return grid

            grid[row][col] = 0 #Si on arrive à une impasse, on continue à la boucle de l'étape précédente
    return False

#Prend un tableau sudoku en entrée
#Affiche la grille complète résolue
def display_solved(grid):
    init()
    solved_grid = solve(grid)
    if not solved_grid:
        return "Pas de solution"
    for i in range(9):
        print()
        if i in (3,6):
            print()
        for j in range(9):
            if grid[i][j] == 0:
                print(Fore.RED + Style.BRIGHT + str(solved_grid[i][j]) + Style.RESET_ALL, end='')
            else:
                print( solved_grid[i][j] , end='')
            if j in (2,5):
                print(" ", end='')


