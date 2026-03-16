import numpy as np
import pandas as pd
from utils import getIntegerValueFromUser

_number_of_increments = 10_000
increment = getIntegerValueFromUser("Please enter a valid increment: ")

def main():
    brownian_motion = simulate_1D_brownian_motion()
    print(brownian_motion)

def simulate_1D_brownian_motion():
    timeline = np.arange(increment, increment * (_number_of_increments + 1), increment)
    values = np.empty(increment * _number_of_increments)
    series = pd.Series(values, index = [time for time in timeline])
    for time in timeline:
        realisation = obtain_normal_realisation()
        series.loc[time] = realisation + series.get(time - increment, default = 0)
    return series

def obtain_normal_realisation():
    return np.random.normal(0, np.sqrt(increment))

if __name__ == "__main__":
    main()

 