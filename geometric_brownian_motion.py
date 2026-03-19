from classes.SimulationInitialiser import SimulationInitialiser
from classes.OneDimBrownianMotionProcessor import OneDimBrownianMotionProcessor
from classes.GeometricBrownianMotionProcessor import GeometricBrownianMotionProcessor


def main():
    brownian_motions = [0] * number_of_sample_paths
    gbms = [0] * number_of_sample_paths
    for i in range(number_of_sample_paths):
        brownian_motions[i] = geom_bm_processor.simulate_1D_brownian_motion()
        gbms[i] = geom_bm_processor.simulate_geometric_brownian_motion(
            brownian_motions[i])
    print("Plotting simulations...")
    geom_bm_processor.plot_geometric_brownian_motions(gbms)


if __name__ == "__main__":

    simulation_initialiser = SimulationInitialiser()
    increment, max_time, number_of_sample_paths = simulation_initialiser.get_1D_bm_parameters()
    mu, sigma, s_0 = simulation_initialiser.get_geom_bm_parameters()

    one_dim_bm_processor = OneDimBrownianMotionProcessor(
        increment, max_time, number_of_sample_paths)
    geom_bm_processor = GeometricBrownianMotionProcessor(
        one_dim_bm_processor, mu, sigma, s_0)

    main()
