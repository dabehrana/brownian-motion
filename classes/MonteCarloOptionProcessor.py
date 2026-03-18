import numpy as np
import pandas as pd
from .GeometricBrownianMotionProcessor import GeometricBrownianMotionProcessor

class MonteCarloOptionProcessor:
    
    def __init__(self, geom_bm_processor : GeometricBrownianMotionProcessor, strike_price):
        self.geom_bm_processor = geom_bm_processor
        self.strike_price = strike_price

    
    def calculate_payoff(self, gbms : pd.Series):
        return np.maximum(gbms.tail(1).item() - self.strike_price, 0)
    
    def calculate_expectation(self, arr):
        return np.mean(arr)
