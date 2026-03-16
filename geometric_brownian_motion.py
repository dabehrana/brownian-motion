import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helper_functions import get_float_from_user
from helper_functions import get_int_from_user
from 1D_brownian_motion import simulate_1D_brownian_motion

def main():
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
    
    number_of_sample_paths = get_int_from_user("How many sample paths do you want? ")
    main()