from algorithms import monte_carlo_with_exploring_starts_control
from grid_world import *
from utils import pygame_grid_line_world

if __name__ == "__main__":
    Q, Pi = monte_carlo_with_exploring_starts_control(len(S), len(A), is_terminal, step,
                                                      episodes_count=1, max_steps_per_episode=100)

    print('--------------------------------------')
    print(Q)
    print(Pi)


    #pygame_grid_line_world.display_results("grid",Q,Pi,S,T,P,(width,height))
