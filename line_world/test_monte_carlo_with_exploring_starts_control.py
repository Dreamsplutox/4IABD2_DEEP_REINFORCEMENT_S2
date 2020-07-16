from algorithms import monte_carlo_with_exploring_starts_control
from line_world import *
from utils import pygame_grid_line_world

if __name__ == "__main__":
    Q, Pi = monte_carlo_with_exploring_starts_control(len(S), len(A), is_terminal, step)
    print(Q)
    print(Pi)
    pygame_grid_line_world.display_results("line", Q, Pi, S, T, P, (num_states, 1))