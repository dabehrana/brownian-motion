import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .OneDimBrownianMotionProcessor import OneDimBrownianMotionProcessor


class GeometricBrownianMotionProcessor:

    def __init__(self, one_dim_bm_processor: OneDimBrownianMotionProcessor, drift, sigma, s_0):

        self.one_dim_bm_processor = one_dim_bm_processor
        self.drift = drift
        self.sigma = sigma
        self.s_0 = s_0

    def simulate_1D_brownian_motion(self):
        return self.one_dim_bm_processor.simulate_1D_brownian_motion()

    def simulate_geometric_brownian_motion(self, bm):
        realisations = []
        timeline = np.arange(
            0, self.one_dim_bm_processor.max_time, self.one_dim_bm_processor.increment)
        for t in timeline:
            realisation = self.s_0 * \
                np.exp(self.sigma*bm.loc[t] +
                       (t*(self.drift - 0.5 * (self.sigma**2))))
            realisations = np.concatenate([realisations, [realisation]])
        return pd.Series(realisations, index=[time for time in timeline])

    def plot_geometric_brownian_motions(self, gbms):
        cmap = plt.cm.get_cmap(
            "tab20", self.one_dim_bm_processor.number_of_sample_paths)
        plt.figure(figsize=(20, 10))

        for i in range(self.one_dim_bm_processor.number_of_sample_paths):
            gbms[i].plot(color=cmap(i))

        plt.title("Geometric Brownian Motion")
        plt.xlabel("t")
        plt.ylabel("S(t)")
        plt.grid(True, linewidth=0.2, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.show()
