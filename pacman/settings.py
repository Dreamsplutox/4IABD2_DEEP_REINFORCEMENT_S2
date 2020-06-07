from pygame.math import Vector2 as vec
import pygame

# Screen settings
WIDTH, HEIGHT = 610, 670
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - TOP_BOTTOM_BUFFER, HEIGHT - TOP_BOTTOM_BUFFER
FPS = 60
COLS = 28
ROWS = 30

# color settings
BLACK = (0,0,0)
RED = (208,22,22)
GREY = (107,107,107)
WHITE = (255,255,255)
PLAYER_COLOUR  = (190,194,15)
COINS_COLOUR = (124,123,7)
GOLD = (244, 208, 63)

# font settings
START_TEXT_SIZE = 16
START_FONT = 'arial black'

# objects images settings

HEART_IMG = pygame.transform.scale(pygame.image.load(r'sprites/heart.png'), (20,20))
COIN_IMG = pygame.transform.scale(pygame.image.load(r'sprites/coin.png'), (9,9))


# enemies images settings

GHOST_B_IMG = [ pygame.transform.scale(pygame.image.load(r'sprites/ghost_three/ghost3l.png'), (20,20)), 
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_three/ghost3r.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_three/ghost3u.png'), (20,20)), 
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_three/ghost3d.png'), (20,20))
			  ]
GHOST_R_IMG = [ pygame.transform.scale(pygame.image.load(r'sprites/ghost_one/ghost1l.png'), (20,20)), 
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_one/ghost1r.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_one/ghost1u.png'), (20,20)), 
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_one/ghost1d.png'), (20,20))
			  ]
GHOST_P_IMG = [ pygame.transform.scale(pygame.image.load(r'sprites/ghost_two/ghost2l.png'), (20,20)), 
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_two/ghost2r.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_two/ghost2u.png'), (20,20)), 
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_two/ghost2d.png'), (20,20))
			  ]
GHOST_O_IMG = [ pygame.transform.scale(pygame.image.load(r'sprites/ghost_four/ghost4l.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_four/ghost4r.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_four/ghost4u.png'), (20,20)), 
				pygame.transform.scale(pygame.image.load(r'sprites/ghost_four/ghost4d.png'), (20,20))
			  ]		  


# pacman image settings

PACMAN_L = [ 	pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacman0.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmanl1.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmanl2.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmanl1.png'), (20,20))
			]

PACMAN_R = [ 	pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacman0.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmanr1.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmanr2.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmanr1.png'), (20,20))
			]

PACMAN_U = [ 	pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacman0.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmanu1.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmanu2.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmanu1.png'), (20,20))
			]

PACMAN_D = [ 	pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacman0.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmand1.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmand2.png'), (20,20)),
				pygame.transform.scale(pygame.image.load(r'sprites/pacman/pacmand1.png'), (20,20))
			]
