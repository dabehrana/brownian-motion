from classes.SimulationInitialiser import SimulationInitialiser
from classes.OneDimBrownianMotionProcessor import OneDimBrownianMotionProcessor


def main():
    brownian_motions = [0] * number_of_sample_paths
    for i in range(number_of_sample_paths):
        brownian_motions[i] = bm_processor.simulate_1D_brownian_motion()
    bm_processor.plot_brownian_motions(brownian_motions)


if __name__ == "__main__":
    
    simulation_initialiser = SimulationInitialiser()
    increment, max_time, number_of_sample_paths = simulation_initialiser.get_1D_bm_parameters()

    bm_processor = OneDimBrownianMotionProcessor(
        increment, max_time, number_of_sample_paths)

    main()
