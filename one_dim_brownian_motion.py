from helper_functions import get_float_from_user
from helper_functions import get_int_from_user
from classes.OneDimBrownianMotionProcessor import OneDimBrownianMotionProcessor


def main():
    brownian_motions = [0] * number_of_sample_paths
    for i in range(number_of_sample_paths):
        brownian_motions[i] = bm_processor.simulate_1D_brownian_motion()
    bm_processor.plot_brownian_motions(brownian_motions)


if __name__ == "__main__":
    increment = get_float_from_user("How large should each increment to be? ")

    while True:
        max_time = get_int_from_user(
            "At what time should the simulation end? ")
        if (max_time > increment):
            break

    number_of_sample_paths = get_int_from_user(
        "How many sample paths do you want? ")

    bm_processor = OneDimBrownianMotionProcessor(
        increment, max_time, number_of_sample_paths)
    main()
