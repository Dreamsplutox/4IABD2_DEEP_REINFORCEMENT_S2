from algorithms import on_policy_first_visit_monte_carlo_control, off_policy_monte_carlo_control
from line_world import *
from utils import pygame_grid_line_world

if __name__ == "__main__":
    Q, Pi = off_policy_monte_carlo_control(len(S), len(A),
                                           reset,
                                           is_terminal, step)
    print(Q)
    print(Pi)

    pygame_grid_line_world.display_results("line", Q, Pi, S, T, P, (num_states, 1))