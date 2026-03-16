import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helper_functions import get_float_from_user
from helper_functions import get_int_from_user


def main():
    brownian_motions = [0] * number_of_sample_paths
    for i in range(number_of_sample_paths):
        brownian_motions[i] = simulate_1D_brownian_motion()
    plot_brownian_motions(brownian_motions)


def simulate_1D_brownian_motion():
    timeline = np.arange(0, max_time, increment)
    realisations = np.random.normal(0, np.sqrt(increment), len(timeline[1:]))
    process = np.concatenate([[0], np.cumsum(realisations)])
    return pd.Series(process, index=[time for time in timeline])


def plot_brownian_motions(brownian_motions):
    cmap = plt.cm.get_cmap("tab20", number_of_sample_paths)
    plt.figure(figsize=(20, 10))
    for i in range(number_of_sample_paths):
        brownian_motions[i].plot(color=cmap(i))
    plt.title("1D Brownian Motion")
    plt.xlabel("t")
    plt.ylabel("X(t)")
    plt.grid(True, linewidth=0.2, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    increment = get_float_from_user("How large should each increment to be? ")

    while True:
        max_time = get_int_from_user(
            "At what time should the simulation end? ")
        if (max_time > increment):
            break

    number_of_increments = (np.floor(max_time/increment)).astype(
        int) if max_time % increment == 0 else (np.floor(max_time/increment)).astype(int) + 1
    
    number_of_sample_paths = get_int_from_user("How many sample paths do you want? ")
    main()
