import numpy as np

width = 3
height = 3
num_states = width * height
S = np.arange(num_states)
# les 9 positions de la grille dans le sens de lecture,  1 2 3 (première ligne), 4 5 6 (deuxième ligne), 7 8 9 (dernière ligne)
A = np.arange(9)
T = np.array([width - 1, num_states - 1])
P = np.zeros((len(S), len(A), len(S), 2))

print(np.shape(S))
print(np.shape(A))
print(np.shape(T))
print(np.shape(P))