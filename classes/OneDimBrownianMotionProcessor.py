import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class OneDimBrownianMotionProcessor:

    def __init__(self, increment, max_time, number_of_sample_paths):
        self.increment = increment
        self.max_time = max_time
        self.number_of_sample_paths = number_of_sample_paths

    def simulate_1D_brownian_motion(self):
        timeline = np.arange(0, self.max_time, self.increment)
        realisations = np.random.normal(
            0, np.sqrt(self.increment), len(timeline[1:]))
        process = np.concatenate([[0], np.cumsum(realisations)])
        return pd.Series(process, index=[time for time in timeline])

    def plot_brownian_motions(self, brownian_motions):
        cmap = plt.cm.get_cmap("tab20", self.number_of_sample_paths)
        plt.figure(figsize=(20, 10))

        for i in range(self.number_of_sample_paths):
            brownian_motions[i].plot(color=cmap(i))

        plt.title("1D Brownian Motion")
        plt.xlabel("t")
        plt.ylabel("X(t)")
        plt.grid(True, linewidth=0.2, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.show()
