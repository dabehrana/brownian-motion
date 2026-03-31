import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .OneDimBrownianMotionProcessor import OneDimBrownianMotionProcessor
from helper_functions import find_coprime
from helper_functions import conduct_bijection


class GeometricBrownianMotionProcessor:

    def __init__(self, one_dim_bm_processor: OneDimBrownianMotionProcessor, drift, sigma, s_0):

        self.one_dim_bm_processor = one_dim_bm_processor
        self.drift = drift
        self.sigma = sigma
        self.s_0 = s_0

    def simulate_1D_brownian_motion(self):
        return self.one_dim_bm_processor.simulate_1D_brownian_motion()

    def simulate_geometric_brownian_motion(self, bm: pd.Series):
        realisations = []
        timeline = np.arange(
            0, self.one_dim_bm_processor.max_time, self.one_dim_bm_processor.increment)

        # Calculate value of Geometric BM at time t
        for t in timeline:
            realisation = self.s_0 * \
                np.exp(self.sigma*bm.loc[t] +
                       (t*(self.drift - 0.5 * (self.sigma**2))))
            realisations = np.concatenate([realisations, [realisation]])

        return pd.Series(realisations, index=[time for time in timeline])

    def plot_in_real_time(self, gbms):
        cmap = plt.cm.get_cmap(
            "tab20", self.one_dim_bm_processor.number_of_sample_paths)
        plt.ion()
        fig, ax = plt.subplots()
        plt.title("Geometric Brownian Motion")
        plt.xlabel("t")
        plt.ylabel("S(t)")
        plt.grid(True, linewidth=0.2, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()

        # Will use this value to "randomise" the order of colours on the graph
        a = find_coprime(self.one_dim_bm_processor.number_of_sample_paths)

        for i in range(self.one_dim_bm_processor.number_of_sample_paths):
            # "randomise" the order of colours on the graph
            j = conduct_bijection(
                i, self.one_dim_bm_processor.number_of_sample_paths, a)
            gbms[i].plot(ax=ax, color=cmap(j))
            plt.pause(0.001)

        plt.ioff
        input("Press enter to close the figure or end the program")

    def plot_and_display(self, gbms):
        cmap = plt.cm.get_cmap(
            "tab20", self.one_dim_bm_processor.number_of_sample_paths)
        plt.figure(figsize=(20, 10))

        # Will use this value to "randomise" the order of colours on the graph
        a = find_coprime(self.one_dim_bm_processor.number_of_sample_paths)

        for i in range(self.one_dim_bm_processor.number_of_sample_paths):
            # "randomise" the order of colours on the graph
            j = conduct_bijection(
                i, self.one_dim_bm_processor.number_of_sample_paths, a)
            gbms[i].plot(color=cmap(j))

        plt.title("Geometric Brownian Motion")
        plt.xlabel("t")
        plt.ylabel("S(t)")
        plt.grid(True, linewidth=0.2, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.show()
