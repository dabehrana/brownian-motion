import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helper_functions import find_coprime
from helper_functions import conduct_bijection


class OneDimBrownianMotionProcessor:

    def __init__(self, increment, max_time, number_of_sample_paths):
        self.increment = increment
        self.max_time = max_time
        self.number_of_sample_paths = number_of_sample_paths

    def simulate_1D_brownian_motion(self):
        timeline = np.arange(0, self.max_time, self.increment)

        # Obtain normal realisations for each timestep of length increment
        realisations = np.random.normal(
            0, np.sqrt(self.increment), len(timeline[1:]))

        # Build 1D BM by combining the normal realisations
        process = np.concatenate([[0], np.cumsum(realisations)])

        return pd.Series(process, index=[time for time in timeline])

    def plot_in_real_time(self, brownian_motions):
        cmap = plt.cm.get_cmap("tab20", self.number_of_sample_paths)
        plt.ion()
        fig, ax = plt.subplots()
        plt.title("1D Brownian Motion")
        plt.xlabel("t")
        plt.ylabel("X(t)")
        plt.grid(True, linewidth=0.2, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()

        # Will use this value to "randomise" the order of colours on the graph
        a = find_coprime(self.number_of_sample_paths)

        for i in range(self.number_of_sample_paths):
            j = conduct_bijection(i, self.number_of_sample_paths, a)
            brownian_motions[i].plot(ax=ax, color=cmap(j))
            plt.pause(0.001)

        plt.ioff
        input("Press enter to close the figure or end the program")

    def plot_and_display(self, brownian_motions):
        cmap = plt.cm.get_cmap("tab20", self.number_of_sample_paths)
        plt.figure(figsize=(20, 10))

        # Will use this value to "randomise" the order of colours on the graph
        a = find_coprime(self.number_of_sample_paths)

        for i in range(self.number_of_sample_paths):
            j = conduct_bijection(i, self.number_of_sample_paths, a)
            brownian_motions[i].plot(color=cmap(j))

        plt.title("1D Brownian Motion")
        plt.xlabel("t")
        plt.ylabel("X(t)")
        plt.grid(True, linewidth=0.2, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.show()
