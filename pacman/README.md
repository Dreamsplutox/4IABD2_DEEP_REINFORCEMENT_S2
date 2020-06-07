# GUIDE PACMAN
### Plan
- architecture du dossier
- Guide des fonctions et des fichiers :
-- fichier app_class
-- fichier enemy_class
-- fichier player_class
-- fichier walls
- ajout de maps
- sources

## Architecture du dossier : 
- dossier sprites => contient les images nécessaire à l'affichage des coeurs, des fantômes, de pacman et des pièces
- main.py => fichier main pour lancer l'application (python main.py)
- pp_class.py => contient les fonctions principale pour gérer le jeu, l'affichage, les fenêtre, les conditions de victoire/game over, le déroulé du jeu, etc....
- player_classe.py => contient les fonctions et les caractérisques de pacman
- enemy_class.py => contient les fonctions et les caractéristiques des fantômes, les règles de déplacement, ....
- settings.py => contient les paramètres de l'application, les liens vers les images, les couleurs, les dimmensions de la fenêtre, les fps, ...
- pacman_maze.png => image de fond => labyrinthe
- score.txt => contient la sauvegarde du meilleur score obtenu (pour les récupérer même si on ferme le jeu)
- walls.txt => contient les coordonnées des murs, des pièces et les points de départ de pacman et des fantômes ==> voir la partie ajout de maps

## Fonctions et fichiers
### app_class.py

run() => les états de l'application => écran d'acceuil, écran de jeu, écran game over, écran victoire

draw_text() => écris du texte dans la page
load() => charge le fichier walls.txt pour avoir les coordonnées des murs, pièces, ... ainsi que l'image de fond
make_enemies() => charge la position et le nombre d'ennemis
draw_grid() => fonction utilitaire pour afficher la grille du jeu ==> aide pour remplir le fichier walls en cas de création de maps ou pour réajuster la fenêtre de jeu
reset() => fonction de reset du jeu pour relancer le jeu après un game over ou une victoire

start_events() ==> évènement clavier sur la page d'intro
start_update() ==> inutilisé mais peut être utilisée pour faire des animation sur la page
start_draw() ==> affichage de la page, text, ....

playing_events() => évènement clavier sur le jeu
playing_update() => mise à jour de l'affichage de pacman, des fantomes, des pièces, .... + check en temps réel du nombre de pièces pour victoire + perte vie en cas de conctact entre pacman et les fantômes
playing_draw() => affichage des éléments
remove_lives() => règle du game over + perte de vie + reset des positions de pacman et des fantômes à la perte d'une vie
draw_coins() => affichage des pièces

game_over_events() => évènement clavier pour la page
game_over_draw() => affichage

victory_events() => évènement clavier pour la page
victory_draw() => affichage

## enemy_class
init() => initialisation des variables
update() => mis à jour de la position et de la direction
draw() => affichage du personnage en fonction du type
set_speed() => vitesse en fonction du type
set_target() => détermine la cible à atteindre pour les fantomes => fuir pacman ou le chasser
time_to_move() => détermine s'il peut bouger
move() => détermine la façons de bouger selon le type
get_path_direction() => retourne la direction à prendre en fonction de la nouvelle case
find_next_cell_in_path() => détermine la nouvelle case en fonction du chemin
BFS() => détermine le nouveau chemin en fonction de la position de la cible
get_random_direction() => renvoi une direction aléatoire
get_pix_pos() => renvoi la position en pixel
set_colour() => détermine l'affichage du fantôme
set_personnality => détermine la personnalité du fantôme

## player_class
init() => initialisation des variables
update() => mis à jour de la position et de la direction ainsi que dévorer un pixel ou non
draw() => animation du pacman
on_coin() => détermine si on est sur un pièce
eat_coin() => augmente le score et supprime la pièce
move() => mouvement
get_pix_pos() => position au pixel près
time_to_move() => détermine si on peut bouger
can_move() => renvoi True si on ne rencontre pas un mur au prochain mouvement

## walls
fichier contenant la liste des murs, pièces, ...
Exemple : 

111111C11C111BB111C11C111111
111111C11C15000041C11C111111
111111CCCC10000001CCCC111111
111111C11C12000031C11C111111
111111C11C11111111C11C111111
111111C11CCCCCCCCCC11C111111
111111C11C11111111C11C111111
111111C11C11111111C11C111111
1CCCCCCCCCCCC11CCCCCCCCCCCC1
1C1111C11111C11C11111C1111C1
1C1111C11111C11C11111C1111C1
1CCC11CCCCCCCPCCCCCCCC11CCC1

chaque valeur est une case de ma grille de jeu : 
- 1 => mur
- 2, 3, 4, 5 => position d'origine d'un fantôme
- C => emplacement des pièces
- B => mur infranchissable pour pacman mais pas pour les fantomes
- P => position d'origine de pacman


## Ajout de maps
Pour ajouter une map il faut : 
- choisir un fond de map
- ajuster la taille de la fenêtre de jeu pour correspondre à la taille de la map (voir le fichier settings)
- afficher la grille pour avoir la liste des cases (ajuster si besoin) => fonction self.draw_grid() à décommenter dans la fonction playing_draw() du fcihier app_class.py
- crééer un fichier txt contenant une ligne pour chaque ligne de votre grille et un caractère par cellule => voir exemple au dessus
- dans le fichier app_class.py modifier la fonction load pour modifier le background et remplacer walls.txt par le fichier que vous souhaitez.

Sources :
Ce programme a été codé en suivant le tuto youtube : https://www.youtube.com/playlist?list=PLryDJVmh-ww3AMl8NSjp9YygWWTOfePu7

Il y a également eu plusieurs ajouts en suivant des tutos pour l'animation de personnage sur pygame.



