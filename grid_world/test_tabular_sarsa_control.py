from algorithms import tabular_sarsa_control
from grid_world import *
from utils import pygame_grid_line_world

if __name__ == "__main__":
    Q, Pi = tabular_sarsa_control(len(S), len(A),
                                  reset,
                                  is_terminal, step,
                                  epsilon=0.75,
                                  max_steps_per_episode=100)

    pygame_grid_line_world.display_results("grid",Q,Pi,S,T,P,(width,height))
