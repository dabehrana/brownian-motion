from helper_functions import get_float_from_user
from helper_functions import get_int_from_user


class SimulationInitialiser:

    def get_1D_bm_parameters(self):
        increment = get_float_from_user("How large should each increment be? ")

        while True:
            max_time = get_int_from_user(
                "At what time should the simulation end? ")
            if (max_time > increment):
                break

        number_of_sample_paths = get_int_from_user(
            "How many sample paths do you want? ")

        return increment, max_time, number_of_sample_paths

    def get_geom_bm_parameters(self):
        mu = get_float_from_user("Please enter a value for drift: ")
        sigma = get_float_from_user("Please enter a value for volatility: ")
        s_0 = get_int_from_user("Please enter the initial value: ")
        return mu, sigma, s_0

    def get_monte_carlo_parameters(self):
        strike_price = get_float_from_user("Please enter a strike price: ")
        return strike_price
