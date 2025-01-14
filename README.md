# Jeu de la Vie

Une implémentation en Python du célèbre "Jeu de la Vie" de Conway.

## Description

Le Jeu de la Vie est un automate cellulaire qui simule l'évolution de cellules selon des règles simples :

- Une cellule morte avec exactement 3 voisines vivantes devient vivante
- Une cellule vivante avec 2 ou 3 voisines vivantes reste vivante
- Dans tous les autres cas, la cellule meurt ou reste morte

## Fonctionnalités

- Création d'une grille aléatoire de cellules
- Affichage de la grille dans le terminal (■ pour cellules vivantes)
- Mise à jour automatique des générations
- Grille torique (les bords sont connectés)

## Utilisation

```python
# Lance une simulation de 100 générations sur une grille 20x20
run_game(20, 20, 100)

# Paramètres ajustables :
# - rows : nombre de lignes
# - cols : nombre de colonnes 
# - generations : nombre de générations à simuler
# - delay : délai entre les générations (défaut: 0.2s)