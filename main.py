import backtracking as bt

FILE_PATH = f"grids/{input('Entrez le nom du fichier : ')}" # /!\ Le fichier doit se trouver dans le dossier grids
#FILE_PATH = 'grids/evilsudoku.txt'

#Conversion du fichier texte en un tableau Python 9x9 d'entiers
try:
    with open(FILE_PATH, "r") as f:
        data = f.readlines()
except FileNotFoundError as e:
    print(e)
    exit()
grid = []
for line in data:
    row = [int(n) if n.isnumeric() else '*' for n in line.strip()] #Une astérisque représente une case vide
    grid.append(row)

#Affichage de la grille initiale et de la grille résolue (oui, pas de couleurs parce que ça ne marche pas chez moi donc voilà)

print('*******  GRILLE INITIALE *******')
bt.display_grid(grid)
print('\n')

if not bt.solve(grid):
    print("Cette grille n'a pas de solution")
    exit()

print('*******  GRILLE RESOLUE *******')
bt.display_grid(grid)
