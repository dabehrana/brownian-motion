from classes.SimulationInitialiser import SimulationInitialiser
from classes.OneDimBrownianMotionProcessor import OneDimBrownianMotionProcessor
from classes.GeometricBrownianMotionProcessor import GeometricBrownianMotionProcessor
from functools import partial
import concurrent.futures


def main():
    brownian_motions = [0] * number_of_sample_paths
    gbms = [0] * number_of_sample_paths

    # Parallelise simulations
    with concurrent.futures.ProcessPoolExecutor() as excecutor:
        f = partial(run_simulations, geom_bm_processor=geom_bm_processor)
        gbms = list(excecutor.map(f, brownian_motions, gbms, chunksize=100))

    print("Plotting simulations...")
    geom_bm_processor.plot_geometric_brownian_motions(gbms)


def run_simulations(brownian_motions, gbms, geom_bm_processor: GeometricBrownianMotionProcessor):
    brownian_motions = geom_bm_processor.simulate_1D_brownian_motion()
    gbms = geom_bm_processor.simulate_geometric_brownian_motion(
        brownian_motions)
    return gbms


if __name__ == "__main__":
    simulation_initialiser = SimulationInitialiser()

    # timestep, duration and no. of simulations
    increment, max_time, number_of_sample_paths = simulation_initialiser.get_1D_bm_parameters()

    # drift, volatitlity and initial value of Geometric B<M
    mu, sigma, s_0 = simulation_initialiser.get_geom_bm_parameters()

    # value of Geometric BM is dependent on 1D BM
    one_dim_bm_processor = OneDimBrownianMotionProcessor(
        increment, max_time, number_of_sample_paths)

    geom_bm_processor = GeometricBrownianMotionProcessor(
        one_dim_bm_processor, mu, sigma, s_0)

    main()
