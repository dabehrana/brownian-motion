import numpy as np
import pandas as pd
from scipy.stats import norm
from .GeometricBrownianMotionProcessor import GeometricBrownianMotionProcessor


class MonteCarloOptionProcessor:
    

    def __init__(self, geom_bm_processor: GeometricBrownianMotionProcessor, strike_price):
        self.geom_bm_processor = geom_bm_processor
        self.strike_price = strike_price
        self.RISK_FREE_RATE = 0.04

    def calculate_payoff(self, gbms: pd.Series):
        return np.maximum(gbms.tail(1).item() - self.strike_price, 0)

    def calculate_expectation(self, arr):
        return np.mean(arr)

    def calculate_fair_price(self, gbms: pd.Series, expectation):
        return np.exp(-self.RISK_FREE_RATE * gbms.index[-1]) * expectation

    def calulate_black_scholes(self, gbms: pd.Series):
        s_0 = self.geom_bm_processor.s_0
        k = self.strike_price
        sigma = self.geom_bm_processor.sigma
        final_time = gbms.index[-1]
        d_1 = (np.log(s_0/k) + final_time * (self.RISK_FREE_RATE + 0.5 * (sigma**2))) / (self.geom_bm_processor.sigma * np.sqrt(final_time))
        d_2 = d_1 - sigma * np.sqrt(final_time)
        norm_d1 = norm.cdf(d_1)
        norm_d2 = norm.cdf(d_2)
        discount_factor = np.exp(-self.RISK_FREE_RATE * final_time)
        return s_0 * norm_d1 - k * discount_factor * norm_d2
