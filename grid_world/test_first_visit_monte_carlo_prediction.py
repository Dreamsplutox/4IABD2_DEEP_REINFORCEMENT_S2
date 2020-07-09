from algorithms import first_visit_monte_carlo_prediction
from grid_world import *
from policies import tabular_uniform_random_policy
import time

if __name__ == "__main__":

    start_time = time.time()
    Pi = tabular_uniform_random_policy(S.shape[0], A.shape[0])
    V = first_visit_monte_carlo_prediction(Pi, is_terminal, reset, step, max_steps_per_episode=10, episodes_count=10000)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(V)
    print(Pi)
