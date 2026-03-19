from classes.SimulationInitialiser import SimulationInitialiser
from classes.OneDimBrownianMotionProcessor import OneDimBrownianMotionProcessor
from classes.GeometricBrownianMotionProcessor import GeometricBrownianMotionProcessor
from classes.MonteCarloOptionProcessor import MonteCarloOptionProcessor


def main():
    brownian_motions = [0] * number_of_sample_paths
    gbms = [0] * number_of_sample_paths
    call_payoffs = [0] * number_of_sample_paths
    for i in range(number_of_sample_paths):
        brownian_motions[i] = geom_bm_processor.simulate_1D_brownian_motion()
        gbms[i] = geom_bm_processor.simulate_geometric_brownian_motion(
            brownian_motions[i])
        call_payoffs[i] = monte_carlo_option_processor.calculate_payoff(
            gbms[i])
    expectation = monte_carlo_option_processor.calculate_expectation(
        call_payoffs)
    fair_price = monte_carlo_option_processor.calculate_fair_price(gbms[0], expectation)
    print(fair_price)


if __name__ == "__main__":

    simulation_initialiser = SimulationInitialiser()
    increment, max_time, number_of_sample_paths = simulation_initialiser.get_1D_bm_parameters()
    mu, sigma, s_0 = simulation_initialiser.get_geom_bm_parameters()
    strike_price = simulation_initialiser.get_monte_carlo_parameters()

    one_dim_bm_processor = OneDimBrownianMotionProcessor(
        increment, max_time, number_of_sample_paths)
    geom_bm_processor = GeometricBrownianMotionProcessor(
        one_dim_bm_processor, mu, sigma, s_0)
    monte_carlo_option_processor = MonteCarloOptionProcessor(
        geom_bm_processor, strike_price)

    main()
