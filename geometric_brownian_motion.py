import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helper_functions import get_float_from_user
from helper_functions import get_int_from_user
from one_dim_brownian_motion import simulate_1D_brownian_motion


def main():
    brownian_motions = [0] * number_of_sample_paths
    gbms = [0] * number_of_sample_paths
    for i in range(number_of_sample_paths):
        brownian_motions[i] = simulate_1D_brownian_motion()
        gbms[i] = simulate_geometric_brownian_motion(brownian_motions[i])
    print(gbms[0])
    # plot_geometric_brownian_motions(gbms)

def simulate_geometric_brownian_motion(bm):
    timeline = np.arange(0, max_time, increment)
    for t in timeline:
        realisation = np.array(s_0*np.exp(sigma*bm.loc[t] +(t*(mu - 0.5 * (sigma**2)))))
    realisations = np.concatenate([[realisations] or realisation, realisation])
    return pd.Series(realisations, index=[time for time in timeline])

def plot_geometric_brownian_motions(gbms):
    pass


if __name__ == "__main__":
    increment = get_float_from_user("How large should each increment to be? ")

    while True:
        max_time = get_int_from_user(
            "At what time should the simulation end? ")
        if (max_time > increment):
            break

    number_of_increments = (np.floor(max_time/increment)).astype(
        int) if max_time % increment == 0 else (np.floor(max_time/increment)).astype(int) + 1

    number_of_sample_paths = get_int_from_user(
        "How many sample paths do you want? ")
    
    mu = get_float_from_user("Please enter a value for drift: ")
    sigma = get_float_from_user("Please enter a value for volatility: ")
    s_0 = get_int_from_user("Please enter the initial value: ")
    main()
