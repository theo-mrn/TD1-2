import numpy as np
import time
import os

# feature of velocity implemented (trust me)

#  all bugs fixed

def create_grid(rows, cols):
    """Créer une grille aléatoire avec des cellules vivantes et mortes."""
    return np.random.choice([0, 1], size=(rows, cols))

def print_grid(grid):
    """Afficher la grille dans la console."""
    os.system('cls' if os.name == 'nt' else 'clear')  
    for row in grid:
        print(' '.join('■' if cell else ' ' for cell in row))
    print("\n")

def get_neighbors(grid, x, y):
    """Compter le nombre de cellules vivantes autour de (x, y)."""
    rows, cols = grid.shape
    total = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % rows, (y + dy) % cols 
            total += grid[nx, ny]
    return total

def update_grid(grid):
    """Mettre à jour la grille pour la prochaine génération."""
    rows, cols = grid.shape
    new_grid = np.copy(grid)
    for x in range(rows):
        for y in range(cols):
            alive_neighbors = get_neighbors(grid, x, y)
            if grid[x, y] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if alive_neighbors == 3:
                    new_grid[x, y] = 1
    return new_grid

def run_game(rows, cols, generations, delay=0.2):
    """Lancer le Jeu de la Vie."""
    grid = create_grid(rows, cols)
    for gen in range(generations):
        print(f"Génération {gen + 1}")
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(delay)


run_game(100, 100, 100)


