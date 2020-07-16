from tictactoe.tictactoe_env import *
from tictactoe.tictactoe_demo_iavrandom import *
from typing import Callable

import numpy as np

from policies import tabular_uniform_random_policy


def off_policy_monte_carlo_control(
        states_count: int,
        actions_count: int,
        is_terminal_func: Callable,
        step_func: Callable,
        episodes_count: int = 10000,
        max_steps_per_episode: int = 10,
        epsilon: float = 0.2,
        gamma: float = 0.99,
) -> (np.ndarray, np.ndarray):
    states = np.arange(states_count)
    b = tabular_uniform_random_policy(states_count, actions_count)
    pi = np.zeros((states_count, actions_count))
    C = np.zeros((states_count, actions_count))
    q = np.random.random((states_count, actions_count))
    for i in range(
            len(pi)):
        for j in range(i):
            if j == i:
                pi[i][j] = 0.0
                q[i][j] = 0.0

    for episode_id in range(episodes_count):
        # print("pi : ", pi)
        s0 = np.random.choice(states)  # état initial aléatoire
        board = [0 for i in range(9)]
        board[s0] = 1
        board[np.random.choice(len(availablePositions(board)))] = -1

        s_list, a_list, r_list = play_a_game(s0, board, pi, max_steps_per_episode)

        G = 0
        W = 1
        for t in reversed(range(len(s_list))):
            G = gamma * G + r_list[t]
            st = s_list[t]
            at = a_list[t]

            C[st, at] += W

            q[st, at] += W / C[st, at] * (G - q[st, at])
            pi[st, :] = 0.0
            pi[st, np.argmax(q[st, :])] = 1.0

            if at != np.argmax(q[st, :]):
                break

            W = W / b[st, at]

    return q, pi


if __name__ == "__main__":
    Q, Pi = off_policy_monte_carlo_control(len(S), len(A),
                                                      is_terminal, choose_action,
                                                      episodes_count=50000,
                                                      max_steps_per_episode=100)

    display_results(Q, Pi)