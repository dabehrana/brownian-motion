from classes.SimulationInitialiser import SimulationInitialiser
from classes.OneDimBrownianMotionProcessor import OneDimBrownianMotionProcessor
from functools import partial
import concurrent.futures
import time


def main():
    brownian_motions = [0] * number_of_sample_paths

    # Parallelise simulations
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f = partial(run_simulations, bm_processor=bm_processor)
        brownian_motions = list(executor.map(
            f, brownian_motions, chunksize=100))
        print("Plotting simulations (will display on completion)...")
        bm_processor.plot_and_display(brownian_motions)


def run_simulations(brownian_motions, bm_processor: OneDimBrownianMotionProcessor):
    brownian_motions = bm_processor.simulate_1D_brownian_motion()
    return brownian_motions


if __name__ == "__main__":
    simulation_initialiser = SimulationInitialiser()

    # timestep, duration and no. of simulations of 1D BM
    increment, max_time, number_of_sample_paths = simulation_initialiser.get_1D_bm_parameters()

    bm_processor = OneDimBrownianMotionProcessor(
        increment, max_time, number_of_sample_paths)

    main()
