# 4IABD2_DEEP_REINFORCEMENT_S2

## Guide d'utilisation

### Grid world & Line world : 
    
Pour les implémentation de ces 2 solutions, cela fonctionne de la même manière.

Tout d'abord : 
- dans le dossier "algorithms" se trouve tout les algorithmes implémentés pour l'apprentissage
- dans les dossiers "gri_world" & "line world":
    - le fichier "\_\_init\_\_.py" possède les fonction et les variables nécessaires à la constitution de l'environnement grid ou line world
    - les fichiers "test_......" sont les différentes application des algorithmes présents dans le dossier "algorithms"
- dans le dossier "policies" il y a une fonction permettant d'initialiser la policy
- dans le dossier "utils" il y a le fichier "\_\_init\_\_.py" qui contient une fonction permettant de jouer une partie et de renvoyer les états, utilisée dans certaines fonction pour le grid et line world. Et le fichier "pygame_grid_line_world.py" qui contient la demo pour les grid et line world

### Pour le tic tac toe : 

Cela est implémenté différemment, tout est dans le dossier tictactoe : 

- les fichiers "test_....." contiennent : 
    - la fonction permettant d'entrainer l'IA (correspondant au nom du fichier)
    - appel des cette fonction
    - appel de la fonction de démo
- le fichier "tictactoe_play" contient une version basique du morpion : joueur vs joueur
- le fichier "tictactoe_env" contient les fonctions utiles à la définition de l'environnement ainsi que les fonctions nécessaires pour jouer une partie
- le fichier "tictactoe_demo_iavrandom" contient une demo graphique du morpion faisant jouer une IA entrainé contre un joueur random et affichant le nombre de victoires pour chacun d'eux ainsi que le nombre de match nul


### Pour le pacman : 

Il n'y a pas encore d'algorithms implémentés.

Dans le dossier "pacman" il y a simplement une version jouable du pacman :
- le fichier "app_class.py" contient les fonctions relatives à l'application elle-même (affichage, déroulé du jeu, ....)
- le fichier "enemy_class.py" contient les fonctions relatives aux fantômes (déplacement, affichage, règles IA, ...)
- le fichier "player_class.py" contient les fonctions relatives au joueur (déplacement, affichage, vies, ...)
- le fichier "pacman_maze.png" contient le background du jeu
- le fichier "walls.txt" contient la définition des murs et l'emplacement des fantomes, du joueur et des pièces.
- le fichier "score.txt" contient le score max. (fichier à supprimer pour réset complétement le jeu)
- le fichier "settings.py" contient les paramètres visuels généraux de l'application
- le fichier "README.md" contient tout les information nécessaires pour créer une nouvelle map si besoin et d'autres informations utiles



### Pour toutes les implémentation graphiques : 

Si vous souhaitez accélérer l'exécution jeu il faut réduire la variable "FPS", et faire l'inverse si vous souhaitez le ralentir.
Tout les autres informations sont dans le ppt sur myges (avec images)
