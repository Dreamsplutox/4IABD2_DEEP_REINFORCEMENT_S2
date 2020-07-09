from tictactoe.tictactoe_env import *
from tictactoe.tictactoe_play import *
from typing import Callable

import numpy as np

from policies import tabular_uniform_random_policy

def monte_carlo_with_exploring_starts_control(
        states_count: int,
        actions_count: int,
        is_terminal_func: Callable,
        step_func: Callable,
        episodes_count: int = 10000, # équivalent des epochs
        max_steps_per_episode: int = 10,
        gamma: float = 0.99,
) -> (np.ndarray, np.ndarray):
    states = np.arange(states_count) #états possibles
    pi = tabular_uniform_random_policy(states_count, actions_count) # policy random uniform
    q = np.random.random((states_count, actions_count)) # valeurs aléatoires

    #print("pi init : ", pi)

    for i in range(len(pi)): #met à 0 les états inutiles (état où on va dans la même case que celle actuelle => impossible)
        for j in range(i):
            if j == i:
                pi[i][j] = 0.0
                q[i][j] = 0.0

    returns = np.zeros((states_count, actions_count))
    returns_count = np.zeros((states_count, actions_count))

    for episode_id in range(episodes_count):
        #print("pi : ", pi)
        s0 = np.random.choice(states) # état initial aléatoire
        board = [0 for i in range(9)]
        board[s0] = 1
        board[np.random.choice(len(availablePositions(board)))] = -1

        s_list, a_list, r_list = play_a_game(s0, board, pi, max_steps_per_episode)

        print(s_list, len(s_list))
        print(a_list, len(a_list))
        print(r_list, len(r_list))


        G = 0
        for t in reversed(range(len(s_list))):
            G = gamma * G + r_list[t]
            st = s_list[t]
            at = a_list[t]

            if (st, at) in zip(s_list[0:t], a_list[0:t]):
                continue
            returns[st, at] += G
            returns_count[st, at] += 1
            q[st, at] = returns[st, at] / returns_count[st, at]
            pi[st, :] = 0.0
            pi[st, np.argmax(q[st, :])] = 1.0
    return q, pi


if __name__ == "__main__":
    Q, Pi = monte_carlo_with_exploring_starts_control(len(S), len(A), is_terminal, choose_action,
                                                      episodes_count=10000, max_steps_per_episode=9)

    print('--------------------------------------')
    print(Q)
    print(Pi)


    #pygame_grid_line_world.display_results("grid",Q,Pi,S,T,P,(width,height))