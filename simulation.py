import numpy as np


def run_simulation(
    initial_investment,
    mean_return,
    volatility,
    months,
    simulations
):
    """
    Monte Carlo simulation for future portfolio values.

    Returns:
        numpy array with shape:
        (simulations, months)
    """

    results = np.zeros((simulations, months))

    for sim in range(simulations):

        portfolio_value = initial_investment

        for month in range(months):

            random_return = np.random.normal(
                mean_return,
                volatility
            )

            portfolio_value = portfolio_value * (1 + random_return)

            results[sim, month] = portfolio_value

    return results