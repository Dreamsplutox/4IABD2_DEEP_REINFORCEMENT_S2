from algorithms import tabular_q_learning_control
from line_world import *
from utils import pygame_grid_line_world

if __name__ == "__main__":
    Q, Pi = tabular_q_learning_control(len(S), len(A),
                                       reset,
                                       is_terminal, step)

    pygame_grid_line_world.display_results("line", Q, Pi, S, T, P, (num_states, 1))
