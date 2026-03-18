from helper_functions import get_float_from_user
from helper_functions import get_int_from_user
from classes.OneDimBrownianMotionProcessor import OneDimBrownianMotionProcessor
from classes.GeometricBrownianMotionProcessor import GeometricBrownianMotionProcessor
from classes.MonteCarloOptionProcessor import MonteCarloOptionProcessor

def main():
    pass


if __name__ == "__main__":
    increment = get_float_from_user("How large should each increment to be? ")

    while True:
        max_time = get_int_from_user(
            "At what time should the simulation end? ")
        if (max_time > increment):
            break

    number_of_sample_paths = get_int_from_user(
        "How many sample paths do you want? ")
    
    mu = get_float_from_user("Please enter a value for drift: ")
    sigma = get_float_from_user("Please enter a value for volatility: ")
    s_0 = get_int_from_user("Please enter the initial value: ")

    one_dim_bm_processor = OneDimBrownianMotionProcessor(increment, max_time, number_of_sample_paths)
    geom_bm_processor = GeometricBrownianMotionProcessor(one_dim_bm_processor, mu, sigma, s_0)
    monte_carlo_option_processor = MonteCarloOptionProcessor(geom_bm_processor, K)
    main()
