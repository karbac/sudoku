import backtracking as bt

FILE_PATH = input('Entrez le nom du fichier ou le chemin : ')

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

print('GRILLE RESOLUE')
bt.display_solved(grid)
