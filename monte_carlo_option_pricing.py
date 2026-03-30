from classes.SimulationInitialiser import SimulationInitialiser
from classes.OneDimBrownianMotionProcessor import OneDimBrownianMotionProcessor
from classes.GeometricBrownianMotionProcessor import GeometricBrownianMotionProcessor
from classes.MonteCarloOptionProcessor import MonteCarloOptionProcessor
from functools import partial
import concurrent.futures


def main():
    print("Running simulations...\n")
    brownian_motions = [0] * number_of_sample_paths
    gbms = [0] * number_of_sample_paths
    call_payoffs = [0] * number_of_sample_paths

    # Parallelise simulations
    with concurrent.futures.ProcessPoolExecutor() as excecutor:
        f1 = partial(run_simulations, geom_bm_processor=geom_bm_processor)
        f2 = partial(calculate_payoffs,
                     monte_carlo_option_processor=monte_carlo_option_processor)
        gbms = list(excecutor.map(
            f1, brownian_motions, gbms, chunksize=100))
        call_payoffs = list(excecutor.map(
            f2, gbms, call_payoffs, chunksize=100))

    expectation = monte_carlo_option_processor.calculate_expectation(
        call_payoffs)

    # estimate the option price today using Monte Carlo simulation
    fair_price = monte_carlo_option_processor.calculate_fair_price(
        gbms[0], expectation)

    # obtain option price estimate from the Black-Scholes formula
    black_scholes_estimate = monte_carlo_option_processor.calulate_black_scholes(
        gbms[0])

    # compare values given by both estimates
    pct_error = monte_carlo_option_processor.calculate_error(
        black_scholes_estimate, fair_price)

    print_results(fair_price, black_scholes_estimate, pct_error)


def run_simulations(brownian_motions, gbms, geom_bm_processor: GeometricBrownianMotionProcessor):
    brownian_motions = geom_bm_processor.simulate_1D_brownian_motion()
    gbms = geom_bm_processor.simulate_geometric_brownian_motion(
        brownian_motions)
    return gbms


def calculate_payoffs(gbms, call_payoffs, monte_carlo_option_processor: MonteCarloOptionProcessor):
    call_payoffs = monte_carlo_option_processor.calculate_payoff(gbms)
    return call_payoffs


def print_results(fair_price, black_scholes_estimate, pct_error):
    print(f"Fair price estimate: {fair_price}")
    print(f"Black-Scholes estimate: {black_scholes_estimate}")
    print(f"Percentage error: {pct_error}%")


if __name__ == "__main__":

    simulation_initialiser = SimulationInitialiser()
    # timestep, duration and no. of simulations
    increment, max_time, number_of_sample_paths = simulation_initialiser.get_1D_bm_parameters()

    # volatility and initial value of Geometric BM
    sigma, s_0 = simulation_initialiser.get_risk_free_geom_bm_parameters()

    # price at which option can be bought
    strike_price = simulation_initialiser.get_monte_carlo_parameters()

    # Monte Carlo simulation uses risk-free rate instead of drift given by mu
    RISK_FREE_RATE = 0.04

    one_dim_bm_processor = OneDimBrownianMotionProcessor(
        increment, max_time, number_of_sample_paths)
    geom_bm_processor = GeometricBrownianMotionProcessor(
        one_dim_bm_processor, RISK_FREE_RATE, sigma, s_0)
    monte_carlo_option_processor = MonteCarloOptionProcessor(
        geom_bm_processor, strike_price)

    main()
