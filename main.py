import backtracking as bt

#FILE_PATH = input('Entrez le nom ou chemin du fichier : ')
FILE_PATH = 'evilsudoku.txt'

#Conversion du fichier texte en un tableau Python 9x9 d'entiers
try:
    with open(FILE_PATH, "r") as f:
        data = f.readlines()
except FileNotFoundError as e:
    print(e)
    exit()
grid = []
for line in data:
    row = [int(n) if n.isnumeric() else 0 for n in line.strip()] #0 représente une case vide
    grid.append(row)

#Appel de la fonction de résolution et d'affichage
bt.display_solved(grid)
